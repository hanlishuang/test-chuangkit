class common:
    #初始化driver
    def __init__(self,driver):
        """解决driver问题"""
        self.driver=driver
    #查找方法封装
    def ommon_find(self):
        self.driver.find_element()
    #输入方法封装
    def common_input(self):
        pass
    #点击方法封装
    def common_click(self):
        pass
    #获取元素文本
    def common_get_text(self):
        pass