# python
'''
Author: AsensioRM
'''

'''
tree:
my_package
    __init__.py
    Module1.py
    Module2.py
setup.py

Get jar.z:
python setup.py build
python setup.py sdist

Run:
python setup.py install

就导入到python默认包了
'''

# setup.py:
'''
from distutils.core import setup
setup(name = "New", Version = "1.0", description= "hello", author = "AsensioRM", py_modules=['Module1.py','Module2.py'])
'''