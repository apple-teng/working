# -*- encoding=utf8 -*-
__author__ = "lei.z"

from airtest.core.api import *
import time
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
<<<<<<< HEAD
=======
'''更多界面吸力强度显示'''
def more_suction():
    current_suction = poco("android:id/content").offspring("com.eco.global.app:id/more_items").child("android.widget.LinearLayout")[1].child("com.eco.global.app:id/msg").get_text()
    return current_suction
>>>>>>> dd196aee2fce228a2934b23f7e00c9ea2d2e531d

'''更多页面风力调节'''
# 页面跳转
def more_to_suction():
    swipe((500,300), vector=[0.0, 0.5])
<<<<<<< HEAD
    poco("android:id/content").offspring("com.eco.global.app:id/more_items").child("android.widget.RelativeLayout")[0].click()
    sleep(1)
    suction_level = ("android:id/content").offspring("com.eco.global.app:id/titleContent").get_text().strip()
=======
    poco("android:id/content").offspring("com.eco.global.app:id/more_items").child("android.widget.LinearLayout")[1].click()
    sleep(1)
    suction_level = poco("android:id/content").offspring("com.eco.global.app:id/titleContent").get_text().strip
>>>>>>> dd196aee2fce228a2934b23f7e00c9ea2d2e531d
    return suction_level

# 获取当前所有风力档位
def get_all_suction_level():
    arr = []
    elements = poco("com.eco.global.app:id/tv_left")
    for element in elements:
        arr.append(element .get_text())
    return arr
<<<<<<< HEAD
def get_suction_level():
    '''获取当前风力设定'''
    suction_level = poco("android:id/content").offspring("com.eco.global.app:id/more_items").child("android.widget.RelativeLayout")[0].offspring("com.eco.global.app:id/msg").get_text()
    poco("android:id/content").offspring("com.eco.global.app:id/more_items").child("android.widget.RelativeLayout")[0].child("com.eco.global.app:id/title").click()
    sleep(2)
    filename = r'D:\airtest_result/' +  time.strftime("%m%d-%H%M%S") + 'suction.png'
    snapshot(filename)
    return suction_level

def set_suction_level(suction_level='强劲'):
    '''设定风力档位'''
    arr = MoreSuction.get_all_suction_level()
=======

def get_suction_level():    
    '''获取当前风力设定'''
    suction_level =  poco("com.eco.global.app:id/tv_left").get_text()
    sleep(2)
    filename = r'D:\airtest_result/' +  time.strftime("%m%d-%H%M%S") + 'suction.png'
    snapshot(filename)
    return print(suction_level)
get_suction_level()

def set_suction_level(suction_level='强劲'):
    '''设定风力档位'''
    arr = get_all_suction_level()
>>>>>>> dd196aee2fce228a2934b23f7e00c9ea2d2e531d
    if(suction_level not in arr):
        print("没有此风力档位")
    else:
        poco(text=suction_level).click()
<<<<<<< HEAD
=======
        poco("com.eco.global.app:id/right").click()
        sleep(5)
>>>>>>> dd196aee2fce228a2934b23f7e00c9ea2d2e531d
        filename = r'D:\airtest_result/' +  time.strftime("%m%d-%H%M%S") + 'suction.png'
        snapshot(filename)
    return "设置成功"

<<<<<<< HEAD

=======
>>>>>>> dd196aee2fce228a2934b23f7e00c9ea2d2e531d
