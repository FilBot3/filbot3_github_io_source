# Phil's GitHub Pages

## Overview

## Requirements

To build this site and push it, you'll need to have the following

* A GitHub Account
* Python 3.6 or newer with pip

## Setup

If your system doesn't have GNU Make on it, issue the following command to get
`shovel` installed. Shovel is just another Task execution tool.

```bash
python -m pip install -r python-3-requirements.txt
```

This then will install `shovel` and `mkdocs` plus any dependencies needed.

## Usage

### GNU Make

```bash
make serve
make gh-pages
```

### Shovel

To see the available tasks

```bash
shovel tasks
shovel serve
shovel ghpages
```

## References

* [GitHub Pages Help](https://pages.github.com/)
* [MkDocs Home Page](https://www.mkdocs.org)
* [MkDocs Material Theme](https://squidfunk.github.io/mkdocs-material/)