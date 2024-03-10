# Privacy Notice

We **never store** code permanently. Every `/pilot` command is run in the following way:

1. We check out your code in an **isolated** Docker container
2. PR Pilot  uses GPT-4 to understand your command 
3. It reads/writes the necessary files 
4. The container is deleted