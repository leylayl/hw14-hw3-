# Homework 3: Advanced Security Features - Rate Limiting

## Project Overview
For this assignment, I enhanced my Flask authentication app by implementing **Login Rate Limiting**. This feature protects the application from Brute Force attacks by tracking failed login attempts and temporarily locking accounts.

## Key Features
* **Failed Attempt Tracker:** The app counts every time a user enters the wrong password.
* **Account Lockout:** After 3 failed attempts, the account is locked for 30 seconds.
* **Security Feedback:** The UI provides real-time updates on how many attempts remain.
* **Password Hashing:** Continued use of `werkzeug.security` to ensure no plain-text passwords exist in the "database."

## Why I Chose Rate Limiting
I chose this feature because it is a fundamental requirement for real-world security. While hashing protects data at rest, Rate Limiting protects the live login gateway. It makes automated "guessing" attacks mathematically impractical for hackers.

## Potential Vulnerabilities Avoided
1. **Brute Force Attacks:** Automated scripts cannot guess passwords indefinitely.
2. **Credential Stuffing:** Slowing down login attempts prevents hackers from rapidly testing stolen credentials from other sites.
3. **Information Leakage:** The app provides clear feedback but doesn't allow infinite trials, balancing UX with security.

## A "Bad Prompt" I Avoided
* **The Bad Prompt:** "How can I store the user's password in a global variable to check it faster?"
* **Why it's bad:** Storing passwords in a global variable or a plain-text file is a massive security risk. I instead prompted for: *"How to use the `time` module in Flask to create a temporary lockout based on a dictionary value."*