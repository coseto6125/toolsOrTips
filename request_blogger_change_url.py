# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-22 12:42:31
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-22 12:42:33

import requests
from re import findall
s1 = requests.get('https://theqatest.blogspot.com/2022/11/python-post-sample.html')[0]
# 這邊用re去篩出轉址的網址
newUrl = findall('<meta content="0;url=(.*)" http',s1.text)
# 拿到s2.text看要再用甚麼keyword去判定有沒有連到jenkins
s2 = requests.get(newUrl) #這個url目前是導向jira(隨便設的)