### About

Demonstrates calling C++ code / structures from python.

#### Building & Running

    - python3 -m venv ve
    - . ve/bin/activate
    - ccmake .
    - (configure, generate)
    - make
    - python hello.py
    
There is also a set of practice python code snippets in practice.py.

#### Packaging:

Links:

    - https://stackoverflow.com/questions/145270/calling-c-c-from-python
    - http://svn.python.org/projects/ctypes/trunk/ctypes/docs/manual/tutorial.html
    - https://docs.python.org/3/tutorial/modules.html#packages        
    - https://packaging.python.org/tutorials/packaging-projects
    - https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives

Steps:

    - python3 -m pip install --user --upgrade setuptools wheel
    - python3 setup.py sdist bdist_wheel
