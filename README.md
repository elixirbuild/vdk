# vdk
A Command-Line-Interface for creating C++ projects.

## Unix/MacOs Setup

### 1. Set up dependencies

* Python 3.6 or newer with [pip](https://pip.pypa.io/en/stable/installation/)
* [Click](https://click.palletsprojects.com/en/8.0.x/)
* [Virtualenv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv)

<br>

* Copy the repository code

```shell
git clone https://github.com/elixirbuild/vdk.git
```

* In the `vdk` directory, use:

```shell
python3 -m venv src/env
```

* To activate the shell:

```shell
source env/bin/activate
```

After running those commands you should see a `(env)` next to your input.

When inside the virtualenv, install:
```shell
python3 -m pip install click
```
