// Keeps the installed app from showing a stale cached copy: every page load
// (including from the home-screen icon) tries the network first and ignores
// the browser's HTTP cache, so new deploys show up without the user having
// to manually clear Safari's cache or reinstall the home-screen icon.
self.addEventListener("install", () => { self.skipWaiting(); });
self.addEventListener("activate", (event) => { event.waitUntil(self.clients.claim()); });

self.addEventListener("fetch", (event) => {
  if (event.request.mode === "navigate" || event.request.destination === "document") {
    event.respondWith(
      fetch(event.request, { cache: "no-store" }).catch(() => caches.match(event.request))
    );
  }
});
