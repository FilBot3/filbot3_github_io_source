""" Shovel Tasks file
"""

import os
from shovel import task

@task
def setup():
    """ Setup the User's GitHub Pages repo.
    """
    os.system("""git clone https://github.com/predatorian3/predatorian3.github.io""")

@task
def serve():
    """ MkDocs Serve
    """
    os.system("""python -m mkdocs serve""")
    
@task
def ghpages():
    """ MkDocs gh-deploy
    Because GitHub is stupid.
    https://www.mkdocs.org/user-guide/deploying-your-docs/#organization-and-user-pages
    
    Seems you'll need to have an SSH Key with either no password, or loaded into
    an ssh-agent of some sort.
    """
    os.chdir("../predatorian3.github.io/")
    os.system("""python -m mkdocs gh-deploy \
      --config-file ../predatorian3_github_io_source/mkdocs.yml \
      --remote-branch master""")