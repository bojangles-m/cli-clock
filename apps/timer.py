#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.join(sys.path[0], '../'))

from lib.apps import timer

timer.run(int(sys.argv[1]), sys.argv[2])
