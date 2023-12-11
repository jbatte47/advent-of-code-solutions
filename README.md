# Advent of Code Solutions, 2023

### Setup

#### Python Environment

Pyenv is strongly suggested for controlling your python version/dependencies. See their [installation guide](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation) for setup instructions.

Once installation is complete, it's time to set up your environment for this project. At time of writing we're using Python 3.10.6, so to recreate that environment, run the following:

```sh
pyenv install 3.10.6
pyenv virtualenv 3.10.6 python-advent
pyenv activate python-advent
```

#### Dependencies

```sh
pip install -r requirements.txt
```

**NOTE**: if you're using a different environment manager such as Conda, you're on your own - good luck :grimacing:

### Running the app

```sh
python advent.py
```
