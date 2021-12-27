# This file is part of template-latex-project.
#
# template-latex-project is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# template-latex-project is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with template-latex-project. If not, see <https://www.gnu.org/licenses/>.

from glob import glob
from invoke import task
from os import environ
from pathlib import Path
from shutil import copy


# #####################################################################################################################
# GLOBALS
# #####################################################################################################################


BUILD_DIR = Path("./build")
CONTENT_DIR = Path("./content")
DIST_DIR = Path("./dist")
MAIN_FILE = Path("document.tex")
VERSION_FILE = Path("VERSION")


# #####################################################################################################################
# SUPPORTING CLASSES AND FUNCTIONS
# #####################################################################################################################


def is_ci():
    return "CI" in environ.keys()


# #####################################################################################################################
# TASKS
# #####################################################################################################################


@task
def build(c):
    """Build document"""
    c.run(f"latexmk -interaction=nonstopmode -file-line-error -pdf -outdir={BUILD_DIR} {MAIN_FILE}")


@task
def clean(c):
    """Remove build files and directories"""
    patterns = [
        "./**/*.bak*",
        "./**/__latexindent_temp.tex",
        "./**/*.synctex.gz",
        "./**/*.log",
        f"./{BUILD_DIR}/*.*",
        f"./{DIST_DIR}/*.*"
    ]

    for pattern in patterns:
        for f in glob(pattern, recursive=True):
            c.run(f"rm {f}")


@task
def format(c, file_path=None):
    """Format the code"""
    files = [file_path] if file_path else glob("./**/*.tex", recursive=True)

    for f in files:
        c.run(' '.join([
            "latexindent",
            "--yaml='onlyOneBackUp: 1, removeTrailingWhitespace: 1'",
            "--silent",
            "--overwrite",
            f"--cruft={Path(f).parent}",
            "--check" if is_ci() else "",
            f
        ]))


@task(format)
def lint(c, file_path=None):
    """Check the code for syntax issues"""
    files = [file_path] if file_path else glob("./**/*.tex", recursive=True)

    for f in files:
        c.run(f"chktex {f}")


@task
def release(c):
    copy(f"{BUILD_DIR}/{MAIN_FILE.stem}.pdf", f"{DIST_DIR}/")
