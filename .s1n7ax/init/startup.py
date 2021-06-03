#!/bin/python

import os
import sys

home = os.environ['HOME']
user = os.environ['USER']

sys.path.append(os.path.abspath("{}/.s1n7ax/commons".format(home)))

# execute needs to be imported after adding the module to path
from execute import execute

execute([['xsetroot', '-name', ' {} '.format(user)]], False)

# execute([['st']], False)
# execute([['st']], False)
# execute([['firefox']], False)
# execute([['chromium']], False)

execute([['imwheel', '-b', '45']], False)
execute([['setxkbmap', '-option', 'ctrl:nocaps']], False)
# execute([['picom']], False)
# execute([['xcompmgr']], False)
# execute([['wal', '-R']], False)
