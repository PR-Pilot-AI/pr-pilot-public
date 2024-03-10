# Examples

To showcase the capabilities of PR Pilot, I've forked some popular repositories and copied over open issues.
Here are some examples of what PR Pilot can do.

## [Investigate a Bug Report](https://github.com/PR-Pilot-AI/demo-langchain/issues/1)
Someone reported an issue they've had using the `langchain` library. The bug report is detailed, contains code 
examples and a stack trace. PR Pilot can read the issue, understand the problem, search the web and try to provide a solution.

**Command**: `/pilot Find out what could be the issue and if the problem is in our code`

([Original Issue](https://github.com/langchain-ai/langchain/issues/18809))


## [Understand and Document Code](https://github.com/PR-Pilot-AI/demo-langchain/issues/2)
Here I've created an artificial issue that mentions a part of the code in the `langchain` repo that could be better documented.
PR Pilot can read the issue, understand the code, search for the code in the repository and suggest a better documentation.

**Command**: `/pilot Look at the existing documentation, find out how get_openai_callback works under the hood and provide the content to extend the documentation`