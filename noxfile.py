#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : noxfile.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 01.10.2024

import nox
import os


@nox.session(
    python=["3.6", "3.7", "3.8", "3.9", "3.10", "3.11", "3.12"], reuse_venv=True
)
def run(session):
    session.env["DUT"] = "ahb_template"
    session.env["SIM"] = "icarus"
    session.env["TIMEPREC"] = "1ps"
    session.env["TIMEUNIT"] = "1ns"
    session.env["WAVES"] = "1"
    session.env["COCOTB_COVERAGE_RCFILE"] = os.path.abspath(".coveragerc")
    session.env["COVERAGE_RC_FILE"] = os.path.abspath(".coveragerc")
    session.env["COCOTB_USER_COVERAGE"] = "1"
    session.env["COVERAGE"] = "1"
    # session.env["COCOTB_LOG_LEVEL"] = "debug"
    # session.env['SIM'] = "verilator"

    session.install(
        "pytest",
        "pytest-xdist",
        "pytest-sugar",
        "pytest-cov",
        "pytest-split",
        "cocotb-bus==0.2.1",
        "cocotb>=1.8.0",
    )
    session.install(".")
    session.run(
        "py.test",
        "--cov=cocotbext",
        "--cov-branch",
        "--cov-report=xml",
        "-rP",
        # "-rP",
        "-n",
        "auto",
        *session.posargs
    )


@nox.session(python=["3.9", "3.10", "3.11", "3.12"], reuse_venv=True)
def lint(session):
    session.install("flake8")
    session.run("flake8")
