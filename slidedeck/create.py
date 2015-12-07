"""Code to create a template project
"""

import os
import shutil

TEMPLATE_VARIABLE = 'SLIDEDECK_TEMPLATE'


def curdir(directory):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), directory))


def check_env():
    '''
        Check the current user's environment to return important settings
    '''
    sd_template = os.environ.get(TEMPLATE_VARIABLE, None) or curdir('data')
    return {'template_dir': sd_template}


def create_project(directory, template=None):
    """
        Create a project and copy the template files into it.
    """
    if os.path.exists(directory):
        raise OSError("Directory '%s' already exists" % directory)

    settings = check_env()
    template = template or settings.get('template_dir', None)

    if not os.path.exists(template):
        raise OSError("Template directory '%s' does not exist" % template)
    
    def callback(src, names):
        base = os.path.relpath(src, template)
        for name in names:
            print("\033[92mcreate\033[0m  {:s}".format(os.path.join(directory, base, name)))
        return []

    shutil.copytree(template, directory, ignore=callback)
