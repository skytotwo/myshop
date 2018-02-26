## MyShop
基于Django快速搭建网上商店,演示地址http://39.108.95.135/

### 环境要求
Python 3.4+
Django 2.0

### 主要功能
- 商品分类
- 购物车 (基于django sessions实现)
- 付款功能
- 邮件通知 (基于Celery,RabbitMQ异步实现)
- 导出订单生成csv文件
- 简易商品推荐引擎 (基于redis实现)

### 下载与安装
1. 拉取代码  
  `git clone https://github.com/ybcc2015/myshop.git`
2. 安装项目依赖  
  `pip install -r requirements`
3. 生成数据库  
  `python manage.py migrate`
4. 创建超级用户  
  `python manage.py createsuperuser`
5. 安装并启动redis  
  `sudo apt-get update`  
  `sudo apt-get install redis-server`  
  `sudo /etc/init.d/redis-server start`  
6. 启动项目  
  `python manage.py runserver`

最后浏览器中打开http://127.0.0.1:8000/ 即可访问

### 预览
- 首页  
![](https://github.com/ybcc2015/myshop/blob/master/screen_shot/index.png)  
- 商品详情页  
![](https://github.com/ybcc2015/myshop/blob/master/screen_shot/detail.png)
- 购物车  
![](https://github.com/ybcc2015/myshop/blob/master/screen_shot/cart.png)  
- 付款页  
![](https://github.com/ybcc2015/myshop/blob/master/screen_shot/payment.png)
