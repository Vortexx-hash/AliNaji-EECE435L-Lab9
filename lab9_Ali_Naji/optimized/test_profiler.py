"""Same correctness checks after replacing fast_function everywhere."""

import time
import unittest
from unittest.mock import patch
import memory_profiler
import profiler


class TestProfiler(unittest.TestCase):
    def time_function(self, func):
        start = time.perf_counter()
        result = func()
        return result, time.perf_counter() - start

    def test_slow_function(self):
        result, duration = self.time_function(profiler.slow_function)
        print(f"slow_function executed in {duration:.6f} seconds.", flush=True)
        self.assertEqual(result, 333283335000)
        self.assertGreaterEqual(duration, 2)

    def test_optimized_fast_function(self):
        result, duration = self.time_function(profiler.optimized_fast_function)
        print(f"optimized_fast_function executed in {duration:.9f} seconds.", flush=True)
        self.assertEqual(result, 328350)
        self.assertLess(duration, 1)

    def test_memory_intensive_function(self):
        before = memory_profiler.memory_usage(-1, interval=0.01, timeout=0.01)[0]
        result, duration = self.time_function(profiler.memory_intensive_function)
        after = memory_profiler.memory_usage(-1, interval=0.01, timeout=0.01)[0]
        print(f"memory_intensive_function executed in {duration:.6f} seconds.", flush=True)
        print(f"Memory before: {before:.3f} MiB; after: {after:.3f} MiB; "
              f"change: {after - before:+.3f} MiB.", flush=True)
        print(f"Handout 5 second performance target met: {duration < 5}", flush=True)
        self.assertEqual(result, 333333283333335000000)
        self.assertGreater(before, 0)
        self.assertGreater(after, 0)

    def test_main_calls_all_functions(self):
        with patch.object(profiler, "slow_function") as slow, \
             patch.object(profiler, "optimized_fast_function") as fast, \
             patch.object(profiler, "memory_intensive_function") as memory:
            self.assertIsNone(profiler.main())
        slow.assert_called_once_with()
        fast.assert_called_once_with()
        memory.assert_called_once_with()


if __name__ == "__main__":
    unittest.main(verbosity=2)
