"""Load a yaml file as options input.

All params in the config are cast to the Options() object.
"""

import os
import yaml

__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.3"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Beta"


class Options(object):
    """OH OH DO a yaml file!."""

    def __init__(self, data_path=None):
        """OH OH DO a yaml file!."""
        if data_path is None:
            data_path = os.path.join(os.getcwd(),
                                     "config",
                                     "config.yaml")
        self.config = self.load_options(data_path)
        for i in self.config:
            setattr(self, '{}'.format(i),
                    '{}'.format(self.config[i]))

    def __call__(self):
        """Sanity check."""
        if self.config:
            return True
        return False

    def __str__(self):
        """Print all options."""
        options = ""
        for i in self.__dict__:
            if 'config' not in i:
                # print("{}: {}".format(i, self.__dict__[i]))
                options += "{}: {}\n".format(i, self.__dict__[i])
        return options

    @staticmethod
    def load_options(data_path):
        """Open and read yaml file just like any other."""
        with open(data_path, 'r') as config:
            new_config = yaml.load(config)
        return new_config
