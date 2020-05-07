setup:
	git clone https://github.com/filbot3/filbot3.github.io

python:
	python -m pip install -r python-3-requirements.txt

serve:
	python -m mkdocs serve

gh-pages:
	python -m mkdocs build
	# Because GitHub is dumb.
	# https://www.mkdocs.org/user-guide/deploying-your-docs/#organization-and-user-pages
	# Seems that SSH Keys that have passwords on them, unless you're using an
	# ssh-agent seem to fail with the mkdocs gh-deploy command. So, that is dumb.
	cd ../filbot3.github.io/
	#python -m mkdocs gh-deploy \
	#  --config-file ../predatorian3_github_io_source/mkdocs.yml --remote-name master
	cp -R ../filbot3_github_io_source/site/* ./
	git add .
	git commit -m 'Built on $(shell date +"%y-%m-%d-%k%M%S")'
	git push origin master
