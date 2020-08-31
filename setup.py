#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import simple_platformer.config

# Create data folder
data_folder = simple_platformer.config.DATA_FOLDER
try:
    os.mkdir(data_folder)
except OSError:
    print ("Creation of the directory %s failed" % data_folder)
else:
    print ("Successfully created the directory %s " % data_folder)

# Installer for python dependecies?
# TODO