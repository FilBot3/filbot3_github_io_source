setup:
	git clone https://github.com/predatorian3/predatorian3.github.io

python:
	python -m pip install -r python-3-requirements.txt
	
serve:
	python -m mkdocs serve
	
gh-pages:
	# Because GitHub is dumb.
	# https://www.mkdocs.org/user-guide/deploying-your-docs/#organization-and-user-pages
	# Seems that SSH Keys that have passwords on them, unless you're using an
	# ssh-agent seem to fail with the mkdocs gh-deploy command. So, that is dumb.
	cd ../predatorian3.github.io/
	python -m mkdocs gh-deploy \
	  --config-file ../predatorian3_github_io_source/mkdocs.yml \
		--remote-name master