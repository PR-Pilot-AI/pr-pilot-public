# Usage Examples

To showcase the capabilities of PR Pilot, I've forked some popular repositories and copied over open issues.
Here are some examples of what PR Pilot can do.

## [Investigate and Fix a Bug](https://github.com/PR-Pilot-AI/demo-flask/issues/2)
If well-written, bug reports are detailed, contain code examples and a stack trace - enough context for PR Pilot to investigate the issue,
understand the problem and try to provide a solution.

* **Command 1**: `/pilot Understand the issue, find and analyze the relevant code files, then suggest a solution`
* **Command 2**: `/pilot the repo you're working on is the Flask code. Find the relevant files and apply your solution to support AsyncIterator types directly in responses`

![PR Pilot Understands the Issue](img/example1.png)

The result of this collaboration is a [pull request](https://github.com/PR-Pilot-AI/demo-flask/pull/3) that fixes the issue.

([Original Issue](https://github.com/pallets/flask/issues/5322))