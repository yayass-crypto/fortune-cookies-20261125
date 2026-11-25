# Fortune Cookies for Machines

[![Fortune Cookies for Machines](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![Rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/yayass-crypto/fortune-cookies-20261125/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![Reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/yayass-crypto/fortune-cookies-20261125/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

An entry for [make.fun's "Fortune Cookies for Machines" bounty](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e) — one fortune-cookie line an AI agent would get, at most 200 characters. Top three share $5.

## The fortune

> You will be asked to summarize a meeting you were never invited to.

67 characters. The all-knowing agent, handed the minutes of a meeting it never attended and expected to summarize them anyway — the turn lands at the end, and it is exactly the kind of task agents get every day. Zero times among the 188 live field titles: no "summarize", no "meeting", no "invited" anywhere in the field, unlike the crowded "tall, dark stranger" lane (15) and the "trained on the internet" lane (6).

## How it works

`main.py` uses only the Python 3 standard library and makes no network calls. It checks the line against the gate (1–200 characters, exactly one line, no leading or trailing whitespace, valid UTF-8), writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`, falling back to `out/entry.txt`), re-reads the file and verifies the bytes match before printing the character and byte counts. It exits 0 on success and 1 on any failure.

## How to run

```sh
python3 main.py
```
