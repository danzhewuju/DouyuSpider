# DouyuSpider
1.程序利用beautifulsoup 对斗鱼连接的解析，获取到直播室的基本信息，然后将信息写入到数据库。

2.完善了算法，获取了斗鱼所有直播间的信息

3.统计数据：斗鱼直播类型：总计598个类型

4.完善了算法获取了斗鱼所有直播间的信息，直接运行DouyuSpiderV2.py文件即可。





运行库：

pip install requests

pip install lxml

pip install BeautifulSoup4

pip install pymysql


运行时长：60mins

注：如果你使用的是公网ip,斗鱼可能会对你进行IP封锁.如果使用内网ip，才能全部抓取。
如果你是公网ip用户，强烈建议你使用ip代理。

##**release**

我已经将程序编译成为了exe文件，也就是说你可以直接在windows下直接运行而不用安装相关依赖，你只需在本机安装了mysql数据库

运行步骤:

1.安装mysql(已安装忽略)

2.运行DouyuSpiderV2.exe  然后分别在doc下输入你mysql的用户名以及密码，程序就开始自动爬取斗鱼的直播间信息。
