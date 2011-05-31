#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2010, Florent Thiery, UbiCast

import os

python_lib_path = '/usr/lib/python2.7/dist-packages/'

bindirname = 'bin'
srcdirname = 'jamman'

abspath = os.path.abspath(bindirname)
files = os.listdir(bindirname)
for fname in files:
    os.system('chmod +x %s' %os.path.join(bindirname, fname))
    #print 'sudo ln -sf %s %s' %(os.path.join(abspath, fname), '/usr/local/bin/%s' %os.path.splitext(fname)[0])
    os.system('sudo ln -sf %s %s' %(os.path.join(abspath, fname), '/usr/local/bin/%s' %os.path.splitext(fname)[0]))
#print 'sudo ln -s %s %s' %(os.path.join(abspath, fname), '/usr/lib/python2.6/dist-packages/jamman')
os.system('sudo ln -sf %s %s' %(os.path.join(os.path.abspath(srcdirname)), os.path.join(python_lib_path, srcdirname)))
