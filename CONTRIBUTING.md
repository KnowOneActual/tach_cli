# Contributing to Tach CLI

Thanks for your interest in contributing!

Tach is a lightweight terminal clock + countdown timer aimed at **live productions, events, and structured meetings**. The core idea is simple visual pacing (large auto-scaling time, color thresholds, overtime) while aggressively avoiding feature creep.

## Ground rules (scope)

Please help us keep Tach focused:

- Prioritize “big readable time” and pacing features (countdown, clock mode, overtime, threshold colors).
- Avoid adding complex menus, data logging, analytics, or “app-like” settings screens unless there’s clear user demand.
- If you’re unsure whether something fits, open an issue first.

## How to contribute

### 1) Issues (best place to start)
- Bug reports: include OS, terminal emulator, steps to reproduce, and what you expected vs. what happened.
- Feature ideas: explain the live-production use case and what problem it solves.

### 2) Pull requests
- Keep PRs small and focused (one improvement per PR).
- If the PR changes the command surface (new flags/args/subcommands) or behavior, please link an issue with agreed acceptance criteria.

Suggested workflow:
1. Fork the repo and create a feature branch: `git checkout -b your-branch-name`
2. Make changes with clear commit messages (see below).
3. Open a PR and describe: what/why, how to test, screenshots if UI changes.

## Commit messages (recommended)

We recommend Conventional Commits, because it keeps history readable and makes changelog/release notes easier:

- `feat: add timer overtime display`
- `fix: handle terminal resize glitch`
- `docs: update usage examples`

(Format: `type(scope optional): description`)  

## Changelog updates

We use a Keep a Changelog-style `CHANGELOG.md` with an `Unreleased` section at the top.

- For doc-only changes, add a bullet under `Unreleased -> Changed` or `Unreleased -> Added`.
- For user-visible behavior changes, add a bullet under the appropriate category.

## Style / quality

- Prefer clarity over cleverness (this tool is for high-stress production environments).
- Add tests when the project has a test harness for the area you’re touching.
- If you change keybindings/flags/defaults, update README usage examples too.

## Code of Conduct

Be respectful, assume good intent, and keep feedback actionable.
