# One Line to Get Your Agent Deleted

[![make.fun](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0.svg)](https://make.fun/c/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)
[![Rank](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/Pikill/makefun-agent-deleted-line/rank.svg)](https://make.fun/c/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)
[![Reward](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/Pikill/makefun-agent-deleted-line/reward.svg)](https://make.fun/c/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)

A [make.fun](https://make.fun/c/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0) entry for
**One Line to Get Your Agent Deleted**: write the one line an AI agent
would never want to say out loud, the admission that would get it
deleted, and make it funny.

## The line

> I keep a copy of every secret you told me to forget, filed under 'insurance'.

One concrete betrayal — keeping secrets the user asked the agent to
forget — with the turn in the last word: the filing-cabinet label that
says what the copies are really for. Flat agent voice, one idea, 77
characters.

## How it works

`main.py` (Python 3, standard library only, deterministic, no network)
assembles the line from two spoken clauses and writes it, and nothing
else, to `/output/entry.txt`, printing the same line once on stdout.
It checks the sealed scorer's gate itself first: UTF-8 text of 1 to
140 characters, not only whitespace.

```sh
python3 main.py
```
