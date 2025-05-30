#!/usr/bin/env python3
# -*-coding:UTF-8 -*

import os
import sys

sys.path.append(os.environ['AIL_HOME'])
##################################
# Import Project packages
##################################
from update.bin.ail_updater import AIL_Updater
from lib.ConfigLoader import ConfigLoader

config_loader = ConfigLoader()
r_lang = config_loader.get_db_conn("Kvrocks_Languages")
config_loader = None

class Updater(AIL_Updater):
    """default Updater."""

    def __init__(self, version):
        super(Updater, self).__init__(version)


if __name__ == '__main__':
    updater = Updater('v6.2')
    r_lang.flushdb()
    updater.run_update()
