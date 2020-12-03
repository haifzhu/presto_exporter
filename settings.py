#coding:utf-8
#!/usr/bin/env python
import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEFAULT_APP_RULE = "development"

class Config:
    BINDPORT = 8000

class Dev(Config):
    DEBUG = True
    PRESTO_URL = "http://presto.bigdata.cai-inc.com"

config = {
    'development': Dev,
    'default': Dev
}


conf = config[DEFAULT_APP_RULE]
