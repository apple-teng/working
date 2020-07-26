# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco import exceptions
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)

auto_setup(__file__)

def more_to_disturb():
    """
    function:
        从更多进入勿扰界面
    args：
        none
    return:
        none
    """
    try:
        if poco(text='勿扰模式').exists():
            sleep(2)
            poco(text='勿扰模式').click()
            sleep(2)
    except:
        log("进入勿扰模式出错...")
    
def disturb_to_more():
    """
    function:
        从勿扰界面进入更多
    args：
        none
    return:
        none
    """
    try:
        if poco(text='勿扰模式', name='com.eco.global.app:id/titleContent').exists():
            sleep(2)
            poco(name='com.eco.global.app:id/title_back').click()
            sleep(2)
    except:
        raise AssertionError("返回更多页面出错...")
        
"""
开启勿扰模式

"""
def change_disturb(switch = "开启"):
    if switch == "开启":
        if exists(Template(r"tpl1594274471543.png", record_pos=(-0.074, -0.367), resolution=(1080, 2340))):
            logger.debug("勿扰模式已开启")
        elif exists(Template(r"tpl1594264881399.png", rgb=True, record_pos=(0.408, -0.708), resolution=(1080, 2340))):
            
            poco("com.eco.global.app:id/dnd_toggle_btn").click()
            wait(Template(r"tpl1594265800986.png", rgb=True, record_pos=(0.405, -0.703), resolution=(1080, 2340)))
            
            if exists(Template(r"tpl1594265800986.png", rgb=True, record_pos=(0.405, -0.703), resolution=(1080, 2340))):
                logger.debug("勿扰模式开启成功")
            else:
                raise AssertionError("勿扰模式开启失败")
        
        else:
            raise AssertionError("勿扰界面显示错误")
    elif switch == "关闭":
        if exists(Template(r"tpl1594274506519.png", rgb=True, record_pos=(-0.088, -0.372), resolution=(1080, 2340))):
            poco("com.eco.global.app:id/progressBar").click()
            sleep(5)
            if exists(Template(r"tpl1594264881399.png", rgb=True, record_pos=(0.408, -0.708), resolution=(1080, 2340))):
                logger.debug("勿扰模式关闭成功")
            else:
                raise AssertionError("勿扰模式关闭失败")
        elif exists(Template(r"tpl1594274519418.png", rgb=True, record_pos=(-0.077, -0.367), resolution=(1080, 2340))):
            logger.debug("勿扰模式已开启")
        else:
            raise AssertionError("勿扰界面显示错误")
    else:
        raise AssertionError("勿扰界面显示有误")
# change_disturb(switch = "开启")                   
    
def click_disturb_switch():
    """
    function:
        从点击勿扰开关（包含打开勿扰开关和关闭勿扰开关）
    args：
        none
    return:
        none
    Raises:
        InvalidOperationException
    """
    if poco(text='勿扰模式', name='com.eco.global.app:id/titleContent').exists():
        try:
            poco(name='com.eco.global.app:id/dnd_toggle_btn').click()
            sleep(2)
            # 要注意设置图像的rgb，开启彩色识别，提高图像识别阈值
            if exists(Template(r"tpl1586857830519.png", threshold=0.9, rgb=True, record_pos=(0.444, -0.66), resolution=(720, 1280))):
                log("关闭勿扰成功...")
            # 要注意设置图像的rgb，开启彩色识别，提高图像识别阈值
            elif exists(Template(r"tpl1586858010741.png", threshold=0.9, rgb=True, record_pos=(0.444, -0.656), resolution=(720, 1280))):
                log("开启勿扰成功...")
            else:
                log("图像识别有问题...")
        except InvalidOperationException:
            log("开关勿扰出现问题，请重试...")
    else:
        raise AssertionError("当前不在勿扰模式页面")

        
def check_description_of_disturb():
    """
    function:
        检查勿扰功能的文字说明
    args：
        none
    return:
        none
    Raises:
        InvalidOperationException
    """
    if poco(text='勿扰模式', name='com.eco.global.app:id/titleContent').exists():
        description_of_disturb = '开启后，勿扰时间段内，不主动执行预约清扫和断点续扫，并关闭地宝语音和灯光'
        if poco(name='com.eco.global.app:id/dnd_description').get_text() == description_of_disturb:
            log("勿扰模式使用指导文字显示正确...")
        else:
            raise AssertionError('勿扰模式使用指导文字显示错误,请检查...')
    else:
        raise AssertionError("当前不在勿扰模式页面")
        
        
def set_distrub_time(start_time=None, end_time=None):
    """
    function:
        设置勿扰时间
    args：
        start_time:勿扰开始时间,(obj:str),
            写入格式为HH:MM（小时：分钟）
        end_time:勿扰结束时间，(obj:str),
            写入格式为HH:MM（小时：分钟）
    return:
        none
    Raises:
        InvalidOperationException
    """  
    if poco(text='勿扰模式', name='com.eco.global.app:id/titleContent').exists():
        try:
            # 判断是否传了要设置时间的参数
            if start_time:             
                sleep(2)
                startTime_hour = start_time.split(':')[0]
                startTime_min = start_time.split(':')[1]
                endTime_hour = end_time.split(':')[0]
                endTime_min = end_time.split(':')[1]
                # 设置开始时间
                poco(text='开始时间').click()
                while True:
                    if poco("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text().split(":")[0] == startTime_hour:
                        poco("com.eco.global.app:id/ib_ok").click()
                        continue
                    else:
                        # 小时往上滑一个
                        poco(name='android:id/numberpicker_input')[0].swipe('down')
                        print(2222222222222222222222222)
                        tv_start_time =poco("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text().split(":")[0]
                        print(33333333333333333333333333333333333)
                        if tv_start_time == startTime_hour:
                            poco("com.eco.global.app:id/ib_ok").click()
                            break
                        else:
                            continue
                if  exists(Template(r"tpl1594275908205.png", record_pos=(0.002, -0.024), resolution=(1080, 2340))):
                    print("开始结束时间相同")
                else:
                    poco(text='结束时间').click()
                    while True:
                        if poco("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text().split(":")[0] == endTime_hour:
                        
                            continue
                        # 小时往上滑一个
                        else:
                            poco(name='android:id/numberpicker_input')[0].swipe('up')
                            print(2222222222222222222222222)
                            tv_end_time = poco("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text().split(":")[0]
                            print(33333333333333333333333333333333333)
                            if tv_end_time == endTime_hour:
                                poco("com.eco.global.app:id/ib_ok").click()
                                break
                            else:
                                continue
        finally:
            log('...')
    else:
        raise AssertionError("当前不在勿扰模式页面")
    
"""
检查勿扰设置相同时间弹窗显示

"""
def check_sametime_prompt():
    if exists(Template(r"tpl1594262696088.png", record_pos=(0.0, -0.022), resolution=(1080, 2340))):
        logger.debug("app显示时间设置无效弹窗")
    else:
        raise AssertionError("app未显示相同时间提示弹窗")
        
"""
点击“知道了”按钮
"""
def click_know():
    poco("com.eco.global.app:id/tv_cancel").click()
        
# if __name__ == 'airtest.cli.runner':
#     set_distrub_time('6:20','5:30')
    