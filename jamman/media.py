#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2011, Florent Thiery

PLAY_CMD = 'mplayer %s'

import os
from termcolor import colored

def play_file(filename):
    if os.path.isfile(filename):
        print colored('Playing file %s' %filename, 'green')
        os.system(PLAY_CMD %filename)
    else:
        print colored('Wrong input, file %s doesn\'t exist' %filename, 'red')
