motech-platform | مهندس | 2026-09-23 | draft — to be sealed by the editor

# Motech Platform — Project Explainer

## Executive Summary

1. **Problem:** Supporting dozens of remote client PCs today relies on shared passwords and scattered, unrotated SSH keys, with no record of who accessed what.
2. **Solution:** A central Go backend generates an ed25519 keypair per client, encrypts the private key with AES-256-GCM, and pushes only the public key to a signed agent on a NetBird mesh.
3. **Experience:** Clients install from a single link (`/setup/{token}`); admins get a ready SSH command, key rotation with confirm/ack, and a full activity log for every operation.
4. **Reach:** A companion CLI (Motech CLI) does the same in one command on Windows, Linux, and macOS (amd64 + arm64), with signed releases.
5. **Status:** A working, fully documented build (12 technical docs), run and verified locally; designed to scale from 3 to 1,000+ clients. Deployment figures: to be confirmed.

---

## What is the problem?

IT teams and software vendors who support client and branch machines remotely (mostly Windows) depend on manual tooling: shared passwords, SSH keys scattered across laptops with no rotation or ownership, and no log showing who reached which machine and what they did. That model does not scale from a handful of clients to hundreds, and it leaves a standing security gap every time a staff member leaves or a key is forgotten.

## How does it work?

The platform is central, and the keys belong to the backend — not to the devices:

- **Backend:** Go with chi and sqlx, on PostgreSQL 16 reached only through `DATABASE_URL`. When a client is added, the backend generates an ed25519 keypair, stores the private key encrypted with AES-256-GCM, and issues a one-time install link `/setup/{token}`.
- **Agent:** An Authenticode-signed Windows .exe running as a service; it joins the NetBird mesh, installs the public key pushed by the backend, and sends a heartbeat every 20 seconds.
- **Dashboard:** RTL Arabic, dark/light, built with HTML, Tailwind, and Alpine.js and served by the backend itself. From it, admins manage clients, rotate keys through a confirm/ack cycle, and copy the full connection block (NetBird IP + user + ready SSH command).
- **Activity log:** Every operation — create, rotate, key access, disable — is recorded in `activity_log`.
- **Auth:** Hand-written JWT in Go with no external SDK, plus a login limit of 5 attempts per minute per IP.
- **Motech CLI:** A companion tool that downloads, registers, and installs the background service in one command on Windows, Linux, and macOS, with six commands (setup, register, run, status, uninstall, version) and releases signed with cosign keyless plus SHA256SUMS. The activation token is never accepted as a command-line argument, so it cannot leak into shell history.

## Who is it for?

IT teams and software vendors supporting remote Windows fleets — from a small office with three machines to a branch network beyond a thousand.

## What sets it apart?

- **Backend-owned keys:** The private key never touches the client machine; the agent and the CLI only ever hold the public key.
- **Portability first:** Standard PostgreSQL, and a single variable (`NETBIRD_API_URL`) switches between NetBird Cloud and self-hosted.
- **Single Go binary** for both backend and agent — simple deployment, no runtime dependencies.
- **NetBird-native access:** SSH through NetBird's built-in mechanism instead of editing `authorized_keys` on Windows.
- **Everything documented:** 12 technical documents (ARCHITECTURE, DATABASE, API, NETBIRD, SECURITY, SETUP, DEPLOYMENT, TROUBLESHOOTING, CHANGELOG, ROADMAP, PROGRESS, DECISIONS) and an ADR decision log.
- **Operationally verified:** Built and run locally from a clean clone; migrations 001–005 apply automatically, `/health` returns `{"db":"ok","status":"ok"}`, and the full flow (create client → setup token → agent registration → heartbeat → activity log) worked end to end.

**Contact:** Let's scope your access setup — DM or email.

<!-- Sources: brief.en.md (Problem, Solution, Result, Who it's for, Contact) · tech.md (stack; figures: 3→1,000+ design target, 20 s heartbeat, 6 CLI commands, 3 OS × 2 archs, 12 docs; operational check: 5 logins/min, migrations 001–005, /health, E2E flow) · README moain2026/motech-platform (components, features, core principles, DATABASE_URL/NETBIRD_API_URL) · README moain2026/motech-cli (six commands, cosign keyless, SHA256SUMS, token never a CLI argument). No real deployment figures — brief: "to be confirmed". -->
