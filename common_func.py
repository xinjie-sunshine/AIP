import time
import datetime
import os

def dir_exist(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        print(dirname + "目录创建成功！")




def screenshot_bycss(browser,element_label,file_prefix):
    """
    截图并保存，通过css的方式定位
    # element_label 元素定位标签（#panel-50）
    # file_prefix 文件保存的前缀用于 保存图片用
    """
    browser.find_element_by_css_selector(element_label).screenshot("pic\\" + file_prefix + datetime.datetime.now().strftime("%Y%m%d%H%M") + ".png")

def screenshot_byxpath(browser,element_label,file_prefix):
    """
    截图并保存，通过css的方式定位
    # element_label 元素定位标签（#panel-50）
    # file_prefix 文件保存的前缀用于 保存图片用
    """
    browser.find_element_by_xpath(element_label).screenshot("pic\\" + file_prefix + datetime.datetime.now().strftime("%Y%m%d%H%M")+ ".png")



def get_tomorrow_date():
    tomorrow = datetime.datetime.now()+datetime.timedelta(days=1)
    tomorrow_date = tomorrow.date()
    return  tomorrow_date

def scrolling(browser,up_down="bottom"):
    
    """
    滚动屏幕
    # up_down top/bottom 滚动到顶部/底部
    """
    js_top = "var q=document.documentElement.scrollTop=0"
    js_bottom = "window.scrollTo(0,document.body.scrollHeight)"
    if up_down == "top":
        browser.execute_script(js_top) 
    elif up_down == "bottom":
        browser.execute_script(js_bottom)

def scrolling100(browser):
   # scrolling(browser,up_down="bottom")
    target = browser.find_element_by_xpath("//*[@id='ta']/tbody/tr[last()]/td[3]")
    browser.execute_script("arguments[0].scrollIntoView();",target)
    time.sleep(3)
    browser.execute_script("""
        (function () {
            var y = 1006;
            var step = 100;
            window.scroll(0, 0);
            function f() {
                if (y = document.body.scrollHeight) {
                    y -= step;
                    window.scroll(0, 0);
                    setTimeout(f, 100);
                } 
            }
            setTimeout(f, 1000);
        })();
    """)
    time.sleep(2)
    screenshot_byxpath(browser,element_label="//*[@id='ta']",file_prefix="jiaoyi_")


def common_login(browser,username,pwd,username_label,pwd_label,login_btn_label):
    """
    通用登录方法，采用xpath选择器
    # username： 用户名
    # pwd 密码
    # username_label 用户名所在的xpath路径
    # pwd_label 密码框所在的xpath路径
    # login_btn_label 登录按钮所在的xpath路径
    """
    ## 输入用户名和密码
    browser.find_element_by_xpath(username_label).send_keys(username)
    browser.find_element_by_xpath(pwd_label).send_keys(pwd)

    # 点击按钮提交登录表单
    browser.find_element_by_xpath(login_btn_label).click()
    time.sleep(5)

# #加载项目地址
# def load_url(self,ur1): 
#   self.driver.get(url)
# #元素定位
# def locator(self,loc):
#   ele=self.driver.find_element(*loc)
#   return ele
# #输入
# def input(self,1oc ,value):
#   #元素定位，执行输入
#   self.locator(1oc). send_ keys(value)