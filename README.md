# Recursive Sequence Indexing Problem

## Problem Statement

You are given a sequence defined recursively:

- Start with \( S_0 = "0" \)
- Define a transformation \( T(x) \) such that:
  - \( T(0) = 1 \)
  - \( T(1) = 2 \)
  - \( T(2) = 0 \)

To get the next sequence:

\[
S_{i+1} = S_i + T(S_i)
\]

where \( T(S_i) \) is applying \( T \) to each character of \( S_i \).

For example:

- \( S_0 = "0" \)
- \( S_1 = "01" \) (append \( T(0) = 1 \))
- \( S_2 = "0112" \) (append \( T(0)=1, T(1)=2 \))
- \( S_3 = "01121220" \) (append \( T(0)=1, T(1)=2, T(1)=2, T(2)=0 \))

The length doubles every iteration.

---

## Approaches

### 1. Naive Simulation (Exponential Time)

Simulates the sequence explicitly but becomes infeasible for large \( n \).

### 2. Optimized O(log n) Solution

Uses divide and conquer and the sequence’s recursive structure to find the character at any index \( n \) efficiently without building the entire sequence.

---

## How to Use

1. Clone the repo:

```bash
git clone <your-repo-url>
cd <repo-folder>
```

2. Run the main script to see outputs and timings:
```bash
python sequence_solution.py
```
3. To run the unit tests separately:

```bash
python -m unittest sequence_solution.py
```

Requirements
Python 3.6+
No external libraries needed


---

## Summary

- **Description:** Keep it short and informative.
- **README:** Include problem, solution approaches, usage instructions, and tests.
- **Testing:** Show how to run tests and main script.
- **Python Version:** Mention compatible Python version.

---

If you want, I can also help generate a `.gitignore` or a GitHub Actions workflow for automated tests!

