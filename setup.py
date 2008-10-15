# -*- coding: utf-8 -*-

from distutils.core import setup
import sys, os

if __name__ == "__main__":
    setup(scripts    = ["bin/savemysqldb"],
          data_files =[('/etc', ['conf/savemysqldb.conf']),
                       ('/etc/cron.d', ['conf/savemysqldb.cron'])],
         )
