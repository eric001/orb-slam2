#!/usr/bin/env python
# coding=utf-8
import subprocess
p = subprocess.Popen("./build/mono_tum ./Vocabulary/ORBvoc.txt ./Examples/Monocular/TUM1.yaml ./tum_data/rgbd_dataset_freiburg1_xyz/",shell = True )
p.wait()

