# RoundUpMicroSaver
# Round-Up Micro-Saver (AGRS)

A tiny, Python-based “spare-change” savings tool that **rounds every purchase up** to the next dollar (or any configured granularity), **accumulates** the deltas in a pool, and **automatically transfers** a fixed threshold into savings. It’s lightning-fast, uses only **O(1)** memory, and comes with full tests and a benchmark.

---

## Features

- **Configurable granularity**: round to \$1.00, \$0.50, \$0.10, etc.  
- **Adaptive threshold** (optional): adjust transfer amount based on your spending patterns.  
- **O(1) per-transaction** performance (modulus + addition).  
- **Automated tests** (pytest) + **performance smoke test**.  
- **Error-bound guarantee**: pool always stays below `max(granularity, threshold)`.

---

## Prerequisites

- Python ≥ 3.7
- (optional) [virtualenv](https://docs.python.org/3/library/venv.html)
- `pytest` for running the test suite

---

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Bawer-Bajelori/round-up-saver.git
   cd round-up-saver

