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
from database_interface import Database
import ag.logging as log

__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.1"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Alpha"

log.set(5)

class Chatter(object):
    """Chatter App."""

    def __init__(self, options):
        """Gonna need a db, and some creds."""
        log.debug("Starting AG Chatter Bot.")
        self.options = options
        self.db = Database(host=options.redis_host, pass_=options.redis_pass)
        self.creds = "mycreds"
        self.database = "mydatabase"
        log.debug(options)

    def sanity(self):
        """This kind of thing should be standardized."""
        log.debug("Starting Stanity Check")
        key = "stuff"
        value = "morestuff"
        self.db.write_data(key, value)
        new_value = self.db.read_data(key)
        assert value == new_value
        return True

    def main(self):
        """This kind of thing should be standardized."""
        if self.sanity:
            return True
        return False

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
        log.error("and thats okay too.")
        sys.exit(e)
