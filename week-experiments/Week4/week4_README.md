# Week 4 — Environment Reproducibility

My focus shifted from code to environments.
Capturing dependencies with requirements.txt, environment.yml, and poetry.lock provided byte-for-byte reproducibility.
It was also where I experienced the fragility of environment setup — PowerShell execution policies, Conda prefix paths, and Poetry’s Python version mismatches.
This taught me that reproducibility requires choosing one consistent toolchain and documenting it clearly so others can recreate the exact environment.
