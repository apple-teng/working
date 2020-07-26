# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco import exceptions
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
"""
以下函数皆与 拖地水量有关
"""


def more_to_wateryeild():
    """
    function:
        从更多进入拖地水量
    args：
        none
    return:
        none
    """
    try:
        poco(text='拖地水量').click()
        sleep(2)
        if poco(text='拖地水量', name='com.eco.global.app:id/titleContent').exists():
            log("进入拖地水量...")        
    except:
        log("进入拖地水量出错...")
    
    
def wateryeild_to_more():
    """
    function:
        从拖地水量界面进入更多
    args：
        none
    return:
        none
    """
    try:
        if poco(text='拖地水量', name='com.eco.global.app:id/titleContent').exists():
            sleep(2)
            poco(name='com.eco.global.app:id/title_back').click()
            sleep(2)
    except:
        raise AssertionError("返回更多页面出错...")
        
        
def check_wateryeild_title():
    """
    function:
        检查拖地水量界面的title
    args：
        none
    return:
        none
    """
    if poco(text='拖地水量', name='com.eco.global.app:id/titleContent').exists():
        log("拖地水量的title正确")
    else:
        raise AssertionError("拖地水量的title不正确")
        
        
def check_wateryeild_level():
    """
    function:
        检查拖地水量界面的水量及水量排位,是UI检查
    args：
        __waterLevel_list__:水量列表，eg:['超高', '高', '中', '低']
        __position_dic__:水量值在當前界面的所處位置的高度，
            eg:{'超高': 0.3236111111111111, '高': 0.262037037037037, '中': 0.20046296296296295, '低': 0.1388888888888889}
    return:
        __waterLevel_list__
    """
    __waterLevel_list__ = []
    __position_dic__ = {}
    elements = poco("android.widget.RelativeLayout").offspring("com.eco.global.app:id/tv_left")
    print(elements)
    for i in elements:
        __waterLevel_list__.append(i.get_text())
    __waterLevel_list__ = set(__waterLevel_list__)
    print("当前拖地水量的值有：" + str(__waterLevel_list__))

    # 获取水量的纵坐标位置
    for j in __waterLevel_list__:
        __position_dic__[j] = poco(text=j).get_position()[1]
    #     print("当前水量和其对应的纵坐标位置为：",end="")
    #     print(__position_dic__)
    # 判断水量的排序    
    if "超高" in __position_dic__:
        if __position_dic__['低'] < __position_dic__['中'] < __position_dic__['高'] < __position_dic__['超高']:
            log("当前排位正确")
        else:
            raise AssertionError("水量排位错误！")
    else:
        if __position_dic__['低'] < __position_dic__['中'] < __position_dic__['高']:
            log("当前排位正确")
        else:
            raise AssertionError("水量排位错误！")
    return __waterLevel_list__


def check_notice_of_setting_wateryeild_superhigh():
    """
        function:
            检查拖地水量界面的水量及水量排位
        args：
            __waterLevel_list__:水量列表，eg:['超高', '高', '中', '低']
        return:
            none
    """
    __waterLevel_list__ = []
    elements = poco("android.widget.RelativeLayout").offspring("com.eco.global.app:id/tv_left")
    print(elements)
    for i in elements:
        __waterLevel_list__.append(i.get_text())
    __waterLevel_list__ = set(__waterLevel_list__)
    print("当前拖地水量的值有：" + str(__waterLevel_list__))
    if "超高" in __waterLevel_list__:
        poco(text="超高").click()
        try:
            wait(Template(r"tpl1587023366690.png", record_pos=(0.102, 0.611), resolution=(1080, 2160)),10)
        except:
            raise AssertionError("选择超高水量，没有弹出弱消息提示...")
    else:
        raise AssertionError("超高水量不存在，请检查...")


def check_selected_wateryeild_icon():
    """
        function:
            检查拖地水量界面的右边有选中图标
        args：
            none
        return:
            none
    """          
    try:
        if poco(name='com.eco.global.app:id/tv_Right').exists():
            log("水量选择有对应的弹框...")
    except:
        raise AssertionError("水量选择没有对应的弹框...")
        
        
def set_wateryeild_level(__waterLevel__):
    """
        function:
            检查拖地水量界面的水量及水量排位
        args：
            waterLevel_range:水量的取值范围
            __waterLevel__:需要传入的拖地水量，obj：str
                取值范围为：'超高', '高', '中', '低'。
                eg. set_wateryeild_level("高")
        return:
            none
    """
    # 获取当前水量的取值范围
    waterLevel_range = []
    waterLevel_range = check_wateryeild_level()
    if __waterLevel__ in waterLevel_range:
        # 获取设置水量左边的位置的纵坐标
        text_pos = poco(text=__waterLevel__).get_position()[1]
        poco(text=__waterLevel__).click()
    else:
        # assert(__waterLevel__ in waterLevel_range)
        raise AssertionError(__waterLevel__ + " 不在可选择的水量范围...")
    # 获取选中水量对应icon的图标的纵坐标
    icon_pos = poco(name='com.eco.global.app:id/tv_Right').get_position()[1]
    if text_pos == icon_pos:
        log("拖地水量选择成功")
    else:
        raise AssertionError(__waterLevel__ + " 拖地水量设置失败")
  

def click_to_save_waterLevel():
    """
        function:
            点击“保存”按钮
        args：
            none
        return:
            none
    """
    try:
        poco(text="保存").click()
        # 点完保存后页面跳转到更多页面
        poco(name='com.eco.global.app:id/titleContent', text="更多").wait_for_appearance()
    except InvalidOperationException:
        log("保存拖地水量失败")
        
        
def click_cancle_to_return_to_more():
    """
        function:
            点击取消按钮
        args：
            none
        return:
            none
    """
    try:
        poco(text="取消").click()
        # 当前在更多页面(寻找地宝图标 为判断依据)
        if poco(name='com.eco.global.app:id/locate_deebot').exists():
            log("返回到更多页面")
        else:
            raise AssertionError("返回到更多页面失败")
    except InvalidOperationException:
        log("返回到更多页面失败")
        

def click_how_to_start_mopping():
    """
        function:
            点击如何启动拖地模式的超链接
        args：
            none
        return:
            none
    """
    hyperlink_str = "如何启动拖地模式 >"
    # __page_dic__ = {"第一步": "取出水箱，装水", "第二步": "将抹布安装到支架上", "第三步": "将装好抹布的支架紧扣至水箱上", "第四步": "将二者装回机器，即刻进入拖地模式"}
    
    try:
        if poco(name="com.eco.global.app:id/wateryield_guide").get_text() == hyperlink_str:
            poco(text=hyperlink_str).click()
            # 该方法只对比了文字内容，不够全面
    #         # 检查弹出的图片
    #         poco(name="com.eco.global.app:id/iv_guide").wait_for_appearance()
    #         # 对比每页的title和contents的文字是否对应的上
    #         for title in __page_dic__.keys():
    #             if __page_dic__[title] == poco(name="com.eco.global.app:id/tv_page_contents").get_text():
    #                 poco(name="com.eco.global.app:id/iv_guide").swipe([-0.9, 0])
    #                 sleep(2)
    #             else:
    #                 raise AssertionError(title + "文字内容有误")
    #         # 循环结束，点击“知道了”
    #         poco(text="知道了").click()
    #
        else:
            raise AssertionError("拖地水量的如何启动拖地模式的超链接文字内容不对")
    except:
        raise Exception("查看启动拖地水量超链接出错")
        
    page_index = 1
    # 第一页显示
    if exists(Template(r"tpl1587279374495.png", record_pos=(-0.001, -0.161), resolution=(1080, 2160))):
        log("拖地超链接第 " + str(page_index) + " 步显示正确")
        poco(name="com.eco.global.app:id/iv_guide").swipe([-0.9, 0])
        page_index += 1
        sleep(2)
    else:
        log("拖地超链接第 " + str(page_index) + " 步显示不正确")
    # 第二页显示
    if exists(Template(r"tpl1587279623599.png", record_pos=(0.003, -0.141), resolution=(1080, 2160))):
        log("拖地超链接第 " + str(page_index) + " 步显示正确")
        poco(name="com.eco.global.app:id/iv_guide").swipe([-0.9, 0])
        page_index += 1
        sleep(2)
    else:
        log("拖地超链接第 " + str(page_index) + " 步显示不正确")
    # 第三页显示
    if exists(Template(r"tpl1587279855074.png", record_pos=(-0.002, -0.116), resolution=(1080, 2160))):
        log("拖地超链接第 " + str(page_index) + " 步显示正确")
        poco(name="com.eco.global.app:id/iv_guide").swipe([-0.9, 0])
        page_index += 1
        sleep(2)
    else:
        log("拖地超链接第 " + str(page_index) + " 步显示不正确")
    # 第四页显示
    if exists(Template(r"tpl1587279923100.png", record_pos=(-0.001, 0.013), resolution=(1080, 2160))):
        log("拖地超链接第 " + str(page_index) + " 步显示正确")
        sleep(2)
        poco(text="知道了").click()
    else:
        log("拖地超链接第 " + str(page_index) + " 步显示不正确")


def get_wateryeild_level_from_more():
    """
            function:
                点击如何启动拖地模式的超链接
            args：
                none
            return:
                __water_level__:更多页面的拖地水量值
                该值可以与set_wateryeild_level()中带入的参数值对比，来确认设置是否成功
        """
    try:
        # 在更多页面
        poco(text='更多', name='com.eco.global.app:id/titleContent').exists()
    except:
        raise AssertionError("当前页面非更多主页面")
    # 获取更多列表中拖地水量的x,y轴坐标
    x, y = poco(text="拖地水量").get_position()
    # 非强效拖地模式下
    if not poco(text="强效拖地方式").exists():
        # 通过拖地水量在更多页面的列表中排行第二来获取列表中的值
        # 需要注意的是，更多的左边列表，是从index=1开始的
        if poco(name='com.eco.global.app:id/title')[2].get_text() == "拖地水量":
            log("拖地水量在更多页面中的显示位置正确")
            # 获取拖地水量的值
            __water_level__ = poco(name='com.eco.global.app:id/msg')[1].get_text()
            # 判断更多中左边第二个值（即拖地水量）和右边第二个值（即水量）是否在一个水平面
            if poco(text=__water_level__).get_position()[1] - y < 0.01:
                log("拖地水量的值为：" + __water_level__)
                return __water_level__
            else:
                raise Exception("拖地水量与其对应的水量值不对应")
        else:
            raise Exception("拖地水量在更多页面中的显示位置不正确")
    else:
        if poco(name='com.eco.global.app:id/title')[3].get_text() == "拖地水量":
            log("拖地水量在更多页面中的显示位置正确")
            # 获取拖地水量的值
            __water_level__ = poco(name='com.eco.global.app:id/msg')[2].get_text()
            # 判断更多中左边第二个值（即拖地水量）和右边第二个值（即水量）是否在一个水平面
            if poco(text=__water_level__).get_position()[1] - y < 0.01:
                log("拖地水量的值为：" + __water_level__)
                return __water_level__
            else:
                raise Exception("拖地水量与其对应的水量值不对应")
        else:
            raise Exception("拖地水量在更多页面中的显示位置不正确")
    

"""
函数的使用方法举例
"""
# if __name__ == "airtest.cli.runner":    
if __name__ == "__main__":    
    water_level= "高"
    # 更多到拖地水量
    more_to_wateryeild()
    sleep(3)
    # 设置拖地水量
    set_wateryeild_level(water_level)
    # 保存设置的拖地水量
    click_to_save_waterLevel()
    sleep(3)
    # 更多页面检查拖地水量 与 设置的拖地水量值 是否一致
    if get_wateryeild_level_from_more() == water_level:
        log("设置水量及更多页面检查设置水量成功")










