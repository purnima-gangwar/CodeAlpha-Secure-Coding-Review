# CodeAlpha Cyber Security Internship
## Task 3: Secure Coding Review

### 1. Objective
To review a Python application for common security vulnerabilities, identify risks, and recommend secure coding practices.

### 2. Tools Used
- Python 3.11.9
- Bandit Static Analysis Tool
- Visual Studio Code

### 3. Application Overview
A sample Python application was reviewed to identify insecure coding practices.

### 4. Vulnerabilities Identified

**Finding 1: Hardcoded Password**
- Issue: A password was stored directly in the source code.
- Risk: Credentials may be exposed if the code is shared.
- Severity reported by Bandit: Low.
- Recommendation: Store secrets in environment variables or a secret manager.

**Finding 2: Unsafe Use of eval()**
- Issue: The application used `eval()` to evaluate an expression.
- Risk: Untrusted input could execute unintended code.
- Severity reported by Bandit: Medium.
- Recommendation: Remove `eval()` and use explicit, allowlisted operations.

### 5. Remediation
A corrected version of the sample application was created. The hardcoded password was removed and `eval()` was replaced with allowlisted operations.

### 6. Verification
The original application was scanned using Bandit and two findings were identified. The corrected application was scanned again, and Bandit reported no issues identified.

### 7. Conclusion
The review demonstrated how static analysis and manual code inspection can help identify and remediate common security weaknesses. A clean static analysis result does not guarantee complete application security.
