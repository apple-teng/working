# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"

from airtest.core.api import *
from poco import exceptions
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
using("UniversalModule.air")
import UniversalModule
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
auto_setup(__file__)

"""
以下函数皆与 工作日志 有关
"""

def cleaning_log_to_more():
    """
        function:
           从清扫日志退到更多
        args：
            none
        return:
            none
    """
    try:
        if poco(text='工作日志', name='com.eco.global.app:id/titleContent').exists():
            sleep(2)
            poco(name='com.eco.global.app:id/title_back').click()
            sleep(2)
    except:
        raise AssertionError("返回更多页面出错...")
        

        

def check_cleaning_log_display():
    """
        function:
           检查工作日志界面的显示，通过检查是否存在工作日志/累计面积/工作次数
        args：
            none
        return:
            none
    """
    try:
        poco(text='工作日志', name='com.eco.global.app:id/titleContent').wait_for_appearance()
        logger.debug("在工作日志界面")
        log("在工作日志界面")
    except:
        snapshot(msg="不在工作日志界面")
        raise AssertionError("不在工作日志界面")
    if poco(text='累计面积').exists():
        logger.debug("累计面积")
        log("累计面积")
    else:
        snapshot(msg="工作日志界面没显示累计面积")
        raise AssertionError("工作日志界面没显示累计面积")
    if poco(text='工作次数').exists():
        logger.debug("工作次数")
        log("工作次数")
    else:
        snapshot(msg="工作日志界面没显示工作次数")
        raise AssertionError("工作日志界面没显示工作次数")
    if poco(text='累计时长').exists():
        logger.debug("累计时长")
        log("累计时长")
    else:
        snapshot(msg="工作日志界面没显示累计时长")
        raise AssertionError("工作日志界面没显示累计时长")

        
def click_the_newest_cleaning_log():
    """
        function:
            点击工作日志界面的日日志列表的排在第一的工作日志，进入日志详情
        args：
            none
        return:
            none
    """
    
    try:
        poco(text='工作日志', name='com.eco.global.app:id/titleContent').wait_for_appearance()
        logger.debug("在工作日志界面")
        log("在工作日志界面")
    except:
        snapshot(msg="不在工作日志界面")
        raise AssertionError("不在工作日志界面")
    poco(name='com.eco.global.app:id/tv_log_info').click()
    try:
        poco(name='com.eco.global.app:id/btn_share').exists()
    except:
        snapshot(msg="没有进入日志详情")
        raise AssertionError("没有进入日志详情")
        
        
def click_cleaning_log_share_button():
    """
        function:
            点击日志详情页中的分享按钮
        args：
            none
        return:
            none
    """
    if exists(Template(r"tpl1594111989759.png", record_pos=(0.312, -0.737), resolution=(1080, 2340))):
        touch(Template(r"tpl1594111989759.png", record_pos=(0.312, -0.737), resolution=(1080, 2340)))

    elif poco(name='com.eco.global.app:id/btn_share').exists():        
        poco(name='com.eco.global.app:id/btn_share').click()
        logger.debug("击日志详情页中的分享按钮")
        log("击日志详情页中的分享按钮")
    else:
        snapshot(msg="没有进入日志详情")
        raise AssertionError("没有进入日志详情")
        
        
def check_share_cleaning_log_display():        
    """
        function:
            检查点击日志详情页中的分享按钮后，弹出的页面
        args：
            none
        return:
            none
    """    
        ## 首次分享，会弹出权限申请
    if poco(text='ECOVACS HOME 需要获得以下权限才能为你提供服务').exists():
        poco(text='去设置').click()
    if poco(text='是否允许“ECOVACS HOME”访问您设备上的照片、媒体内容和文件？'):
        poco(text='始终允许').click()
    sleep(3)
    try:
        poco(text='微信朋友圈').exists()
        logger.debug("app弹出朋友圈")
        poco(name='com.eco.global.app:id/wechat').exists()
        logger.debug("app弹出微信好友")
        poco(name='com.eco.global.app:id/qzone').exists()
        logger.debug("app弹出QQ空间")
        poco(name='com.eco.global.app:id/sina').exists()
        logger.debug("app弹出新浪微博")
        poco(name='com.eco.global.app:id/cancle').exists()
        logger.debug("app弹出取消")
        logger.debug("app弹出朋友圈，微信好友，QQ空间，新浪微博这四个分享和取消按钮")
        log("app弹出朋友圈，微信好友，QQ空间，新浪微博这四个分享和取消按钮")
    except:
        snapshot(msg="app弹出朋友圈，微信好友，QQ空间，新浪微博这四个分享和取消按钮中，有缺失")
        raise AssertionError("app弹出朋友圈，微信好友，QQ空间，新浪微博这四个分享和取消按钮中，有缺失")
        
        
def click_to_cancel_share_cleaning_log():
    """
        function:
           点击取消分享
        args：
            none
        return:
            none
    """  
    poco(text='取消').click()
    # 弹框消失，显示单条日志
    if not poco(name='com.eco.global.app:id/wechat').exists():
        logger.debug("11111111111111111111")
    else:
        snapshot(msg="消失弹框功能有误")
        raise AssertionError("消失弹框功能有误")
    if not poco(text='取消').exists():
        logger.debug("4444444444444444")
    else:
        snapshot(msg="消失弹框功能有误")
        raise AssertionError("消失弹框功能有误")
    try:
        poco(name='com.eco.global.app:id/tv_item_cleantype ').exists()
        logger.debug("2222222222222222222222")
        poco(name='com.eco.global.app:id/tv_reason_msg').exists()
        logger.debug("3333333333333333333333333")        
        logger.debug("弹框消失，显示单条日志")
        log("弹框消失，显示单条日志")
    except:
        snapshot(msg="消失弹框功能有误")
        raise AssertionError("消失弹框功能有误")
           
# if __name__ == 'main':        
if __name__ == 'airtest.cli.runner': 
    click_to_cancel_share_cleaning_log()
#     check_share_cleaning_log_display()
        
        
        