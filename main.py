# -*- coding: utf-8 -*-
# @Author  : xinjie
import base64
from common_func import *
from selenium import webdriver

import scrapys
import ToWord2
from excel_ops import ExcelUtil
from utils.logger import Logger

# create a logger instance
logger = Logger(logger='BasePage').getlog()


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()

    ## 从excel中读取需要巡检的系统信息
    logger.info("开始读取需要巡检的系统!!!")

    filepath = "AIP.xlsx"
    sheetName = "pwd"    
    data = ExcelUtil(filepath, sheetName)
    obs_list = data.dict_data()

    for system in obs_list:
        logger.info("开始{}巡检!!!".format(system["system_name"]))

        ## 判断该系统是否需要登录
        if len(system["login_url"]) != 0:
            #密码解密
            raw_string = base64.b64decode(system["pwd"])  # 解码 返回字节数组.
            pwd_decode =raw_string.decode()
            ## 登录
            logger.info("{}系统开始登录中，请稍后!!!".format(system["system_name"]))
            driver.get(system["login_url"])
            time.sleep(2)
            common_login(driver,username=system["user"],pwd=pwd_decode,username_label=system["username_label"],pwd_label=system["pwd_label"],login_btn_label=system["login_btn_label"])
            time.sleep(2)


        logger.info("{}系统巡检指标获取中!!!".format(system["system_name"]))
        # 获取巡检对象
        filepath = "AIP.xlsx"
        sheetName = system["system_name"] 
        data = ExcelUtil(filepath, sheetName)
        obs_list = data.dict_data()
        logger.info("{}系统巡检指标获取成功,开始抓取!!!".format(system["system_name"]))
        scrapys.xunjian(driver,obs_list)


    ## 判断是否需要输出Word报告
    filepath = "AIP.xlsx"
    sheetName = "pic_reporter_prefix"    
    data = ExcelUtil(filepath, sheetName)
    is_toword = data.get_main_title()
    if is_toword !="NO":
        logger.info("巡检即将完成，正在将分析报告保存为doc报告！！")
        ToWord2.toword()
    logger.info("该项目无需输出Word报告，已完成巡检,正在退出浏览器")
    driver.quit()
    



    