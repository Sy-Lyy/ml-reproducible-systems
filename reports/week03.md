# 📅 Week 3: [Testing, debugging, and OOP]
## 🛠️ 1. What I Built
- **Summary**:  I implemented a DataProcessor class in processor.py with mean() and variance() methods. I wrote unit tests using pytest, confirmed test failures after intentionally inserting a bug, and used the VS Code debugger to inspect sum(self.data) and len(self.data). I also handled edge cases such as empty input data and verified correctness with additional tests.
- **Key Tools Used**: Python, pytest, VS Code Debugger
- **Artifact Location**:
  - https://github.com/tcsai/portfolio-25-26-Sy-Lyy.git

- Mean Error Execution Result
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy>
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> cd "C:\Users\수영\portfolio-25-26-Sy-Lyy"
PS C:\Users\수영\portfolio-25-26-Sy-Lyy> python -m pytest -q
FF.                                                      [100%]
========================== FAILURES ===========================
_______________________ test_mean_basic _______________________

```
def test_mean_basic():
    p = DataProcessor([1, 2, 3, 4, 5])

```

> assert p.mean() == 3.0
> 

E       assert 75 == 3.0
E        +  where 75 = mean()
E        +    where mean = <processor.DataProcessor object at 0x0000019CCF6FD000>.mean

tests\test_processor.py:8: AssertionError
_____________________ test_variance_basic _____________________

```
def test_variance_basic():
    p = DataProcessor([1, 2, 3, 4, 5])

```

> assert math.isclose(p.variance(), 2.0, rel_tol=1e-9)
> 

E       assert False
E        +  where False = <built-in function isclose>(5186.0, 2.0, rel_tol=1e-09)
E        +    where <built-in function isclose> = math.isclose

E        +    and   5186.0 = variance()
E        +      where variance = <processor.DataProcessor object at 0x0000019CCF6FC670>.variance

tests\test_processor.py:12: AssertionError
=================== short test summary info ===================
FAILED tests/test_processor.py::test_mean_basic - assert 75 == 3.0
FAILED tests/test_processor.py::test_variance_basic - assert False
2 failed, 1 passed in 0.32s
PS C:\Users\수영\portfolio-25-26-Sy-Lyy>

- Breaking point
  <img width="1843" height="957" alt="image" src="https://github.com/user-attachments/assets/ca5bdbc3-1e1e-4038-b937-8ce2831a4fe8" />

- Debugging result
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy>  & 'c:\Users\수영\AppData\Local\Microsoft\WindowsApps\python3.10.exe' 'c:\Users\수영\.vscode\extensions\ms-python.debugpy-2025.10.0-win32-x64\bundled\libs\debugpy\launcher' '50924' '--' 'C:\Users\수영\Desktop\Tilburg Univ\[stuessor.py](http://stuessor.py/)'
loaded: [1, 2, 3]
Help on method mean in module **main**:

mean() -> float method of **main**.DataProcessor instance
Broken: wrong formula to simulate a bug for practice.

PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy>

- Empty data result

PS C:\Users\수영\portfolio-25-26-Sy-Lyy> git pull origin main
remote: Enumerating objects: 12, done.
remote: Counting objects: 100% (12/12), done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 12 (delta 4), reused 6 (delta 2), pack-reused 0 (from 0)
Unpacking objects: 100% (12/12), 3.36 KiB | 30.00 KiB/s, done.
From https://github.com/tcsai/portfolio-25-26-Sy-Lyy

- branch main -> FETCH_HEAD
fedd22c..69c7068 main -> origin/main
Updating fedd22c..69c7068
Fast-forward
src/processor.py | 17 +++++++++++------
1 file changed, 11 insertions(+), 6 deletions(-)
PS C:\Users\수영\portfolio-25-26-Sy-Lyy> python -m pytest -q
... [100%]
3 passed in 0.06s
PS C:\Users\수영\portfolio-25-26-Sy-Lyy>

- **How to Run** (if applicable)

[o] Installation steps (if needed) : pip install pytest
[o] Run command(s) : cd C:\Users\수영\portfolio-25-26-Sy-Lyy
                    python -m pytest -q
[o] Expected output : 3 passed in 0.06s

## 🔍 2. My Exploration
- **What I Investigated Further**:
- Why pytest always reported “3 passed” instead of “2 passed”.
- How to check which tests pytest discovers using --collect-only.
Summary of the answer: pytest collects all test_*.py files and their test_ functions. My repo has 2 tests in test_processor.py and 1 in test_smoke.py, so the total is 3. Running pytest --collect-only confirmed this.

- **Link to Evidence**

PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> python -m pytest -q --collect-only

tests/test_processor.py::test_mean_basic
tests/test_processor.py::test_variance_basic
tests/test_smoke.py::test_import

PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> tree /F tests
폴더 PATH의 목록입니다.
│  README.md
│  test_processor.py
│  test_smoke.py
│
└─__pycache__
test_processor.cpython-310-pytest-8.4.2.pyc
test_smoke.cpython-310-pytest-8.4.2.pyc


## 🤖 3. Use of GenAI (if applicable)
- **What I Asked It To Do**:
  - ## GenAI Usage Log
2025-09-14: Asked how to install pytest and run it properly (python -m pytest -q).
2025-09-14: Asked why pytest showed 3 tests.
2025-09-14: Asked how to use pytest --collect-only to see discovered tests.
2025-09-14: Asked about OOP basics.

- **What I Got and Did With It**:
- Installed pytest successfully and executed tests from the project root.
- Discovered the reason for 3 tests passing: presence of test_smoke.py.
- Used pytest --collect-only to confirm test discovery.
- Reviewed OOP fundamentals to understand the class-based structure of the project.

- **Risks or Misuses You Noticed**: There were no issues.

## 💬 4. Reflection
- **How did this week’s work support reproducibility or deployment?** :  Writing unit tests with pytest ensured reproducibility by making it easy to rerun the same checks after any code changes. Debugging with breakpoints improved code reliability.
- **What was most confusing or interesting?** : I found it most interesting to use breakpoints in VS Code to directly inspect values and confirm the bug in the mean() function.
- **If someone else looked at your repo, what would help them use this part of the project?** : I believe others would find it easier to use my repo if I added clear instructions on how to install pytest, run the tests.
If someone else looked at your repo, what would help them use this part of the project? : I believe others would find it easier to use my repo if I added clear instructions on how to install pytest and run the tests.
