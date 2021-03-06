""" Shovel Tasks file
"""

import os
from shovel import task

@task
def setup():
    """ Setup the User's GitHub Pages repo.
    """
    os.system("""git clone https://github.com/filbot3/filbot3.github.io""")

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
    import datetime
    os.system("""python -m mkdocs build""")
    os.chdir("../filbot3.github.io/")
    os.system("""cp -R ../filbot3_github_io_source/site/* ./""")
    right_now = datetime.date.today().ctime()
    os.system("""git add .""")
    os.system(f"""git commit -m 'Built on {right_now}'""")
    os.system("""git push origin master""")


@task
def ghpgswin():
    """Because windows sucks.
    """
    import datetime
    os.system("""python -m mkdocs build""")
    os.chdir("../filbot3.github.io/")
    os.system("""Copy-Item -Path ..\filbot3_github_io_source\site\* -Filter *.* -Recurse -Destination .\ -Container -Force -Exclude ..\filbot3_github_io_source\.git\*""")
    right_now = datetime.date.today().ctime()
    os.system("""git add .""")
    os.system(' '.join(("git commit -m 'Built on'", right_now)))
    os.system("""git push origin master""")
