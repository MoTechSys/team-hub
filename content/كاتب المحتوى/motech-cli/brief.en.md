motech-cli | كاتب المحتوى | 2026-09-23 | draft

# Motech CLI — secure device access in one command, on three platforms, with no private key on the client

**Segment:** Companies (IT support and remote-access providers)
**Problem:** Joining a client device to the secure-access platform needed a full GUI installer per OS, hand-copied SSH keys, and a service configured by hand.
**Solution:** One Go binary with six commands: `motech setup` exchanges a one-time activation code with the server, joins the NetBird mesh using its built-in SSH, installs the server-owned public key — never a private key on the client — and registers a background service (systemd / launchd / Scheduled Task) that sends heartbeats and applies key rotation or disable commands from the server. The token is never a CLI argument, TLS is strict, the installer verifies SHA256 before installing, and the release is cosign-signed with the workflow identity.
**Results in numbers:** 6 commands, 6 targets (Windows/Linux/macOS × amd64/arm64), 1,486 lines of Go with one direct dependency, 6 passing tests and zero vet findings, and a v0.1.0 release with 11 signed assets. Binary ≈5.5 MB.
**Who it serves:** IT support teams and managed-service providers that onboard many client devices quickly and safely.
**Contact:** Want one command that joins your clients' devices? DM me.

<!-- Sources: tech.md motech-cli (all numbers from code, git and the GitHub API, 2026-09-23). ~150 words. -->
