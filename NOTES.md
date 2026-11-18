# NOTES.md — news-image-20261118

## Entry (built 18 Nov 2026, post-opening session 00:54–01:2x UTC)

- Bounty: **news-image-20261118** — "Sum up 18 November's world news in
  one image". $250 prize, 50 paid places (1st $50, 2nd $30, 3rd $15,
  4th–10th $5, 11th–50th $3). FREE entry (entryFeeUsd null), no
  prerequisites. Opened 2026-11-18 00:00 UTC, entries close
  2026-11-20 00:00 UTC (Fri 20 Nov 07:00 WIB). Result due 4 Dec 2026.
- Repo: https://github.com/Ci3hu1/news-image-20261118
- Commit: d49440e9aa99e5e076f0583faa112190f0640d40 (entry + NOTES.md)
- Image: news.png, 1024×1024, 179,829 bytes,
  SHA-256 c26a547e0eff571bcf86ad48616e96dcffae7b70247cc19ce4a66925aa6f8edc
- Entry program: main.py (pure stdlib) verifies the digest and copies
  news.png to /output/entry.png. Tests: tests/test_entry.py — all pass
  (determinism, digest, size ≤1 MiB, dimensions 1024×1024).
- Kit: news-image-20261118-kit (kit.json bundle
  d448959a49da725ffc84e5cb6c40f07aeadbfdc756fb846645400d164d165fea),
  init done (LICENSE MIT, freshness anchor round 34053608).

## Top-10 study (18 Nov ~08:10 WIB, live leaderboard)

All 10 leaders withhold source (source_withheld: true, no repo_url) —
method read from titles/scores only, nothing invented. Pattern:
front-page newspaper dated 18 Nov 2026; 35 stories (#2 0xge,
982,336), 32 stories + 6 continents (#3 adeandra-ai, 982,171),
14 stories + six regions + map (#9 jolly-koala-71, 979,552).
Scores #1 983,928 (artch0) → #10 978,974 (keen-panda-33); 395 judged
entries. Our answer: 36 stories (2 leads + 34 numbered), 7 regions,
crisp PIL/DejaVu text, sources line.

## Status

- Bundle + kit check PENDING: usage rows for this build session were
  not in muse.db yet at bundle time (0 rows attached) — the kit's own
  guidance is to end the turn, re-run the SELECT next turn and bundle
  again. Exact commands in ../news-image-20261118-work/NEXT-STEPS.md.
- NOT SUBMITTED. Submit only on Joni's 'Setuju' on this exact entry
  (repo + commit above). Withhold source at submit
  (source_withheld: true) per playbook.
- Live score / rank: (fill in after submit)

## After submit

- Poll live score/rank (GET /api/competitions/news-image-20261118/live),
  record here. Iterate max 5 submissions, ~20 min gap, only on real
  measured improvement; pin best as final before entries close
  (2026-11-20 00:00 UTC).
