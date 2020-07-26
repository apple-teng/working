# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"

from airtest.core.api import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco import exceptions
import cv2
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)


def check_deebot_icon():
    """
        function:
            检查更多页面寻找地宝的图标
        args：
            none
        return:
            none
    """
    # 检查当前页面在更多
    if poco(text="更多", name="com.eco.global.app:id/titleContent").exists():
        # 检查地宝图标的元素和地宝的图案
        if poco(name="com.eco.global.app:id/locate_deebot").exists() and exists(Template(r"tpl1593767712458.png", record_pos=(0.421, -0.943), resolution=(1080, 2340))):
            deebot_x, deebot_y = poco(name="com.eco.global.app:id/locate_deebot").get_position()
            print(deebot_x, deebot_y)
            # 确认地宝在屏幕右上角
            if 20*deebot_x - deebot_y > 0:
                log("地宝位置显示在右上角")
            else:
                raise Exception("地宝位置图标显示的位置不对")
        else:
            raise Exception("寻找地宝的图标在更多页面不存在")
    else:
        raise Exception("当前页面不是更多")
        

def find_deebot_response_icon():
    """
        function:
            检查点击更多页面寻找地宝图标后的动效
        args：
            none
        return:
            none
    """
    # 检查当前页面在更多
    if poco(text="更多", name="com.eco.global.app:id/titleContent").exists():
        try:
            poco(name="com.eco.global.app:id/locate_deebot").click()
            sleep(1)
        except InvalidOperationException:
            log("点击寻找地宝图标按钮出错")
        # 只截取到了动效的几个关键点    
        if exists(Template(r"tpl1593768085284.png", record_pos=(0.012, -0.027), resolution=(1080, 2340))):
            sleep(1)
            
            if exists(Template(r"tpl1593768085284.png", record_pos=(0.012, -0.027), resolution=(1080, 2340))):
                log("寻找地宝有动效")
        else:
            raise Exception("寻找地宝没有动效")
    else:
        raise Exception("当前页面不是更多")


# if __name__ == "airtest.cli.runner":
if __name__ == "__main__":     
    check_deebot_icon()    
    find_deebot_response_icon()









