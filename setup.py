from setuptools import setup, find_packages
''' BReak, need to do more work 
URLS:

sayboltm/leet: Wrapper for some functions I use but don't upload to GH
https://github.com/sayboltm/leet

How to delete a tag in Git - a post by Manik Rathee | Design, UX and Engineering
http://www.manikrathee.com/how-to-delete-a-tag-in-git.html

Building and Distributing Packages with Setuptools — setuptools 39.0.1 documentation
https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode

Installing Python Modules (Legacy version) — Python 2.7.14 documentation
https://docs.python.org/2/install/index.html#distutils-configuration-files

python - Configuring so that pip install can work from github - Stack Overflow
https://stackoverflow.com/questions/8247605/configuring-so-that-pip-install-can-work-from-github

pip install — pip 9.0.3 documentation
https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support

pip install — pip 9.0.3 documentation
https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs

Minimal Structure — Python Packaging Tutorial
https://python-packaging.readthedocs.io/en/latest/minimal.html

reflection - How to list all functions in a Python module? - Stack Overflow
https://stackoverflow.com/questions/139180/how-to-list-all-functions-in-a-python-module

Right way to set python package with sub-packages - Stack Overflow
https://stackoverflow.com/questions/26528178/right-way-to-set-python-package-with-sub-packages

Building and Distributing Packages with Setuptools — setuptools 39.0.1 documentation
http://setuptools.readthedocs.io/en/latest/setuptools.html
'''

setup(
    entry_points={
        'plottr': 'plottr = leet.plottr:__init__'},
    name='leet',
    version='0.1',
    description='The funniest joke in the world',
    url='http://github.com/sayboltm/leet',
    author='Mike',
    author_email='sayboltm@users.noreply.github.com',
    license='MIT',
#      packages=['leet', 'plottr'],
    packages=find_packages(),
    zip_safe=False)

## distutils < setuptools
#from distutils.core import setup
#
#if __name__=='__main__':
#    setup(
#        name='leet'
#        version='0.1'
#        description='testdescription'
#        url='http://github.com/sayboltm/leet',
#        author='Mike'
#        package_dir = {'leet': 'leet',
#            'leet.plottr': 'leet/plottr'}
#        packages = ['leet', 'leet.plottr']
#        )
#
#setup(name='leet',
#      version='0.1',
#      description='The funniest joke in the world',
#      url='http://github.com/sayboltm/leet',
#      author='Mike',
#      author_email='sayboltm@users.noreply.github.com',
#      license='MIT',
##      packages=['leet', 'plottr'],
#      packages=find_packages()
#      zip_safe=False)


