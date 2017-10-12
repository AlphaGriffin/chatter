#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright (C) 2017 Alpha Griffin

import os
import re
import time
import numpy as np
import ag.logging as log
import collections


__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.1"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Alpha"


class Model(object):
    """AG_BOT using tensorflow."""
    def __init__(self, options):
        self.options = options
        pass
