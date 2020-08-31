#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import simple_platformer.config

# Create folders
for folder in [simple_platformer.config.DATA_FOLDER, simple_platformer.config.DEMO_FOLDER]:
    try:
        os.mkdir(folder)
    except OSError:
        print ("Creation of the directory %s failed" % folder)
    else:
        print ("Created %s folder" % folder)

# Installer for python dependecies?
# TODO