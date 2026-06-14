# Security Policy

## Scope

This is an offline governance toolkit. It reads local YAML/Markdown and writes
local files; it makes no network calls and stores no credentials.

## Reporting a vulnerability

Please **do not open a public issue** for security problems (for example, a YAML
deserialization issue or a dependency advisory). Use GitHub's
[private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability)
via the **Security → Report a vulnerability** tab. I aim to acknowledge reports
within 5 business days.

## Notes for adopters

- YAML is parsed with `yaml.safe_load` only — never `yaml.load` with the full loader.
- Treat governance artifacts (model cards, DPIAs) as potentially containing
  sensitive information; review before publishing them.
- Dependencies are monitored via Dependabot.
