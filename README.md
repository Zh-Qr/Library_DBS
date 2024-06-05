# Library_DBS

本项目作为数据库系统课程作业，在此感谢朱老师的教导！
本次实验采用Python开发语言与Mysql数据库相结合。前端开发使用ui设计，使用QtDesigner设计工具。本系统除完成常规图书管理系统的MySQl数据库、后端逻辑系统、前端UI设计外，还考虑到了数据的冲突解决、数据的备份保护、用户的使用体验等。
MYSQL、Python 3.8、Qt Designer
程序建议运行在Windows 10 系统。

## 建造本地数据库内容
环境准备：
```
pip install -r requirements.txt
```
具体数据库用户名、密码根据情况设定
```
db = pymysql.connect(host='localhost',
port=3306,
user='root',
passwd='123456',
charset='utf8')
```
建立database和需要的table等
```
python construct.py
```

## 项目执行
### 后端测试项目
```
python main.py
```
### 综合系统运行测试
```
cd ui
python page1.py
```

## 项目介绍
### 数据库结构
![借阅表](https://github.com/Zh-Qr/Library_DBS/blob/main/%E5%9B%BE%E7%89%87/%E5%80%9F%E9%98%85%E8%A1%A8.png)
![学生表](https://github.com/Zh-Qr/Library_DBS/blob/main/%E5%9B%BE%E7%89%87/%E5%AD%A6%E7%94%9F%E8%A1%A8.png)
![管理员表](https://github.com/Zh-Qr/Library_DBS/blob/main/%E5%9B%BE%E7%89%87/%E7%AE%A1%E7%90%86%E5%91%98%E8%A1%A8.png)
![书籍表](https://github.com/Zh-Qr/Library_DBS/blob/main/%E5%9B%BE%E7%89%87/%E4%B9%A6%E7%B1%8D%E8%A1%A8.png)
![数据库内容](https://github.com/Zh-Qr/Library_DBS/blob/main/%E5%9B%BE%E7%89%87/%E6%95%B0%E6%8D%AE%E5%BA%93%E5%86%85%E5%AE%B9.png)
管理员待定表、用户待定表结构和管理员表、用户表相同

### 前端设计
![管理员、用户登录界面框架](https://github.com/Zh-Qr/Library_DBS/blob/main/%E5%9B%BE%E7%89%87/%E7%AE%A1%E7%90%86%E5%91%98%E3%80%81%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95%E7%95%8C%E9%9D%A2%E6%A1%86%E6%9E%B6.png)
![管理员操作框架图](https://github.com/Zh-Qr/Library_DBS/blob/main/%E5%9B%BE%E7%89%87/%E7%AE%A1%E7%90%86%E5%91%98%E6%93%8D%E4%BD%9C%E6%A1%86%E6%9E%B6%E5%9B%BE.png)
![用户操作框架](https://github.com/Zh-Qr/Library_DBS/blob/main/%E5%9B%BE%E7%89%87/%E7%94%A8%E6%88%B7%E6%93%8D%E4%BD%9C%E6%A1%86%E6%9E%B6.png)
![用户借阅界面](https://github.com/Zh-Qr/Library_DBS/blob/main/%E5%9B%BE%E7%89%87/%E7%94%A8%E6%88%B7%E5%80%9F%E9%98%85%E7%95%8C%E9%9D%A2.png)

### 前端、后端交互逻辑
这里以访问借阅表为例，展示前后端链接的操作逻辑
![访问数据库获取数据流程图](https://github.com/Zh-Qr/Library_DBS/blob/main/%E5%9B%BE%E7%89%87/%E8%AE%BF%E9%97%AE%E6%95%B0%E6%8D%AE%E5%BA%93%E8%8E%B7%E5%8F%96%E6%95%B0%E6%8D%AE%E6%B5%81%E7%A8%8B%E5%9B%BE.png)

### 主要功能简述
![主要功能](https://github.com/Zh-Qr/Library_DBS/blob/main/%E5%9B%BE%E7%89%87/%E4%B8%BB%E8%A6%81%E5%8A%9F%E8%83%BD.png)
![添加书籍界面](https://github.com/Zh-Qr/Library_DBS/blob/main/%E5%9B%BE%E7%89%87/%E6%B7%BB%E5%8A%A0%E4%B9%A6%E7%B1%8D%E7%95%8C%E9%9D%A2.png)
![修改书籍信息（或者删除）界面](https://github.com/Zh-Qr/Library_DBS/blob/main/%E5%9B%BE%E7%89%87/%E4%BF%AE%E6%94%B9%E4%B9%A6%E7%B1%8D%E4%BF%A1%E6%81%AF%E7%95%8C%E9%9D%A2.png)
![管理员申请、审核流程](https://github.com/Zh-Qr/Library_DBS/blob/main/%E5%9B%BE%E7%89%87/%E7%AE%A1%E7%90%86%E5%91%98%E7%94%B3%E8%AF%B7%E3%80%81%E5%AE%A1%E6%A0%B8%E6%B5%81%E7%A8%8B.png)
![借阅书籍界面](https://github.com/Zh-Qr/Library_DBS/blob/main/%E5%9B%BE%E7%89%87/%E5%80%9F%E9%98%85%E4%B9%A6%E7%B1%8D%E7%95%8C%E9%9D%A2.png)
![书籍归还操作](https://github.com/Zh-Qr/Library_DBS/blob/main/%E5%9B%BE%E7%89%87/%E4%B9%A6%E7%B1%8D%E5%BD%92%E8%BF%98%E6%93%8D%E4%BD%9C.png)
