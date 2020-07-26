# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"
import random
from airtest.core.api import *
from airtest.core.android.minitouch import *
import time
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

using("UniversalModule.air")
import UniversalModule
# log输出等级为：error
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)

"""已下函数，皆与虚拟墙有关"""

def click_main_to_virtualWall():
    """
        function:
            从main点击虚拟墙按钮，进入虚拟墙编辑页面
        args：
            none        
        return:
            none
    """
    if poco(name='com.eco.global.app:id/deebot_statues').exists():
        poco(name='com.eco.global.app:id/iv_mapmgr_btn').click()
        sleep(2)
    else:
        snapshot(msg='请保证主机为运行状态，否则没有虚拟墙按钮')
        raise AssertionError("请保证主机为运行状态，否则没有虚拟墙按钮")
        
        
def click_virtualWall_to_main():
    """
        function:
            点击虚拟墙编辑页面的返回按钮，返回到主界面
        args：
            none        
        return:
            none
    """
    if poco(name='com.eco.global.app:id/top_status_back1').exists():
        poco(name='com.eco.global.app:id/top_status_back1').click()
        logger.debug("虚拟墙返回主界面")
        log("虚拟墙返回主界面")
    elif poco(name='com.eco.global.app:id/back_btn').exists():
        poco(name='com.eco.global.app:id/back_btn').click()
        logger.debug("虚拟墙返回主界面[2]")
        log("虚拟墙返回主界面[2]")
    else:
        snapshot(msg='点击虚拟墙编辑页面的返回按钮出错，截图检查')
        raise AssertionError("点击虚拟墙编辑页面的返回按钮出错")
    try:
        poco(name='com.eco.global.app:id/tv_dianLiang').wait_for_appearance()
    except:
        snapshot(msg='点击虚拟墙编辑页面的返回按钮，没有返回主页面，截图检查')
        raise AssertionError("点击虚拟墙编辑页面的返回按钮，没有返回主页面")
        
        
def check_virtalWall_popMsg():
    """
        function:
            检查首次进入虚拟墙编辑页面的引导，并点击取消引导
            包括：虚拟墙有什么用,拖地禁区引导有什么用
        args：
            none        
        return:
            none
    """
    # 查看虚拟墙引导消息
    if exists(Template(r"tpl1594272403913.png", record_pos=(-0.057, 0.484), resolution=(1080, 2340))):
        logger.debug("弹出虚拟墙引导消息")
        log("弹出虚拟墙引导消息")
    elif poco(name='com.eco.global.app:id/vwall_guide_func').exists():
        if poco(name='com.eco.global.app:id/vwall_guide_func_detail').get_text() == '设定虚拟墙后，地宝工作时会自动避开虚拟墙框定区域':
            logger.debug("弹出虚拟墙引导消息")
            log("弹出虚拟墙引导消息")
        else:
            logger.debug("弹出虚拟墙引导消息不对")
            log("弹出虚拟墙引导消息不对")
    else:
#       logger.debug("没有弹出虚拟墙引导消息")
#       log("没有弹出虚拟墙引导消息")
        snapshot(msg='没有弹出虚拟墙引导消息')
        raise AssertionError('没有弹出虚拟墙引导消息')
    # 切换引导到拖地禁区
    poco(name='com.eco.global.app:id/vwall_guide_func_detail').click()
    sleep(1)
    
    
def check_mopping_popMsg():
    """
        function:
            检查首次进入虚拟墙编辑页面的引导
            包括：拖地禁区引导有什么用
        args：
            none        
        return:
            none
    """
    # 查看拖地禁区引导
    if exists(Template(r"tpl1594272799601.png", record_pos=(0.064, 0.478), resolution=(1080, 2340))):
        logger.debug("弹出拖地禁区引导消息")
        log("弹出拖地禁区引导消息")
    elif poco(name='com.eco.global.app:id/mopwall_guide_func').exists():
        if poco(name='com.eco.global.app:id/mopwall_guide_func_detail').get_text() == '设定拖地禁区后，地宝仅在拖地时会自动避开该拖地禁区':
            logger.debug("弹出拖地禁区引导消息内容正确")
            log("弹出拖地禁区引导消息内容正确")
        else:
            logger.debug("弹出拖地禁区引导消息不对")
            log("弹出拖地禁区引导消息不对")
    else:
#         logger.debug("没有弹出虚拟墙引导消息")
#         log("没有弹出虚拟墙引导消息")
        snapshot(msg='没有弹出拖地禁区引导消息')
        raise AssertionError('没有弹出拖地禁区引导消息') 
        
        
        
def check_draw_virtalWall_direction():
    """
        function:
            查看如何绘制矩形虚拟墙与拖地禁区?
        args：
            none        
        return:
            none
    """
    # 查看如何绘制矩形虚拟墙与拖地禁区?
    try:
        wait(Template(r"tpl1594273031450.png", record_pos=(-0.006, 0.189), resolution=(1080, 2340)))
        logger.debug("如何绘制矩形虚拟墙与拖地禁区显示正确")
        log("如何绘制矩形虚拟墙与拖地禁区显示正确")
    except:
        snapshot(msg='没有弹出如何绘制矩形虚拟墙与拖地禁区，查看截图')
        raise AssertionError("没有弹出如何绘制矩形虚拟墙与拖地禁区")
    else:
        if poco(name='com.eco.global.app:id/rect_guide_txt').exists():
            if poco(name='com.eco.global.app:id/rect_guide_detail').get_text() == '1.选取矩形工具' + '\n' + '2.在地图上滑动，设定范围':
                logger.debug("如何绘制矩形虚拟墙与拖地禁区内容正确")
                log("如何绘制矩形虚拟墙与拖地禁区内容正确")
            else:
                logger.debug(poco(name='com.eco.global.app:id/rect_guide_detail').get_text())
                log(poco(name='com.eco.global.app:id/rect_guide_detail').get_text())
                snapshot(msg='如何绘制矩形虚拟墙与拖地禁区内容不对，查看截图')
                raise AssertionError("如何绘制矩形虚拟墙与拖地禁区内容不对")
        else:
            snapshot(msg='没有弹出如何绘制矩形虚拟墙与拖地禁区，查看截图')
            raise AssertionError("没有弹出如何绘制矩形虚拟墙与拖地禁区")
            
            
def check_draw_line_virtallWall_dirction():
    """
        function:
            查看如何绘制线性虚拟墙?
        args：
            none        
        return:
            none
    """
    try:
        wait(Template(r"tpl1594273631921.png", record_pos=(-0.004, 0.143), resolution=(1080, 2340)))
    except:
        snapshot(msg='没有线性虚拟墙引导')
        raise AssertionError('没有线性虚拟墙引导')
    else:
        if poco(name='com.eco.global.app:id/line_guide_txt').exists():
            if poco(name='com.eco.global.app:id/line_guide_detail').get_text() == '1.选取线形工具' + '\n' + '2.在地图上滑动，设定范围':
                logger.debug("如何绘制线性虚拟墙引导内容正确")
                log("如何绘制线性虚拟墙引导内容正确")                
            else:
                logger.debug(poco(name='com.eco.global.app:id/line_guide_detail').get_text())
                log(poco(name='com.eco.global.app:id/line_guide_detail').get_text())
                snapshot(msg='如何绘制线性虚拟墙引导内容不对，查看截图')
                raise AssertionError("如何绘制线性虚拟墙引导内容不对")
        else:
            snapshot(msg='没有弹出如何绘制矩形虚拟墙与拖地禁区，查看截图')
            raise AssertionError("没有弹出如何绘制矩形虚拟墙与拖地禁区")
            
            
def click_virtalWall_popMsg():
    """
        function:
            点击取消引导虚拟墙消息的蒙层
            包括：虚拟墙有什么用,拖地禁区引导有什么用
        args：
            none        
        return:
            none
    """
    while True:
        if poco(name='com.eco.global.app:id/vwall_guide_func_detail').exists():
            # 切换引导到拖地禁区
            poco(name='com.eco.global.app:id/vwall_guide_func_detail').click()
            sleep(1)

        elif poco(name='com.eco.global.app:id/mopwall_guide_func_detail').exists():
            # 取消引导消息的蒙层
            poco(name='com.eco.global.app:id/mopwall_guide_func_detail').click()
            sleep(1)
        elif poco(name='com.eco.global.app:id/rect_guide_detail').exists():
            # 如何绘制线性虚拟墙引导
            poco(name='com.eco.global.app:id/rect_guide_detail').click()
        else:
            break
 

def click_Iknow_to_exit_virtualWall_dirction():
    """
        function:
            点击知道了，退出引导
        args：
            none        
        return:
            none
    """
    # 点击知道了，退出引导
    if exists(Template(r"tpl1594273703264.png", record_pos=(0.004, 0.639), resolution=(1080, 2340))):
        touch(Template(r"tpl1594273703264.png", record_pos=(0.004, 0.639), resolution=(1080, 2340)))
        logger.debug("点击知道了，退出引导")
        log("点击知道了，退出引导") 
    elif poco(text='知道了').exists():
        poco(name='com.eco.global.app:id/i_know').click()
        logger.debug("点击知道了，退出引导[2]")
        log("点击知道了，退出引导[2]") 
    else:
        snapshot(msg='退出虚拟墙引导出错，查看截图')         
        raise AssertionError("退出虚拟墙引导出错")

                
def check_virtualWall_direction():
    """
        function:
            检查首次进入虚拟墙编辑页面的引导，并一一点掉
            包括：虚拟墙有什么用,拖地禁区引导有什么用
            查看如何绘制矩形性虚拟墙? 查看如何绘制线性虚拟墙?
        args：
            none        
        return:
            none
    """
    # 查看虚拟墙引导消息
    if exists(Template(r"tpl1594272403913.png", record_pos=(-0.057, 0.484), resolution=(1080, 2340))):
        logger.debug("弹出虚拟墙引导消息")
        log("弹出虚拟墙引导消息")
    elif poco(name='com.eco.global.app:id/vwall_guide_func').exists():
        if poco(name='com.eco.global.app:id/vwall_guide_func_detail').get_text() == '设定虚拟墙后，地宝工作时会自动避开虚拟墙框定区域':
            logger.debug("弹出虚拟墙引导消息")
            log("弹出虚拟墙引导消息")
        else:
            logger.debug("弹出虚拟墙引导消息不对")
            log("弹出虚拟墙引导消息不对")
    else:
#       logger.debug("没有弹出虚拟墙引导消息")
#       log("没有弹出虚拟墙引导消息")
        snapshot(msg='没有弹出虚拟墙引导消息')
        raise AssertionError('没有弹出虚拟墙引导消息')
    # 切换引导到拖地禁区
    poco(name='com.eco.global.app:id/vwall_guide_func_detail').click()
    sleep(1)
    # 查看拖地禁区引导
    if exists(Template(r"tpl1594272799601.png", record_pos=(0.064, 0.478), resolution=(1080, 2340))):
        logger.debug("弹出拖地禁区引导消息")
        log("弹出拖地禁区引导消息")
    elif poco(name='com.eco.global.app:id/mopwall_guide_func').exists():
        if poco(name='com.eco.global.app:id/mopwall_guide_func_detail').get_text() == '设定拖地禁区后，地宝仅在拖地时会自动避开该拖地禁区':
            logger.debug("弹出拖地禁区引导消息内容正确")
            log("弹出拖地禁区引导消息内容正确")
        else:
            logger.debug("弹出拖地禁区引导消息不对")
            log("弹出拖地禁区引导消息不对")
    else:
#         logger.debug("没有弹出虚拟墙引导消息")
#         log("没有弹出虚拟墙引导消息")
        snapshot(msg='没有弹出拖地禁区引导消息')
        raise AssertionError('没有弹出拖地禁区引导消息') 
    # 取消引导消息的蒙层
    poco(name='com.eco.global.app:id/mopwall_guide_func_detail').click()
    sleep(1)
    # 查看如何绘制矩形虚拟墙与拖地禁区?
    try:
        wait(Template(r"tpl1594273031450.png", record_pos=(-0.006, 0.189), resolution=(1080, 2340)))
        logger.debug("如何绘制矩形虚拟墙与拖地禁区显示正确")
        log("如何绘制矩形虚拟墙与拖地禁区显示正确")
    except:
        snapshot(msg='没有弹出如何绘制矩形虚拟墙与拖地禁区，查看截图')
        raise AssertionError("没有弹出如何绘制矩形虚拟墙与拖地禁区")
    else:
        if poco(name='com.eco.global.app:id/rect_guide_txt').exists():
            if poco(name='com.eco.global.app:id/rect_guide_detail').get_text() == '1.选取矩形工具' + '\n' + '2.在地图上滑动，设定范围':
                logger.debug("如何绘制矩形虚拟墙与拖地禁区内容正确")
                log("如何绘制矩形虚拟墙与拖地禁区内容正确")
            else:
                logger.debug(poco(name='com.eco.global.app:id/rect_guide_detail').get_text())
                log(poco(name='com.eco.global.app:id/rect_guide_detail').get_text())
                snapshot(msg='如何绘制矩形虚拟墙与拖地禁区内容不对，查看截图')
                raise AssertionError("如何绘制矩形虚拟墙与拖地禁区内容不对")
        else:
            snapshot(msg='没有弹出如何绘制矩形虚拟墙与拖地禁区，查看截图')
            raise AssertionError("没有弹出如何绘制矩形虚拟墙与拖地禁区")

    # 如何绘制线性虚拟墙引导
    poco(name='com.eco.global.app:id/rect_guide_detail').click()
    sleep(1)
    try:
        wait(Template(r"tpl1594273631921.png", record_pos=(-0.004, 0.143), resolution=(1080, 2340)))
    except:
        snapshot(msg='没有线性虚拟墙引导')
        raise AssertionError('没有线性虚拟墙引导')
    else:
        if poco(name='com.eco.global.app:id/line_guide_txt').exists():
            if poco(name='com.eco.global.app:id/line_guide_detail').get_text() == '1.选取线形工具' + '\n' + '2.在地图上滑动，设定范围':
                logger.debug("如何绘制线性虚拟墙引导内容正确")
                log("如何绘制线性虚拟墙引导内容正确")                
            else:
                logger.debug(poco(name='com.eco.global.app:id/line_guide_detail').get_text())
                log(poco(name='com.eco.global.app:id/line_guide_detail').get_text())
                snapshot(msg='如何绘制线性虚拟墙引导内容不对，查看截图')
                raise AssertionError("如何绘制线性虚拟墙引导内容不对")
        else:
            snapshot(msg='没有弹出如何绘制矩形虚拟墙与拖地禁区，查看截图')
            raise AssertionError("没有弹出如何绘制矩形虚拟墙与拖地禁区")                 

    #  点击知道了，退出引导
    if exists(Template(r"tpl1594273703264.png", record_pos=(0.004, 0.639), resolution=(1080, 2340))):
        touch(Template(r"tpl1594273703264.png", record_pos=(0.004, 0.639), resolution=(1080, 2340)))
        logger.debug("点击知道了，退出引导")
        log("点击知道了，退出引导") 
    elif poco(text='知道了').exists():
        poco(name='com.eco.global.app:id/i_know').click()
        logger.debug("点击知道了，退出引导[2]")
        log("点击知道了，退出引导[2]") 
    else:
        snapshot(msg='退出虚拟墙引导出错，查看截图')         
        raise AssertionError("退出虚拟墙引导出错")
                 

def click_virtualWall_button(button_type): 
    """
        function:
            在虚拟墙编辑页面，点击虚拟墙、拖地禁区
        args：
            button_type：虚拟墙 或 拖地禁区按钮
            - 取值包括："vwall"：虚拟墙
                        "mop"：拖地禁区按钮
        return:
            none
    """
    if poco(text='虚拟墙').exists():
        if button_type == 'vwall':
            poco(name='com.eco.global.app:id/vwall_set_title').click()
        elif button_type == 'mop':
            poco(name='com.eco.global.app:id/mop_forbid_vwall_set_title').click()
        else:
            raise AssertionError("按钮参数值有误，请检查")
    else:
        snapshot(msg='当前页面虚拟墙、拖地禁区按钮不可用，请检查')
        raise AssertionError("当前页面虚拟墙、拖地禁区按钮不可用")
        
        
def click_rect_line_button(wall_type):
    """
        function:
            选择点击矩形虚拟墙 或者 线性虚拟墙
        args：
            wall_type：矩形虚拟墙 或者 线性虚拟墙
            - 取值包括："rect"：矩形虚拟墙
                        "line" ：线性虚拟墙
        return:
            none
    """ 
    if wall_type == "rect":
        poco(name='com.eco.global.app:id/vwall_rect_btn').click()
    elif wall_type == "line":
        poco(name='com.eco.global.app:id/vwall_line_btn').click()
    else:
        raise AssertionError("按钮参数值有误，请检查")
   
        
def check_default_choose_of_virtualWall(working_type):
    """
        function:
            检查主机在清扫状态，默认选中“虚拟墙”，
                    在拖地模式，默认选中“拖地禁区”
            或者用于检查选择“虚拟墙”或者“拖地禁区”的title是否被选中
        args：
            working_type：主机的工作模式，为清扫或者拖地
            - 'clean'：清扫状态
            - 'mop'：拖地模式
        return:
            none
    """
    if working_type == 'clean':
        try:
            poco(name='com.eco.global.app:id/bar_vwall').exists()
        except:
            snapshot("清扫状态，没有默认选中“虚拟墙”，截图检查")
            raise AssertionError("清扫状态，没有默认选中“虚拟墙”")    
    elif working_type == 'mop':
        try:
            poco(name='com.eco.global.app:id/bar_mop_forbid').exists()
        except:
            snapshot(msg="拖地状态下没有默认选中“拖地禁区，截图检查")
            raise AssertionError("拖地状态下没有默认选中“拖地禁区")
            
            
def click_virtualWall_quiz():
    """
        function:
            点击虚拟墙编辑页面的“？”
        args：
            none
        return:
            none
    """
    if poco(name='com.eco.global.app:id/quiz').exists():
        poco(name='com.eco.global.app:id/quiz').click()
        sleep(1)
    else:
        snapshot(msg='当前页面不是虚拟墙编辑页面，截图检查')
        raise AssertionError("当前页面不是虚拟墙编辑页面")
        
        
def check_draw_moppingWall_display():
    """
        function:
            检查点击“拖地禁区”矩形拖地禁区后的页面显示
        args：
            none
        return:
            none
    """
    check_default_choose_of_virtualWall('mop')
    if poco(text='请在地图范围内设定拖地禁区').exists():
        logger.debug("进入拖地禁区编辑页面")
        log("进入拖地禁区编辑页面")
    else:
        snapshot(msg='进入拖地禁区编辑页面没有预期的文字显示，截图检查')
        raise AssertionError("进入拖地禁区编辑页面没有预期的文字显示")
        

def draw_a_virtualwall():
    """
        function:
            在手机屏幕界面的中心位置画一个矩形虚拟墙（包含拖地禁区）,但是没有点击“√”或者“×”
        args：
            none
        return:
            none
    """
    # 设置虚拟墙的初始参数
    x1, y1 = poco(name='android.view.View').get_position() # 拖拽的起点
    logger.debug(x1)
    logger.debug(y1)
    x2, y2 = x1-0.1, y1-0.1# 拖拽的终点
    sleep(1)
    poco.swipe([x1,y1],[x2,y2])
    

def draw_a_line_virtualwall():
    """
        function:
            在手机屏幕界面的中心位置画一个线性虚拟墙,但是没有点击“√”或者“×”
        args：
            none
        return:
            none
    """
    pass


def drag_virtualwall():
    """
        function:
            对尚未提交的虚拟墙（包含拖地禁区）进行拖拽
        args：
            none
        return:
            none
    """
#     if exists(Template(r"tpl1594351459359.png", record_pos=(0.067, -0.255), resolution=(1080, 2340))):
#         x1, y1 =
    pass


def check_edit_virtualwall_display():
    """
        function:
            检查虚拟墙尚未提交处于编辑状态时的显示
        args：
            none
        return:
            none
    """
    if exists(Template(r"E:\airTest\冒烟测试用例\zj1921\base\virtualWall.air\tpl1594364666555.png", record_pos=(-0.137, -0.816), threshold=0.6, resolution=(1080, 2340))):
        logger.debug("虚拟墙编辑状态时存在提交按钮")
        log("虚拟墙编辑状态时存在提交按钮")
    else:
        snapshot(msg='虚拟墙编辑状态时不存在提交按钮，截图检查')
        raise AssertionError("虚拟墙编辑状态时不存在提交按钮")
    if exists(Template(r"E:\airTest\冒烟测试用例\zj1921\base\virtualWall.air\tpl1594364679015.png", record_pos=(-0.133, -0.03), threshold=0.6, resolution=(1080, 2340))):
        logger.debug("虚拟墙编辑状态时存在删除按钮")
        log("虚拟墙编辑状态时存在删除按钮")
    else:
        snapshot(msg='虚拟墙编辑状态时没存在预期的删除按钮，截图检查')
        raise AssertionError("虚拟墙编辑状态时没存在预期的删除按钮")
        
    if not poco(text='请在地图范围内设定拖地禁区').exists():
        logger.debug("手动画定拖地禁区矩形框，处于待确认状态，文字消失")
        log("手动画定拖地禁区矩形框，处于待确认状态，文字消失")
    else:
        snapshot(msg='手动画定拖地禁区矩形框，处于待确认状态，文字没消失，截图检查')
        raise AssertionError("手动画定拖地禁区矩形框，处于待确认状态，文字没消失")


def click_to_submit_a_virtualwall():
    """
        function:
            点击“√”，提交编辑状态时的虚拟墙
        args：
            none
        return:
            none
    """
    if exists(Template(r"E:\airTest\冒烟测试用例\zj1921\base\virtualWall.air\tpl1594364666555.png", record_pos=(-0.137, -0.816), threshold=0.6, resolution=(1080, 2340))):
        touch(Template(r"E:\airTest\冒烟测试用例\zj1921\base\virtualWall.air\tpl1594364666555.png", record_pos=(-0.137, -0.816), threshold=0.6, resolution=(1080, 2340)))
        sleep(1)
        logger.debug("提交虚拟墙")
        log("提交虚拟墙")
    else:
        snapshot(msg='虚拟墙不处于编辑状态，截图检查')
        raise AssertionError("虚拟墙不处于编辑状态")
    sleep(2)
    if not exists(Template(r"E:\airTest\冒烟测试用例\zj1921\base\virtualWall.air\tpl1594364666555.png", record_pos=(-0.137, -0.816), threshold=0.6, resolution=(1080, 2340))) and not exists(Template(r"E:\airTest\冒烟测试用例\zj1921\base\virtualWall.air\tpl1594364679015.png", record_pos=(-0.133, -0.03), threshold=0.6, resolution=(1080, 2340))):
        logger.debug("提交虚拟墙后，确认和取消按钮消失")
        log("提交虚拟墙后，确认和取消按钮消失")
    else:
        snapshot(msg='提交虚拟墙失败，截图检查')
        raise AssertionError("提交虚拟墙失败")
        

def click_to_cancel_a_virtualwall():
    """
        function:
            点击“×”，取消编辑状态时的虚拟墙
        args：
            none
        return:
            none
    """
    if exists(Template(r"E:\airTest\冒烟测试用例\zj1921\base\virtualWall.air\tpl1594364679015.png", record_pos=(-0.133, -0.03), threshold=0.6, resolution=(1080, 2340))):
        touch(Template(r"E:\airTest\冒烟测试用例\zj1921\base\virtualWall.air\tpl1594364679015.png", record_pos=(-0.133, -0.03), threshold=0.6, resolution=(1080, 2340)))
        sleep(1)
        logger.debug("取消虚拟墙")
        log("取消虚拟墙")
    else:
        snapshot(msg='虚拟墙不处于编辑状态，截图检查')
        raise AssertionError("虚拟墙不处于编辑状态")
    sleep(2)
    if (not exists(Template(r"E:\airTest\冒烟测试用例\zj1921\base\virtualWall.air\tpl1594364679015.png", record_pos=(-0.133, -0.03), threshold=0.7, resolution=(1080, 2340)))) and (not exists(Template(r"E:\airTest\冒烟测试用例\zj1921\base\virtualWall.air\tpl1594364666555.png", record_pos=(-0.137, -0.816), threshold=0.7, resolution=(1080, 2340)))):
        logger.debug("取消虚拟墙后，确认和取消按钮消失")
        log("取消虚拟墙后，确认和取消按钮消失")
    else:
        snapshot(msg='取消虚拟墙失败，截图检查')
        raise AssertionError("取消虚拟墙失败")
        
        
def check_popmsg_by_mopping_vwall():
    """
        function:
            检查在清扫状态下设置拖地禁区，回到主界面，APP上弹出弱提示：清扫过程中不显示拖地禁区
        args：
            none
        return:
            none
    """
    try:
        wait(Template(r"E:\airTest\冒烟测试用例\zj1921\base\virtualWall.air\tpl1594368216304.png", record_pos=(0.056, 0.649), resolution=(1080, 2340)))
        logger.debug("APP上弱提示：清扫过程中不显示拖地禁区")
        log("APP上弱提示：清扫过程中不显示拖地禁区")
    except:
        snapshot(msg='APP上没有弹出弱提示：清扫过程中不显示拖地禁区，截图检查')
        raise AssertionError("APP上没有弹出弱提示：清扫过程中不显示拖地禁区")
        
        
            
# if __name__ == 'main':
if __name__ == 'airtest.cli.runner':
    click_to_cancel_a_virtualwall()
#     click_rect_line_button("rect")
#     print(11111111111111111111)
#     sleep(2)
#     draw_a_virtualwall()
#     print(222222222222222222222222)
#     check_edit_virtualwall_display()
#     click_to_submit_a_virtualwall()
#     sleep(2)
#     click_virtualWall_to_main()
#     check_popmsg_by_mopping_vwall()
#     check_draw_moppingWall_display()
#     click_virtualWall_quiz()
#     check_virtualWall_direction()
#     click_virtualWall_button(button_type='mop')
#     click_virtualWall_button(button_type='vwall')
#     click_rect_line_button("line")
#     click_rect_line_button("rect")
        
    
            
    
        

    
    




