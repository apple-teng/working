# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"

from airtest.core.api import *
# 双指操作需要导入Android minitouch
from airtest.core.android.minitouch import *
from airtest.core.android.rotation import XYTransformer
from poco import exceptions
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)
auto_setup(__file__)

"""
以下函数与 区域页面 / 自定义页面相关
"""
def check_click_area_popMsg():
    """
        function:
            首次进入主界面的“区域”，点击弹出的消息
        args：
            none
        return:
    """
    if poco(name='com.eco.global.app:id/tv1').exists():
        if poco(name='com.eco.global.app:id/tv1').get_text() == "选择清扫次数":
            poco(text="知道了").click()
        else:
            snapshot(msg="首次进入区域的popmsg内容显示不对")
            raise AssertionError("首次进入区域的popmsg内容显示不对")


def check_click_custom_popMsg():
    """
        function:
            首次进入主界面的“区域”，点击弹出的消息
        args：
            none
        return:
    """
    if poco(name='com.eco.global.app:id/tv1').exists():
        if poco(name='com.eco.global.app:id/tv1').get_text() == "框选清扫范围":
            poco(text="知道了").click()
        else:
            snapshot(msg="首次进入自定义的popmsg内容显示不对")
            raise AssertionError("首次进入自定义的popmsg内容显示不对")

 
def check_custom_clean_display():
    """
        function:
            检查自定义页面的特征显示，包括自定义框 和 次数
        args：
            none
        return:
            none
    """
    if exists(Template(r"tpl1594800365603.png", rgb=True, record_pos=(-0.4, 0.292), resolution=(1080, 2340))) and exists(Template(r"tpl1594800380100.png", record_pos=(-0.408, 0.456), resolution=(1080, 2340))):
        logger.debug("自定义框存在")
        log("自定义框存在")
    elif poco('com.eco.global.app:id/custom_area_image').exists() and poco('com.eco.global.app:id/times').exists():
        logger.debug("自定义框存在[2]")
        log("自定义框存在[2]")
    else:
        snapshot("自定义页面的显示缺少标志性元素，截图检查")
        raise AssertionError("自定义页面的显示缺少标志性元素")


def check_custom_clean_area_tips(expection='存在'):
    """
        function:
            检查自定义页面的清扫框是否被选中
        args：
            expection：是否被选中
            - '存在': 被选中（缺省）
            - '不存在': 没被选中
        return:
            none
    """
    if expection == '存在':
        if exists(Template(r"tpl1594800820296.png", rgb=True, record_pos=(-0.405, 0.294), resolution=(1080, 2340))):
            logger.debug("自定义页面的清扫框被选中")
            log("自定义页面的清扫框被选中")
            if poco(text='请框选清扫区域').exists():
                logger.debug("自定义页面的清扫框被选中,且有文字提示")
                log("自定义页面的清扫框被选中,且有文字提示")
            else:
                snapshot(msg="自定义页面的清扫框被选中,但没有文字提示，截图检查")
                raise AssertionError("自定义页面的清扫框被选中,但没有文字提示")
        else:
            snapshot(msg="自定义页面的清扫框没被选中截图检查")
            raise AssertionError("自定义页面的清扫框没被选中")
    elif expection == '不存在':
        if exists(Template(r"tpl1594801186483.png", rgb=True, record_pos=(-0.403, 0.295), resolution=(1080, 2340))):
            logger.debug("自定义页面的清扫框没被选中")
            log("自定义页面的清扫框没被选中")
            if not poco(text='请框选清扫区域').exists():
                logger.debug("自定义页面的清扫框没被选中,且没有文字提示")
                log("自定义页面的清扫框没被选中,且没有文字提示")
            else:
                snapshot(msg="自定义页面的清扫框被选中,但有文字提示，截图检查")
                raise AssertionError("自定义页面的清扫框被选中,但有文字提示")
        else:
            snapshot(msg="自定义页面的清扫框被选中，截图检查")
            raise AssertionError("自定义页面的清扫框被选中")
    else:
        raise AssertionError("expection参数不对，请检查")
        
            
        

# if __name__ == "__main__":  
if __name__ == "airtest.cli.runner": 
    check_custom_clean_area_tips(expection='不存在')
#     check_custom_popMsg()
#     check_area_popMsg()