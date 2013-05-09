#
# Add required modules to PYTHONPATH
#
import os
import sys

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__)))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

def insert(path):
    if path not in sys.path:
        sys.path.insert(0, path)

def insert_modules(root_path, modules):
    insert(root_path)
    for mod in modules:
        mod_path = os.path.join(root_path, mod)
        insert(mod_path)
