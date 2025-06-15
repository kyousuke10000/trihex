export default {
  async fetch(request) {
    const json = await request.json();
    const token = json.token;

    if (token !== "your_secret_token") {
      return new Response("Unauthorized", { status: 403 });
    }

    const response = await fetch("https://script.google.com/macros/s/<<GAS-DEPLOY-URL>>/exec", {
      method: "POST",
      body: JSON.stringify(json),
      headers: { "Content-Type": "application/json" }
    });

    return new Response("Forwarded to GAS", { status: 200 });
  }
}
