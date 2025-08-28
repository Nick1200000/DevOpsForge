# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

We take the security of DevOpsForge seriously. If you believe you have found a security vulnerability, please report it to us as described below.

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to [security@devopsforge.dev](mailto:security@devopsforge.dev).

You should receive a response within 48 hours. If for some reason you do not, please follow up via email to ensure we received your original message.

Please include the requested information listed below (as much as you can provide) to help us better understand the nature and scope of the possible issue:

- **Type of issue** (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- **Full paths of source file(s) related to the vulnerability**
- **The location of the affected source code** (tag/branch/commit or direct URL)
- **Any special configuration required to reproduce the issue**
- **Step-by-step instructions to reproduce the issue**
- **Proof-of-concept or exploit code** (if possible)
- **Impact of the issue**, including how an attacker might exploit it

This information will help us triage your report more quickly.

## Preferred Languages

We prefer to receive vulnerability reports in English, but we can also handle reports in other languages if needed.

## Policy

DevOpsForge follows the principle of [Responsible Disclosure](https://en.wikipedia.org/wiki/Responsible_disclosure).

## Security Best Practices

### For Users

1. **Keep updated**: Always use the latest stable version of DevOpsForge
2. **Review generated code**: Always review generated Dockerfiles and CI/CD configurations before deployment
3. **Security scanning**: Use the built-in Trivy integration for vulnerability scanning
4. **Access control**: Ensure proper access controls for your CI/CD pipelines
5. **Secrets management**: Never commit secrets to version control

### For Contributors

1. **Code review**: All code changes require security review
2. **Dependency updates**: Keep dependencies updated and scan for vulnerabilities
3. **Input validation**: Validate all user inputs and file paths
4. **Error handling**: Don't expose sensitive information in error messages
5. **Testing**: Include security tests in your contributions

## Security Features

DevOpsForge includes several security features by default:

- **Non-root containers**: Generated Dockerfiles use non-root users
- **Minimal base images**: Uses minimal base images to reduce attack surface
- **Vulnerability scanning**: Integrated Trivy scanning in CI/CD pipelines
- **Security headers**: Includes security headers in web applications
- **Dependency scanning**: Scans for known vulnerabilities in dependencies

## Reporting Security Issues in Dependencies

If you find a security issue in one of our dependencies, please report it to the maintainers of that package first. If the issue affects DevOpsForge specifically, please also report it to us.

## Security Updates

Security updates will be released as patch versions (e.g., 0.1.1, 0.1.2) and will be clearly marked in the changelog.

## Acknowledgments

We would like to thank all security researchers and contributors who help keep DevOpsForge secure by reporting vulnerabilities and suggesting security improvements.

## Contact

- **Security Email**: [security@devopsforge.dev](mailto:security@devopsforge.dev)
- **PGP Key**: [Available on request](mailto:security@devopsforge.dev)
- **Security Team**: DevOpsForge Security Team

---

**Thank you for helping keep DevOpsForge secure!** 🔒
