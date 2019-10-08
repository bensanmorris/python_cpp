### About

Demonstrates calling C++ code / structures from python.

#### Building & Running

    - sudo apt-get install python3-venv 
    - (gdb debugging support) sudo apt-get install gdb python3-dbg
    - python3 -m venv ve
    - . ve/bin/activate
    - ccmake .
    - (configure, generate)
    - make
    - python hello.py
    
#### Debugging

    - gdb python
    - break file:linenum or break function_name
    - run script.py
    - bt
    - list or list n (where n is numbers around current location)

#### Packaging:

Links:

    - https://www.codeproject.com/articles/11805/embedding-python-in-c-c-part-i
    - https://stackoverflow.com/questions/145270/calling-c-c-from-python
    - http://svn.python.org/projects/ctypes/trunk/ctypes/docs/manual/tutorial.html
    - https://docs.python.org/3/tutorial/modules.html#packages        
    - https://packaging.python.org/tutorials/packaging-projects
    - https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives

Steps:

    - python3 -m pip install --user --upgrade setuptools wheel
    - python3 setup.py sdist bdist_wheel
