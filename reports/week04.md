# 📅 Week 3: [Testing, debugging, and OOP]
## 🛠️ 1. What I Built
- **Summary**:  I implemented a DataProcessor class in processor.py with mean() and variance() methods. I wrote unit tests using pytest, confirmed test failures after intentionally inserting a bug, and used the VS Code debugger to inspect sum(self.data) and len(self.data). I also handled edge cases such as empty input data and verified correctness with additional tests.
- **Key Tools Used**: Python, pytest, VS Code Debugger
- **Artifact Location**:
  - https://github.com/tcsai/portfolio-25-26-Sy-Lyy.git
  <details>
  <summary>View Execution Logs</summary>

```powershell
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> python -m venv .sandboxA
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> source .sandboxA/bin/activate
source : 'source' 용어가 cmdlet, 함수, 스크립트 파일 또는 실행할 수 있는 프로그램 이름으로 인식되지 않습니다. 이름이 정확한지 확인하고 경로가 포함된 경우 경로가 올바른지 검증한 다음 다시 시도하십시오.
위치 줄:1 문자:1

source .sandboxA/bin/activate

`+ CategoryInfo : ObjectNotFound: (source:String) [], CommandNotFoundException + FullyQualifiedErrorId : CommandNotFoundException`

S C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> C:/ProgramData/anaconda/Scripts/activate
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> conda activate base
conda : 'conda' 용어가 cmdlet, 함수, 스크립트 파일 또는 실행할 수 있는 프로그램 이름으로 인식되지 않습니다. 이름이 정확한지 확인하고 경로가 포함된 경우 경로가 올바른지 검증한 다음 다시 시도하십시오.
위치 줄:1 문자:1

conda activate base

`+ CategoryInfo : ObjectNotFound: (conda:String) [], CommandNotFoundException + FullyQualifiedErrorId : CommandNotFoundException`

PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> .\.sandboxA\Scripts\Activate.ps1
.\.sandboxA\Scripts\Activate.ps1 : 이 시스템에서 스크립트를 실행할 수 없으므로 C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\.sandboxA\Scripts\Activate.ps1 파일을 로드할 수 없습니다
. 자세한 내용은 about_Execution_Policies(https://go.microsoft.com/fwlink/?LinkID=135170)를 참조하십시오.
위치 줄:1 문자:1

.\.sandboxA\Scripts\Activate.ps1

`+ CategoryInfo : 보안 오류: (:) [], PSSecurityException + FullyQualifiedErrorId : UnauthorizedAccess`

PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> .\.sandboxA\Scripts\Activate.ps1
(.sandboxA) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> pip install numpy==1.24.0
Collecting numpy==1.24.0
Downloading numpy-1.24.0-cp310-cp310-win_amd64.whl (14.8 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.8/14.8 MB 10.6 MB/s eta 0:00:00
Installing collected packages: numpy
Successfully installed numpy-1.24.0

[notice] A new release of pip is available: 23.0.1 -> 25.2
[notice] To update, run: python.exe -m pip install --upgrade pip
(.sandboxA) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> python -c "import numpy; print(numpy.**version**)"
1.24.0
(.sandboxA) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> deactive
deactive : 'deactive' 용어가 cmdlet, 함수, 스크립트 파일 또는 실행할 수 있는 프로그램 이름으로 인식되지 않습니다. 이름이 정확한지 확인하고 경로가 포함된 경우 경로가 올바른지 검증한 다음 다시 시도하십시
오.
위치 줄:1 문자:1

- deactive
- `+ CategoryInfo : ObjectNotFound: (deactive:String) [], CommandNotFoundException + FullyQualifiedErrorId : CommandNotFoundException`

(.sandboxA) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> deactivate

### Step 2 – Creating Environment B

PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> python -m venv .sandboxB
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> source .sandboxB/bin/activate      # Windows: .sandboxB\Scripts\activate
source : 'source' 용어가 cmdlet, 함수, 스크립트 파일 또는 실행할 수 있는 프로그램 이름으로 인식되지 않습니다. 이름이 정확한지 확인하고 경로가 포함된 경우 경로가 올바른지 검증한 다음 다시 시도하십시오.
위치 줄:1 문자:1

source .sandboxB/bin/activate # Windows: .sandboxB\Scripts\activ ...

`+ CategoryInfo : ObjectNotFound: (source:String) [], CommandNotFoundException + FullyQualifiedErrorId : CommandNotFoundException`

PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> .\.sandboxB\Scripts\Activate.ps1
(.sandboxB) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> pip install numpy==1.26.0
Collecting numpy==1.26.0
Downloading numpy-1.26.0-cp310-cp310-win_amd64.whl (15.8 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.8/15.8 MB 17.7 MB/s eta 0:00:00
Installing collected packages: numpy
Successfully installed numpy-1.26.0

[notice] A new release of pip is available: 23.0.1 -> 25.2
[notice] To update, run: python.exe -m pip install --upgrade pip
(.sandboxB) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> python -c "import numpy; print(numpy.**version**)"
1.26.0

(.sandboxB) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> deactivate
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> python -c "import numpy; print(numpy.**version**)"
1.26.4

## Modern standard: `pyproject.toml`

PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> poetry install
The currently activated Python version 3.10.11 is not supported by the project (^3.11).
Trying to find and use a compatible version.
Using python.exe (3.11.0)
The virtual environment found in C:\Users\수영\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0 seems to be broken.
Recreating virtualenv mystery-box-70sNDKc3-py3.11 in C:\Users\수영\AppData\Local\pypoetry\Cache\virtualenvs\mystery-box-70sNDKc3-py3.11
Updating dependencies
Resolving dependencies... (2.0s)

Package operations: 10 installs, 0 updates, 0 removals

- Installing numpy (2.3.3)
- Installing six (1.17.0)
- Installing joblib (1.5.2): Failed

FileNotFoundError

[Errno 2] No such file or directory: 'C:\\Users\\수영\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\Local\\pypoetry\\Cache\\virtualenvs\\mystery-box-70sNDKc3-py3.11\\Lib\\site-packages\\joblib\\test\\data\\joblib_0.9.4.dev0_compressed_cache_size_pickle_py35_np19.gz_01.npy.z'

at C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\lib\[pathlib.py:1119](http://pathlib.py:1119/) in open

1115│         the built-in open() function does.
1116│         """

1117│         if "b" not in mode:

1118│             encoding = io.text_encoding(encoding)

→ 1119│         return self._accessor.open(self, mode, buffering, encoding, errors,

1120│                                    newline)

1121│

1122│     def read_bytes(self):

1123│         """

Cannot install joblib.

- Installing python-dateutil (2.9.0.post0)
- Installing pytz (2025.2)
- Installing scipy (1.16.2)
- Installing threadpoolctl (3.6.0)
- Installing tzdata (2025.2)
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> poetry lock
The currently activated Python version 3.10.11 is not supported by the project (^3.11).
Trying to find and use a compatible version.
Using python.exe (3.11.0)
The virtual environment found in C:\Users\수영\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0 seems to be broken.
Recreating virtualenv mystery-box-70sNDKc3-py3.11 in C:\Users\수영\AppData\Local\pypoetry\Cache\virtualenvs\mystery-box-70sNDKc3-py3.11
Updating dependencies
Resolving dependencies... (1.6s)

Writing lock file
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> poetry run python [train.py](http://train.py/)
The currently activated Python version 3.10.11 is not supported by the project (^3.11).
Trying to find and use a compatible version.
Using python.exe (3.11.0)
The virtual environment found in C:\Users\수영\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0 seems to be broken.
Recreating virtualenv mystery-box-70sNDKc3-py3.11 in C:\Users\수영\AppData\Local\pypoetry\Cache\virtualenvs\mystery-box-70sNDKc3-py3.11
C:\Users\수영\AppData\Local\Programs\Python\Python311\python.exe: can't open file 'C:\\Users\\수영\\Desktop\\Tilburg Univ\\study\\RM\\portfolio-25-26-Sy-Lyy\\[train.py](http://train.py/)': [Errno 2] No such file or directory
# # Error(option b)

(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> conda --version
******            일괄 재귀가 스택 한도를 초과합니다.            ******
재귀 횟수=335, 스택 사용=90퍼센트
******                일괄 처리가 중단되었습니다.               ******
(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> conda create -n envB python=3.11 -y
******            일괄 재귀가 스택 한도를 초과합니다.            ******
재귀 횟수=335, 스택 사용=90퍼센트
******                일괄 처리가 중단되었습니다.               ******
(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> powershell -NoProfile
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

새로운 기능 및 개선 사항에 대 한 최신 PowerShell을 설치 하세요! https://aka.ms/PSWindows

PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> & "C:\ProgramData\anaconda\Scripts\conda.exe" --version
conda 24.11.3
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> & "C:\ProgramData\anaconda\Scripts\conda.exe" create -n envB python=3.11 -y
Channels:

defaults
Platform: win-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan

environment location: C:\Users\수영\.conda\envs\envB

added / updated specs:
  python=3.11

The following packages will be downloaded:

```
package                    |            build
---------------------------|-----------------
bzip2-1.0.8                |       h2bbff1b_6          90 KB
ca-certificates-2025.9.9   |       haa95532_0         127 KB
expat-2.7.1                |       h8ddb27b_0         259 KB
libffi-3.4.4               |       hd77b12b_1         122 KB
libzlib-1.3.1              |       h02ab6af_0          64 KB
openssl-3.0.17             |       h35632f6_0         7.8 MB
pip-25.2                   |     pyhc872135_0         1.2 MB
python-3.11.13             |       h981015d_0        18.7 MB
setuptools-78.1.1          |  py311haa95532_0         2.3 MB
sqlite-3.50.2              |       hda9a48d_1        1017 KB
tk-8.6.15                  |       hf199647_0         3.5 MB
tzdata-2025b               |       h04d1e81_0         116 KB
ucrt-10.0.22621.0          |       haa95532_0         620 KB
vc-14.3                    |      h2df5915_10          19 KB
vc14_runtime-14.44.35208   |      h4927774_10         825 KB
vs2015_runtime-14.44.35208 |      ha6b5a95_10          19 KB
wheel-0.45.1               |  py311haa95532_0         182 KB
xz-5.6.4                   |       h4754444_1         280 KB
zlib-1.3.1                 |       h02ab6af_0         113 KB
------------------------------------------------------------
                                       Total:        37.2 MB

```

The following NEW packages will be INSTALLED:

bzip2              pkgs/main/win-64::bzip2-1.0.8-h2bbff1b_6
ca-certificates    pkgs/main/win-64::ca-certificates-2025.9.9-haa95532_0
expat              pkgs/main/win-64::expat-2.7.1-h8ddb27b_0
libffi             pkgs/main/win-64::libffi-3.4.4-hd77b12b_1
libzlib            pkgs/main/win-64::libzlib-1.3.1-h02ab6af_0
openssl            pkgs/main/win-64::openssl-3.0.17-h35632f6_0
pip                pkgs/main/noarch::pip-25.2-pyhc872135_0
python             pkgs/main/win-64::python-3.11.13-h981015d_0
setuptools         pkgs/main/win-64::setuptools-78.1.1-py311haa95532_0
sqlite             pkgs/main/win-64::sqlite-3.50.2-hda9a48d_1
tk                 pkgs/main/win-64::tk-8.6.15-hf199647_0
tzdata             pkgs/main/noarch::tzdata-2025b-h04d1e81_0
ucrt               pkgs/main/win-64::ucrt-10.0.22621.0-haa95532_0
vc                 pkgs/main/win-64::vc-14.3-h2df5915_10
vc14_runtime       pkgs/main/win-64::vc14_runtime-14.44.35208-h4927774_10
vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.44.35208-ha6b5a95_10
wheel              pkgs/main/win-64::wheel-0.45.1-py311haa95532_0
xz                 pkgs/main/win-64::xz-5.6.4-h4754444_1
zlib               pkgs/main/win-64::zlib-1.3.1-h02ab6af_0

done

# 

# To activate this environment, use

# 

# $ conda activate envB

# 

# To deactivate an active environment, use

# 

# $ conda deactivate

PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> gci Env:CONDA*

Name                           Value

---

CONDA_SHLVL                    1
CONDA_EXE                      C:\ProgramData\anaconda\condabin\conda.bat
CONDA_PROMPT_MODIFIER          (base)
CONDA_PYTHON_EXE               C:\ProgramData\anaconda\python.exe
CONDA_DEFAULT_ENV              base
CONDA_PREFIX                   C:\ProgramData\anaconda

PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> Remove-Item Env:CONDA_EXE -ErrorAction SilentlyContinue
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> Remove-Item Env:_CE_CONDA -ErrorAction SilentlyContinue
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> Remove-Item Env:_CONDA_ROOT -ErrorAction SilentlyContinue
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> $ps7 = "$HOME\Documents\PowerShell\Microsoft.PowerShell_profile.ps1"
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> $ps5 = "$HOME\Documents\WindowsPowerShell\profile.ps1"
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> if (Test-Path $ps7) { Copy-Item $ps7 "$ps7.bak" -Force }
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> if (Test-Path $ps5) { Copy-Item $ps5 "$ps5.bak" -Force }
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> notepad $ps7

> 
> 

PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> notepad $ps5
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> notepad $ps7
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> conda init --reverse powershell
no change     C:\ProgramData\anaconda\Scripts\conda.exe
no change     C:\ProgramData\anaconda\Scripts\conda-env.exe
no change     C:\ProgramData\anaconda\Scripts\[conda-script.py](http://conda-script.py/)
no change     C:\ProgramData\anaconda\Scripts\[conda-env-script.py](http://conda-env-script.py/)
no change     C:\ProgramData\anaconda\condabin\conda.bat
no change     C:\ProgramData\anaconda\Library\bin\conda.bat
no change     C:\ProgramData\anaconda\condabin\_conda_activate.bat
no change     C:\ProgramData\anaconda\condabin\rename_tmp.bat
no change     C:\ProgramData\anaconda\condabin\conda_auto_activate.bat
no change     C:\ProgramData\anaconda\condabin\conda_hook.bat
no change     C:\ProgramData\anaconda\Scripts\activate.bat
no change     C:\ProgramData\anaconda\condabin\activate.bat
no change     C:\ProgramData\anaconda\condabin\deactivate.bat
no change     C:\ProgramData\anaconda\Scripts\activate
no change     C:\ProgramData\anaconda\Scripts\deactivate
no change     C:\ProgramData\anaconda\etc\profile.d\[conda.sh](http://conda.sh/)
no change     C:\ProgramData\anaconda\etc\fish\conf.d\conda.fish
no change     C:\ProgramData\anaconda\shell\condabin\Conda.psm1
no change     C:\ProgramData\anaconda\shell\condabin\conda-hook.ps1
no change     C:\ProgramData\anaconda\Lib\site-packages\xontrib\conda.xsh
no change     C:\ProgramData\anaconda\etc\profile.d\conda.csh
modified      C:\Users\수영\Documents\WindowsPowerShell\profile.ps1

==> For changes to take effect, close and re-open your current shell. <==

PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> conda init powershell
no change     C:\ProgramData\anaconda\Scripts\conda.exe
no change     C:\ProgramData\anaconda\Scripts\conda-env.exe
no change     C:\ProgramData\anaconda\Scripts\[conda-script.py](http://conda-script.py/)
no change     C:\ProgramData\anaconda\Scripts\[conda-env-script.py](http://conda-env-script.py/)
no change     C:\ProgramData\anaconda\condabin\conda.bat
no change     C:\ProgramData\anaconda\Library\bin\conda.bat
no change     C:\ProgramData\anaconda\condabin\_conda_activate.bat
no change     C:\ProgramData\anaconda\condabin\rename_tmp.bat
no change     C:\ProgramData\anaconda\condabin\conda_auto_activate.bat
no change     C:\ProgramData\anaconda\condabin\conda_hook.bat
no change     C:\ProgramData\anaconda\Scripts\activate.bat
no change     C:\ProgramData\anaconda\condabin\activate.bat
no change     C:\ProgramData\anaconda\condabin\deactivate.bat
no change     C:\ProgramData\anaconda\Scripts\activate
no change     C:\ProgramData\anaconda\Scripts\deactivate
no change     C:\ProgramData\anaconda\etc\profile.d\[conda.sh](http://conda.sh/)
no change     C:\ProgramData\anaconda\etc\fish\conf.d\conda.fish
no change     C:\ProgramData\anaconda\shell\condabin\Conda.psm1
no change     C:\ProgramData\anaconda\shell\condabin\conda-hook.ps1
no change     C:\ProgramData\anaconda\Lib\site-packages\xontrib\conda.xsh
no change     C:\ProgramData\anaconda\etc\profile.d\conda.csh
modified      C:\Users\수영\Documents\WindowsPowerShell\profile.ps1

==> For changes to take effect, close and re-open your current shell. <==

PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

해결

(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> $ps7 = "$HOME\Documents\PowerShell\Microsoft.PowerShell_profile.ps1"
(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> $ps5 = "$HOME\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1"

> if (Test-Path $ps7) { Copy-Item $ps7 "$ps7.bak" -Force }
(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> if (Test-Path $ps5) { Copy-Item $ps5 "$ps5.bak" -Force }
(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> if (Test-Path $ps7) { notepad $ps7 }
(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> if (Test-Path $ps5) { notepad $ps5 }
(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> if (Test-Path $ps7) { notepad $ps7 }
(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy>
(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy>
> 
> 
> History restored
> 

(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> $PSVersionTable.PSVersion

Major  Minor  Build  Revision

---

5      1      26100  6584

(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> conda --version
conda 24.11.3
(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> conda info --envs

---

그래서 다시 실행 

step 1 **Create Environment A**

(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> conda create -n envA python=3.11 -y
Channels:

defaults
Platform: win-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan

environment location: C:\Users\수영\.conda\envs\envA

added / updated specs:
- python=3.11

The following NEW packages will be INSTALLED:

bzip2              pkgs/main/win-64::bzip2-1.0.8-h2bbff1b_6
ca-certificates    pkgs/main/win-64::ca-certificates-2025.9.9-haa95532_0
expat              pkgs/main/win-64::expat-2.7.1-h8ddb27b_0
libffi             pkgs/main/win-64::libffi-3.4.4-hd77b12b_1
libzlib            pkgs/main/win-64::libzlib-1.3.1-h02ab6af_0
openssl            pkgs/main/win-64::openssl-3.0.17-h35632f6_0
pip                pkgs/main/noarch::pip-25.2-pyhc872135_0
python             pkgs/main/win-64::python-3.11.13-h981015d_0
setuptools         pkgs/main/win-64::setuptools-78.1.1-py311haa95532_0
sqlite             pkgs/main/win-64::sqlite-3.50.2-hda9a48d_1
tk                 pkgs/main/win-64::tk-8.6.15-hf199647_0
tzdata             pkgs/main/noarch::tzdata-2025b-h04d1e81_0
ucrt               pkgs/main/win-64::ucrt-10.0.22621.0-haa95532_0
vc                 pkgs/main/win-64::vc-14.3-h2df5915_10
done

# 

# To activate this environment, use

# 

# $ conda activate envA

# 

# To deactivate an active environment, use

# 

# $ conda deactivate

(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> conda activate envA
(envA) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> python -m pip install numpy==1.24.0
Collecting numpy==1.24.0
Downloading numpy-1.24.0-cp311-cp311-win_amd64.whl.metadata (5.6 kB)
Downloading numpy-1.24.0-cp311-cp311-win_amd64.whl (14.8 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.8/14.8 MB 10.0 MB/s  0:00:01
Installing collected packages: numpy
Successfully installed numpy-1.24.0
(envA) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> python -c "import numpy; print(numpy.**version**)"
1.24.0
(envA) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> conda deactivate

## step 2 : **Create Environment B**

(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> conda create -n envB python=3.11 -y
Channels:

defaults
Platform: win-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan

environment location: C:\Users\수영\.conda\envs\envB

added / updated specs:
- python=3.11

The following NEW packages will be INSTALLED:

bzip2              pkgs/main/win-64::bzip2-1.0.8-h2bbff1b_6
ca-certificates    pkgs/main/win-64::ca-certificates-2025.9.9-haa95532_0
expat              pkgs/main/win-64::expat-2.7.1-h8ddb27b_0
libffi             pkgs/main/win-64::libffi-3.4.4-hd77b12b_1
libzlib            pkgs/main/win-64::libzlib-1.3.1-h02ab6af_0
openssl            pkgs/main/win-64::openssl-3.0.17-h35632f6_0
pip                pkgs/main/noarch::pip-25.2-pyhc872135_0
python             pkgs/main/win-64::python-3.11.13-h981015d_0
setuptools         pkgs/main/win-64::setuptools-78.1.1-py311haa95532_0
sqlite             pkgs/main/win-64::sqlite-3.50.2-hda9a48d_1
tk                 pkgs/main/win-64::tk-8.6.15-hf199647_0
tzdata             pkgs/main/noarch::tzdata-2025b-h04d1e81_0
ucrt               pkgs/main/win-64::ucrt-10.0.22621.0-haa95532_0
vc                 pkgs/main/win-64::vc-14.3-h2df5915_10
done

# 

# To activate this environment, use

# 

# $ conda activate envB

# 

# To deactivate an active environment, use

# 

# $ conda deactivate

(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> conda activate envB
(envB) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> python -m pip install numpy==1.26.0
Collecting numpy==1.26.0
Downloading numpy-1.26.0-cp311-cp311-win_amd64.whl.metadata (61 kB)
Downloading numpy-1.26.0-cp311-cp311-win_amd64.whl (15.8 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.8/15.8 MB 28.4 MB/s  0:00:00
Installing collected packages: numpy
Successfully installed numpy-1.26.0
(envB) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> python -c "import numpy; print(numpy.**version**)"
1.26.0
(envB) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> conda deactivate

(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> python -c "import numpy; print(numpy.**version**)"
1.26.4

---

## Capturing & Recreating Environments

### With `venv` – requirements.txt

(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> .\.sandboxA\Scripts\Activate.ps1
(.sandboxA) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> pip install numpy pandas
Requirement already satisfied: numpy in c:\users\수영\desktop\tilburg univ\study\rm\portfolio-25-26-sy-lyy\.sandboxa\lib\site-packages (1.24.0)
Collecting pandas
Downloading pandas-2.3.2-cp312-cp312-win_amd64.whl.metadata (19 kB)
Collecting numpy
Downloading numpy-2.3.3-cp312-cp312-win_amd64.whl.metadata (60 kB)
Collecting python-dateutil>=2.8.2 (from pandas)
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz>=2020.1 (from pandas)
Downloading pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.7 (from pandas)
Downloading tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas)
Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Downloading pandas-2.3.2-cp312-cp312-win_amd64.whl (11.0 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.0/11.0 MB 25.5 MB/s eta 0:00:00
Downloading numpy-2.3.3-cp312-cp312-win_amd64.whl (12.8 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.8/12.8 MB 28.7 MB/s eta 0:00:00
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading pytz-2025.2-py2.py3-none-any.whl (509 kB)
Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: pytz, tzdata, six, numpy, python-dateutil, pandas
Attempting uninstall: numpy
Found existing installation: numpy 1.24.0
Uninstalling numpy-1.24.0:
Successfully uninstalled numpy-1.24.0
Successfully installed numpy-2.3.3 pandas-2.3.2 python-dateutil-2.9.0.post0 pytz-2025.2 six-1.17.0 tzdata-2025.2

[notice] A new release of pip is available: 24.2 -> 25.2
[notice] To update, run: python.exe -m pip install --upgrade pip
(.sandboxA) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> pip freeze > requirements.txt
(.sandboxA) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> @"

> numpy==1.26.0
pandas==2.2.2
"@ | Set-Content requirements.txt
(.sandboxA) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> python -m venv .sandboxA_new
(.sandboxA) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> source .sandbox_new/bin/activate
source : 'source' 용어가 cmdlet, 함수, 스크립트 파일 또는 실행할 수 있는 프로그램 이름으로 인식되지 않습니다. 이름이 정확한지 확인하고 경로가 포함된 경우 경로가 올바른지 검증한 다음 다시 시도하십시오.
위치 줄:1 문자:1
> 
> 
> source .sandbox_new/bin/activate
> 
> `+ CategoryInfo : ObjectNotFound: (source:String) [], CommandNotFoundException + FullyQualifiedErrorId : CommandNotFoundException`
> 

(.sandboxA) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> conda deactivate
(.sandboxA) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> python -m venv .sandboxA_new

(.sandboxA) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> source .sandbox_new/bin/activate
source : 'source' 용어가 cmdlet, 함수, 스크립트 파일 또는 실행할 수 있는 프로그램 이름으로 인식되지 않습니다. 이름이 정확한지 확인하고 경로가 포함된 경우 경로가 올바른지 검증한 다음 다시 시도하십시오.
위치 줄:1 문자:1

source .sandbox_new/bin/activate

`+ CategoryInfo : ObjectNotFound: (source:String) [], CommandNotFoundException + FullyQualifiedErrorId : CommandNotFoundException`

(.sandboxA) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> source .sandbox_new/bin/activate.ps1
source : 'source' 용어가 cmdlet, 함수, 스크립트 파일 또는 실행할 수 있는 프로그램 이름으로 인식되지 않습니다. 이름이 정확한지 확인하고 경로가 포함된 경우 경로가 올바른지 검증한 다음 다시 시도하십시오.
위치 줄:1 문자:1

source .sandbox_new/bin/activate.ps1

`+ CategoryInfo : ObjectNotFound: (source:String) [], CommandNotFoundException + FullyQualifiedErrorId : CommandNotFoundException`

(.sandboxA) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy>  .\sandbox_new/bin/activate.ps1

.\sandbox_new/bin/activate.ps1 : '.\sandbox_new/bin/activate.ps1' 용어가 cmdlet, 함수, 스크립트 파일 또는 실행할 수 있는 프로그램 이름으로 인식되지 않습니다. 이름이 정확한지 확인하고 경로가 포함된 경우
경로가 올바른지 검증한 다음 다시 시도하십시오.
위치 줄:1 문자:2

.\sandbox_new/bin/activate.ps1

`+ CategoryInfo : ObjectNotFound: (.\\sandbox_new/bin/activate.ps1:String) [], CommandNotFoundException + FullyQualifiedErrorId : CommandNotFoundException`

(.sandboxA) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> python -m venv .sandboxA_new
(.sandboxA) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> .\.sandboxA_new\Scripts\Activate.ps1
(.sandboxA_new) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> pip install -r requirements.txt
Collecting numpy==1.26.0 (from -r requirements.txt (line 1))
Downloading numpy-1.26.0-cp312-cp312-win_amd64.whl.metadata (61 kB)
Collecting pandas==2.2.2 (from -r requirements.txt (line 2))
Downloading pandas-2.2.2-cp312-cp312-win_amd64.whl.metadata (19 kB)
Collecting python-dateutil>=2.8.2 (from pandas==2.2.2->-r requirements.txt (line 2))
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz>=2020.1 (from pandas==2.2.2->-r requirements.txt (line 2))
Using cached pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.7 (from pandas==2.2.2->-r requirements.txt (line 2))
Using cached tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas==2.2.2->-r requirements.txt (line 2))
Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Downloading numpy-1.26.0-cp312-cp312-win_amd64.whl (15.5 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.5/15.5 MB 17.1 MB/s eta 0:00:00
Downloading pandas-2.2.2-cp312-cp312-win_amd64.whl (11.5 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.5/11.5 MB 28.8 MB/s eta 0:00:00
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: pytz, tzdata, six, numpy, python-dateutil, pandas
Successfully installed numpy-1.26.0 pandas-2.2.2 python-dateutil-2.9.0.post0 pytz-2025.2 six-1.17.0 tzdata-2025.2

[notice] A new release of pip is available: 24.2 -> 25.2
[notice] To update, run: python.exe -m pip install --upgrade pip

### With `conda` – environment.yml

(.sandboxA_new) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> conda activate envA
(.sandboxA_new) (envA) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> conda env export > environment.yml
(.sandboxA_new) (envA) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> Get-Content .\environment.yml

name: envA
channels:

defaults

https://repo.anaconda.com/pkgs/main

https://repo.anaconda.com/pkgs/r

https://repo.anaconda.com/pkgs/msys2
dependencies:

bzip2=1.0.8=h2bbff1b_6

ca-certificates=2025.9.9=haa95532_0

expat=2.7.1=h8ddb27b_0

libffi=3.4.4=hd77b12b_1

libzlib=1.3.1=h02ab6af_0

openssl=3.0.17=h35632f6_0

pip=25.2=pyhc872135_0

python=3.11.13=h981015d_0

setuptools=78.1.1=py311haa95532_0

sqlite=3.50.2=hda9a48d_1

tk=8.6.15=hf199647_0

tzdata=2025b=h04d1e81_0

ucrt=10.0.22621.0=haa95532_0

vc=14.3=h2df5915_10

vc14_runtime=14.44.35208=h4927774_10

vs2015_runtime=14.44.35208=ha6b5a95_10

wheel=0.45.1=py311haa95532_0

xz=5.6.4=h4754444_1

zlib=1.3.1=h02ab6af_0

pip:

numpy==1.24.0
prefix: C:\Users\수영\.conda\envs\envA
(.sandboxA_new) (envA) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> conda env create -f environment.yml

CondaValueError: prefix already exists: C:\Users\수영\.conda\envs\envA

(.sandboxA_new) (envA) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> Get-Content .\environment.yml
name: envA
channels:

defaults

https://repo.anaconda.com/pkgs/main

https://repo.anaconda.com/pkgs/r

https://repo.anaconda.com/pkgs/msys2
dependencies:

bzip2=1.0.8=h2bbff1b_6

ca-certificates=2025.9.9=haa95532_0

expat=2.7.1=h8ddb27b_0

libffi=3.4.4=hd77b12b_1

libzlib=1.3.1=h02ab6af_0

openssl=3.0.17=h35632f6_0

pip=25.2=pyhc872135_0

python=3.11.13=h981015d_0

setuptools=78.1.1=py311haa95532_0

sqlite=3.50.2=hda9a48d_1

tk=8.6.15=hf199647_0

tzdata=2025b=h04d1e81_0

ucrt=10.0.22621.0=haa95532_0

vc=14.3=h2df5915_10

vc14_runtime=14.44.35208=h4927774_10

vs2015_runtime=14.44.35208=ha6b5a95_10

wheel=0.45.1=py311haa95532_0

xz=5.6.4=h4754444_1

zlib=1.3.1=h02ab6af_0

pip:

numpy==1.24.0
prefix: C:\Users\수영\.conda\envs\envA
(.sandboxA_new) (envA) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> Get-Content .\environment.yml | Where-Object { $_ -notmatch '^prefix:' } | Set-Content .\environment_clean.ym
Ran pip subprocess with arguments:
['C:\\Users\\수영\\.conda\\envs\\envA_clone\\python.exe', '-m', 'pip', 'install', '-U', '-r', 'C:\\Users\\수영\\Desktop\\Tilburg Univ\\study\\RM\\portfolio-25-26-Sy-Lyy\\condaenv.xpg0b8_p.requirements.t]
Pip subprocess output:
Collecting numpy==1.24.0 (from -r C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\condaenv.xpg0b8_p.requirements.txt (line 1))
Using cached numpy-1.24.0-cp311-cp311-win_amd64.whl.metadata (5.6 kB)
Using cached numpy-1.24.0-cp311-cp311-win_amd64.whl (14.8 MB)
Installing collected packages: numpy
Successfully installed numpy-1.24.0

done

# 

# To activate this environment, use

# 

# $ conda activate envA_clone

# 

# To deactivate an active environment, use

# 

# $ conda deactivate

(.sandboxA_new) (envA) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> conda activate envA_clone

# `pyproject.toml`

S C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> Get-ChildItem -Recurse -Filter [train.py](http://train.py/)
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> @"

> if name == "main":
print("training starts")  )
"@ | Set-Content -Encoding utf8 .\train.py
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> git add train.py
warning: in the working copy of 'train.py', LF will be replaced by CRLF the next time Git touches it
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> git commit -m "feat: add train.py"
[main 2b665b0] feat: add train.py
1 file changed, 2 insertions(+)
create mode 100644 train.py
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 328 bytes | 54.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/tcsai/portfolio-25-26-Sy-Lyy.git
6966e47..2b665b0  main -> main
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> poetry run python .\train.py
The currently activated Python version 3.10.11 is not supported by the project (^3.11).
Trying to find and use a compatible version.
Using python.exe (3.11.0)
The virtual environment found in C:\Users\수영\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0 seems to be broken.
Recreating virtualenv mystery-box-70sNDKc3-py3.11 in C:\Users\수영\AppData\Local\pypoetry\Cache\virtualenvs\mystery-box-70sNDKc3-py3.11
training starts
> 

S C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> Get-ChildItem -Recurse -Filter [train.py](http://train.py/)
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> @"

> if name == "main":
print("training starts")  )
"@ | Set-Content -Encoding utf8 .\train.py
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> git add train.py
warning: in the working copy of 'train.py', LF will be replaced by CRLF the next time Git touches it
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> git commit -m "feat: add train.py"
[main 2b665b0] feat: add train.py
1 file changed, 2 insertions(+)
create mode 100644 train.py
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 328 bytes | 54.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/tcsai/portfolio-25-26-Sy-Lyy.git
6966e47..2b665b0  main -> main
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> poetry run python .\train.py
The currently activated Python version 3.10.11 is not supported by the project (^3.11).
Trying to find and use a compatible version.
Using python.exe (3.11.0)
The virtual environment found in C:\Users\수영\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0 seems to be broken.
Recreating virtualenv mystery-box-70sNDKc3-py3.11 in C:\Users\수영\AppData\Local\pypoetry\Cache\virtualenvs\mystery-box-70sNDKc3-py3.11
training starts
> 

PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> poetry add requests
The currently activated Python version 3.10.11 is not supported by the project (^3.11).
Trying to find and use a compatible version.
Using python.exe (3.11.0)
The virtual environment found in C:\Users\수영\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0 seems to be broken.
Recreating virtualenv mystery-box-70sNDKc3-py3.11 in C:\Users\수영\AppData\Local\pypoetry\Cache\virtualenvs\mystery-box-70sNDKc3-py3.11
Using version ^2.32.5 for requests

Updating dependencies
Resolving dependencies... (1.3s)

Package operations: 15 installs, 0 updates, 0 removals

Installing numpy (2.3.3)

Installing six (1.17.0)

Installing certifi (2025.8.3)

Installing charset-normalizer (3.4.3)

Installing idna (3.10)

Installing joblib (1.5.2): Failed

FileNotFoundError

[Errno 2] No such file or directory: 'C:\\Users\\수영\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\Local\\pypoetry\\Cache\\virtualenvs\\mystery-box-70sNDKc3-py3.11\\Lib\\site-packages\\joblib\\test\\data\\joblib_0.9.4.dev0_compressed_cache_size_pickle_py35_np19.gz_01.npy.z'

at C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\lib\[pathlib.py:1119](http://pathlib.py:1119/) in open

1115│         the built-in open() function does.
1116│         """

1117│         if "b" not in mode:

1118│             encoding = io.text_encoding(encoding)

→ 1119│         return self._accessor.open(self, mode, buffering, encoding, errors,

1120│                                    newline)

1121│

1122│     def read_bytes(self):

1123│         """

Cannot install joblib.

- Installing python-dateutil (2.9.0.post0)
- Installing pytz (2025.2)
- Installing scipy (1.16.2)
- Installing threadpoolctl (3.6.0)
- Installing tzdata (2025.2)
- Installing urllib3 (2.5.0)
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> poetry remove pandas
The currently activated Python version 3.10.11 is not supported by the project (^3.11).
Trying to find and use a compatible version.
Using python.exe (3.11.0)
The virtual environment found in C:\Users\수영\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0 seems to be broken.
Recreating virtualenv mystery-box-70sNDKc3-py3.11 in C:\Users\수영\AppData\Local\pypoetry\Cache\virtualenvs\mystery-box-70sNDKc3-py3.11
Updating dependencies
Resolving dependencies... (0.1s)

Package operations: 5 installs, 0 updates, 0 removals

- Installing numpy (2.3.3)
- Installing joblib (1.5.2): Failed

FileNotFoundError

[Errno 2] No such file or directory: 'C:\\Users\\수영\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\Local\\pypoetry\\Cache\\virtualenvs\\mystery-box-70sNDKc3-py3.11\\Lib\\site-packages\\joblib\\test\\data\\joblib_0.9.4.dev0_compressed_cache_size_pickle_py35_np19.gz_01.npy.z'

at C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\lib\[pathlib.py:1119](http://pathlib.py:1119/) in open

1115│         the built-in open() function does.
1116│         """

1117│         if "b" not in mode:

→ 1119│         return self._accessor.open(self, mode, buffering, encoding, errors,
1120│                                    newline)
1121│
1122│     def read_bytes(self):
1123│         """

Cannot install joblib.

- Installing scipy (1.16.2)
- Installing threadpoolctl (3.6.0)

PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> docker version
Client:
Version:           28.3.2
API version:       1.51
Go version:        go1.24.5
Git commit:        578ccf6
Built:             Wed Jul  9 16:12:31 2025
OS/Arch:           windows/amd64
Context:           desktop-linux
error during connect: Get "http://%2F%2F.%2Fpipe%2FdockerDesktopLinuxEngine/v1.51/version": open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> docker build -t reproducible-proj .
ERROR: error during connect: Head "http://%2F%2F.%2Fpipe%2FdockerDesktopLinuxEngine/_ping": open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> Start-Process "$Env:ProgramFiles\Docker\Docker\Docker Desktop.exe"
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> docker version
Client:
Version:           28.3.2
API version:       1.51
Go version:        go1.24.5
Git commit:        578ccf6
Built:             Wed Jul  9 16:12:31 2025
OS/Arch:           windows/amd64
Context:           desktop-linux

Server: Docker Desktop 4.43.2 (199162)
Engine:
Version:          28.3.2
API version:      1.51 (minimum version 1.24)
Go version:       go1.24.5
Git commit:       e77ff99
Built:            Wed Jul  9 16:13:55 2025
OS/Arch:          linux/amd64
Experimental:     false
containerd:
Version:          1.7.27
GitCommit:        05044ec0a9a75232cad458027ca83437aae3f4da
runc:
Version:          1.2.5
GitCommit:        v1.2.5-0-g59923ef
docker-init:
Version:          0.19.0
GitCommit:        de40ad0
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> docker build -t reproducible-proj .
[+] Building 527.6s (10/10) FINISHED                                                                                                                                                  docker:desktop-linux
=> [internal] load build definition from Dockerfile                                                                                                                                                  0.5s
=> => transferring dockerfile: 446B                                                                                                                                                                  0.2s
=> [internal] load metadata for [docker.io/library/python:3.11.13-slim](http://docker.io/library/python:3.11.13-slim)                                                                                                                                5.6s
=> [internal] load .dockerignore                                                                                                                                                                     0.2s
=> => transferring context: 2B                                                                                                                                                                       0.0s
=> [internal] load build context                                                                                                                                                                   396.8s
=> => transferring context: 379.23MB                                                                                                                                                               396.2s
=> [1/5] FROM [docker.io/library/python:3.11.13-slim@sha256:a0939570b38cddeb861b8e75d20b1c8218b21562b18f301171904b544e8cf228](http://docker.io/library/python:3.11.13-slim@sha256:a0939570b38cddeb861b8e75d20b1c8218b21562b18f301171904b544e8cf228)                                                                         67.5s
=> => resolve [docker.io/library/python:3.11.13-slim@sha256:a0939570b38cddeb861b8e75d20b1c8218b21562b18f301171904b544e8cf228](http://docker.io/library/python:3.11.13-slim@sha256:a0939570b38cddeb861b8e75d20b1c8218b21562b18f301171904b544e8cf228)                                                                          1.5s
=> => sha256:a4aefcec16c5bdc01af2ad1c5341b420d4179f3b825c0dc866367fb43f0d50ac 250B / 250B                                                                                                            0.4s
=> => sha256:764e05fe66b6768e40fa2a21d5108eceb8f3f8f2c32463d72c109c54dde0d5c1 14.64MB / 14.64MB                                                                                                     21.0s
=> => sha256:11b89692b2085631f6e2407edd8545b033c8e6945837103875d6db484e945b6f 1.29MB / 1.29MB                                                                                                        4.8s
=> => sha256:ce1261c6d567efa8e3b457673eeeb474a0a8066df6bb95ca9a6a94a31e219dd3 29.77MB / 29.77MB                                                                                                     32.8s
=> => extracting sha256:ce1261c6d567efa8e3b457673eeeb474a0a8066df6bb95ca9a6a94a31e219dd3                                                                                                            20.4s
=> => extracting sha256:11b89692b2085631f6e2407edd8545b033c8e6945837103875d6db484e945b6f                                                                                                             1.7s
=> => extracting sha256:764e05fe66b6768e40fa2a21d5108eceb8f3f8f2c32463d72c109c54dde0d5c1                                                                                                             6.5s
=> => extracting sha256:a4aefcec16c5bdc01af2ad1c5341b420d4179f3b825c0dc866367fb43f0d50ac                                                                                                             0.2s
=> [2/5] WORKDIR /app                                                                                                                                                                                2.2s
=> [3/5] COPY requirements.txt .                                                                                                                                                                     0.5s
=> [4/5] RUN pip install -r requirements.txt                                                                                                                                                        33.1s
=> [5/5] COPY . .                                                                                                                                                                                   27.0s
=> exporting to image                                                                                                                                                                               62.8s
=> => exporting layers                                                                                                                                                                              32.7s
=> => exporting manifest sha256:dfe1830e7975a1e3be946847ab3a8b9470451eb4558876af10f934e04e24a5dd                                                                                                     0.0s
=> => exporting config sha256:d914aee722ae6fe957e2f64b0a4564006fa245582dd655be876084ef4b2bb039                                                                                                       0.0s
=> => exporting attestation manifest sha256:93b635db5668962e48334106650d12e422de663b75e2702c3e61e0dec100f10d                                                                                         0.2s
=> => exporting manifest list sha256:0319c0cd5241e76e7868f4552b51fac5b1712520b37e368c140cc7981100b559                                                                                                0.1s
=> => naming to [docker.io/library/reproducible-proj:latest](http://docker.io/library/reproducible-proj:latest)                                                                                                                                           0.0s
=> => unpacking to [docker.io/library/reproducible-proj:latest](http://docker.io/library/reproducible-proj:latest)

PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> docker run reproducible-proj
Running experiment...
Numpy version: 1.24.0
Computation: 6

## Push & Pull Your Own Docker Images

PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> docker build -t sooyyy/soo_docker:latest .
[+] Building 7.2s (10/10) FINISHED                                                                                                                                                    docker:desktop-linux
=> [internal] load build definition from Dockerfile                                                                                                                                                  0.1s
=> => transferring dockerfile: 446B                                                                                                                                                                  0.0s
=> [internal] load metadata for [docker.io/library/python:3.11.13-slim](http://docker.io/library/python:3.11.13-slim)                                                                                                                                0.9s
=> [internal] load .dockerignore                                                                                                                                                                     0.0s
=> => transferring context: 2B                                                                                                                                                                       0.0s
=> [1/5] FROM [docker.io/library/python:3.11.13-slim@sha256:a0939570b38cddeb861b8e75d20b1c8218b21562b18f301171904b544e8cf228](http://docker.io/library/python:3.11.13-slim@sha256:a0939570b38cddeb861b8e75d20b1c8218b21562b18f301171904b544e8cf228)                                                                          0.1s
=> => resolve [docker.io/library/python:3.11.13-slim@sha256:a0939570b38cddeb861b8e75d20b1c8218b21562b18f301171904b544e8cf228](http://docker.io/library/python:3.11.13-slim@sha256:a0939570b38cddeb861b8e75d20b1c8218b21562b18f301171904b544e8cf228)                                                                          0.1s
=> [internal] load build context                                                                                                                                                                     5.1s
=> => transferring context: 1.66MB                                                                                                                                                                   4.9s
=> CACHED [2/5] WORKDIR /app                                                                                                                                                                         0.0s
=> CACHED [3/5] COPY requirements.txt .                                                                                                                                                              0.0s
=> CACHED [4/5] RUN pip install -r requirements.txt                                                                                                                                                  0.0s
=> CACHED [5/5] COPY . .                                                                                                                                                                             0.0s
=> exporting to image                                                                                                                                                                                0.5s
=> => exporting layers                                                                                                                                                                               0.0s
=> => exporting manifest sha256:dfe1830e7975a1e3be946847ab3a8b9470451eb4558876af10f934e04e24a5dd                                                                                                     0.0s
=> => exporting config sha256:d914aee722ae6fe957e2f64b0a4564006fa245582dd655be876084ef4b2bb039                                                                                                       0.0s
=> => exporting attestation manifest sha256:bbf9c33d4207a97976d8d2ff65d7fb2df24f1dec14abc0ee166e2c5c3676a612                                                                                         0.1s
=> => exporting manifest list sha256:194a576fb7c3804a7d80269d359374613f17a18fb4f405198ba2b68d1cac0e71                                                                                                0.1s
=> => naming to [docker.io/sooyyy/soo_docker:latest](http://docker.io/sooyyy/soo_docker:latest)                                                                                                                                                   0.1s
=> => unpacking to [docker.io/sooyyy/soo_docker:latest](http://docker.io/sooyyy/soo_docker:latest)                                                                                                                                                0.0s
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> docker push sooyyy/soo_docker:latest:latest
invalid reference format
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> docker push sooyyy/soo_docker:latest
The push refers to repository [[docker.io/sooyyy/soo_docker](http://docker.io/sooyyy/soo_docker)]
efc08dc7a5c5: Pushed
764e05fe66b6: Pushed
9178a0db92aa: Pushed
a283d3a0e70c: Pushed
8744d288d81d: Pushed
a4aefcec16c5: Pushed
e7c578bb4fbc: Pushed
11b89692b208: Pushed
ce1261c6d567: Pushed
latest: digest: sha256:194a576fb7c3804a7d80269d359374613f17a18fb4f405198ba2b68d1cac0e71 size: 856

S C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> docker pull sooyyy/soo_docker:latest
latest: Pulling from sooyyy/soo_docker
Digest: sha256:194a576fb7c3804a7d80269d359374613f17a18fb4f405198ba2b68d1cac0e71
Status: Image is up to date for sooyyy/soo_docker:latest
[docker.io/sooyyy/soo_docker:latest](http://docker.io/sooyyy/soo_docker:latest)
PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> docker run sooyyy/soo_docker:latest
Running experiment...
Numpy version: 1.24.0
Computation: 6
</details>```

 
