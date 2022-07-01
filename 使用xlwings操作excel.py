import xlwings
import os
app = xlwings.App(visible=False)

filePath = 'D:\python\py22\袁老板'
lists = os.listdir(filePath)
for path in lists:
    path_xl = f"{filePath}\{path}"
    wt = app.books.open(path_xl)
    sheet = wt.sheets[0]
    sheet.api.Rows(1).Insert()
    wt.save()
    wt.close()


# 加载excel文件
#
#
# # 加载第一个sheet页签
# sheet = wt.sheets[0]
#
#
# sheet.api.Rows(1).Insert()
#
# wt.save()
# # 释放资源，不然脚本无法打开，会处于锁定状态。
# wt.close()

