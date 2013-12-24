#!/usr/bin/env python
# --*-- coding:gbk --*--
###############################################################################
#
# Project:  rabbit-gis software
# Purpose:  �����ͼ����
# Author:   wenyulin.lin@gmail.com
#
###############################################################################
# Copyright (c) 2013, (www.atolin.net)
# 
# Beijing, China.
###############################################################################


import os
import sys
import ConfigParser
import logging

logger = logging.getLogger("")

def from_file(_path, _section):
    if not os.path.isfile(_path):
        return None
    _items = {}
    cfg = ConfigParser.ConfigParser()
    try:
	cfg.read(_path)
    except ConfigParser.Error:
	logger.error(ConfigParser.Error.message)
	return None
    if cfg.has_section(_section):
        for k,v in cfg.items(_section):
            _items[k] = v
    return _items

def to_file(_path, _section, _items):
    config = ConfigParser.ConfigParser()
    config.add_section(_section.lower())
    for k,v in _items.items():
        config.set(_section.lower(), k, v)

    with open(_path, 'wb') as configfile:
        config.write(configfile)

if __name__=="__main__":
    print 'unsupport main function.'


