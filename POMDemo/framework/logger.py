# -*- cdding: utf-8 -*-
import logging
import os.path
import time

class Logger(object):

    def __init__(self,logger):

        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定文件中
        :param driver:
        :return:
        """

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handle，用于写日志文件
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_path = os.path.dirname(os.path.abspath('.')) + '/logs'  # 项目根目录下/Logs 保存日志
        # 如果case组织结构是/testsuit/featuremodel/xxx.py ,那么得到的相对路径的父路径就是项目的根目录
        log_name = log_path + rq + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handle，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handle的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s -%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handle
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger



