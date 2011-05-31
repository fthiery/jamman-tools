#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2011, Florent Thiery

from termcolor import colored
import os

def get_files(directory='.'):
    if os.path.isdir(directory):
        return os.listdir(directory)
    return None

def dir_is_project(directory='.', quit=False):
    if os.path.isdir(directory):
        files = get_files()
        if '1.wav' in files:
            return True
    if quit:
        print colored('Current directory not a jamman project, exiting', 'red')
        import sys
        sys.exit()
    return False

def get_samples():
    samples = list()
    files = get_files()
    files.sort()
    for fname in files:
        if os.path.isfile(fname):
            name, ext = os.path.splitext(fname) 
            if ext == '.wav':
                try:
                    name_to_int = int(name)
                    is_sample = True
                except Exception, e:
                    is_sample = True
                if is_sample:
                    samples.append(fname)
    return samples

def read_file(filename):
    fname = open(filename)
    data = fname.read()
    fname.close()
    return data

def get_project_name(path='.'):
    name = os.path.abspath(path).split('/')[-1]
    return name
