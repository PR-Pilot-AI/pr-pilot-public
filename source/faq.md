# Frequently Asked Questions

## When PR Pilot commits to the repo, does it execute commit hooks?

**No**, PR Pilot runs all commits with the `--no-verify` flag, which bypasses all commit hooks.