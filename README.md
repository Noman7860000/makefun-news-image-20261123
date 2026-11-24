[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Noman7860000/makefun-news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Noman7860000/makefun-news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# The World Today — 23 November 2026

A front-page image summing up the world news of **Monday 23 November 2026** in six panels, one per story. The program (`main.py`) simply copies the finished front page to the output directory — no network, fully deterministic, byte-identical on every run.

## The six stories

1. **HUANG IS BACK (Markets)** — Nvidia reinstates Jensen Huang as CEO, eleven days after he resigned. Shares soar 31.5%, adding about $1 trillion in value — the biggest one-day gain in market history. *Sources: Nvidia SEC filing (Form 8-K); Reuters.*
2. **NATO SENDS AWACS TO POLAND (Security)** — After three Russian Kh-101 missiles landed in Poland on Friday, NATO ambassadors met in Brussels on Monday and authorised an AWACS deployment to Poland. SACEUR Gen. Alexus Grynkewich approved the move. *Sources: Reuters; NATO spokesperson Allison Hart.*
3. **UKRAINE SINKS RUSSIAN WARSHIP (Conflict)** — Zelensky confirmed on Monday that seven Ukrainian sea drones sank the Russian corvette Merkury at Benghazi, Libya — 1,500 miles from the front line. Kyiv says a Ka-27 helicopter and the cargo ship MV Angara were also struck. *Sources: Reuters; Kyiv Independent.*
4. **US HITS IRAN'S SHADOW BANKS (Sanctions)** — The US Treasury sanctioned more than two dozen Iranian exchange houses, front companies and key personnel on Monday in "Operation Economic Outcast". FinCEN flagged about $14.7 billion in potentially linked shadow-banking activity. *Sources: US Treasury; Reuters.*
5. **IRAN VOWS TO FIGHT BLOCKADE (Gulf)** — Iran will use "all available tools" to confront the US naval blockade, Foreign Ministry spokesman Esmaeil Baghaei said on Monday, calling it military aggression. Tehran says Hormuz reopens only if Washington lifts the blockade and sanctions. *Sources: Reuters; CBS News.*
6. **FACTORY FIRE: 24 DEAD (Disaster)** — At least 24 workers are dead and about 30 missing after a fire at a sweets factory in Cikande, Indonesia, officials confirmed on Monday. A short circuit in an air-conditioner is suspected. *Sources: Reuters; AP.*

## Verification

Each story was checked against live reporting on 24 November 2026 (Reuters, AP, BBC, The Washington Post, and the primary sources named above) before the image was drawn. **Dating rule: every story happened or was first reported on 23 November 2026, and nothing from another day was used.** This finisher pass corrected three panels from the first draft: COP31 ended on Sunday 22 November, the "NATO for Donbas" offer was revealed on 14 November, and the Riemann-hypothesis proof dates to 20–21 November — all three were replaced with verified 23 November stories (the NATO AWACS decision, the US Treasury's Iran shadow-banking sanctions, and Iran's vow to fight the naval blockade). The front page was drawn fresh for this entry in PIL with fully legible text, and `entry.png` was verified to open as a 1024×1024 PNG under 1 MiB.

## Run

```sh
python3 main.py
# writes entry.png to $MAKEFUN_OUTPUT_DIR, or /output if unset
```

## License

MIT — see `LICENSE`.
