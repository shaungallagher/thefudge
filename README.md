# The Fudge [![Build Status](https://travis-ci.org/nvbn/thefudge.svg)](https://travis-ci.org/nvbn/thefudge)

Magnificent app which corrects your previous console command,
inspired by [@liamosaur](https://twitter.com/liamosaur/status/506975850596536320)
twit.

Few examples:

```bash
➜ apt-get install vim
E: Could not open lock file /var/lib/dpkg/lock - open (13: Permission denied)
E: Unable to lock the administration directory (/var/lib/dpkg/), are you root?

➜ fudge
sudo apt-get install vim
[sudo] password for nvbn:
Reading package lists... Done
...

➜ git push
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master


➜ fudge
git push --set-upstream origin master
Counting objects: 9, done.
...

➜ puthon
No command 'puthon' found, did you mean:
 Command 'python' from package 'python-minimal' (main)
 Command 'python' from package 'python3' (main)
zsh: command not found: puthon

➜ fudge
python
Python 3.4.2 (default, Oct  8 2014, 13:08:17)
...

➜ git brnch
git: 'brnch' is not a git command. See 'git --help'.

Did you mean this?
	branch

➜ fudge
git branch
* master
```

## Installation

Install `The Fudge`:

```bash
sudo pip install thefudge
```

And add to `.bashrc` or `.zshrc`:

```bash
alias fudge='$(thefudge $(fc -ln -1))'
```

Or in `config.fish`:

```fish
function fudge
    eval (thefudge (history | head -n1))
end
```

## How it works

The Fudge tries to match rule for the previous command, create new command
using matched rule and run it. Rules enabled by default:

* `git_no_command` &ndash; fixes wrong git commands like `git brnch`;
* `git_push` &ndash; adds `--set-upstream origin $branch` to previous failed `git push`;
* `no_command` &ndash; fixes wrong console commands, for example `vom/vim`;
* `sudo` &ndash; prepends `sudo` to previous command if it failed because of permissions.

## Creating your own rules

For adding your own rule you should create `your-rule-name.py`
in `~/.thefudge/rules`. Rule should contain two functions:
`match(command: Command, settings: Settings) -> bool`
and `get_new_command(command: Command, settings: Settings) -> str`.

`Command` have three attributes: `script`, `stdout` and `stderr`.

`Settings` is `~/.thefudge/settings.py`.

Simple example of the rule for running script with `sudo`:

```python
def match(command, settings):
    return ('permission denied' in command.stderr.lower()
            or 'EACCES' in command.stderr)


def get_new_command(command, settings):
    return 'sudo {}'.format(command.script)
```

[More examples of rules](https://github.com/nvbn/thefudge/tree/master/thefudge/rules),
[utility functions for rules](https://github.com/nvbn/thefudge/tree/master/thefudge/utils.py).

## Settings

The Fudge have a few settings parameters:

* `rules` &ndash; list of enabled rules, by default all;
* `command_not_found` &ndash; path to `command_not_found` binary,
by default `/usr/lib/command-not-found`.

## Developing

Install `The Fudge` for development:

```bash
pip install -r requirements.txt
python setup.py develop
```

Run tests:

```bash
py.test
```

## License MIT
