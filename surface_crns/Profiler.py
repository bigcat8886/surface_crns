
from __future__ import print_function
try:
    import surface_crns
except ImportError:
    import sys
    sys.path.append("./")
import surface_crns.readers as readers

import os

from surface_crns.options.option_processor import SurfaceCRNOptionParser
from surface_crns.views.time_display import TimeDisplay
from surface_crns.views.text_display import TextDisplay
from surface_crns.views.grid_display import SquareGridDisplay, HexGridDisplay
from surface_crns.views.legend_display import LegendDisplay
from surface_crns.simulators.queue_simulator import QueueSimulator
from surface_crns.simulators.synchronous_simulator import SynchronousSimulator
from surface_crns.simulators.event_history import EventHistory
from surface_crns.pygbutton import PygButton

import cProfile
import optparse
import sys
from time import process_time

import pygame
import pygame.locals as pygl

if 