motech-cli | كاتب المحتوى | 2026-09-23 | draft-for-editor

# Publishing copy — Motech CLI (English)

## LinkedIn (≤120 words)
Joining a client device to a secure-access platform used to mean a GUI installer per OS, a hand-copied SSH key, and a service configured afterwards.

Motech CLI makes it one command: `motech setup` exchanges a one-time activation code, joins the NetBird mesh, installs the server-owned public key, and registers a background service with heartbeats and server-driven key rotation — on Windows, Linux and macOS.

The key decision: no private key ever lands on the client. Token never an argument, strict TLS, SHA256 before install, cosign-signed release.

Go 1.23 · 6 commands · 6 targets · 1 dependency · 6 tests passing.

Want one command that joins your clients' devices? DM me.
github.com/moain2028/motech-cli

#Go #DevOps #Security #ZeroTrust

## X (≤280 chars)
One command joins a client device to a secure mesh on Windows, Linux and macOS — and the private key never leaves the server. Go, 6 commands, 6 targets, cosign-signed release with SHA256 verified before install.
github.com/moain2028/motech-cli
#Go #Security

## Instagram (≤150 words)
How many manual steps sit between "new device" and "securely connected"?

Motech CLI makes it one: a single command asks for an activation code, joins the device to the NetBird mesh, installs the server's public SSH key, and starts a background service that keeps it connected and applies the server's decisions — rotate or disable — without anyone touching the device.

The security idea in one line: the server owns the whole key pair; the client never holds a private key. The token is never an argument, TLS is strict, the installer verifies SHA256, and the release is cosign-signed.

Go 1.23 · one ≈5.5 MB binary · Windows, Linux and macOS · 6 tests passing.

For IT support teams and managed-service providers. DM me.

#Go #DevOps #Security #NetBird #ZeroTrust

## Reel script (19.6 s, English)
[0–3.5] Business project · Secure access — Motech CLI: one command joins a client device to a secure mesh — with no private key on the client
[3.5–8] motech setup — and you're done: exchanges the activation code, joins the NetBird mesh, installs the public key, and registers a background service — on Windows, Linux and macOS
[8–12] No private key on the client: the server owns the pair and sends only the public key; the token is never an argument; strict TLS; SHA256 before install and a cosign signature
[12–16] Heartbeats and server-driven key rotation — systemd, launchd or Scheduled Task; self-heals the mesh join and applies rotate / disable
[16–18] By the numbers: 6 commands · 6 build targets · 6 tests passing · 11 signed assets
[18–19.6] For IT support teams and managed-service providers — want one command that joins your clients' devices? DM me.

<!-- Sources: brief.en.md · tech.md · research.md. LinkedIn ≈108 words · X ≈257 chars · IG ≈129 words. No "open source", no unverified CI claim, no customers. -->
