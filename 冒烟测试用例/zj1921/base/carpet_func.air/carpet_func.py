# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco import exceptions
import cv2
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

"""
以下函数皆与 地毯增压有关
"""


def more_to_carpet_func():
    """
    function:
        从更多进入地毯增压
    args：
        none
    return:
        none
    """
    if not poco(text="强效拖地方式").exists():
        try:
            # 在更多页面
            poco(text='地毯增压').click()
            sleep(2)
        except:
            log("点击地毯增压出错...")
        # 地毯增压页面
        if poco(text='地毯增压', name='com.eco.global.app:id/titleContent').exists():
            log("进入地毯增压...")
        else:
            raise AssertionError("进入地毯增压出错...")
    else:
        if poco(text="地毯增压").exists():
            raise Exception("强效拖地模式下,地毯增压不应该显示")
        else:
            log("强效拖地模式下,地毯增压不显示")


def carpet_func_to_more():
    """
    function:
        从地毯增压界面进入更多
    args：
        none
    return:
        none
    """
    try:
        if poco(text='地毯增压', name='com.eco.global.app:id/titleContent').exists():
            sleep(2)
            poco(name='com.eco.global.app:id/title_back').click()
            sleep(2)
    except:
        raise AssertionError("返回更多页面出错...")    
        
        
def click_carpet_func_switch(__action__=None):
    """
    function:
        开启地毯增压,包含开启和关闭
    args：
        __action__：默认为none，还有open和close
        作用是指定对地毯增压开关的操作
    return:
        none
    """
    if not poco(text="强效拖地方式").exists():
        try:
            if poco(text='地毯增压', name='com.eco.global.app:id/titleContent').exists():
                # 不管当前地毯增压状态，直接点击开关
                if not __action__:
                    try:
                        poco(name="com.eco.global.app:id/toggle_btn").click()
                        log("点击地毯增压按键成功")
                        sleep(2)
                    except InvalidOperationException:
                        raise AssertionError("点击地毯增压开关失败")
                # 开启地毯增压
                elif __action__ == "open":
                    if exists(Template(r"tpl1587370114189.png", threshold=0.9, rgb=True, record_pos=(0.439, -0.668), resolution=(720, 1280))):
                        log("地毯增压状态已经为开启")
                    else:
                        try:
                            poco(name="com.eco.global.app:id/toggle_btn").click()
                            sleep(2)
                            if exists(Template(r"tpl1587370440617.png", threshold=0.9, rgb=True, record_pos=(0.438, -0.668), resolution=(720, 1280))):
                                raise AssertionError("地毯增压开启失败")
                            else:
                                log("地毯增压状态开启成功")
                        except InvalidOperationException:
                            raise AssertionError("地毯增压开启失败")
                # 关闭地毯增压开关
                elif __action__ == "close":
                    if exists(Template(r"tpl1587370440617.png", threshold=0.9, rgb=True, record_pos=(0.438, -0.668), resolution=(720, 1280))):
                        log("地毯增压状态已经为关闭")
                    else:
                        try:
                            poco(name="com.eco.global.app:id/toggle_btn").click()
                            sleep(2)
                            if exists(Template(r"tpl1587370114189.png", threshold=0.9, rgb=True, record_pos=(0.439, -0.668), resolution=(720, 1280))):
                                raise AssertionError("地毯增压关闭失败")
                            else:
                                log("地毯增压状态关闭成功")
                        except InvalidOperationException:
                            raise AssertionError("地毯增压关闭失败")
                else:
                    raise Exception("参数值填写错误")
            else:
                raise Exception("当前不在地毯增压界面")
        except PocoException:
            raise AssertionError("返回更多页面出错...")
    else:
        if poco(text="地毯增压").exists():
            raise Exception("强效拖地模式下,地毯增压不应该显示")
        else:
            log("强效拖地模式下,地毯增压不显示")
        

def check_carpet_func_introduce():
    """
    function:
        检查地毯增压的说明文字
    args：
        none
    return:
        none
    """
    # 给定地毯增压的说明文字(可适配修改）
    __introduce_text__ = "开启后，在清扫模式下，地宝识别到地毯时将自动开启强劲吸力 "
    try:
        poco(text='地毯增压', name='com.eco.global.app:id/titleContent').exists()
    except:
        raise AssertionError("当前页面非地毯增压主页面")
    if poco(name="com.eco.global.app:id/robot_carpet_func_tips").get_text() == __introduce_text__:
        log("地毯增压的说明文字正确")
    else:
        raise Exception("地毯增压的说明文字不正确")
    
            
def check_carpet_func_introduce():
    """
    function:
        检查地毯增压使用说明文字
    args：
        none
    return:
        none
    """
    # 给定地毯增压使用说明文字(可适配修改）
    carpet_limit = ["1.请在非地毯区域启动清扫", "2.滚刷缠绕毛发时可能在非地毯界面误启动强吸力模式，请及时清理滚刷"]
    try:
        poco(text='地毯增压', name='com.eco.global.app:id/titleContent').exists()
    except:
        raise AssertionError("当前页面非地毯增压主页面")
    # 声明个空list
    carpet_press_limit = list()
    # 获取第一行说明文字
    carpet_press_limit.append(poco(name=r"com.eco.global.app:id/robot_carpet_func_limit").get_text())
    # 获取第二行说明文字
    carpet_press_limit.append(poco(name=r"com.eco.global.app:id/robot_carpet_press_limit").get_text())
    for i in range(len(carpet_press_limit)):
        if carpet_press_limit[i] == carpet_limit[i]:
            log("地毯增压使用说明,第 " + str(i + 1) + " 行正确")
        else:
            raise Exception("地毯增压使用说明,第 " + str(i + 1) + " 行不正确")


def get_status_of_carpet_func():
    """
        function:
            检查地毯增压开关的状态
        args：
            none
        return:
            __carpet_status__:地毯增压开关的状态值,返回值为：open,close
    """
    __status_dic__ = {"开启":"open", "关闭":"close"}
    try:
        # 在更多页面
        poco(text='更多', name='com.eco.global.app:id/titleContent').exists()
    except:
        raise AssertionError("当前页面非更多主页面")
    # 只有非强效拖地模式下，才有地毯增压
    if not poco(text="强效拖地方式").exists():
        # 地毯增压在更多页面左边第3行，get_position的第二个参数为Y轴
        if poco(name="com.eco.global.app:id/title")[3].get_text() == "地毯增压":
            carpet_pos_y = poco(name="com.eco.global.app:id/title")[3].get_position()[1]
        else:
            raise Exception("地毯增压值不在更多页面，或在更多页面的位置不对")
        # 地毯增压状态在更多页面左边第3行
        capter_status_y = poco(name="com.eco.global.app:id/msg")[2].get_position()[1]
        if carpet_pos_y - capter_status_y < 0.01:
            __carpet_status__ = poco(name="com.eco.global.app:id/msg")[2].get_text()
            __carpet_status__ = __status_dic__[__carpet_status__]
            return __carpet_status__
        else:
           raise Exception("更多页面的行值没对准")
    else:
        if poco(text="地毯增压").exists():
            raise Exception("强效拖地模式下,地毯增压不应该显示")
        else:
            log("强效拖地模式下,地毯增压不显示")


"""
函数的使用方法举例
"""
# if __name__ == "airtest.cli.runner":
if __name__ == "__main__":
    # 更多进入
    more_to_carpet_func()
    sleep(3)
    # 设置状态为关闭
    click_carpet_func_switch("close")
    # 返回更多页面
    carpet_func_to_more()
    sleep(3)
    # 获取
    carpet_status = get_status_of_carpet_func()
    # 检查更多页面显示的地毯增压状态与设置的状态
    if carpet_status == "close":
        log("更多页面显示的地毯增压状态与设置的状态一致")
    else:
        raise Exception("更多页面显示的地毯增压状态与设置的状态 不一致")
