# Mission 7 — How Computers Communicate

## 1. Task / objective
Explain foundational computer-networking terms in my own words with concrete examples, observe privacy-safe connectivity and DNS lookup results for a public domain (`example.com`), and trace step-by-step what happens when a website opens in a browser.

## 2. Work completed

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| --- | --- | --- |
| **LAN (Local Area Network)** | A private network that connects computers and devices within a small physical area such as a single room, home, or building. | A home Wi-Fi network connecting a laptop, smartphone, and printer, or a college computer lab. |
| **MAN (Metropolitan Area Network)** | A medium-sized network that links multiple LANs across a city or a very large university campus. | Fiber-optic links connecting multiple buildings across a large university campus or city-wide municipal Wi-Fi. |
| **WAN (Wide Area Network)** | A vast network spanning cities, countries, or continents by interconnecting many LANs and MANs. | The global Internet, or a bank's network linking branches across all of India. |
| **DNS (Domain Name System)** | The Internet's directory ("phonebook") that translates human-friendly domain names into numerical IP addresses computers use to route data. | Looking up `example.com` and receiving public IPv4 addresses like `104.20.23.154` and `172.66.147.243`. |
| **Router** | A networking device that connects separate networks together and inspects packet destinations to forward data along the best path. | A home Wi-Fi router connecting my home LAN to my Internet Service Provider (ISP). |
| **Protocol** | A standardized set of rules and formats that devices agree to follow so they can exchange and interpret data reliably. | **HTTPS** for encrypted web browsing, **TCP/IP** for reliable internet delivery, or **ICMP** used by `ping`. |
| **Packet switching** | Breaking a message or file into small chunks called packets, sending them independently across the network (even along different routes), and reassembling them in order at the destination. | Streaming a video or loading a webpage where data arrives in thousands of small IP packets. |
| **Client-server** | A communication model where one device or app (the **client**) requests information or a service, and another computer (the **server**) processes the request and sends back a response. | My web browser (client) requesting a repository page from GitHub's web server (server). |

---

### Task 7.2 — Observe network information
Using Terminal, I tested connectivity and DNS resolution for the public domain `example.com` (keeping all personal/local network details redacted):
- `ping -c 3 example.com` transmitted 3 packets, received 3 replies (`0.0% packet loss`), with round-trip times between `6.284 ms` and `15.653 ms`.
- `nslookup example.com` returned the public IPv4 addresses `172.66.147.243` and `104.20.23.154` for `example.com`.

**Answers to reflection questions:**
- **What a connectivity test (`ping`) helps you check:** It checks whether a remote host is reachable over the network, measures how quickly packets make a round trip (latency in milliseconds), and reveals whether any packets were dropped (packet loss).
- **What information a DNS lookup (`nslookup`) displays:** It shows which DNS resolver answered the query (redacted here for privacy) and the canonical domain name mapped to one or more numerical IP addresses (`A` / `AAAA` records) that host that domain.
- **Role of DNS when you enter a website name in a browser:** Network routers cannot route traffic using English names like `example.com`—they need numerical IP addresses. DNS automatically looks up the domain name behind the scenes and returns the server's IP address so the browser knows exactly where to send its request.

---

### Task 7.3 — What happens when you open a website?
1. **User enters URL in the client:** I type `https://example.com` into my web browser, which acts as the **client** initiating the request.
2. **DNS lookup resolves the address:** The browser asks **DNS** to translate the domain name `example.com` into its numerical IP address (for example, `104.20.23.154`).
3. **Connection travels through the router and network:** My computer breaks the request into packets using the **TCP/IP** **protocol** and sends them to my local **router**, which forwards them across my ISP and internet backbone routers toward the destination IP.
4. **Secure handshake and web request:** The browser establishes a secure **HTTPS** (**protocol**) connection with the remote web **server** and sends an HTTP `GET` request asking for the webpage.
5. **Server prepares the response:** The **server** receives the request, locates the HTML/CSS/image resources for the page, and splits the response back into network packets.
6. **Packets return and the browser renders the page:** The response packets travel back through routers to my **client**, where TCP reassembles them in order and the browser renders the finished webpage on my screen.

## 3. Commands / tools used
- `ping -c 3 example.com` — Sent 3 ICMP echo requests to check reachability, latency, and packet loss.
- `nslookup example.com` — Queried DNS to inspect the IPv4 addresses linked to `example.com`.
- `git add` & `git commit` — Staged and committed the Mission 7 documentation and redacted evidence.

## 4. My understanding
Opening a webpage feels instantaneous, yet behind the scenes it relies on several layers working together cleanly: DNS translates readable names to numeric addresses, routers move packets across LANs and WANs via packet switching, and shared protocols like TCP/IP and HTTPS ensure the client and server speak the same language reliably and securely.

## 5. Difficulties faced
The raw `nslookup` output displayed the DNS server's address at the top, and I needed to make sure no local network or personal IP details were accidentally published.

## 6. How I resolved them
Before saving the evidence file, I replaced the resolver `Server` and `Address` fields with `[redacted]` and kept only the public `example.com` responses.

## 7. Evidence / files
- [mission-07-networking/README.md](README.md) — Network concepts table, connectivity/DNS reflections, and 6-step website loading walkthrough.
- [evidence/mission-07-network-output.txt](../evidence/mission-07-network-output.txt) — Redacted `ping` and `nslookup` outputs for `example.com`.

## 8. Commit details
- **Commit message:** `Explain networking concepts and website communication`
- **Push status:** Committed on `main` (staged and committed separately from Mission 6; ready to push to GitHub).
