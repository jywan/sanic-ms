# -*- coding: utf-8 -*-

import os
import consul
import consul.aio

DEFAULT_CONFIG = {
    ''
}

DB_CONFIG = {

}


class Config:

    def __init__(self, loop, host='127.0.0.1', port=8500):
        self.consul = consul.aio.Consul(host=host)
