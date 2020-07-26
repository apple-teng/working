<<<<<<< HEAD
=======
# -*- encoding=utf8 -*-
__author__ = "fangjiu.cheng"

from airtest.core.api import *


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
"""获取重命名标题"""
def get_rename():
    poco(text="其他").click()
    return poco(text="重命名").get_text()   

"""更多页面有重命名选项"""
def check_rename():
    if get_rename() == "重命名":
        print("重命名功能可使用")
    else:
        return ("界面无重命名功能可选择") 

'''获取更多界面地宝名称显示'''
def get_more_rename():
    more_renme = poco("android:id/content").offspring("com.eco.global.app:id/more_items").child("android.widget.LinearLayout")[4].child("com.eco.global.app:id/msg").get_text()
    return more_renme

"""检查默认地宝名称"""
def check_default_name():
    default_name =  poco("android:id/content").offspring("com.eco.global.app:id/more_items").child("android.widget.LinearLayout")[4].child("com.eco.global.app:id/msg").get_text()
    return default_name
        
"""更多界面进入重命名界面"""
def more_to_rename():
    poco(text="重命名").click()
    sleep(5)
    return print("进入重命名界面")

'''检查重命名界面显示'''
def check_rename_show():
    if assert_exists(Template(r"tpl1594108796514.png", record_pos=(0.058, -0.02), resolution=(1080, 2340)), "重命名界面显示"):
        return "重命名界面显示正确"
    else:
        raise AssertionError(snapshot(msg="重命名界面显示错误"))
                
"""获取重命名界面标题"""
def get_rename_title():
    rename_title = poco("com.eco.global.app:id/titleContent").get_text()
    return rename_title

"""获取输入框内默认名称"""
def get_default_name():
    return poco("com.eco.global.app:id/cet_rename_edit").get_text()

"""获取提示文字"""
def get_hint_copywriting():    
    hint_copywriting = poco("com.eco.global.app:id/tv_rename_hint").get_text()
    return hint_copywriting

"""清空地宝名称"""
def clean_deboot_name():
    poco("com.eco.global.app:id/cet_rename_edit").click()
    touch(Template(r"tpl1586776005469.png", record_pos=(0.431, -0.687), resolution=(1080, 2160)))

"""点击取消按钮"""
def cancel_set():
    poco("com.eco.global.app:id/title_back").click()
    
""""设置地宝名称"""
def set_deboot_name():
    more_to_rename()
    poco("com.eco.global.app:id/cet_rename_edit").click()
    text("小白")

"""点击保存按钮"""
def save_set():
    poco("com.eco.global.app:id/right").click()
    return print("重命名保存成功")
    
"""重命名页面进入更多页面"""
def rename_to_more():
    more_to_rename()
    poco("com.eco.global.app:id/title_back").click()
    return print("重命名返回更多界面") 
=======
# -*- encoding=utf8 -*-
__author__ = "fangjiu.cheng"

from airtest.core.api import *


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
"""获取重命名标题"""
def get_rename():
    poco(text="其他").click()
    return poco(text="重命名").get_text()   

"""更多页面有重命名选项"""
def check_rename():
    if get_rename() == "重命名":
        print("重命名功能可使用")
    else:
        return ("界面无重命名功能可选择") 

'''获取更多界面地宝名称显示'''
def get_more_rename():
    more_renme = poco("android:id/content").offspring("com.eco.global.app:id/more_items").child("android.widget.LinearLayout")[4].child("com.eco.global.app:id/msg").get_text()
    return more_renme

"""检查默认地宝名称"""
def check_default_name():
    default_name =  poco("android:id/content").offspring("com.eco.global.app:id/more_items").child("android.widget.LinearLayout")[4].child("com.eco.global.app:id/msg").get_text()
    return default_name
        
"""更多界面进入重命名界面"""
def more_to_rename():
    poco(text="重命名").click()
    sleep(5)
    return print("进入重命名界面")
 
"""获取重命名界面标题"""
def get_rename_title():
    rename_title = poco("com.eco.global.app:id/titleContent").get_text()
    return rename_title

"""获取输入框内默认名称"""
def get_default_name():
    return poco("com.eco.global.app:id/cet_rename_edit").get_text()

"""获取提示文字"""
def get_hint_copywriting():    
    hint_copywriting = poco("com.eco.global.app:id/tv_rename_hint").get_text()
    return hint_copywriting

"""清空地宝名称"""
def clean_deboot_name():
    poco("com.eco.global.app:id/cet_rename_edit").click()
    touch(Template(r"tpl1586776005469.png", record_pos=(0.431, -0.687), resolution=(1080, 2160)))

"""点击取消按钮"""
def cancel_set():
    poco("com.eco.global.app:id/title_back").click()
    
""""设置地宝名称"""
def set_deboot_name():
    more_to_rename()
    poco("com.eco.global.app:id/cet_rename_edit").click()
    text("小白")

"""点击保存按钮"""
def save_set():
    poco("com.eco.global.app:id/right").click()
    return print("重命名保存成功")
    
"""重命名页面进入更多页面"""
def rename_to_more():
    more_to_rename()
    poco("com.eco.global.app:id/title_back").click()
    return print("重命名返回更多界面") 



    

    

    

    
>>>>>>> dd196aee2fce228a2934b23f7e00c9ea2d2e531d
