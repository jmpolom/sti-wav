#!/usr/bin/python

"""
Speech Transmission Index (STI) test script

Copyright (C) 2011 Jon Polom <jmpolom@wayne.edu>
Licensed under the GNU General Public License
"""

from datetime import date
from sti import stiFromAudio, readwav

__author__ = "Jonathan Polom <jmpolom@wayne.edu>"
__date__ = date(2011, 04, 22)
__version__ = "0.5"

# read audio
refAudio, refRate = readwav('speech/eval1.wav')
degrAudio, degrRate = readwav('speech/eval1_echo100.wav')

# calculate the STI. Visually verify console output.
stiFromAudio(refAudio, degrAudio, rate, name='eval1.wav')
