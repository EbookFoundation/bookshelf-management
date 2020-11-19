#!/usr/bin/env python

import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','bookshelf_management.settings.settings_base')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()



#sys.path.append("/mnt/c/Users/damon/Desktop/bookshelf-management/bookshelf_management/bookshelf_management/settings")
#export DJANGO_SETTINGS_MODULE=bookshelf_management.settings
    ''' 
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    '''