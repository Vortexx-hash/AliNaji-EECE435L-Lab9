# EECE435L Lab 9 Python Profiling

**Ali Naji — Fall 2026–2027**

This submission compares the original Python workload with a version that replaces the 100-iteration sum-of-squares loop with an exact arithmetic formula. Both versions were run with cProfile, line_profiler, memory_profiler, unittest, and coverage.py. The Word report contains the analysis and all 16 screenshots of the completed runs.

## Files for review

All paths below are relative to this repository root.

| Item | Location |
| --- | --- |
| Word report with analysis and all screenshots | [lab9_Ali_Naji/lab9_Ali_Naji.docx](lab9_Ali_Naji/lab9_Ali_Naji.docx) |
| Original code and tests | [lab9_Ali_Naji/original/](lab9_Ali_Naji/original/) |
| Optimized code and tests | [lab9_Ali_Naji/optimized/](lab9_Ali_Naji/optimized/) |
| Original HTML coverage report | [lab9_Ali_Naji/original/htmlcov/index.html](lab9_Ali_Naji/original/htmlcov/index.html) |
| Optimized HTML coverage report | [lab9_Ali_Naji/optimized/htmlcov/index.html](lab9_Ali_Naji/optimized/htmlcov/index.html) |
| All 16 screenshot images | [lab9_Ali_Naji/evidence/](lab9_Ali_Naji/evidence/) |
| Text logs, environment details, and benchmark results | [lab9_Ali_Naji/results/](lab9_Ali_Naji/results/) |
| Moodle submission archive | [lab9_Ali_Naji_submission.zip](lab9_Ali_Naji_submission.zip) |
| Lab handout in the repository | [lab9 -Profiling in python.docx](lab9%20-Profiling%20in%20python.docx) |

Each code folder contains `profiler.py`, `profiler_lineprofiler.py`, `profiler_memoryprofiler.py`, and `test_profiler.py`. The two versions use the same 10,000-iteration slow loop, two-second sleep, and 10,000,000-iteration large loop. The optimized version calls `optimized_fast_function()` throughout its workload, profiler scripts, and tests.

The ZIP contains this README and the `lab9_Ali_Naji/` submission folder. The original handout and the ZIP itself are available at the repository root.

To view coverage, download or clone the repository and open either `htmlcov/index.html` in a browser, then select `profiler.py`. Keep the entire `htmlcov` folder with its CSS, JavaScript, and source pages. GitHub displays the HTML source rather than running the interactive report. Statement coverage is 95.65% before optimization and 95.24% afterward; with branch coverage included, the terminal and HTML reports round to 94% and 93%. The only missing statement is the script-entry `main()` call, at original line 35 and optimized line 34.

## Screenshots

Every image is saved directly in `lab9_Ali_Naji/evidence/` and embedded in the Word report. Filenames beginning with `original_` show the code before optimization; those beginning with `optimized_` show it afterward.

| Filename suffix for both versions | Contents |
| --- | --- |
| `cprofile.png` | cProfile command and function timing table |
| `line_small.png` | Line timings for the slow and fast functions |
| `line_large.png` | Line timings for the full 10,000,000-iteration loop |
| `memory_small.png` | Memory usage for the slow and fast functions |
| `memory_large.png` | Memory usage for the full large loop |
| `tests.png` | Four passing tests with timing and memory measurements |
| `coverage.png` | Coverage test run and terminal coverage summary |
| `html.png` | HTML source coverage view and uncovered script-entry line |

The report's timing and memory tables use the values visible in these screenshots, recorded in `lab9_Ali_Naji/results/screenshot_measurements.json`. The text logs in `results/` are from earlier runs of the same code. `benchmark.json` records a separate repeated comparison using `timeit` without profiler tracing.

## Clarifications to the handout

The comment beside `return total` says that the return should not be indented. A Python return must remain inside its function. Here it is indented four spaces, aligned with the `for` statement, so it runs after the loop has finished. At the left margin it would cause `SyntaxError: 'return' outside function`; inside the loop it would stop after the first iteration.

The sample memory test asserts that RSS must increase after `memory_intensive_function()`. That function uses `range` and a single accumulator, so it does not retain a list of squares and a permanent RSS increase is not guaranteed. The submitted tests record RSS before and after execution and verify the exact sum, `333333283333335000000`, instead of requiring an increase.

The sample also requires the large loop to finish within five seconds. The submitted tests print whether that target was met, while correctness is checked separately because tracing overhead and system load affect elapsed time. Both captured test runs meet the target. The slow-function check uses at least two seconds to match `time.sleep(2)`, and the fast-function check retains the one-second limit. These test changes are discussed in the Word report.

## Running the code

From the repository root, create an environment and install the pinned profiling packages:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r .\lab9_Ali_Naji\requirements.txt
cd .\lab9_Ali_Naji\original
..\..\.venv\Scripts\python.exe -m cProfile -s time profiler.py
..\..\.venv\Scripts\python.exe profiler_lineprofiler.py
..\..\.venv\Scripts\python.exe -m memory_profiler profiler_memoryprofiler.py
..\..\.venv\Scripts\python.exe test_profiler.py
..\..\.venv\Scripts\python.exe -m coverage run -m unittest discover -v
..\..\.venv\Scripts\python.exe -m coverage report -m
..\..\.venv\Scripts\python.exe -m coverage html
```

Run the same commands from `lab9_Ali_Naji/optimized/` for the optimized version. Full line-by-line memory profiling can take several minutes. Both test suites run the actual functions; mocks are used only in the additional test that checks the calls made by `main()`.

The report, screenshots, HTML coverage pages, and submission ZIP are complete. The Python files in `original/` and `optimized/` run directly using the commands above and the packages in `requirements.txt`.
