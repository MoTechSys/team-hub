motech-cli | كاتب المحتوى | 2026-09-23 | draft-for-editor

# Motech CLI — Project explainer

## Executive summary
1. One Go binary with six commands that joins a client device to the Motech secure-access platform in a single command on Windows, Linux and macOS — a lightweight alternative to the full GUI installer.
2. The private key never leaves the server: the client receives only the public key, the token is never a CLI argument, TLS is 1.2+ and strict, and the state file is 0600.
3. Joins the NetBird mesh with built-in SSH — no sshd changes — and registers a background service (systemd / launchd / Scheduled Task) that sends heartbeats and applies server-driven key rotation or disable.
4. Actually built and tested on 2026-09-23: `go vet` clean, 6/6 tests passing, 6 targets built, and a v0.1.0 release cosign-signed with 11 assets.
5. Gaps, stated plainly: the code is public to read but the license is proprietary (not open source), the signed release lives on the moain2026 account while moain2028 has a tag without a release, no documented customers, and Authenticode / notarization are pending.

## The problem
An IT provider onboarding many client devices repeats the same ritual on each: a GUI installer per OS, an SSH key copied by hand, a service configured afterwards. Every manual step invites error — the worst being a private key resting on a device you do not own.

## The solution
`motech setup` does it in one command. It takes a one-time activation code (no-echo prompt or an environment variable wiped immediately — never an argument), exchanges it with the server, and receives an agent token, a NetBird setup key and the **public** key only. It joins the mesh with built-in SSH, writes the key to authorized_keys with a tag so only its own line rotates, and registers a background service that sends heartbeats and applies the server's decisions: rotate, disable, install_pubkey or apply_ssh — self-healing the mesh join if it drops.

Six commands: setup · register · run · status · uninstall · version. Output in Arabic and English.

## The key engineering decision
The server owns the whole key pair. Compromising the binary, the state file or the client device leaks no usable private key. Around it: TLS 1.2+ with no verification bypass, 5 retries with exponential backoff, an installer that verifies SHA256 before installing, and a release cosign-signed with the workflow identity — no stored signing key.

## The numbers (from the code and from go test)
6 commands · 6 targets (linux/darwin/windows × amd64/arm64) · 1 direct dependency · 1,486 lines of Go in 16 files · 6 tests passing · zero vet findings · 11 assets in the signed release · ≈5.5 MB per binary.

## Not done yet
The license reads "All rights reserved" although the repository is public — clarify the intent. README and PROGRESS point to moain2026, where the signed release lives; moain2028 (the footer account) has tag v0.1.0 without a release — publish it there or unify the links. The temporary installer host in PROGRESS did not respond. CI is claimed but unverified from the Actions log. Authenticode, notarization and branch protection (SECURITY) are pending. Three commits in one day; no documented customers. For this pack, setup/register were not run against a real server — only the privilege gate was exercised.

## Who it is for
IT support teams and managed-service providers that onboard many client devices quickly and safely. Want one command that joins your clients' devices? DM me.

<!-- Sources: tech.md motech-cli; research.md. ~500 words. No "open source", no "ALL GREEN", no customers. -->
