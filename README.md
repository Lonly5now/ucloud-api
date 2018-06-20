# UCloud-API Script



## API 请求结构


Name | Description | Notes
-      | :- | :- 
API调用地址 | 调用API的webservice入口 | http(s)://api.ucloud.cn
公共参数    | 调用API时需要给出的公共参数 | 参见 [公共参数列表](https://docs.ucloud.cn/api/summary/public)
API指令    | 即API指令名称，如 DescribeUhostInstance | 参见 [API指令列表](https://docs.ucloud.cn/api/index)
指令参数 | 执行每个指令时所需要提供的参数 |	参见 [API指令列表](https://docs.ucloud.cn/api/index)

via https://docs.ucloud.cn/api/summary/overview

---

## 公共参数获取

*PublicKey = ''*

*PrivateKey = ''*

获取地址：
https://console.ucloud.cn/apikey


*ProjectId = ''*

获取地址：https://console.ucloud.cn/dashboard
![](http://p81vbqgtm.bkt.clouddn.com/18-6-20/46709715.jpg)



地域和可用区列表：https://docs.ucloud.cn/api/summary/regionlist


## ucloudapi_general.py

#### 填写对应的公共参数

![](http://p81vbqgtm.bkt.clouddn.com/18-6-20/62146115.jpg)


#### 填写对应的API指令和指令参数
（其中必选参数需要全部填写完整）

![](http://p81vbqgtm.bkt.clouddn.com/18-6-20/94600411.jpg)

#### Demo

获取北京2D机房所有云主机的信息: [API](https://docs.ucloud.cn/api/uhost-api/describe_uhost_instance)

![](http://p81vbqgtm.bkt.clouddn.com/18-6-20/17904959.jpg)



## ucloudapi_url.py

公共参数和ucloudapi_general.py一致


#### Demo
获取api请求的url：

![](http://p81vbqgtm.bkt.clouddn.com/18-6-20/14218682.jpg)

红框中为请求的得到的请求url，**Signature=xxx**为计算出的签名 