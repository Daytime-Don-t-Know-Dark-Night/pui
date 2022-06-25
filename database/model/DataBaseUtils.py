"""
@desc 数据库连接
@auth dingc
@date 2022/06/24
"""
import yaml
import os
from DataBaseOperation import MysqlOperation
from clickhouse_driver.client import Client
import pandas as pd
import logging


def db_config():
    p_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    path = os.path.join(p_path, "config", "db_config.yaml")
    f = open(path, encoding="utf-8")
    config = yaml.load(f.read(), yaml.FullLoader)
    return config


class MysqlUtils:

    def __init__(self):
        self.config = db_config()

    @property
    def dingchao_db(self):
        conf = self.config["dingchao_db"]
        self._dingchao = MysqlOperation(conf["host"], conf["user"], conf["password"], conf["db"])
        return self._dingchao

