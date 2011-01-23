#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2011, Florent Thiery

import os
from termcolor import colored
from jamman.utils import dir_is_project

preview = False
#preview = True
bitrate = 256000
folder = 'encoded'

def compress_to(filename, codec):
    if codec in ['mp3', 'flac']:
        print colored('Encoding file %s to %s format' %(filename, codec), 'green')
        output_filename = os.path.join(folder, ('%s.%s' %(os.path.splitext(filename)[0], codec)))
        os.system('ffmpeg -ab %s -i %s %s' %(bitrate, filename, output_filename))
        return output_filename
    return None

def play_file(filename):
    print colored('Playing encoded file file %s' %filename, 'green')
    os.system('mplayer %s' %filename)

if dir_is_project('.', quit=True):
    if not os.path.isdir(folder):
        os.mkdir(folder)

    codecs = ['mp3', 'flac']

    for codec in codecs:
        out = compress_to('preview.wav', codec)
        if preview:
            play_file(out)

print colored('All done', 'green')
