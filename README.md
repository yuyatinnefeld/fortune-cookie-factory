# Poetry Package with Fortune Cookie Factory Project

## About
A simple Python package `fortune-cookie-facrory` is written with the modern Python development tool, `Poetry` and deployed with `GitHub Actions`. 

You can see the message inside the cookie, a Chinese phrase with a list of lucky numbers for you to enjoy, share, or put in your own cookies.

The main goal of this project is that you have fun playing the fortune cookie app. My personal goals are learning GitHub Actions CI/CD well, creating, testing and mirroring a poetry project.


## How it works?       

```bash
# install the package
pip install fortune-cookie-factory

# use the 'open_cookie' function
$ python

>>> import fortune_cookie.app as app

>>> app.open_cookie()
🎉 Your fortune cookie tells 🎉
🍪 When fear hurts you, conquer it and defeat it! 🍪

>>> app.open_cookie()
🎉 Your fortune cookie tells 🎉
🍪 People are naturally attracted to you. 🍪

>>> app.open_cookie()
🎉 Your fortune cookie tells 🎉
🍪 If winter comes, can spring be far behind? 🍪
```



## How to run the project locally?
```bash
### local test ###

# run script
git clone git@github.com:yuyatinnefeld/fortune-cookie-factory.git
cd fortune-cookie-factory/fortune-cookie-factory
poetry run my-demo-script

# install pacakges
poetry env use python3.11

poetry install

# run test
poetry add pytest pytest-cov bandit safety -D
poetry run pytest

# reformat
poetry add black -D
poetry run black fortune_cookie

### local deploy ###
# create a API token in the PyPI Repo

# set as an env variable
export POETRY_PYPI_TOKEN_PYPI=<my-token>

# enable token for pypi
poetry config pypi-token.pypi $POETRY_PYPI_TOKEN_PYPI

# build the project
poetry build

# publish the project to pypi
poetry publish

# clean up
poetry shell
poetry env info
poetry env remove --all
```