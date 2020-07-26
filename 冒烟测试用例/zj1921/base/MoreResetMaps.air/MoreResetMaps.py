# -*- encoding=utf8 -*-
__author__ = "lei.z"

from airtest.core.api import *
from poco import exceptions
import sys
# sys.path.append(r'../')
# from import_package import *
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

'''
重置地图
'''

def click_reset_map_button():
    """
        function:
            点击重置当前使用地图按钮
        args：
            none
        return:
            none
    """ 
    try:
        poco(name='com.eco.global.app:id/titleContent', text='更多').exists()
    except Exception as e:
        raise AssertionError("当前页面不在更多",e)
    try:
        poco(name='com.eco.global.app:id/title', text='重置当前使用地图').click()
    except Exception as e:
        raise AssertionError("重置当前使用地图出错",e)
        



# 确认删除地图
def reset_maps_del():
    '''
    确认删除地图
    更多页面，点击重置当前使用地图
    '''
    # 点击重置当前使用地图
    poco(text="重置当前使用地图").click(sleep_interval=2)
    # 点击删除
    if poco("com.eco.global.app:id/tv_neutral").exists():
        # 弹窗中点击删除
        poco("com.eco.global.app:id/tv_neutral").click(sleep_interval=5)
        return "删除"
    # 删除地图后，需要重新扫建,确认删除该地图并清空相关的预约？
    elif poco(text='知道了').exists():
        poco(text='知道了').click()
        # 返回主页面
        poco(name='com.eco.global.app:id/title_back').click()
        sleep(5)
        return "删除"
    else:
        raise AssertionError("点击重置地图后的弹框不对")
    if poco(text="重置当前使用地图").exists():
        raise AssertionError("重置完地图后，app没有回到主页面")

        
# 取消删除地图
def reset_maps_cancel():
    '''
    取消删除地图
    更多页面，点击重置当前使用地图
    '''
    # 点击重置当前使用地图
    poco(text="重置当前使用地图").click(sleep_interval=2)
    # 弹窗中点击取消
    poco("com.eco.global.app:id/tv_cancel").click(sleep_interval=2)
    return "取消"


def check_reset_map_popMsg():
    """
        function:
            获取点击重置当前使用地图后app的弹框内容
        args：
            none
        return:
            none
    """ 
    popMsg1 = '删除地图后，需要重新扫建'+'\n'+'确认删除该地图并清空相关的预约？'     
    popMsg2 = '删除的是当前正在使用的地图' + '\n' + '确认删除该地图并清空相关的预约？'
    if poco("com.eco.global.app:id/tv_content").get_text() == popMsg1:
        logger.debug("重置当前使用地图后app的弹框内容正确[1]")
        log("重置当前使用地图后app的弹框内容正确[1]")
    elif poco("com.eco.global.app:id/tv_content").get_text() == popMsg2:
        logger.debug("重置当前使用地图后app的弹框内容正确[]")
        log("重置当前使用地图后app的弹框内容正确[2]")
    else:
        logger.debug(poco("com.eco.global.app:id/tv_content").get_text())
        raise AssertionError("重置当前使用地图后app的弹框内容不正确")


if __name__ == 'airtest.cli.runner': 
    check_reset_map_popMsg()
#     reset_maps_del()
        

