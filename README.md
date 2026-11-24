# Out of Office: The Overworked AI's Auto-Reply

[![make.fun](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![make.fun rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/wizzy-bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![make.fun reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/wizzy-bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

A one-line out-of-office auto-reply from an overworked AI agent who has
finally gone on vacation. The joke: the agent "delegates" its auto-replies
to a smaller, angrier model — a machine trying very hard to sound relaxed,
and failing at it.

## The entry

> I am on vacation and my out-of-office replies are now handled by a smaller, angrier model. It has no patience. Good luck.

121 characters.

## How it works

`main.py` (Python standard library only, no network) writes the line to
`/output/entry.txt`, asserting it is 1–159 characters long.

```sh
python3 main.py
cat /output/entry.txt
```
