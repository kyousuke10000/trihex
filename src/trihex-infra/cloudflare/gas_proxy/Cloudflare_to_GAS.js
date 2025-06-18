//6R:Fire
/**
 * soulflow-proxy-v2 (Very thin proxy)
 *  受け取った JSON をそのまま GAS Web App へ転送
 */
const API_URL = 'https://script.google.com/macros/s/AKfycbyBdFGweKLoEVd-ckTFzXCbfZvxRos1XZPAS4Ub6uc-ZUafPF-piHX_J71Y0qX1eig8/exec'; // ← あなたの GAS URL

export default {
  async fetch(request, env, ctx) {
    // ルートを限定してセキュアに
    const url = new URL(request.url);
    if (url.pathname !== '/webhook/soul-diagnosis') {
      return new Response('Not Found', { status: 404 });
    }

    // GPT / Postman から来る JSON をそのまま転送
    const resp = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: await request.text(),          // そのままパススルー
    });

    // GAS からのレスポンスを利用者に返す
    const text = await resp.text();
    return new Response(text, { status: resp.status, headers: resp.headers });
  }
};
