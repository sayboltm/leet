# Readme

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
pip uninstall
```

Fun fact: the potentially unusual looking URL looks like what it does because the syntax is VCS+protocol. So this is saying use git as VCS, and Git protocol as transfer protocol. If you're using Mercurial over SSH at home or something, it would look like hg+ssh://...

Extra:
If you work behind a corporate firewall with a proxy and don't feel like configuring the proxy to work with pip, try using http instead of Git protocol.
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

To actually install:
```
```

