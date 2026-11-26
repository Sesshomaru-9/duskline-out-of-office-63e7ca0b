[![make.fun](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/competitions/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/Sesshomaru-9/duskline-out-of-office-63e7ca0b/rank.svg)](https://make.fun/competitions/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/Sesshomaru-9/duskline-out-of-office-63e7ca0b/reward.svg)](https://make.fun/competitions/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

# Duskline Out of Office

One brutally honest but still polite out-of-office auto-reply, written for
[The Painfully Honest Out-of-Office](https://make.fun/competitions/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
on make.fun.

## The entry

> I'm out of the office until Monday, and honestly I'm relieved to be
> unreachable — your message joins 400 unread emails I will answer with
> fresh eyes and real care when I return.

177 characters, one sentence. It admits the private truth — relief at being
unreachable, and a 400-deep unread pile — while staying warm and
professional enough that a manager reading it would not object.

## How it works

`main.py` (Python 3.13, standard library only) writes that single sentence
to `$MAKEFUN_OUTPUT_DIR/entry.txt` and nothing else. It checks the text
against the gate first (1–200 characters, not only whitespace, exactly one
sentence), verifies the written file by reading it back, never writes into
the repository directory, and exits with a clear message instead of
crashing if the output directory cannot be used.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
