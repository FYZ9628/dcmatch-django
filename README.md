# dcmatch-django


idea项目：https://github.com/FYZ9628/dcmatch

webstorm项目：https://github.com/FYZ9628/dcmatch-vue

pycharm项目：https://github.com/FYZ9628/dcmatch-django

学科竞赛赛程管理信息系统

本项目是我的本科毕业设计项目《学科竞赛赛程管理信息系统》，该系统采用了前后端完全分离的开发方法开发本系统，系统最开始是只做了java版的后端，后来因为对python比较感兴趣，于是花了一些时间做了一个python的后端，复用了前端，使用python版的后端可能有些功能会有一些bug，如有发现bug可看看java版的后端，也可私信我。使用到的技术有：

一、后端技术

1、java版

（1）SpringBoot

（2）JPA（Hibernate）

（3）MySQL


2、python版

（1）Django

（2）Django's ORM

（3）MySQL


二、前端技术

1、Vue.js

2、Element UI

3、Axios


三、版本信息

1、后端

（1）、java版

开发工具：idea（IntelliJ IDEA），2019年1月份发布的版本（切记不要用更高版本的工具，减少出现bug的可能）

框架：SpringBoot（版本：2.1.6.RELEASE）

（2）python版

开发工具：PyCharm，2019年1月份发布的版本（切记不要用更高版本的工具，减少出现bug的可能）

框架：Django（版本：3.0.5）

PyMySQL：0.9.3

Pip：19.0.3


2、前端

vue：2.5.2

vuex：3.1.2

axios：0.19.1

element – ui：2.13.0


四、项目分析

1、用户分析

系统的角色有：举办方、教师、学生、未认证用户、管理员。
 

2、各个角色的主要功能

（1）、举办方：通知发布、通知管理、竞赛发布、竞赛管理、报名名单管理、获奖名单管理、数据分析。
 

（2）、教师：查看通知、查看竞赛、竞赛报名、报名管理、获奖管理
 


（3）、学生：查看通知、查看竞赛、竞赛报名、报名管理、获奖管理
 


（4）、未认证用户：查看通知、查看竞赛、认证
 

（5）、管理员：认证管理、用户管理、竞赛管理、报名管理
