#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2011, Florent Thiery

import os

enable_backup = True

backup_dir = 'jam_backup'
move_cmd_pattern = 'cp %s %s'
backup_cmd_pattern = 'mv %%s %s/' %backup_dir
delete_cmd_pattern = 'rm -rf %s'

loop_nb = 1
dirs = os.listdir('.')
dirs.sort()
loop_dirs = list()
print 'Copying files'
for directory in dirs:
    if directory.startswith('LOOP'):
        loop_dirs.append(directory)
        wave_path = os.path.join(directory, 'LOOP.WAV')
        if os.path.isfile(wave_path):
            new_wave_path = '%s.WAV' %loop_nb
            print "%s -> %s" %(wave_path, new_wave_path)
            os.system(move_cmd_pattern %(wave_path, new_wave_path))
            loop_nb += 1

if enable_backup:
    if not os.path.isdir(backup_dir):
        print 'Creating backup dir', backup_dir
        os.mkdir(backup_dir)
        for loop_dir in loop_dirs:
            os.system(backup_cmd_pattern %loop_dir)
        print 'Backup complete'

else:
    print 'Will remove dirs: %s' %loop_dirs
    for loop_dir in loop_dirs:
        os.system(remove_cmd_pattern %loop_dir)
