digital-forensics-lab | الباحث | 2026-09-23 | v2 — F (publishing copy — draft for the editor)

> Every number traces to tech.md; no person, institution, or academic attribution. Framing: "educational project / hands-on lab".

## LinkedIn (EN)
Digital forensics is mostly taught from slides. This lab flips that: five topics — Windows Registry, Event Log, Autopsy, FTK Imager, Browser Forensics — each run on real evidence, with a screenshot and a hash.

Inside:
• A Python parser for Chrome history that works on a copy and re-verifies MD5/SHA-256 before and after — 19 records, Integrity re-check: PASSED.
• A one-line PowerShell runner: Registry (USBSTOR, BAM) + Event Log (4624/4625/1102/6005) → unified timeline tagged with MITRE ATT&CK + SHA-256 chain of custody for seven files + Arabic HTML report.
• A real case: 15 failed logons in a brute-force pattern mapped to T1110, and 7 USB devices with their serials.
• 3 original Sigma rules and 16 MITRE techniques referenced in code.

An open-source educational project for cybersecurity and DFIR students.
github.com/moain2028/digital-forensics-lab

#DFIR #DigitalForensics #CyberSecurity #MITREATTACK #Sigma

## X (EN) — ≤ 280 chars
Open-source digital-forensics lab: 5 topics on real evidence, hashed before and after analysis (19 records · PASSED), 15 failed logons surfaced via Event 4625, 3 Sigma rules, 16 MITRE techniques.
github.com/moain2028/digital-forensics-lab
#DFIR

## Instagram (EN) — carousel caption
Real evidence never reaches the student in most forensics courses. This lab changes that 👇

Swipe:
1️⃣ Problem: slides, not a single extracted artifact
2️⃣ Solution: five topics, one method — acquire, hash, analyse, document, re-hash
3️⃣ How it works: from Event 4625 to a brute-force pattern mapped to MITRE T1110
4️⃣ Numbers: 5 topics · 19 browser records · 7 USB devices · 16 MITRE techniques
5️⃣ Who it's for: cybersecurity and DFIR students

Public repo — link in bio.
#DFIR #DigitalForensics #CyberSecurity #Sigma #MITRE

## Reel script (EN) — 25.5 s, 6 scenes, no music (added at publish time)
| # | Dur | On screen | Editor note |
|---|---|---|---|
| 1 | 4s | Forensics taught from slides? / Real evidence never reaches the student | text card |
| 2 | 5s | Five topics on real evidence / Registry · Event Log · Autopsy · FTK Imager · Browser | chrome://history shot (clean lab profile) |
| 3 | 5s | Event 4625: brute-force pattern / 15 failed logons mapped to MITRE T1110 | PowerShell shot, User column blurred |
| 4 | 5s | Unified timeline, MITRE-tagged / Arabic HTML report from one command | report shot |
| 5 | 5s | Hashed before and after / 19 · 7 · 3 / Integrity re-check: PASSED | Chain of Custody shot |
| 6 | 4s | Public repo — reproduce it / github.com/moain2028/digital-forensics-lab | closing card |
