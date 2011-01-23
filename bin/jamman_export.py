#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2010, Florent Thiery

import os
from termcolor import colored
from jamman.utils import dir_is_project
import shutil

encoded_folder_name = 'encoded'
encoded_files = list()

preferred_codec = 'mp3'
output_folder = 'exported'

print colored('Will export all compressed files with format %s' %preferred_codec, 'green')
a = raw_input('Are you sure ? This will create an "exported" directory in the current dir. y/N ')

def walk_cb(arg, dirname, fnames):
    if dirname.find(encoded_folder_name) != -1:
        print 'Walk: directory %s, filenames: %s' %(dirname, fnames)
        for fname in fnames:
            if fname.endswith(preferred_codec):
                input_file = os.path.join(dirname, fname)
                output_dir = os.path.join(output_folder, preferred_codec)
                if not os.path.isdir(output_dir):
                    os.system('mkdir -p %s' %output_dir)

                output_file = os.path.join(output_dir, '%s.%s' %(input_file.split('/')[-3], preferred_codec))
                print 'Copying %s to %s' %(input_file, output_file)
                shutil.copy(input_file, output_file)

if 'Y' in a.upper():
    os.path.walk('.', walk_cb, None)

print colored('All done', 'green')
