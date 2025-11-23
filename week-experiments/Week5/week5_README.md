# Week 5 — Pipeline Reproducibility

This week expanded reproducibility to the entire ML workflow.
I modularized the pipeline into separate scripts (fetch, scrape, clean, train) and connected them through the Makefile.
Seeing the full pipeline re-run end-to-end and produce identical outputs was extremely rewarding.
However, differences between PowerShell and Bash syntax reminded me that automation also depends on the underlying shell.
Adding shell-specific notes and dependency details made the project more accessible and reproducible for others.
