"""
@desc 数据库连接
@auth dingc
@date 2022/06/24
"""
import yaml
import os
import pandas as pd
from clickhouse_driver.client import Client
import logging


def db_config():
    p_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    path = os.path.join(p_path, "config", "db_config.yaml")
    f = open(path, "utf-8")
    config = yaml.load(f.read(), yaml.FullLoader)
    return config


class MysqlUtils:

    def __init__(self):
        self.config = db_config()

    @property
    def order(self):
        conf = self.config["order"]
        print("Aaa")
        return None


