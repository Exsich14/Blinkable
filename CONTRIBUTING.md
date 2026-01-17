# Contributing to Blinkable

Thank you for your interest in contributing to Blinkable! We welcome contributions of all kinds — bug reports, feature requests, documentation improvements, tests, and code. This document explains how to contribute in a way that helps maintainers review and accept your changes quickly.

## Table of contents
- How to report a bug
- How to propose a feature
- Development setup
- Submitting changes (pull requests)
- Coding style & commit message guidelines
- Tests & CI
- Code review process
- License and copyright
- Code of Conduct

## Code of Conduct
By participating in this project you agree to follow our Code of Conduct. Be respectful, constructive, and patient. If you encounter or witness unacceptable behavior, please open an issue or contact a maintainer privately.

## How to report a bug
1. Check existing issues to see if the bug is already reported.
2. If not found, open a new issue and include:
   - A clear title and description of the problem.
   - Steps to reproduce.
   - Expected vs actual behavior.
   - Environment details (OS, browser, Node/Python version, etc.) if relevant.
   - Any relevant logs, screenshots, or small code samples.

## How to propose a feature
1. Search existing issues and discussions for duplicates.
2. Open an issue titled like: "Feature: short description".
3. In the issue describe:
   - The problem you want to solve.
   - Why this feature is useful.
   - Suggested design or API (if applicable).
   - Backwards-compatibility considerations.

## Development setup
1. Fork the repo and clone your fork:
   - git clone https://github.com/<Exsich14>/Blinkable.git
   - cd Blinkable
2. Add the upstream remote:
   - git remote add upstream https://github.com/Exsich14/Blinkable.git
3. Create and switch to a topic branch for your work:
   - git checkout -b feat/short-description
4. Run linters and tests locally (see Tests & CI section).

## Submitting changes (pull requests)
1. Keep changes in a single branch with a clear name (e.g. `fix/issue-123`, `feat/new-feature`).
2. Rebase or merge the latest `main` from upstream before opening a PR:
   - git fetch upstream
   - git rebase upstream/main
3. Push your branch to your fork and open a Pull Request against `Exsich14/Blinkable:main`.
4. In the PR description include:
   - Summary of changes
   - Related issue number (if any): `Closes #123`
   - How to test the change
   - Any other notes for reviewers
5. Keep PRs small and focused. Large or sweeping changes may be split into multiple PRs.

## Coding style & commit message guidelines
- Follow existing code style in the repository.
- Run linters and formatters before committing.
- Commit messages should be clear and descriptive. Suggested format:
  - Short (50 chars) summary line
  - Blank line
  - More detailed explanation if necessary
- Optionally use Conventional Commits (e.g. `feat:`, `fix:`, `docs:`) for clarity.

## Tests & CI
- Add or update tests to cover your changes.
- Ensure all tests pass locally before opening a PR.
- CI runs on every PR. Fix any CI failures that appear.
- If your change adds new behavior, include tests demonstrating the expected behavior.

## Code review process
- Maintainers will review PRs and may request changes.
- Be prepared to iterate on feedback.
- Once approved, a maintainer will merge the PR (or ask you to rebase/resolve conflicts).
- Do not merge your own PRs unless you are explicitly authorized.

## Security issues
If you discover a security vulnerability, please do NOT open a public issue. Contact a project maintainer privately (email or GitHub) and provide details so we can address it responsibly.

## License and copyright
By contributing you agree that your contributions will be licensed under the project’s license. Ensure you have the right to submit the code (don’t copy large sections from other projects unless compatible with this license).

## Additional notes
- If your change involves user-visible behavior or documentation, update the README or other docs.
- For larger changes, open a draft PR or discuss the approach in an issue first.

---

Thank you for helping make Blinkable better! If you’d like, I can add this CONTRIBUTING.md to the repository directly — tell me whether to commit it to `main` (and provide preferred commit message), or create a new branch and open a pull request.
