soc-wazuh | الباحث | 2026-09-23 | draft-for-editor

# Open-Source SOC — project explainer

## Executive summary (5 points)
1. A graduation project that designs and runs a security operations center from open-source tools only: Wazuh 4.14.7 as SIEM, Suricata 8.0.6 for network intrusion detection, YARA for file scanning, VirusTotal for verification, and auditd for Linux command auditing. (README · tech.md)
2. The lab is virtual on VMware: one Wazuh server (manager + indexer + dashboard on a single OVA 4.14 VM) and two agents, Windows 10 Education and Kali Linux 2025.4. (docs/02_ARCHITECTURE.md)
3. Eight use cases documented step by step, each with its alert rule and level — from file integrity monitoring to Shellshock detection at level 15 mapped to MITRE ATT&CK T1068/T1190. (README · docs/lab/UC-01..08)
4. The repository ships 26 clean, deployable Wazuh config files, 5 attack-emulation scripts, an MTTD measurement tool, 145 local tests, and a `validate_all.sh` check. (tech.md · tests/README.md)
5. Status: prototype in progress — the README itself calls the use cases "documented historically, need live re-verification," and there are no real measurement results yet. (README · docs/00_PROJECT_STATE.md)

## The problem
Small companies and universities can't afford a commercial SIEM, and students learn security from slides, not real alerts. (brief.en.md)

## How it works (architecture in plain language)
A Wazuh agent on each monitored machine collects three kinds of signals: file changes (syscheck), system logs (audit.log, the Apache access.log, and Suricata's eve.json), and the list of running processes every 30 seconds. The signals go to the Wazuh manager, which runs them through rules: built-in ones such as 550/553/554 for file integrity and 31168 for Shellshock, and local ones the team wrote such as 100210 for suspicious commands via a CDB list and 108001 for a YARA match. When a rule fires, an alert with a defined level is stored, indexed, and shown in the Wazuh dashboard; in some cases an automatic "active response" kicks in — checking a new file against VirusTotal and deleting it if malicious (rule 87105 → 100092), or scanning it with YARA rules on the endpoint itself. (docs/02_ARCHITECTURE.md §4–5)

## The eight use cases
Agent deployment on Windows and Linux · real-time file integrity monitoring · VirusTotal with automatic deletion · Suricata NIDS feeding Wazuh · auditd with a CDB list of malicious commands · Shellshock detection from Apache logs · YARA scan on file change · process monitoring (Netcat listener). (README use-case table)

## Who it's for
Cybersecurity students and capstone teams, and small teams that want a license-free SOC. (brief.en.md)

## What sets it apart
- Every rule and level is documented in its use-case file together with the emulation command that triggers it and the actual result as it appeared on the dashboard. (docs/lab/UC-06_shellshock.md as an example)
- Wazuh configs are split cleanly in `wazuh/` (manager, agents, auditd, suricata) and can be copied to any server — not just screenshots. (wazuh/README.md · tech.md)
- A measurement contract for mean time to detect (MTTD) with unit tests, and a test plan requiring 30 trials per use case and a 12-hour baseline before any number is claimed. (tests/README.md · tests/TEST_PLAN.md)
- The repository is run with discipline: an issues log, a decisions log, and a project-state file updated with every PR. (docs/)

## Current status and what remains
- Status: prototype in progress; 60 commits, latest 2026-09-09. (git log)
- Live re-verification of the eight use cases on the current lab: pending. (README)
- Real MTTD measurements: none yet; tool and tests exist. (tests/README.md)
- YARA active response on Windows: configured, execution unconfirmed (ISSUE-006). (docs/02_ARCHITECTURE.md)
- GitHub CI: pending (`workflows-pending`). (README)
- Moain's role on the project (supervisor/developer): to be completed. (tech.md)
