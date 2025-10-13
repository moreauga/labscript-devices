#####################################################################
#                                                                   #
# /pulseblasterUSB.py                                               #
#                                                                   #
# Copyright 2013, Monash University                                 #
#                                                                   #
# This file is part of labscript_devices, in the labscript suite    #
# (see http://labscriptsuite.org), and is licensed under the        #
# Simplified BSD License. See the license.txt file in the root of   #
# the project for the full license.                                 #
#                                                                   #
#####################################################################
from labscript_devices import BLACS_tab, runviewer_parser
from labscript_devices.PulseBlaster_No_DDS import (
    PulseBlaster_No_DDS,
    Pulseblaster_No_DDS_Tab,
    PulseblasterNoDDSWorker,
    PulseBlaster_No_DDS_Parser,
)


class PulseBlasterESR_PRO_250(PulseBlaster_No_DDS):
    description = 'SpinCore PulseBlasterESR_PRO_250'        
    clock_limit = 50e6 # previously 8.3e6 THIS MUST BE CHANGED AT EVERY CLASS LEVEL?
    clock_resolution = 4e-9 # previously 4ns
    n_flags = 24
    core_clock_freq = 250.0 # previously 250 MHz


@BLACS_tab
class PulseBlasterESR_PRO_250Tab(Pulseblaster_No_DDS_Tab):
    # Capabilities
    num_DO = 24
    def __init__(self,*args,**kwargs):
        self.device_worker_class = PulseBlasterESR_PRO_250Worker 
        Pulseblaster_No_DDS_Tab.__init__(self,*args,**kwargs)


class PulseBlasterESR_PRO_250Worker(PulseblasterNoDDSWorker):
    core_clock_freq = 250.0 #this is correct; not 100 MHz

@runviewer_parser
class PulseBlasterESR_PRO_250Parser(PulseBlaster_No_DDS_Parser):
    pass


