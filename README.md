### 1. 首先命令行运行以下代码
知乎有检测机制，运行以下代码可以躲避。  
第一个路径为Chrome浏览器的地址，可以右击桌面快捷方式查看
第二个路径为临时文件保存地址，随便创建一个。
```shell
cd C:/Program Files/Google/Chrome/Application
chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/Users/caka/Desktop/chromedriver"
```
### 2. 将代码中chromedriver的路径替换成自己的路径，若没有，百度，下载对应版本
```python
service = Service(r'C:\Users\caka\Desktop\文件\chromedriver.exe')
```
### 3. 将代码中目标url替换，改成自己想要爬的问题的url，可以在知乎网站地址看到
```python
url = 'https://www.zhihu.com/question/404870865'
```
### 4. 运行代码