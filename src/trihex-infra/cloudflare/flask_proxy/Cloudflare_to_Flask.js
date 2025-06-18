//6R:Fire
export default {
  async fetch(request) {
    const url = "https://soul-diagnosis-webhook.onrender.com/webhook/soul-diagnosis";
    const modified = new Request(url, {
      method: request.method,
      headers: request.headers,
      body: request.body
    });

    const response = await fetch(modified);
    return new Response(await response.text(), {
      status: response.status,
      headers: response.headers
    });
  }
};
