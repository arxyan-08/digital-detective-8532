# Mission 7 — How Computers Communicate

## 1. Task / objective
Explain key networking concepts, observe real connectivity and DNS data using Terminal, and describe step by step what happens when a website opens in a browser.

## 2. Work completed

### Task 7.1 — Network concepts

| Concept | What it means | Example |
| --- | --- | --- |
| **LAN** | A network covering a small area like a home or a lab | My home Wi-Fi connecting my laptop, phone, and printer |
| **MAN** | A network covering a city or large campus, connecting multiple LANs | Fiber links connecting different buildings across a university campus |
| **WAN** | A huge network spanning countries or the whole world | The Internet itself |
| **DNS** | The Internet's phonebook — translates domain names (like `example.com`) into IP addresses (like `104.20.23.154`) | Typing `example.com` in a browser and DNS finding the server's IP behind the scenes |
| **Router** | A device that connects different networks and figures out the best path to forward data | My home Wi-Fi router connecting my LAN to my ISP's network |
| **Protocol** | An agreed-upon set of rules for how devices communicate | HTTPS for secure web browsing, TCP/IP for reliable data delivery |
| **Packet switching** | Splitting data into small chunks (packets), sending them independently, and reassembling at the destination | Loading a webpage — the HTML, images, and CSS arrive as thousands of separate packets |
| **Client-server** | One device (client) asks for something, another (server) provides it | My browser (client) requesting a page from GitHub's web server (server) |

### Task 7.2 — Observing network information
I tested connectivity with a public domain (`example.com`):

**Ping test (`ping -c 3 example.com`):**
- Sent 3 packets, received all 3 back — 0% packet loss
- Round-trip times ranged from about 6 ms to 16 ms

**DNS lookup (`nslookup example.com`):**
- Returned the IP addresses `172.66.147.243` and `104.20.23.154` for `example.com`
- DNS resolver address redacted for privacy

**What I learned from these:**
- **Ping** tells you whether a remote server is reachable and how fast the round trip is. If packets get lost or the time is very high, something's wrong with the connection.
- **nslookup** shows you the actual IP address(es) behind a domain name. It's proof that DNS is doing its job — translating human-readable names into numbers that routers can actually work with.
- **DNS's role in browsing:** When I type a URL, my browser can't just send a request to "example.com" — routers don't understand names, they need numbers. DNS handles that translation automatically before my browser even sends its first request.

### Task 7.3 — What happens when you open a website (6 steps)
1. **I type `https://example.com` in my browser.** The browser is the *client* starting the whole process.
2. **DNS lookup.** The browser asks DNS to translate `example.com` into an IP address. DNS responds with something like `104.20.23.154`.
3. **Packets leave through my router.** My computer breaks the request into small *packets* using the TCP/IP *protocol* and sends them to my local *router*, which forwards them out to the internet.
4. **Secure connection established.** Using HTTPS, the browser and the destination *server* do a quick handshake to set up encryption, then the browser sends an HTTP request asking for the webpage.
5. **Server responds.** The web *server* at that IP address finds the HTML, CSS, and images for the page, splits them into packets, and sends them back.
6. **Browser renders the page.** The packets travel back through routers to my computer, TCP reassembles them in order, and my browser puts together and displays the finished webpage.

## 3. Commands / tools used
- `ping -c 3 example.com` — tested whether the server is reachable and measured latency
- `nslookup example.com` — looked up the IP addresses for the domain

## 4. My understanding
Before this mission, opening a website felt instant and kind of magical. Now I can see the machinery behind it — DNS translating names to numbers, packets being split up and routed independently across networks, protocols making sure everything arrives intact and in order. The whole thing takes milliseconds but involves a surprising number of steps and devices working together.

## 5. Difficulties faced
The `nslookup` output showed my DNS resolver's IP address at the top, which is a private network detail I shouldn't publish.

## 6. How I resolved them
Replaced the resolver's server address with `[redacted]` in the evidence file, keeping only the public `example.com` results.

## 7. Evidence / files
- [mission-07-networking/README.md](README.md) — Concepts table, observations, and 6-step website trace
- [evidence/mission-07-network-output.txt](../evidence/mission-07-network-output.txt) — Redacted `ping` and `nslookup` outputs

## 8. Commit details
- **Message:** `Explain networking concepts and website communication`
- Committed on `main` and pushed to GitHub.
