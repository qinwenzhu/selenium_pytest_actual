# Selenium Pytest Actual（Selenium + Pytest）

## 准备环境 (python 3.7.4)

```s
pip install -r requirements.txt

# If timeout, use command below
# 
# 清华：https://pypi.tuna.tsinghua.edu.cn/simple
# 阿里云：http://mirrors.aliyun.com/pypi/simple/
# 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
# 华中理工大学：http://pypi.hustunique.com/
# 山东理工大学：http://pypi.sdutlinux.org/
# 豆瓣：http://pypi.douban.com/simple/

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

```

## 目录结构

```s
├─guard: Guard项目
│  ├─config: 测试服务器相关配置文件
│  ├─data: 测试数据
│  ├─pages: web功能模块页面
│  │  └─components: 封装的重用性高的模块组件
│  ├─tests: 测试用例
│  └─tools: 封装的常用工具方法
├─outputs: 测试报告
|  ├─allure: allure格式的测试报告
|  ├─html: html格式的测试报告
|  ├─logs: 脚本输出日志
|  ├─web_screenshot: 错误界面截图
└─utils: 基础工具类
```

## 执行用例

```s
# 无浏览器模式
pytest --headless

# 带标签模式
pytest guard/tests/*/test_*.py -v -m "webtest" --html=report/report.html --host=10.151.3.96 --maxfail=2 --pdb -s

# 指定浏览器模式
pytest guard/tests/module/test_portrait.py --html=report/report.html --host=10.151.3.96 --browser=(choose from 'chrome', 'edge', 'firefox', 'ie', 'opera', 'phantomjs', 'safari', 'android', 'iphone', 'ipad', 'remote')
```

## Chromedriver

* 在Chrome浏览器地址栏中输入“chrome://version/”进行版本查看
* 访问http://chromedriver.storage.googleapis.com/index.html下载对应chromedriver