# -*- encoding=utf8 -*-
__author__ = "fangjiu.cheng"

from airtest.core.api import *


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
"""从更多界面进入地宝信息界面"""
def more_into_dmesg():
    poco(text="其他").click()
    poco(text="地宝信息").click()
    return print("进入地宝信息界面")
# more_into_dmesg()

"""获取抬头名称"""
def get_deboot_title():
    deboot_title = poco("com.eco.global.app:id/titleContent").get_text()
    return print(deboot_title)

"""获取固件版本选项名称"""
def get_fw_version_title():
    fw_version_title = poco("android:id/content").offspring("com.eco.global.app:id/miv_firmversion").child("android.widget.LinearLayout").offspring("com.eco.global.app:id/tv_left").get_text()
    return print(fw_version)

"""获取固件版本"""
def get_fw_version():
    fw_version = poco("android:id/content").offspring("com.eco.global.app:id/miv_firmversion").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").offspring("com.eco.global.app:id/tv_Right").get_text()
    if fw_version == None:
        raise AssertionError("未显示当前固件版本")
    else:
        return fw_version

"""获取SN选项名称"""
def get_sn_title():
    sn_title = poco("android:id/content").offspring("com.eco.global.app:id/miv_sn").child("android.widget.LinearLayout").offspring("com.eco.global.app:id/tv_left").get_text()
    return print(sn_title)

"""获取SN号"""
def get_sn_num():
    sn_num = poco("android:id/content").offspring("com.eco.global.app:id/miv_sn").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").offspring("com.eco.global.app:id/tv_Right").get_text()
    if sn_num == None:
        raise AssertionError("SN未显示")
    else:
        return print(sn_num)

"""获取网络信息选项名称"""
def get_network_info():
    network_info = poco("android:id/content").offspring("com.eco.global.app:id/miv_network").child("android.widget.LinearLayout").offspring("com.eco.global.app:id/tv_left").get_text()
    return print(network_info)

"""进入网络信息界面"""
def into_network():
    poco("android:id/content").offspring("com.eco.global.app:id/miv_network").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").child("android.widget.RelativeLayout").click()
    return "进入网络信息界面"

"""获取网络信息选项名称"""
def get_wifi_info_title():
    wifi_info_title = poco("android:id/content").offspring("com.eco.global.app:id/titleContent").get_text()
    if wifi_info_title != '网络信息':
        raise AssertionError("网络信息界面标题显示错误")
    else:
        return wifi_info_title 

""" 获取WiFI名称选项名称 """
def get_wifi_options():
    wifi_options_title = poco("android:id/content").offspring("com.eco.global.app:id/miv_wifi_name").child("android.widget.LinearLayout").offspring("com.eco.global.app:id/tv_left").get_text()
    if wifi_options_title != "Wi-Fi名称":
        raise AssertionError("wifi名称标题显示错误")
    else:
        return wifi_options_title
    
"""获取wifi名称"""
def get_wifi_name():
    wifi_name = poco("android:id/content").offspring("com.eco.global.app:id/miv_wifi_name").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").offspring("com.eco.global.app:id/tv_Right").get_text()
    if wifi_name == None:
        raise AssertionError("未显示WiFi名称")
    else:
        return wifi_name

"""获取WIfi强度选项名称"""
def get_wifi_power_options():
    wifi_power_title = poco("android:id/content").offspring("com.eco.global.app:id/miv_wifi_pharse").child("android.widget.LinearLayout").offspring("com.eco.global.app:id/tv_left").get_text()
    if wifi_power_title != "Wi-Fi强度":
        raise AssertionError("wifi强度标题显示错误")
    else:
        return wifi_power_title
"""获取wifi强度"""
def get_wifi_power():
    wifi_power = poco("android:id/content").offspring("com.eco.global.app:id/miv_wifi_pharse").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").offspring("com.eco.global.app:id/tv_Right").get_text()
    if wifi_power == None:
        raise AssertionError("wifi强度显示有误")
    else:
        return wifi_power

"""获取IP地址选项名称"""
def get_ip_address_options():
    ip_adress_title = poco("android:id/content").offspring("com.eco.global.app:id/miv_ip").child("android.widget.LinearLayout").offspring("com.eco.global.app:id/tv_left").get_text()
    if ip_adress_title != "IP地址":
        raise AssertionError("IP地址标题显示错误")
    else:
        return ip_adress_title

"""获取IP地址"""
def get_ip_address():
    ip_address = poco("android:id/content").offspring("com.eco.global.app:id/miv_ip").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").offspring("com.eco.global.app:id/tv_Right").get_text()
    if ip_address == None:
        raise AssertionError("ip地址显示有误")
    else:
        return ip_address

"""获取Mac地址选项名称"""
def get_mac_address_options():
    mac_adress_title = poco("android:id/content").offspring("com.eco.global.app:id/mac").child("android.widget.LinearLayout").offspring("com.eco.global.app:id/tv_left").get_text()
    if mac_adress_title != "Mac地址":
        raise AssertionError("Mac地址标题显示错误")
    else:
        return mac_adress_title

"""获取Mac地址"""
def get_mac_address():
    mac_address =  poco("android:id/content").offspring("com.eco.global.app:id/mac").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").offspring("com.eco.global.app:id/tv_Right").get_text()
    if mac_address == None:
        raise AssertionError("mac地址未显示")
    else:
        return mac_address

"""返回至地宝信息界面"""
def back_deboot_message():
    poco("com.eco.global.app:id/title_back").click()

"""进入固件版本详情界面"""
def into_fw_details():
    poco("android:id/content").offspring("com.eco.global.app:id/miv_firmversion").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").child("android.widget.RelativeLayout").click()
    return print("进入固件版本详情界面")

"""获取检查新版本选项名称"""
def get_check_new_version_title():
    check_new_version_title = poco("com.eco.global.app:id/tv_left").get_text()
    return print(check_new_version_title)
# get_check_new_version_title()

'''获取自动更新选项名称'''
def get_auto_update_title():
    auto_update_title = poco("com.eco.global.app:id/tv_silencename").get_text()
    
"""固件版本页面返回至地宝信息页面"""
def fw_back_message():
    poco("com.eco.global.app:id/title_back").click()

    
"""固件版本页面进入检查新版本页面"""
def fw_into_new():
    poco("android:id/content").offspring("android.widget.LinearLayout").child("android.widget.RelativeLayout").child("android.widget.RelativeLayout").click()
    
"""检查新版本进入固件版本页面"""
def new_back_fw():
    poco("com.eco.global.app:id/title_back").click()
    
'''检查固件版本页面，自动更新的提示文字'''
def check_auto_date_prompt():
    prompt_copy = poco("com.eco.global.app:id/tv_silencetip").get_text()
    if prompt_copy != "开启后，地宝将于凌晨0点到6点之间自动更新固件版本":
        raise AssertionError("自动更新提示文案显示有误")
    else:
        return prompt_copy
    
'''未开启自动更新，当前最新固件版本的页面显示'''
def check_switch_close():        
    if exists(Template(r"tpl1593313055846.png", record_pos=(-0.01, -0.684), resolution=(1080, 2340))) == True:
        print("界面显示正确")
    else:
        raise AssertionError("界面显示错误")

'''打开自动更新按钮'''
def open_auto_update():
    poco("com.eco.global.app:id/st_silence").click()
# open_auto_update()

'''开启自动更新，当前最新固件版本的页面显示'''
def check_switch_close():        
    if exists(Template(r"tpl1593313169669.png", record_pos=(-0.002, -0.684), resolution=(1080, 2340))) == True:
        print("界面显示正确")
    else:
        raise AssertionError("界面显示错误")

'''关闭自动更新按钮'''
def closed_auto_update():
    poco("com.eco.global.app:id/st_silence").click()
# closed_auto_update()
    
"""返回至更多界面"""
def back_more():
    poco("com.eco.global.app:id/title_back").click()
