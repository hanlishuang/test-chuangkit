# conding=utf-8
import json

import requests


# 定义一个方法，传入需要的参数url和data
class Runmian:
    def send_post(url=None, data=None):
        """
        post 方法封装
        :param url:
        :param data:
        :return:
        """
        # 参数必须按照url，data的顺序传入
        # 这里是封装url和data，所以值不能写死
        result = requests.post(url=url, data=data).json()
        res = json.dump(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res


    def send_get(url=None, data=None):
        """
        get 方法封装
        :param url:
        :param data:
        :return:
        """
        result = requests.get(url=url, data=data)
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res


    def run_main(self, method, url=None, data=None):
        result = None
        if method == 'post':
            result = self.send_post(url, data)
        elif method == 'get':
            result = self.send_get(url, data)
        else:
            print("错误")
            return result
if __name__=='__mian__':
    url='http://www.baidu/com'
    res=Runmian.send_get("get",url)
    print(res)
