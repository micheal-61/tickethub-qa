# TicketHub QA Package

[![CI](https://github.com/micheal-61/tickethub-qa/actions/workflows/ci.yml/badge.svg)](https://github.com/micheal-61/tickethub-qa/actions/workflows/ci.yml)

Software Quality Testing — Practical Project Test 1
Student: Micheal Otim (SEP24/BSE/4497U)

## Overview

Black-box test design, automation and defect reporting for the TicketHub
order module (`src/tickethub.py`). Tests are designed **from the
Requirements Specification (Appendix A)**, not from the source code.

## One-command run

    make install && make test

Or directly:

    pip install -r requirements.txt
    pytest tests/ -v

## Project structure

    src/           tickethub.py (SUT, unchanged)
    tests/         pytest suite, traceable to TC IDs
    test_design/   test case sheet, cause-effect graph, state diagram
    defects/       DEF-01..DEF-08, one per distinct root cause
    ci/            pipeline config, green + failing run evidence, JUnit XML
    report/        final test report (Parts A-E)

## Test report

After running the suite:

    ci/report.html         (human-readable)
    ci/test-results.xml    (JUnit XML, published by CI)

## xfail policy

Tests tied to open defects are marked `@pytest.mark.xfail(strict=True,
reason="DEF-0n")`. `strict=True` means the pipeline turns RED again when a
defect is fixed — the signal to remove the marker and close the defect.

Current suite status: **44 passed, 19 xfailed, 0 failed**. All 8 open
defects are xfailed pending fixes.

## Environment

- Python 3.10+
- pytest 8.2.0, pytest-html 4.1.1 (pinned in `requirements.txt`)
- CI: GitHub Actions (`.github/workflows/ci.yml`)