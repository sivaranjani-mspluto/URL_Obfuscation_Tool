# 🌐 URL Obfuscation & Deobfuscation Tool

A simple Python-based tool to encode and decode URLs using **URL encoding** and **Base64**. Useful for cybersecurity learners and analysts to understand how attackers hide malicious links — and how to reveal them.

---

## Features

- Obfuscate any URL using:
  - URL Encoding (`https://example.com → https%3A%2F%2Fexample.com`)
  - Base64 Encoding (`https://example.com → aHR0cHM6Ly9leGFtcGxlLmNvbQ==`)
- Deobfuscate URLs back to original
- CLI interface (no external libraries required)

---

## Use Cases

-  Analyze suspicious/phishing links
-  Practice decoding obfuscated malware URLs
-  Learn URL manipulation techniques in cybersecurity

---

## How to Run

```bash
python url_obfuscation_tool.py
```
## Sample Ouput
- Obfuscate a URL
  ![image alt]()
- Deobfuscate a URL
  ![image alt]()
