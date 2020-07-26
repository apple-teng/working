# -*- encoding=utf8 -*-
__author__ = "fangjiu.cheng"

from airtest.core.api import *



from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)
auto_setup(__file__)

# 进入使用帮助界面
def more_to_help():
    poco(text="使用帮助").click()
    sleep(3)
    
# 检测使用帮助界面显示
def check_help_show():
    if exists(Template(r"tpl1594350975211.png", record_pos=(-0.407, -0.923), resolution=(1080, 2340))):
        logger.debug("返回按钮显示正确")
    else:
        raise AssertionError("未显示返回按钮")
    if poco("com.eco.global.app:id/actionbar_title").get_text() == "T8 MAX":
        logger.debug("使用帮助标题机型显示正确")
    else:
        raise AssertionError('使用帮助标题机型显示错误')
    if poco("com.eco.global.app:id/help").get_text() == "使用帮助":
        logger.debug("使用帮助小标题显示正确")
    else:
        raise AssertionError("使用帮助小标题显示错误")
    if exists(Template(r"tpl1594350992632.png", record_pos=(0.004, -0.207), resolution=(1080, 2340))):
        logger.debug("app有使用视频")
    else:
        raise AssertionError("app未显示使用帮助视频")
    if exists(Template(r"tpl1594351009455.png", record_pos=(0.002, 0.299), resolution=(1080, 2340))):
        logger.debug("app显示使用帮助说明书按钮")
    else:
        raise AssertionError('APP未显示使用帮助说明书按钮')
    
    swipe(Template(r"tpl1594351029283.png", record_pos=(-0.363, 0.448), resolution=(1080, 2340)), Template(r"tpl1594351063871.png", record_pos=(-0.331, -0.793), resolution=(1080, 2340))) 

    sleep(2)
    if exists(Template(r"tpl1594351093591.png", record_pos=(-0.002, -0.17), resolution=(1080, 2340))):
        logger.debug("常见问题栏显示正常")
    else:
        raise AssertionError("app未显示常见问题显示栏")
    swipe(Template(r"tpl1594351122110.png", record_pos=(-0.461, -0.152), resolution=(1080.0, 2340.0)), vector=[0.0892, -0.3957])

    
    sleep(2)
    if exists(Template(r"tpl1594351137335.png", record_pos=(0.0, -0.08), resolution=(1080, 2340))):
        logger.debug('APP显示全部问题按钮')
    else:
        raise AssertionError("app未显示全部问题按钮")
        
    if exists(Template(r"tpl1594351154941.png", record_pos=(-0.014, 0.235), resolution=(1080, 2340))):
        logger.debug('APP显示使用技巧栏')
    else:
        raise AssertionError("app未显示使用技巧栏")
    if exists(Template(r"tpl1594351167476.png", record_pos=(0.002, 0.701), resolution=(1080, 2340))):
        logger.debug('使用帮助下方显示客服栏')
    else:
        raise AssertionError("使用帮助下方未显示客服栏")   
    
    swipe(Template(r"tpl1594351192787.png", record_pos=(0.474, -0.781), resolution=(1080.0, 2340.0)), vector=[-0.0543, 1])



# 进入使用说明书界面
def into_operation_instruction():
     poco("com.eco.global.app:id/spec").click()
    
#检查使用说明书预览界面
def check_operation_instruction_preview():
    if exists(Template(r"tpl1594351235469.png", rgb=True, record_pos=(0.004, -0.031), resolution=(1080, 2340))) and exists(Template(r"tpl1594351256183.png", rgb=True, record_pos=(-0.002, 0.885), resolution=(1080, 2340))):
        logger.debug("使用说明书预览界面显示正确")     
    else:
        raise AssertionError(snapshot(msg="使用说明书预览界面显示错误"))
        
# 点击下载说明书按钮
def install_operation_instruction():
    poco("com.eco.global.app:id/progress_button").click()    
     
# 检查使用说明书可以正常下载
def check_install_operation_instruction():
    if exists(Template(r"tpl1594351283236.png", rgb=True, record_pos=(0.0, 0.887), resolution=(1080, 2340))) or exists(Template(r"tpl1594351290587.png", rgb=True, record_pos=(0.006, 0.885), resolution=(1080, 2340))):
        logger.debug("app显示下载进度条")
    else:
        raise AssertionError("app未显示下载进度条")

# 检查下载成功按钮
def check_examine_operation_instruction():
    if exists(Template(r"tpl1594351256183.png", record_pos=(-0.002, 0.885), resolution=(1080, 2340))):
        return "主机未开始下载"
    elif exists(Template(r"tpl1594351338042.png", rgb=True, record_pos=(-0.002, 0.878), resolution=(1080, 2340))):
        return('下载成功')
    else:
        raise AssertionError("使用说明书下载有误")

# 点击查看完整说明书按钮
def examine_operation_instruction():
    poco("com.eco.global.app:id/progress_button").click()

# 使用说明书返回至使用帮助界面
def operation_instruction_back_help():
    touch(Template(r"tpl1594351366905.png", rgb=True, record_pos=(0.016, -0.544), resolution=(1080.0, 2340.0)))


    poco("com.eco.global.app:id/actionbar_left").click()
    
# 检查使用帮助初显示界面
def check_help_start():
    if exists(Template(r"tpl1594351398937.png", rgb=True, record_pos=(-0.006, -0.143), resolution=(1080, 2340))):
        return "进入使用帮助界面"
    else:
        raise AssertionError("使用帮助界面显示有误")

# 点击查看使用帮助视频
def examine_help_video():
    poco("android:id/content").offspring("android.widget.ScrollView").child("android.widget.LinearLayout").offspring("com.eco.global.app:id/videoBlock").offspring("android.widget.FrameLayout")[0].child("android.widget.ImageView").click()
# examine_help_video()    

# 检测视频可以播放：
def check_help_video_ok():
    if exists(Template(r"tpl1594351470449.png", rgb=True, record_pos=(0.0, -0.032), resolution=(1080, 2340))):
        logger.debug("视频加载中")
        
        if wait(Template(r"tpl1594351455896.png", rgb=True, record_pos=(0.0, -0.021), resolution=(1080, 2340))):
            logger.debug("视频正在播放")
        else:
            raise AssertionError("使用帮助视频未正常播放")
    else:
        examine_help_video()
# check_help_video_ok()

# 点击返回至使用帮助界面
def video_back_help():
    poco("com.eco.global.app:id/close").click()

    
    
    
        


    

     
    
        


       






