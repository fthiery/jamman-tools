#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2011, Florent Thiery

import os
from termcolor import colored
import jamman.utils as utils

normalize = True
play_preview = False
show_info = False

sequence_file = 'sequence.jam'
preview_name = 'preview.wav'
merge_cmd = 'wavmerge -o %s' %preview_name
normalize_cmd = 'normalize %s' %preview_name
info_cmd = 'wavinfo %s' %preview_name
playback_cmd = 'mplayer %s' %preview_name

wave_files = list()

if utils.dir_is_project('.', quit=True):
    print colored('Rendering project %s\n' %utils.get_project_name(), 'green')

files = os.listdir('.')
for filename in files:
    if filename.upper().endswith('.WAV'):
        if filename != preview_name:
            wave_files.append(filename)

if os.path.isfile(preview_name):
    print colored('File %s already exists, not merging' %preview_name, 'red')
    answear = raw_input('Do you want to overwrite it ? y/N ')
    if 'Y' in answear.upper():
        os.remove(preview_name)

if os.path.isfile(preview_name):
    print 'Quitting'
    import sys
    sys.exit()
else:
    wave_files.sort()
    if not os.path.isfile(sequence_file):
        for wave in wave_files:
            merge_cmd += ' %s' %wave
    else:
        sequence = utils.read_file(sequence_file) 
        print sequence
        merge_cmd += ' %s' %sequence
    print colored('\nMerging files: %s' %merge_cmd, 'green')
    os.system(merge_cmd)

    if show_info:
        print colored('Finished merging, file info:', 'green')
        os.system(info_cmd)

    if normalize:
        print colored('\nNormalizing', 'green')
        os.system(normalize_cmd)

    if play_preview:
        print 'Starting playback'
        os.system(playback_cmd)

    print colored('All done', 'green')
