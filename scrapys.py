# -*- coding: utf-8 -*-
# @Author  : xinjie

import json
import datetime
import time
from tkinter import N
from xml.sax.handler import property_lexical_handler
from selenium.webdriver.common.by import By
import re

from common_func import get_tomorrow_date,screenshot_byxpath,screenshot_bycss,common_login

from excel_ops import ExcelUtil
from utils.logger import Logger

# create a logger instance
logger = Logger(logger='BasePage').getlog()


# 定义停顿间隔时间
interval_time =5

def xunjian(driver,obs_list):
    for item in obs_list:
        print("正在巡检>>>>>"+ item["target_name"]+"\n url>>>>:"+item["url"])
        driver.get(item["url"])
        # driver.implicitly_wait(interval_time)
        interval_time = int(item["speed_time"])
        time.sleep(interval_time)
        if item["action"] == "screenshot":
            driver.find_element(By.XPATH,item["x_path"]).screenshot("pic\\" + item["target_name"]  + datetime.datetime.now().strftime("%Y%m%d%H%M")+ ".png")
            print("已截图保存到pic目录\n")
        elif item["action"] == "identification":
            current_vlaue = driver.find_element(By.XPATH,item["x_path"]).text
            with open("reporter_{}.txt".format(datetime.datetime.now().strftime("%Y%m%d")),"a",encoding="utf-8") as f:
                f.write(datetime.datetime.now().strftime("%m%d%H%M") +"  >>>>  "+ item["target_name"]+"指标当前为"+ current_vlaue +"\n")
            print(item["target_name"]+"指标当前为"+ current_vlaue +"\n")

            ## 判断该指标是否需要对比阈值
            if item["SLO"] != "" :
                current_vlaue = get_number(current_vlaue)
                if float(current_vlaue) > float(item["SLO"]):
                    errmsg ='alert("该指标异常,请检查")'
                    driver.execute_script(errmsg)
                    time.sleep(10)
        elif item["action"] == "general":
            pass
        elif item["action"] == "scroll_view":
            pass
        else:
            print("请检查配置文件里面action参数")
        time.sleep(1)


def kenfen_reporter(driver,obs_list):

    tomorrow_date = get_tomorrow_date()
    for item in obs_list:
        item["url"] = item["url"] + "&checktime={0}+00%3A00".format(tomorrow_date)
        print("正在巡检>>>>>"+item["target_name"]+"\n url>>>>:"+item["url"])
        driver.get(item["url"])
        # driver.implicitly_wait(interval_time)
        target = driver.find_element_by_xpath("//*[@id='ta']/tbody/tr[last()]/td[3]")
        driver.execute_script("arguments[0].scrollIntoView();",target)
        time.sleep(2)
        driver.execute_script("""
                (function () {
                    var y = 1006;
                    var step = 100;
                    window.scroll(0, 0);
                    function f() {
                        if (y = document.body.scrollHeight) {
                            y -= step;
                            window.scroll(0, y);
                            setTimeout(f, 100);
                        } 
                    }
                    setTimeout(f, 1000);
                })();
            """)
        time.sleep(2)
        if item["action"] == "screenshot":
            driver.find_element(By.XPATH,item["x_path"]).screenshot("pic\\" + item["target_name"]  + datetime.datetime.now().strftime("%Y%m%d%H%M")+ ".png")
            print("已截图保存到pic目录\n")
        elif item["action"] == "identification":
            current_vlaue = driver.find_element(By.XPATH,item["x_path"]).text
            with open("reporter_{}.txt".format(datetime.datetime.now().strftime("%Y%m%d")),"a",encoding="utf-8") as f:
                f.write(datetime.datetime.now().strftime("%m%d%H%M") +"  >>>>  "+ item["target_name"]+"指标当前为"+ current_vlaue +"\n")
            print(item["target_name"]+"指标当前为"+ current_vlaue +"\n")
        else:
            print("请检查配置文件里面action参数")
        time.sleep(1)


def get_number(text):
    number = re.findall(r"\d+\.?\d*",text)[0]
    return number


if __name__ == '__main__':
    pass

