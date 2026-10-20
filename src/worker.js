// Answers requests that match no page or asset (wrangler.jsonc sets not_found_handling to "none") with the normal 404 page.
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const page = await env.ASSETS.fetch(new URL('/404.html', url));
    return new Response(page.body, { status: 404, headers: page.headers });
  },
};
