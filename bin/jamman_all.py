#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2011, Florent Thiery

import os
from termcolor import colored
from jamman.utils import dir_is_project

processed = list()

def render_project(path='.'):
    if path != '.':
        print 'Entering', path
        os.chdir(path)

    if dir_is_project('.'):
        processed.append(path)
        print colored('Re-rendering project %s' %path, 'green')

        raw = False
        for filename in os.listdir('.'):
            if filename.startswith('LOOP'):
                raw = True
        if raw:
            print colored('Extracting files', 'green')
            os.system('jamman_extract.py')

        if not raw and os.path.isfile('preview.wav'):
            print colored('Cleaning project', 'green')
            os.system('jamman_clean.py')

        print colored('Rendering project', 'green')
        os.system('jamman_render.py')
        print colored('Compressing project', 'green')
        os.system('jamman_compress.py')

    else:
        print 'Dir is not a project'
    if path != '.':
        print 'Walking back'
        os.chdir('..')


def walk_cb(arg, dirname, fnames):
    #print 'Walk: directory %s, filenames: %s' %(dirname, fnames)
    for fname in fnames:
        if os.path.isdir(fname):
            render_project(os.path.join(dirname, fname))

if not dir_is_project('.'):
    os.path.walk('.', walk_cb, None)
else:
    render_project('.')

processed.sort()
print colored('Processed:', 'green')
for name in processed:
    print '\t', name
