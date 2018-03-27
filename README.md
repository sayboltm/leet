# Readme
--------

readme goes here. Setup tools stuff:
Looks like there's nothing released yet! Cool!


How to install:
locally:
``` python
cd ~/path/to/folder
pip install .
```
or in editable mode:
``` shell
pip install -e .
```

or from github: (example syntax)
``` python
pip install git+git://github.com/sayboltm/leet.git
```
To remove:
```python
pip uninstall leet
```

Fun fact: the potentially unusual looking URL looks like what it does because the syntax is VCS+protocol. So this is saying use git as VCS, and Git protocol as transfer protocol. If you're using Mercurial over SSH at home or something (but why would you), it would look like hg+ssh://...

Problems?
If you work behind a corporate firewall with a proxy and don't feel like configuring the proxy to work with pip, try using http instead of Git protocol.

For example:
```shell
$ pip install git+git://github.com/sayboltm/leet.git
Collecting git+git://github.com/sayboltm/leet.git
  Cloning git://github.com/sayboltm/leet.git to c:\users\cz3qfp\appdata\local\temp\pip-8ditwmha-build
fatal: unable to connect to github.com:
github.com[0: 192.30.253.112]: errno=No error
github.com[1: 192.30.253.113]: errno=No error

Command "git clone -q git://github.com/sayboltm/leet.git C:\Users\CZ3QFP\AppData\Local\Temp\pip-8ditwmha-build" failed with error code 128 in None
```
Oh no! But fear not.

```python
pip install git+http://github.com/sayboltm/leet.git
```
Boom.

------------------------------------------------------------------------------

Some examples of install urls for reference
```
pip install git+git://github.com/myUser/foo.git@v123
```
or
``` python
pip install git+git://github.com/myUser/foo.git@newBranch
```
``` python
pip install -e git://...
```

# Ref urls:
https://stackoverflow.com/questions/8247605/configuring-so-that-pip-install-can-work-from-github

https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support

https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs

https://python-packaging.readthedocs.io/en/latest/minimal.html

TODO: add markdown language... 
input: 
someWord
output:
someWord\n========

use hacktoberfest for both LOL original addition of the comment/block
prettifier and this upgrayyd

