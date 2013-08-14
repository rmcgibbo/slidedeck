"""Code to create a template project
"""

import os
import shutil

def create_project(directory):
    """Create a project and copy the files into it.
    """
    
    if os.path.exists(directory):
        raise OSError("Directory '%s' already exists" % directory)

    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))
    
            
    def callback(src, names):
        base = os.path.relpath(src, data_dir)
        for name in names:
            print("\033[92mcreate\033[0m  {:s}".format(os.path.join(directory, base, name)))
        return []


    shutil.copytree(data_dir, directory, ignore=callback)
