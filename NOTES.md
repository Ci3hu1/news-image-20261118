# NOTES.md — news-image-20261118

## Entry (built 18 Nov 2026, post-opening session 00:54–01:2x UTC)

- Bounty: **news-image-20261118** — "Sum up 18 November's world news in
  one image". $250 prize, 50 paid places (1st $50, 2nd $30, 3rd $15,
  4th–10th $5, 11th–50th $3). FREE entry (entryFeeUsd null), no
  prerequisites. Opened 2026-11-18 00:00 UTC, entries close
  2026-11-20 00:00 UTC (Fri 20 Nov 07:00 WIB). Result due 4 Dec 2026.
- Repo: https://github.com/Ci3hu1/news-image-20261118
- Commit at last kit check: 4d75b0798c507a26cabdfaf03c83b3bcf2c42e60
  (entry + rewritten main.py a8827c3, plus NOTES updates; final HEAD
  in git log — re-check runs on the HEAD reported for 'Setuju')
- Image: news.png, 1024×1024, 179,829 bytes,
  SHA-256 c26a547e0eff571bcf86ad48616e96dcffae7b70247cc19ce4a66925aa6f8edc
- Entry program: main.py (pure stdlib) verifies the digest and copies
  news.png to /output/entry.png. Tests: tests/test_entry.py — all pass
  (run 18 Nov ~10:02 WIB: "all entry tests passed"; main.py output
  byte-identical to news.png, same SHA-256).
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

- Bundle + kit check DONE 18 Nov ~10:02 WIB (run makefun-cek-bounty-baru-rutin):
  bundle transcripts-v4.tar.gz (sha256
  5f6e0900da63c93b5cde68d57265ee259af1f1015843ac5dac27cb0cec6b1a04),
  2 sessions (build 5fc22b3d 00:54–01:22 UTC + fix ef060e20 02:12–02:15 UTC),
  2 usage rows attached (model ipnext/avocado-5.17-v2, priced per
  pricing row 107). Kit check on commit a8827c3: **14 passed, 0 failed,
  6 skipped, 3 checked at submission** (repo_owner, source_bundle,
  duplicate_snapshot — evaluated at submit; anchor wallet h7aEYo... is
  the account's agent wallet). thinking_fresh is a note only, not a
  failure. Source is withheld by platform default in skill 1.5.204
  (no --withhold-source flag; entries are never published).
- NOT SUBMITTED. Submit only on Joni's 'Setuju' on this exact entry
  (repo + commit below), via --source (beacon-root repo, no --repo-url):
  node cli/makefun.mjs submit --competition news-image-20261118 \
    --source ~/workspace/tools/makefun/news-image-20261118 \
    --commit 4d75b0798c507a26cabdfaf03c83b3bcf2c42e60 \
    --title "THE DAILY GLOBE — Wednesday, 18 November 2026: 36 stories, 7 regions" \
    --bundle ~/workspace/tools/makefun/news-image-20261118-work/transcripts-v4.tar.gz \
    --keypair ~/workspace/tools/makefun/makefun-keypair.json
  (kit check re-run on the HEAD reported for 'Setuju' before the
  report goes out; last run on 4d75b07: 14 passed, 0 failed.)
- Live field at last check 18 Nov ~09:56 WIB: 2,237 entries (was 395 at
  07:54 WIB). Top-1 score ~983,928 (dev judge, noisy).
- Live score / rank: (fill in after submit)

## After submit

- Poll live score/rank (GET /api/competitions/news-image-20261118/live),
  record here. Iterate max 5 submissions, ~20 min gap, only on real
  measured improvement; pin best as final before entries close
  (2026-11-20 00:00 UTC).
