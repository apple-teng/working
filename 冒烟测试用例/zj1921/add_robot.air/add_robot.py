# -*- encoding=utf8 -*-
__author__ = "lei.z"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
robot_model = "DEEBOT T5"
robot_name = "DEEBOT T5 Max"
password = "1+2+3+4=10"
poco("com.eco.global.app:id/actionbar_left").click(sleep_interval=1)
touch(Template(r"tpl1589960231094.png", record_pos=(-0.208, -0.42), resolution=(1080, 1920)))

def get_robot_model_list():
    robot_model_list = []
    for i in poco("com.eco.global.app:id/tv_left"):
        robot_model_list.append(i.get_text())
    return robot_model_list
def get_robot_name_list():
    robot_name_list = []
    for i in poco("com.eco.global.app:id/tv_robot"):
        robot_name_list.append(i.get_text())
    return robot_name_list
while True:
    if poco("com.eco.global.app:id/btn_success").exists():
        poco("com.eco.global.app:id/btn_success").click(sleep_interval=1)
        sleep(10)
    else:
        break
    
poco(text="机器人").wait_for_appearance()

while True:
    modellist = get_robot_model_list()
    if robot_model in modellist:
        poco(text=robot_model).click(sleep_interval=1)
        break
    else:
        swipe((110.890),(110.1600))
        continue

while True:
    namelist = get_robot_name_list()
    if robot_name in namelist:
        poco(text=robot_name).click(sleep_interval=1)
        break
    else:
        swipe((110.890),(110.1600))
        continue
if poco("com.eco.global.app:id/btn_two_gosetting").exists():
    poco("com.eco.global.app:id/btn_two_gosetting").click(sleep_interval=1)
else:
    pass
def agree_some_btn(element):
    if element.exists():
        element.click(sleep_interval=1)
    else:
        pass
agree_some_btn(poco("com.android.packageinstaller:id/permission_allow_button"))
poco("com.eco.global.app:id/wifi_password").click(sleep_interval=1)
touch(Template(r"tpl1589962350456.png", record_pos=(0.277, 0.11), resolution=(1080, 1920)))
sleep(1)
text(password)
poco("com.eco.global.app:id/next_step").click(sleep_interval=1)
poco("com.eco.global.app:id/config_switch").click(sleep_interval=1)
poco("com.eco.global.app:id/btn_next").click(sleep_interval=1)
poco("com.eco.global.app:id/config_switch").click(sleep_interval=1)
poco("com.eco.global.app:id/btn_next").click(sleep_interval=1)

poco("com.eco.global.app:id/tv_title").wait_for_appearance(300)