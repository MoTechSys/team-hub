digital-forensics-lab | الباحث | 2026-09-23 | v2 — D (300–500-word explainer + summary)

# How the digital-forensics lab works — from artifact to report

Most digital-forensics courses are taught from slides. Students learn that the Windows Registry remembers USB devices, that the Event Log records logon attempts, and that Autopsy reads disk images — but they rarely extract a single artifact themselves and prove it did not change between acquisition and report. This repository flips that: each of the five required topics (Registry, Event Log, Autopsy, FTK Imager, Browser Forensics) is executed on real evidence and documented with a screenshot and a hash.

**One method for every topic.** Acquire the evidence and record its size and hashes immediately; compare the computed hash with the one stored by the acquisition tool; work on a copy, never the original; analyse with the tool; screenshot every step showing where the artifact lives and how it was extracted; then re-hash at the end to prove the evidence was untouched. These six steps are written in `docs/METHODOLOGY.md` and appear in practice on every path.

**Linux side: browser history.** Chromium browsers keep history in a SQLite database named `History`, with timestamps in microseconds since 1601 (WebKit epoch), not Unix time. The parser `browser_history_parser.py` — Python standard library only — first copies the file to a scratch directory (opening SQLite directly creates journal/WAL files that alter the evidence), opens it read-only, decodes the timestamps, writes CSV and HTML, then recomputes MD5 and SHA-256 and compares. We re-ran it on 2026-09-23: 19 records, both hashes identical to the README, result "Integrity re-check: PASSED".

**Windows side: one command.** `Run-Windows-Forensics.ps1`, run from an elevated PowerShell, pulls system information (`CurrentVersion`), USB devices with serials (`USBSTOR`) and last-executed programs (`BAM`) from the Registry, and successful logons 4624, failed logons 4625, log clearing 1102 and boot/shutdown 6005/6006 from the Security log. It merges them into a unified timeline where each row carries a MITRE ATT&CK tag (T1078 for logons, T1091 for removable media), computes SHA-256 for every extracted file into `chain_of_custody.csv`, and renders an Arabic RTL HTML report. In the bundled evidence, 15 failed logons against one account from 127.0.0.1 over eight days surfaced — a brute-force pattern mapped to T1110 — along with 7 USB devices and their serials.

**Detection as code.** Three original Sigma rules turn what the student learned into deployable detection: Security log cleared (1102), an executable run from a USB drive, and a suspicious PowerShell download cradle — each tagged with MITRE ATT&CK.

**Autopsy and FTK Imager.** A Digital Corpora disk image (`nps-2009-canon2-gen6.E01`) was converted to raw and its MD5 matched the stored value; the file tree was rebuilt and a deleted file (`_MG_0025.JPG`) identified by the `*` marker in `fls`; a case was created in Autopsy 4.21.0 up to the add-data-source step. FTK Imager is documented step by step: physical drive, image format, case details, then the "Match" verification result for MD5 and SHA-1.

## Five-point summary
1. Five forensic topics on real evidence, one method: acquire → hash → copy → analyse → document → re-hash.
2. A dependency-free browser-history parser that works on a copy and re-verifies MD5/SHA-256; re-run locally: 19 records, PASSED.
3. A one-line PowerShell runner that extracts Registry and Event Log into a MITRE-tagged timeline with a SHA-256 chain of custody for seven files.
4. A real case surfaced: 15 failed logons (Event 4625) in a brute-force pattern mapped to T1110, plus 7 USB devices with serials.
5. Three original Sigma rules and 16 MITRE ATT&CK techniques referenced in code — detection written as rules, not slides.
