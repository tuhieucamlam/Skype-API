import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','LOG/','config.ini']

# TARGET
target = Executable(
    script="main.py",
    #base="Win32GUI",
    icon="icon.ico",
    copyright = "TuHieu 0979873414 (C) 2021-06",
)


#python setup.py build

# SETUP CX FREEZE bdist_msi/build_exe
setup(
    name = "SkypeCallEvent",
    version = "1.0.0.1",
    description = "Service by SkypeCallEvent",
    author = "0979873414",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
)
