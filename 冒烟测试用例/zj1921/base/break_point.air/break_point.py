# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"

from airtest.core.api import *

from airtest.core.api import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco import exceptions
import cv2
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

"""
以下函数皆与 断点续扫有关
"""


def more_to_break_point_func():
    """
        function:
            从更多进入断点续扫
        args：
            none
        return:
            none
    """   
    try:
        # 在更多页面
        poco(text='断点续扫').click()
        sleep(2)
    except:
        log("点击断点续扫出错...")
    # 断点续扫页面
    if poco(text='断点续扫', name='com.eco.global.app:id/titleContent').exists():
        log("进入断点续扫...")
    else:
        raise AssertionError("进入断点续扫出错...")
        
        
def break_point_func_to_more():
    """
        function:
            从断点续扫界面进入更多
        args：
            none
        return:
            none
    """
    try:
        if poco(text='断点续扫', name='com.eco.global.app:id/titleContent').exists():
            sleep(2)
            poco(name='com.eco.global.app:id/title_back').click()
            sleep(2)
    except:
        raise AssertionError("返回更多页面出错...") 
        
        
def click_break_point_switch(__action__= None):
    """
        function:
            开启断点续扫,包含开启和关闭
        args：
            __action__：默认为none，还有open和close
            作用是指定对断点续扫开关的操作
        return:
            none
    """
    if poco(text='断点续扫', name='com.eco.global.app:id/titleContent').exists():
        # 不管当前断点续扫状态，直接点击开关
        if not __action__:
            try:
                poco(name="com.eco.global.app:id/toggle_btn").click()
                log("点击断点续扫按键成功")
                sleep(2)
            except InvalidOperationException:
                raise AssertionError("点击断点续扫开关失败")
        # 开启断点续扫
        elif __action__ == "open":
            if exists(Template(r"tpl1587638127802.png", threshold=0.9, rgb=True, record_pos=(0.424, -0.665), resolution=(720, 1280))):
                log("断点续扫状态已经为开启")
            else:
                try:
                    poco(name="com.eco.global.app:id/toggle_btn").click()
                    sleep(2)
                    if exists(Template(r"tpl1587637973431.png", threshold=0.9, rgb=True, record_pos=(0.428, -0.661), resolution=(720, 1280))):
                        raise AssertionError("断点续扫开启失败")
                    else:
                        log("断点续扫状态开启成功")
                except InvalidOperationException:
                    raise AssertionError("断点续扫开启失败")
        # 关闭断点续扫开关
        elif __action__ == "close":
            if exists(Template(r"tpl1587637973431.png", threshold=0.9, rgb=True, record_pos=(0.428, -0.661), resolution=(720, 1280))):
                log("断点续扫状态已经为关闭")
            else:
                try:
                    poco(name="com.eco.global.app:id/toggle_btn").click()
                    sleep(2)
                    if exists(Template(r"tpl1587638127802.png", threshold=0.9, rgb=True, record_pos=(0.424, -0.665), resolution=(720, 1280))):
                        raise AssertionError("断点续扫关闭失败")
                    else:
                        log("断点续扫状态关闭成功")
                except InvalidOperationException:
                    raise AssertionError("断点续扫关闭失败")
        else:
            raise Exception("参数值填写错误")                
    else:
        raise Exception("当前不在断点续扫界面")
    

def get_status_of_break_point_func():
    """
        function:
            检查断点续扫开关的状态
        args：
            none
        return:
            __break_point_status__:断点续扫开关的状态值,返回值为：open,close
    """
    __status_dic__ = {"开启": "open", "关闭": "close"}
    try:
        # 在更多页面
        poco(text='更多', name='com.eco.global.app:id/titleContent').exists()
    except:
        raise AssertionError("当前页面非更多主页面")
    # 断点续扫在更多页面左边第5行，get_position的第二个参数为Y轴
    if poco(name="com.eco.global.app:id/title")[5].get_text() == "断点续扫":
        break_point_pos_y = poco(name="com.eco.global.app:id/title")[5].get_position()[1]
    else:
        raise Exception("断点续扫值在更多页面的位置不对")
    # 断点续扫状态在更多页面左边第5行
    break_point_status_y = poco(name="com.eco.global.app:id/msg")[4].get_position()[1]
    # 断点续扫文字的纵轴 与 断点续扫状态的纵轴 应该为一行
    if break_point_pos_y - break_point_status_y < 0.01:
        # 获取断点续扫的状态
        __break_point_status__ = poco(name="com.eco.global.app:id/msg")[4].get_text()
        # 转化成open、close
        __break_point_status__ = __status_dic__[__break_point_status__]
        return __break_point_status__
    else:
       raise Exception("更多页面的行值没对准")


def check_break_point_func_text():
    """
        function:
            检查断点续扫的说明文字
        args：
            none
        return:
            none
    """
    # 给定断点续扫的说明文字(可适配修改）
    __introduce_text__ = "开启后，地宝在电量充足时，会继续执行未完成的清扫工作。"
    try:
        poco(text='断点续扫', name='com.eco.global.app:id/titleContent').exists()
    except:
        raise AssertionError("当前页面非断点续扫主页面")
    if poco(name="com.eco.global.app:id/break_point_tips").get_text() == __introduce_text__:
        log("断点续扫的说明文字正确")
    else:
        raise Exception("断点续扫的说明文字不正确")
    
    
def check_break_point_func_introduce():
    """
        function:
            检查断点续扫使用说明文字
        args：
            none
        return:
            none
    """
    # 给定断点续扫使用说明文字(可适配修改）
    break_point_limit = ["主界面右上角显示该图标，表示此功能开启", "建议同步开启勿扰模式"]
    try:
        poco(text='断点续扫', name='com.eco.global.app:id/titleContent').exists()
    except:
        raise AssertionError("当前页面非断点续扫主页面")
    # 声明个空list
    break_point_press_limit = list()
    # 获取第一行说明文字
    break_point_press_limit.append(poco(name=r"com.eco.global.app:id/break_point_guide").get_text())
    # 获取第二行说明文字
    break_point_press_limit.append(poco(name=r"com.eco.global.app:id/tv_hint").get_text())
    for i in range(len(break_point_press_limit)):
        if break_point_press_limit[i] == break_point_limit[i]:
            log("断点续扫使用说明,第 " + str(i + 1) + " 行正确")
        else:
            raise Exception("断点续扫使用说明,第 " + str(i + 1) + " 行不正确")


def check_break_point_icon():
    """
        function:
            检查断点续扫在主页面的显示(本函数的默认执行所在页面为：清扫主页面）
        args：
            none
        return:
            none
    """
    # 判断当前页面是不是主页面（抓手是进入更多的元素）
    if poco(name="com.eco.global.app:id/top_status_more").exists():
        # 主界面 -> 更多
        poco(name="com.eco.global.app:id/top_status_more").click()
        # 获取当前断点续扫状态
        if get_status_of_break_point_func() == "open":
            # 更多 -> 主界面
            poco(name="com.eco.global.app:id/title_back").click()
            sleep(2)
            if exists(Template(r"tpl1587891039221.png", record_pos=(0.346, -0.71), resolution=(720, 1280))):
                log("断点续扫开启时，主页面成功找到断点续扫图标")
            else:
                raise Exception("断点续扫开启时，主页面没有找到断点续扫图标")
        elif get_status_of_break_point_func() == "close":
            # 更多 -> 主界面
            poco(name="com.eco.global.app:id/title_back").click()
            if exists(Template(r"tpl1587891039221.png", record_pos=(0.346, -0.71), resolution=(720, 1280))):
                raise Exception("断点续扫关闭时，主页面不应该找到断点续扫图标")
            else:
                log("断点续扫关闭时，主页面成功找不到断点续扫图标")
    else:
        raise Exception("得进入主页面查看断点续扫图标")
            

# if __name__ == "airtest.cli.runner":
if __name__ == "__main__":
    # 更多进入
    more_to_break_point_func()
    # 设置状态
    click_break_point_switch("open")
    # 返回更多页面
    break_point_func_to_more()
    # 获取
    break_point_status = get_status_of_break_point_func()
    # 检查
    if break_point_status == "open":
        log("设置的状态与更多页面获取的状态一致")
    check_break_point_func_text()
    check_break_point_func_introduce()
    # 去往主页面查看断点续扫图标
    check_break_point_icon()














