#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2011, Florent Thiery

import os
from termcolor import colored
import jamman.utils as utils

remove_cmd = 'rm -rf %s'

print colored('Cleaning project %s' %utils.get_project_name(), 'green')
files = ['preview.wav', 'encoded']
for filename in files:
    if os.path.exists(filename):
        print 'Removing', filename
        os.system(remove_cmd %filename)
