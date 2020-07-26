# -*- encoding=utf8 -*-
__author__ = "lei.z"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
using(r"base\\UniversalModule.air")
import UniversalModule
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)
auto_setup(__file__)

# 耗材剩余时间字符串元素字典
accessories_remain_time_dict = {
    "side_brush" : poco("com.eco.global.app:id/tv_side_brush_desc"),
    "roll_brush" : poco("com.eco.global.app:id/tv_roll_brush_desc"),
    "hepa" : poco("com.eco.global.app:id/tv_hepa_desc")
}
# 耗材选项元素字典
accessories_dict = {
    "side_brush" : poco("com.eco.global.app:id/ll_side_brush"),
    "roll_brush" : poco("com.eco.global.app:id/ll_roll_brush"),
    "hepa" : poco("com.eco.global.app:id/ll_hepa")
}
# 耗材reset元素字典
accessories_reset_dict = {
    "side_brush" : poco("com.eco.global.app:id/tv_reset_side_brush"),
    "roll_brush" : poco("com.eco.global.app:id/tv_reset_roll_brush"),
    "hepa" : poco("com.eco.global.app:id/tv_reset_hepa")
}
# 耗材百分比数字元素字典
accessories_percent_number_dict = {
    "side_brush" : poco("com.eco.global.app:id/tv_side_brush_percent"),
    "roll_brush" : poco("com.eco.global.app:id/tv_roll_brush_percent"),
    "hepa" : poco("com.eco.global.app:id/tv_hepa_percent")
}
# 耗材图片元素字典
accessories_icon_dict = {
        "side_brush":poco("android:id/content").offspring("com.eco.global.app:id/sv_life_container").offspring("com.eco.global.app:id/ll_side_brush").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").child("android.widget.LinearLayout").offspring("android.widget.ImageView"),
    "roll_brush":poco("android:id/content").offspring("com.eco.global.app:id/sv_life_container").offspring("com.eco.global.app:id/ll_roll_brush").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").child("android.widget.LinearLayout").offspring("android.widget.ImageView"),
    "hepa":poco("android:id/content").offspring("com.eco.global.app:id/sv_life_container").offspring("com.eco.global.app:id/ll_hepa").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").child("android.widget.LinearLayout").offspring("android.widget.ImageView")
}
# 耗材右上角警告标志元素字典
accessories_warn_icon_dict = {
    "side_brush" : poco("com.eco.global.app:id/iv_side_warn"),
    "roll_brush" : poco("com.eco.global.app:id/iv_roll_warn"),
    "hepa" : poco("com.eco.global.app:id/iv_hepa_warn")
}
# 耗材百分比
accessories_percent_dict = {
    'side_brush':poco("android:id/content").offspring("com.eco.global.app:id/sv_life_container").offspring("com.eco.global.app:id/ll_side_brush").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").child("android.widget.LinearLayout").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").child("android.widget.LinearLayout"),
    'roll_brush':poco("android:id/content").offspring("com.eco.global.app:id/sv_life_container").offspring("com.eco.global.app:id/ll_roll_brush").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").child("android.widget.LinearLayout").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").child("android.widget.LinearLayout"),
    'hepa':poco("android:id/content").offspring("com.eco.global.app:id/sv_life_container").offspring("com.eco.global.app:id/ll_hepa").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").child("android.widget.LinearLayout").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").child("android.widget.LinearLayout")
}
# 页面跳转
def more_to_accessories():
    '''更多页面进入耗材计时页面'''
    ret = poco(text="耗材计时").click(sleep_interval=2)
    return ret

#点击边刷耗材复位按钮
def reset_sidebrush():
    poco("com.eco.global.app:id/tv_reset_side_brush").click()
    
#检查边刷耗材复位弹窗
def check_reset_sidebrach():
    if exists(Template(r"tpl1594359075411.png", rgb=True, record_pos=(0.0, -0.025), resolution=(1080, 2340))):
        return "存在"
           
    else:
        raise AssertionError("app未显示边刷耗材复位弹窗") 

#点击滚刷耗材复位按钮
def reset_rollbrush():
    poco("com.eco.global.app:id/tv_reset_roll_brush").click()    

#检查滚刷耗材复位弹窗
def check_reset_rollbrach():
    if exists(Template(r"tpl1594359096356.png", record_pos=(0.004, -0.021), resolution=(1080, 2340))):
        return "存在"
    else:
        raise AssertionError("app未显示滚刷耗材复位弹窗")

# 点击滤芯耗材复位按钮
def reset_hepa():
    poco("com.eco.global.app:id/tv_reset_hepa").click()

# 检查滤芯复位提示弹窗
def check_reset_hepa():
    if exists(Template(r"tpl1594359114210.png", record_pos=(-0.006, -0.025), resolution=(1080, 2340))):
        return "存在"
    else:
        raise AssertionError("app未显示滤芯耗材复位弹窗")

#点击复位弹窗取消或确定按钮
def reset_or_cancel(choose = "确定"):
    if choose == "确定":
        poco("com.eco.global.app:id/tv_positive").click()
    else:
        '''其他输入均默认为取消复位'''
        poco("com.eco.global.app:id/tv_cancel").click()

#进入购买耗材界面
def acc_buy():
    poco("com.eco.global.app:id/tv_buy").click()

def accessories_to_more():
    '''耗材计时页面返回更多页面'''
    ret = poco("com.eco.global.app:id/title_back").click(sleep_interval=2)
    return ret
# 信息获取
# 转换耗材的名称
def convert_accessories_name(accessory_name = '边刷'):
    '''
    由于用户可能会输入不同的耗材名称，需要进行转换
    根据使用者提供的耗材名称，转换为代码使用的耗材名称
    '''
    try:
        if accessory_name == '边刷' or accessory_name.lower().replace(' ','').replace('_','') == 'sidebrush':
            ret = "side_brush"
        elif accessory_name == '滚刷' or accessory_name.lower().replace(' ','').replace('_','') == 'mainbrush':
            ret = "roll_brush"
        elif accessory_name == '滤芯' or accessory_name.lower().replace(' ','') == 'filter' or accessory_name.lower() == 'hepa':
            ret = "hepa"
        else:
            raise NameError
    except Exception as err:
        print(accessory_name + ',耗材名称错误。')
        ret = err
    return ret

# 获取耗材剩余时间
def get_remain_time(accessory_name = '边刷',args = accessories_remain_time_dict):
    '''获取当前耗材剩余时间，单位为小时'''
    accessoryname = convert_accessories_name(accessory_name)
    remaining_time = accessories_remain_time_dict[accessoryname].get_text()[6:-2]
    return remaining_time

# 获取耗材剩余百分比，不含百分号
def get_remain_percent(accessory_name = '边刷',args =  accessories_percent_number_dict):
    accessoryname = convert_accessories_name(accessory_name)
    return accessories_percent_number_dict[accessoryname].get_text()
# 功能设置
# 重置耗材
def reset_accessories(accessory_name = '边刷',args = accessories_reset_dict):
    '''重置耗材的计时为0'''
    accessoryname = convert_accessories_name(accessory_name)
    ret = accessories_reset_dict[accessoryname].click(sleep_interval=2)
    return ret 

# 断言检查设置
# 检查耗材选项是否存在
def check_accessories_exists(accessory_name = '边刷', args = accessories_dict):
    '''
    检查耗材选项是否存在
    根据提供的耗材名称匹配耗材，并对应相应的poco元素进行判断
    '''
    check_info = "检查耗材选项"
    accessoryname = convert_accessories_name(accessory_name)
    ret = UniversalModule.assert_exists_check(accessories_dict[accessoryname],check_info+'--'+accessory_name,expectation='存在')
    return ret

# 检查耗材剩余时间信息存在
def check_accessories_remain_exists(accessory_name = 'hepa', args = accessories_remain_time_dict):
    '''
    检查耗材剩余时间信息存在
    根据提供的耗材名称匹配耗材，并对应相应的poco元素进行判断
    '''
    accessoryname = convert_accessories_name(accessory_name)
    check_info = '耗材剩余时间信息'
    ret = UniversalModule.assert_exists_check(accessories_remain_time_dict[accessoryname],accessory_name+'--'+check_info,expectation='存在')
    return ret

# 检查耗材百分比存在
def check_accessories_percent_exists(accessory_name = '边刷',args = accessories_percent_dict):
    '''
    检查耗材百分比存在
    根据提供的耗材名称匹配耗材，并对应相应的poco元素进行判断
    '''
    check_info = "检查耗材百分比"
    accessoryname = convert_accessories_name(accessory_name)
    ret = UniversalModule.assert_exists_check(accessories_percent_dict[accessoryname],check_info+'--'+accessory_name,expectation='存在')
    return ret
# 检查耗材警告标志存在
def check_accessories_warn_exists(accessory_name = '边刷', args = accessories_warn_icon_dict):
    '''
    检查耗材用尽告警标志
    根据提供的耗材名称匹配耗材，并对应相应的poco元素进行判断
    '''
    check_info = "检查耗材用尽告警标志"
    accessoryname = convert_accessories_name(accessory_name)
    ret = UniversalModule.assert_exists_check(accessories_warn_icon_dict[accessoryname],check_info+'--'+accessory_name,expectation='存在')
    return ret
    
# 检查购买耗材选项存在
def check_buy_acc():
    if exists(Template(r"tpl1594359140855.png", record_pos=(-0.002, 0.873), resolution=(1080, 2340))):
        return ('存在')
    else:
        raise AssertionError("未显示购买耗材按钮")

# 检查滤芯耗材用尽弹窗提示
def check_hepa_exhaust_sp_window():
    if exists(Template(r"tpl1594359555683.png", record_pos=(0.0, -0.025), resolution=(1080, 2340))):
        return "存在"
    else:
        raise AssertionError("APP未显示滤芯耗材用尽提示弹窗")
        
# 检查滤芯用尽常驻提示栏
def check_hepa_esident_prompt():
    if exists(Template(r"tpl1594359717211.png", rgb=True, record_pos=(-0.008, -0.429), resolution=(1080, 2340))):        
        logger.debug("APP显示滤芯用尽常驻提示栏")
        return "存在"
    else:
        return "不存在"
        
    
# 检查滚刷耗材用尽弹窗提示
def check_rollbrach_exhaust_sp_window():
    if exists(Template(r"tpl1594359584569.png", rgb=True, record_pos=(0.002, -0.023), resolution=(1080, 2340))):
        return "存在"
    else:
        raise AssertionError("app未显示滚刷耗材用尽弹窗提示")
#  检查滚刷用尽常驻提示栏
def check_rollbrach_esident_prompt():
    if exists(Template(r"tpl1594360096954.png", rgb=True, record_pos=(0.002, -0.432), resolution=(1080, 2340))):        
        logger.debug("APP显示滚刷用尽常驻提示栏")
        return "存在"
    else:
         return "不存在"
        
# 检查边刷耗材用尽弹窗提示
def check_sidebrach_exhaust_sp_window():
    if exists(Template(r"tpl1594359604436.png", rgb=True, record_pos=(-0.002, -0.021), resolution=(1080, 2340))):
        return "存在"
    else:
        raise AssertionError("app未显示边刷耗材用尽弹窗提示")  

#检查主界面显示边刷耗材用尽常驻提示
def check_sidebrach_esident_prompt():
    if exists(Template(r"tpl1594360555676.png", rgb=True, record_pos=(0.004, -0.432), resolution=(1080, 2340))):        
        logger.debug("APP显示边刷用尽常驻提示栏")
        return "存在"
    else:
        return "不存在"
        
#点击提示弹窗忽略按钮
def choose_lgnore():
    poco("com.eco.global.app:id/tv_cancel").click()
    
#点击提示弹窗查看按钮
def choose_examine():
    poco("com.eco.global.app:id/tv_positive").click()
    
#点击耗材用尽常驻提示
def into_sidebrach_esident_prompt():
    poco("com.eco.global.app:id/mavelRoundBgView").click()

#检查边刷用尽耗材计时界面显示
def check_sidebrach_exhaust_show():
    if exists(Template(r"tpl1594360502442.png", rgb=True, record_pos=(0.007, -0.591), resolution=(1080, 2340))):
        logger.debug("边刷用尽耗材计时界面显示正确")
    else:
        raise AssertionError(snapshot(msg='边刷用尽耗材计时界面显示错误'))
        
#检查滤芯用尽耗材计时界面显示
def check_hepa_exhaust_show():
    if exists(Template(r"tpl1594360514695.png", rgb=True, record_pos=(-0.005, 0.4), resolution=(1080, 2340))):
        logger.debug("滤芯用尽耗材计时界面显示正确")
    else:
        raise AssertionError(snapshot(msg='滤芯用尽耗材计时界面显示错误'))

#检查滚刷用尽耗材计时界面显示
def check_rollbrach_exhaust_show():
    if exists(Template(r"tpl1594360149650.png", rgb=True, record_pos=(0.006, -0.094), resolution=(1080, 2340))):
        logger.debug("滚刷用尽耗材计时界面显示正确")
    else:
        raise AssertionError(snapshot(msg='滚刷用尽耗材计时界面显示错误'))

#检测滤芯5%提示弹窗
def check_hepa_5():
    if exists(Template(r"tpl1594345162266.png", rgb=True, record_pos=(0.006, -0.029), resolution=(1080, 2340))):
        logger.debug("滤芯即将到期")
    else:
        raise AssertionError(snapshot("APP未显示滤芯5%提示弹窗"))
        
#检测滚刷5%提示弹窗
def check_rollbrach_5():
    if exists(Template(r"tpl1594345351013.png", rgb=True, record_pos=(0.004, -0.023), resolution=(1080, 2340))):
        logger.debug("滚刷即将到期")
    else:
        raise AssertionError("APP未显示滚刷5%提示弹窗")

#检测边刷5%提示弹窗
def check_sidebrach_5():
    if exists(Template(r"tpl1594345369785.png", record_pos=(-0.002, -0.019), resolution=(1080, 2340))):
        logger.debug("边刷即将到期")
    else:
        raise AssertionError(snapshot(msg="APP未显示边刷5%提示弹窗"))


