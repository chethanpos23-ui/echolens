# Security Policy

## Scope

EchoLens is a hackathon prototype maintained as a public case study. It has **not** been
through a professional security review and it is not intended for production deployment. Please
read that as a real limitation rather than boilerplate.

## Reporting a vulnerability

Do not open a public issue for a security problem.

Report it privately through GitHub's [private vulnerability
reporting](https://github.com/chethanpos23-ui/echolens/security/advisories/new), or by email to the
address on the maintainer's GitHub profile.

Please include:

- What the issue is and roughly how severe you think it is
- Steps to reproduce, or a proof of concept
- The commit or version you tested

## What to expect

| Stage | Target |
|---|---|
| Acknowledgement | Within 5 days |
| Initial assessment | Within 14 days |
| Fix or documented decision not to fix | Depends on severity and scope |

This is a personal project, not a funded product, so these are honest targets rather than an SLA.

## Out of scope

- Findings that only apply to a deliberately insecure demo or sample configuration
- Missing hardening in the local development Docker Compose setup, which is not meant to be
  exposed to a network
- Dependency advisories with no demonstrated path to exploitation in this codebase

## Secrets

If you find a credential committed anywhere in this repository's history, report it as a
vulnerability. The project intends to contain no real credentials of any kind — every integration
is configured through environment variables and every checked-in example uses placeholder values.
