# How it works

Here is what happens when you say `/pilot <command>` in a comment on an issue or PR:

1. **PR Pilot** reads your comment and understands your command using GPT-4.
2. It adds a reaction to your comment so you know the command was received
3. A new Docker container is created and your code is checked out into it.
4. **PR Pilot** runs your command in the container. Depending on your command, it will read, write, move, or delete files in your repository, search for code, read and write to issues and PRs, and browse the web to find information.
5. While it is executing the task, it will create events that you can follow in the [dashboard](https://app.prpilot.ai).
6. Once the task is complete, the container is deleted.