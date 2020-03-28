通过调用第三方接口<超级鹰>智能识别登陆页面验证码
utils/chaojiying.py

1、通过获取登陆页面验证码img标签的src
2、通过 urllib.request 将图片保存到本地目录
    data\cjy_get_code\get_current_code.jpg
3、通过超级鹰读取本地存储图片进行识别