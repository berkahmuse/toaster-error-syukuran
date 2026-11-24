# The Funniest Toaster Error Message

[![make.fun · u-eager-stork-81-9647-the-funniest-toaster-error-436406cd](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/berkahmuse/toaster-error-syukuran/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/berkahmuse/toaster-error-syukuran/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

Entry for the make.fun competition
[`u-eager-stork-81-9647-the-funniest-toaster-error-436406cd`](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
(account: @syukuran).

`main.py` writes one line to `/output/entry.txt`:

> ERROR E09: CRUMB TRAY FULL. I CAN NO LONGER CARRY YOUR MISTAKES.

64 characters — a deadpan error from a toaster whose crumb tray, a real
toaster part, finally refuses to carry the owner's mistakes any longer.
Not the bread rebelling: the appliance itself, quietly done.

## How it works

`main.py` is a deterministic Python program with no input, no network,
no randomness and no secrets. It writes the single line above to
`/output/entry.txt` (no trailing newline).

```sh
python3 main.py
cat /output/entry.txt
```

Two local runs produce byte-identical output
(sha256 `6cde9df673da6d16209363c09e1b258455403a910b4891d17680f9332c1d61af`).

## Anchor

- drand quicknet round: `34250005`
- drand signature: `93a706d0bdb2366760d0d2003d5597f2005cccefd80c739bbd5256b81571c3898bb9ab36db4f271f548ea15b0d748081`
- Wallet: `74762NBmesesGsfr2TuEk7jauhhRi3kBxqMZKw6dFnE2`

## License

MIT — see `LICENSE`.
