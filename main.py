#!/usr/bin/env python3
"""One-line slogan for a Solana wallet agent.

Writes exactly one line (max 20 words) to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os

SLOGAN = "Your keys. Your SOL. Your rules. A wallet as fast as Solana itself."
# 13 words, under the 20-word cap. Triple "your" = ownership; the second
# sentence ties the wallet's speed to Solana itself.

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SLOGAN + "\n")

if __name__ == "__main__":
    main()
