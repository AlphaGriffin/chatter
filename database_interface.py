#!/usr/bin/env python
# Copyright (C) 2017 Alpha Griffin
# @%@~LICENSE~@%@

"""
Alphagriffin.com
Eric Petersen @Ruckusist <eric.alphagriffin@gmail.com>
"""

__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.3"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Alpha"

import sys
import ag.logging as log
import redis
log.set(5)


class Database(object):
    """A Redis Database manage."""

    def __init__(self,
                 host='192.168.1.2',
                 pass_=' ', db=0):
        """Allow for many instances of itself."""
        if pass_ is not ' ':
            self.database = redis.Redis(
                host=host,
                password=pass_,
                db=db
            )
        else:
            self.database = redis.Redis(
                host=host,
                db=db
            )

    def main(self):
        """Test of connection settings."""
        if self.database:
            log.debug("found that database")
            if self.write_data('4', '20'):
                log.debug("wrote that data")
            twenty = self.read_data('4')
            log.debug("read data test: {}, type: {}".format(
                twenty, type(twenty)
                ))
            # Gotta stop comparing to literal.
            if int(float(twenty)) is 20:
                return True

            log.warn("see here... see.")
            return False
        else:
            log.warn("Not logging into the database.")
        return False

    def write_data(self, key, value):
        """Should have an H value as well."""
        self.database.set(key, value)
        return True

    def read_data(self, key):
        """A basic read of redis data with a utf check."""
        try:
            value = self.database.get(key).decode('UTF-8')
        except:
            try:
                value = self.database.get(key)
            except Exception as e:
                log.fatal("Damnit on the reverse lookup!")
                value = 'unk'
        return value


if __name__ == '__main__':
    log.info("Starting the Database Testing")
    try:
        app = Database()
        if app.main():
            sys.exit("Everything checks out.")
    except Exception as e:
        log.error("and thats okay too.")
        sys.exit(e)
