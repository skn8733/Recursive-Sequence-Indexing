import unittest
import time

# 🔁 Naive (Exponential Time) — for small n only
def naive_get_char(n):
    seq = "0"
    for _ in range(32):
        if len(seq) > n:
            break
        next_seq = ""
        for c in seq:
            if c == "0":
                next_seq += "1"
            elif c == "1":
                next_seq += "2"
            else:
                next_seq += "0"
        seq += next_seq
    return int(seq[n])

# ⚡ Optimized O(log n) solution
def optimized_get_char(n):
    if n == 0:
        return 0
    length = 1
    while length * 2 <= n:
        length *= 2
    return (optimized_get_char(n - length) + 1) % 3

# 📤 Function to print outputs with runtimes for demonstration
def print_outputs(start=0, end=20):
    print("Index | Naive | Time (s) | Optimized | Time (s)")
    print("-------------------------------------------------")
    for n in range(start, end):
        start_naive = time.time()
        naive = naive_get_char(n)
        end_naive = time.time()

        start_opt = time.time()
        optimized = optimized_get_char(n)
        end_opt = time.time()

        naive_time = end_naive - start_naive
        opt_time = end_opt - start_opt

        print(f"{n:5} | {naive:5} | {naive_time:.6f} | {optimized:9} | {opt_time:.6f}")

# 🧪 Unit Tests verifying correctness and printing runtimes
class TestSequenceMethods(unittest.TestCase):

    def test_small_values_with_timing(self):
        print("\nRunning tests for small values with timing:")
        for n in range(20):
            start_naive = time.time()
            expected = naive_get_char(n)
            end_naive = time.time()

            start_opt = time.time()
            result = optimized_get_char(n)
            end_opt = time.time()

            naive_time = end_naive - start_naive
            opt_time = end_opt - start_opt

            print(f"[Test n={n}] naive: {expected}, time: {naive_time:.6f}s | optimized: {result}, time: {opt_time:.6f}s")
            self.assertEqual(result, expected, f"Failed at index {n}")

    def test_base_cases(self):
        print("\nRunning base case tests:")
        self.assertEqual(optimized_get_char(0), 0)
        self.assertEqual(optimized_get_char(1), 1)
        self.assertEqual(optimized_get_char(2), 1)
        self.assertEqual(optimized_get_char(3), 2)
        print("Base cases passed.")

    def test_larger_index(self):
        print("\nRunning tests for large indices (optimized only):")
        large_indices = [10**6, 10**9, 2**32 - 1]
        for n in large_indices:
            start = time.time()
            result = optimized_get_char(n)
            end = time.time()
            print(f"[Large Index {n}] Result: {result}, Time: {end - start:.6f}s")
            self.assertIn(result, [0, 1, 2])

if __name__ == "__main__":
    print("=== Output Comparison with Timings (n = 0 to 19) ===")
    print_outputs(0, 20)

    print("\n=== Running Unit Tests with Timings and Outputs ===")
    unittest.main(argv=[''], exit=False)

