#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright (C) 2017 Alpha Griffin
# @%@~LICENSE~@%@

"""
AG_Chatter
"""

import os, sys
import numpy
import tensorflow
from config.__options__ import Options

__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.1"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Alpha"

print("is this working?")

class Chatter(object):
    """Chatter App."""

    def __init__(self, options):
        """Gonna need a db, and some creds."""
        self.options = options
        self.creds = "mycreds"
        self.database = "mydatabase"
        print(options)

    def main(self):
        return True

def main():
    """Launcher for the app."""
    options = Options()
    app = Chatter(options)


    if app.main():
        sys.exit('Alphagriffin.com | 2017')
    return True


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("and thats okay too.")
        sys.exit(e)
