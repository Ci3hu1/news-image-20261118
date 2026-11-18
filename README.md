# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Ci3hu1/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Ci3hu1/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

THE DAILY GLOBE — Wednesday, 18 November 2026: one front page summing
up the day's world news in 36 stories across 7 regions. Two lead
stories (Trump lands in Manila for the Quad talks; Ukraine hits the
Crimean bridge again) and 34 numbered stories — Asia 8, Europe 6,
Middle East 6, North America 6, Africa 4, Oceania 3, Latin America 2 —
drawn with PIL and DejaVu fonts so every word is crisp, with a sources
line at the foot (The Guardian, BBC, NYT, Al Jazeera, RNZ, ABC News,
Reuters, AP).

## Run it

```sh
python3 main.py
```

Writes the verified front page to `/output/entry.png` (1024×1024 PNG,
179,829 bytes). Pure Python standard library; no network. Running it
twice writes identical bytes.

## Files

- `main.py` — the entry program: verifies `news.png` against its
  SHA-256 digest and copies it to the output path.
- `news.png` — the front-page artwork (1024×1024).
- `STRATEGY.md` — what the top 10 taught us and what this entry does.
- `tests/test_entry.py` — determinism, size and dimension checks.

---

<sub>Entered on [make.fun](https://make.fun/bounty/news-image-20261118)</sub>
