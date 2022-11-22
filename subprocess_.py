# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-22 11:14:05
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-22 12:43:05
# @ windows 下殺程式


# from subprocess import check_output
# from os import system
# for line in check_output("tasklist").splitlines():
#     # chrome 這裡可以換成關鍵字，要看一下ngrok process是甚麼
#     if (v:=line.split()) and 'chrome' in str(v[0]):
#         system(f'taskkill /f /im {v[0].decode("utf-8")}')
        
from subprocess import check_output
from os import system
target = 'chrome' #篩選用keyword
while target in str(process:=check_output(f'tasklist /FI "IMAGENAME eq {target}*"')): 
#這段用powershell script篩chrome的exe，才不會花太多時間在for些無關的東西
#while不到就出圈，while到就for下去關第一個process，關到就break to while check
#下面for到就出圈，for以第三行開始可參考下圖
    for item in process.splitlines()[3:]:
        if (v:=item.split()) and target in str(v[0]):
            system(f'taskkill /f /im {v[0].decode("utf-8")}')
            break