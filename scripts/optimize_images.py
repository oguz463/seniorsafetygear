#!/usr/bin/env python3
"""Optimizes the photos in static/img and writes their WebP variants.

Run it after adding or replacing a JPEG, then commit the results. Cloudflare only runs build.py, so the converted files are committed.
Needs cwebp, djpeg, cjpeg and jpegtran (libjpeg-turbo and webp from Homebrew) and sips (macOS).

Hero photos (static/img/hero/NAME.jpg, 1600 px wide, plus NAME-800.jpg):
  NAME.webp, NAME-800.webp, NAME-400.webp at quality 80, and both JPEGs re-encoded progressive at quality 82 without metadata
  (a JPEG that is already lighter than that is only made progressive, losslessly).
Product images (static/img/NAME.jpg):
  padded to 400 x 400 on white, NAME.webp (400 px) and NAME-200.webp (200 px) at quality 80, and the JPEG made progressive without
  metadata, losslessly.
A JPEG that is already progressive and has all its WebP files is skipped, so re-running only touches new images.
"""
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMG = ROOT / 'static' / 'img'
HERO = IMG / 'hero'
WEBP_Q = '80'
JPEG_Q = '82'


def progressive(path):
    d = path.read_bytes()
    i = 2
    while i < len(d) - 4:
        if d[i] != 0xFF:
            i += 1
            continue
        m = d[i + 1]
        if m in (0xC0, 0xC1):
            return False
        if m == 0xC2:
            return True
        if m == 0xDA:
            return False
        i += 2 + int.from_bytes(d[i + 2:i + 4], 'big')
    return False


def run(cmd, **kw):
    subprocess.run(cmd, check=True, **kw)


def webp(src, dst, width=None):
    cmd = ['cwebp', '-q', WEBP_Q, '-m', '6', '-metadata', 'none', '-quiet']
    if width:
        cmd += ['-resize', str(width), '0']
    run(cmd + [str(src), '-o', str(dst)])


def jpeg_lossy(src, dst):
    with open(dst, 'wb') as out:
        dj = subprocess.Popen(['djpeg', str(src)], stdout=subprocess.PIPE)
        subprocess.run(['cjpeg', '-quality', JPEG_Q, '-optimize', '-progressive'], stdin=dj.stdout, stdout=out, check=True)
        dj.wait()


def jpeg_lossless(src, dst):
    with open(dst, 'wb') as out:
        subprocess.run(['jpegtran', '-optimize', '-progressive', '-copy', 'none', str(src)], stdout=out, check=True)


def replace_if_smaller(new, target):
    if new.stat().st_size < target.stat().st_size:
        shutil.move(str(new), str(target))
        return True
    new.unlink()
    return False


def dims(path):
    out = subprocess.run(['sips', '-g', 'pixelWidth', '-g', 'pixelHeight', str(path)], capture_output=True, text=True, check=True).stdout
    w = int(out.split('pixelWidth:')[1].split()[0])
    h = int(out.split('pixelHeight:')[1].split()[0])
    return w, h


def hero(master, tmp):
    name = master.stem
    v800 = HERO / f'{name}-800.jpg'
    wanted = [HERO / f'{name}.webp', HERO / f'{name}-800.webp', HERO / f'{name}-400.webp']
    if progressive(master) and v800.exists() and progressive(v800) and all(p.exists() for p in wanted):
        return 0
    before = master.stat().st_size + (v800.stat().st_size if v800.exists() else 0)
    webp(master, HERO / f'{name}.webp')
    webp(master, HERO / f'{name}-800.webp', 800)
    webp(master, HERO / f'{name}-400.webp', 400)
    small = tmp / f'{name}-800-src.jpg'
    run(['sips', '--resampleWidth', '800', '-s', 'formatOptions', '100', str(master), '--out', str(small)], capture_output=True)
    opt800 = tmp / f'{name}-800-opt.jpg'
    jpeg_lossy(small, opt800)
    shutil.move(str(opt800), str(v800))
    opt = tmp / f'{name}-opt.jpg'
    jpeg_lossy(master, opt)
    if not replace_if_smaller(opt, master):
        # Already a light JPEG: keep its pixels and only make it progressive.
        jpeg_lossless(master, opt)
        replace_if_smaller(opt, master)
    return before - master.stat().st_size - v800.stat().st_size


def product(path, tmp):
    name = path.stem
    w400, w200 = IMG / f'{name}.webp', IMG / f'{name}-200.webp'
    if progressive(path) and w400.exists() and w200.exists() and dims(path) == (400, 400):
        return 0
    before = path.stat().st_size
    if dims(path) != (400, 400):
        sq = tmp / f'{name}-sq.jpg'
        run(['sips', '--resampleHeightWidthMax', '400', '-s', 'formatOptions', '95', str(path), '--out', str(sq)], capture_output=True)
        run(['sips', '--padToHeightWidth', '400', '400', '--padColor', 'FFFFFF', '-s', 'formatOptions', '95', str(sq), '--out', str(path)], capture_output=True)
        sq.unlink()
    webp(path, w400)
    webp(path, w200, 200)
    opt = tmp / f'{name}-opt.jpg'
    jpeg_lossless(path, opt)
    replace_if_smaller(opt, path)
    return before - path.stat().st_size


def main():
    for tool in ('cwebp', 'djpeg', 'cjpeg', 'jpegtran', 'sips'):
        if not shutil.which(tool):
            sys.exit(f'{tool} not found')
    saved_hero = saved_prod = n_hero = n_prod = 0
    with tempfile.TemporaryDirectory() as t:
        tmp = pathlib.Path(t)
        for master in sorted(HERO.glob('*.jpg')):
            if master.stem.endswith('-800'):
                continue
            s = hero(master, tmp)
            n_hero += 1
            saved_hero += s
        for path in sorted(IMG.glob('*.jpg')):
            s = product(path, tmp)
            n_prod += 1
            saved_prod += s
    print(f'hero photos: {n_hero}, JPEG bytes saved: {saved_hero:,}')
    print(f'product images: {n_prod}, JPEG bytes saved: {saved_prod:,}')


if __name__ == '__main__':
    main()
