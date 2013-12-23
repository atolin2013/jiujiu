# -*- coding:gbk -*-
###############################################################################
#
# Project:  rabbit-gis software
# Purpose:  网络地图下载
# Author:   wenyulin.lin@gmail.com
#
###############################################################################
# Copyright (c) 2013, (www.atolin.net)
# 
# Beijing, China.
###############################################################################


import os, sys
from cx_Freeze import setup, Executable
import version

buildPath=os.path.join(os.path.dirname(__file__), 'build')
for root, dirs, files in os.walk(buildPath):
    for name in files:
        os.remove(os.path.join(root, name))

base = None
if sys.platform == "win32":
    base = "Win32GUI"

buildOpts = dict(
        compressed=True,
        includes=['numpy'],
        excludes=['Tkinter'],
        #zip_includes=['smSci/sci3d.sci3d'],
        include_files=['logo.png','icon.ico','g.tsk','config.cfg','gui.cfg','使用说明.doc'],
        )

exeTables = [Executable("gui.py", targetName='t2f.exe', icon='icon.ico',base=base),]
setup(
        name = "TileServer",
        version = version.__version__[:version.__version__.rfind('.')],
        description = "Download Google tile files.",
        author = 'wenyulin.lin@gmail.com',
        author_email = 'wenyulin.lin@gmail.com',
        maintainer = 'linwenyu',
        url = 'www.atolin.net',
        options = dict(build_exe=buildOpts,),
        executables = exeTables)

