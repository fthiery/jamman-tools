#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2011, Florent Thiery 

import os
from jamman.utils import dir_is_project, get_samples, get_project_name
from termcolor import colored
from jamman.media import play_file

sequence_path = 'sequence.jam'

def write_sequence(text):
    print 'Writing sequence to %s' %sequence_path
    fname = open(sequence_path, 'w')
    fname.write(text)
    fname.close()

def record_sequence():
    os.system('clear')
    current_dir_name = get_project_name()
    print colored('Record or preview sequence of project: %s' %current_dir_name, 'blue')
    samples = get_samples()
    print '\nAvailable samples are'
    for sample in samples:
        print '\t%s' %sample
    print '\nEnter\n  * sequence number separated by spaces\n  * add ? to listen to the sample\n  * "q" to quit'
    print 'Examples: 1 2 3 or 1? 2?\n'
    seq = raw_input('> ')
    numbers = seq.strip().split(' ')
    sequence = ''
    previewed = False
    for number in numbers:
        if number ==  'q':
            import sys
            sys.exit()
        if '?' not in number:
            sample = '%s.WAV' %number
            if os.path.isfile(sample):
                sequence += '%s ' %sample
        else:
            filename = "%s.WAV" %number.replace('?','')
            play_file(filename)
            previewed = True
    if sequence != '' and not previewed :
        print 'Sequence: %s' %sequence
        write_sequence(sequence)
    else:
        record_sequence()

if dir_is_project(quit=True):
    record_sequence()
