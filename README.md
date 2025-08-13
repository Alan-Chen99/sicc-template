# Stationeers SICC Template

A template for [Stationeers SICC Compiler](https://github.com/Alan-Chen99/sicc).

Currently this repo locks a version of SICC slightly more tested than a typical commit.
In the future it will probably pull from PyPI instead. Use `uv lock --upgrade` and then `uv sync` to upgrade.

Please write an issue if this template doesnt work or can include config for whatever tooling you use.

## Install

Install [uv](https://github.com/astral-sh/uv) and run

```bash
git clone https://github.com/Alan-Chen99/sicc-template.git
cd sicc-template
uv sync
# optional: upgrade to latest git version
# uv lock --upgrade
source ./.venv/bin/activate
python main.py
# or: sicc main.py
```
