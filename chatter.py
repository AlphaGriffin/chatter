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
from utils import DataReader
from network import Model
import ag.logging as log

__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.1"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Alpha"

log.set(3)

class Chatter(object):
    """Chatter App."""

    def __init__(self, options):
        """Gonna need a db, and some creds."""
        log.info("Starting AG Chatter Bot.")
        self.options = options
        # Build Constructors
        self.idx2word = Database(
                host=options.redis_host, pass_=options.redis_pass, db=0
            )
        self.word2idx = Database(
                host=options.redis_host, pass_=options.redis_pass, db=1
            )
        self.dataReader = DataReader(
                self.options, self.idx2word, self.word2idx
            )
        self.model = Model(
                self.options
            )
        log.debug(options)
        log.info("Init complete.")

    def sanity(self):
        """This kind of thing should be standardized."""
        log.info("Starting Stanity Check")
        key = "stuff"
        value = "morestuff"
        self.idx2word.write_data(key, value)
        new_value = self.idx2word.read_data(key)
        assert value == new_value
        log.debug("Passed Stanity Check")
        return True

    def main(self):
        """This kind of thing should be standardized."""
        if self.sanity():
            # Add the path to files in the config.yaml
            dataset = self.dataReader.make_buckets()
            print(dataset)
            return True
        return False

def main():
    """Launcher for the app."""
    options = Options() # test
    app = Chatter(options)


    if app.main():
        sys.exit('Alphagriffin.com | 2017')
    return True

if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except Exception as e:
        log.error(e)
        sys.exit("and thats okay too.")
