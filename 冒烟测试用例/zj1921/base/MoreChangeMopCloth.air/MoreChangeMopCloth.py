# -*- encoding=utf8 -*-
__author__ = "lei.z"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

using("base\\UniversalModule.air")
import UniversalModule

auto_setup(__file__)

'''
更换抹布提醒的相关方法和操作检查
'''
# 页面跳转
# 更多页面进入更换抹布提醒
def more_to_change_mop_cloth():
    """页面跳转，
    从更多页面进入更换抹布提醒"""
    poco(text="更换抹布提醒").click(sleep_interval=1)
    return True    

# 更换抹布提醒返回更多页面
def change_mop_cloth_to_more():
    """页面跳转，
    更换抹布提醒返回更多页面"""
    poco("com.eco.global.app:id/title_back").click(sleep_interval=1)
    return True


# 按钮点击
# 点击更多页面更换抹布提醒选项
def click_change_mop_cloth():
    """点击更多页面更换抹布提醒选项"""
    poco(text="更换抹布提醒").click(sleep_interval=1)
    return "已点击更换抹布提醒选项"

# 点击更换抹布提醒开关
def click_switch_btn():
    '''点击更换抹布提醒开关按钮'''
    poco("com.eco.global.app:id/toggle_btn").click(sleep_interval=1)
    return "已点击开关按钮"

# 点击设定时间选项
def click_set_time():
    '''点击设定时间'''
    poco("com.eco.global.app:id/rl_open").click(sleep_interval=1)
    return '已点击设定时间'


# 获取页面信息
# 获取更多页面更换抹布提醒选项按钮名称
def get_name_in_more():
    '''获取更多页面更换抹布提醒选项按钮名称'''
    name = poco(text="更换抹布提醒").get_text()
    return name

# 获取更多页面更换抹布提醒的开关状态名称
def get_status_in_more():
    '''获取更多页面更换抹布提醒的开关状态名称'''
    status = poco("android:id/content").offspring("com.eco.global.app:id/more_items").child("android.widget.RelativeLayout")[6].child("com.eco.global.app:id/msg").get_text()
    return status

# 获取更换抹布提醒的坐标
def get_coordinates():
    '''获取更换抹布提醒的坐标,返回坐标数组[x,y]'''
    cmc_coordinates = poco(text="更换抹布提醒").get_position()
    return cmc_coordinates

# 获取更换抹布提醒的抬头
def get_title():
    '''获取更换抹布提醒的抬头'''
    title = poco("com.eco.global.app:id/titleContent").get_text()
    return title

# 获取更换抹布提醒页面，更换抹布提醒的显示名称
def get_name_inside():
    '''获取更换抹布提醒页面，更换抹布提醒的显示名称'''
    name = poco("com.eco.global.app:id/tv").get_text()
    return name

# 获取更换抹布提醒页面，设定时间的显示名称
def get_name_of_set_time():
    '''获取更换抹布提醒页面，设定时间的显示名称'''
    name = poco("com.eco.global.app:id/subtitle").get_text()
    return name

# 获取更换抹布提醒页面，设定时间的显示时间数字
def get_time_value_of_set_time():
    '''获取更换抹布提醒页面，设定时间的显示时间数字'''
    time_str = poco("com.eco.global.app:id/msg").get_text()
    time_value = time_str[:2]
    return int(time_value)

# 获取更换抹布提醒页面，设定时间的显示时间单位
def get_time_unit_of_set_time():
    '''获取更换抹布提醒页面，设定时间的显示时间单位'''
    time_nuit = poco("com.eco.global.app:id/msg").get_text()[-3:]
    return time_nuit


# 设定操作
# 设定抹布提醒时间
def set_time(set_time,now_time):
    '''
    设定抹布提醒时间
    方向参数direction_parameter为负数，屏幕向上滑动
    '''   
    if set_time in [15,30,45,60]:
        if set_time > now_time:
            swipe_times = int((set_time - now_time)/15)
            direction_parameter = -1
            a=0.05*direction_parameter
            for i in range(swipe_times):
                swipe((500,1600), vector=[0.0, a])
            sleep(1)
        elif set_time < now_time:
            swipe_times = int((now_time - set_time)/15)
            direction_parameter = 1
            a=0.05*direction_parameter
            for i in range(swipe_times):
                swipe((500,1600), vector=[0.0, a])
            sleep(1)
        else:
            pass
    else:
        print("输入的时间设定不符合标准")


#页面元素检查
# 检查页面默认值是15min
def default_time_check():
    '''检查默认的时间设置值'''
    # 默认时间值
    default_time = '15min'
    # 获取当前时间值
    current_time = poco("com.eco.global.app:id/msg").get_text().strip()
    # 比较时间值，如果是默认值pass，反之fail
    try:
        assert_equal(current_time,default_time,"check default time")
    except Exception as e:
        print(e)

# 检查更多页面默认开关是关闭状态
def default_status_check():
    '''检查更多页面默认开关是关闭状态'''
    # 默认状态
    default_status = '关闭'
    # 当前状态
    current_status = poco("android:id/content").offspring("com.eco.global.app:id/more_items").child("android.widget.RelativeLayout")[6].child("com.eco.global.app:id/msg").get_text().strip()
    # 比较两个状态,如果是默认值pass，反之fail
    try:
        assert_equal(current_status,default_status,"check default status")
    except Exception as e:
        print(e)

# 检查内部页面开关默认是关闭状态
def default_switch_check():
    '''检查内部页面开关默认是关闭状态'''
    # 默认开关状态
    default_switch = '关闭'
    # 当前开关状态
    current_switch = UniversalModule.get_switch_status()
    # 比较开关状态,如果是默认值pass，反之fail
    try:
        assert_equal(current_switch, default_switch, "check switch status")
    except Exception as e:
        print(e)




