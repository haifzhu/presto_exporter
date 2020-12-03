## Presto Exporter

### 配置

设置配置文件settings.py
~~~
#coding:utf-8
#!/usr/bin/env python
import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEFAULT_APP_RULE = "development"

class Config:
    BINDPORT = 8000

class Dev(Config):
    DEBUG = True
    PRESTO_URL = "" // 设置为真实presto url

config = {
    'development': Dev,
    'default': Dev
}


conf = config[DEFAULT_APP_RULE]
~~~

### 启动

~~~
python install -r requirements.txt
python app.py
~~~

### 访问

可以通过url: http://[host]:8000访问到监控metrics。


