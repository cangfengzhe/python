## python学习

### 修改编码方式,适用于 2.7

```python
#! /usr/bin/env python 
# -*- coding: utf-8 -*- 
import sys 
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入 
sys.setdefaultencoding('utf-8') 
```


---------
以下为python 3.4版本

### 数据库导出csv

```
imporr sqlite3, csv, codecs  

con = sqlite3.connect('filename')
cu = con.cursonr() # 获取cursor
cu.execute('select * from shop_list') # 执行
data = cu.fetchall() # 获得全部数据

# 列名
colnames = ['shopId', 'shopLogo' , 'shopMaster','shopName', 'shopSn', 'shopTotalGoods']
#            'goodsId' , 'appointmentedStatus' , 'goodsInfo' , 'shopId' , 'title' , 'goodsMaterialId' , 'goodsSn' , 'goodsTypeId' , 'has_cert' ,'isAppointmented' , 'isConcern' , 'isRecommended' ,'isimplant' , 'orderStatus' , 'price', 'priceRangeName' , 'quantity' , 'goodPattern', 'goodPatternId' , 'goodsCateId', 'goodsCateName']
# 先打开文件，写入codecs.BOM_UTF8后关闭，然后追加csv
csvfile = open('商家信息.csv', 'wb')  
csvfile.write(codecs.BOM_UTF8)
csvfile.close()

csvfile = open('商家信息.csv', 'a', encoding = 'utf-8')  
writers = csv.writer(csvfile) 
writers.writerow(colnames)

for line in data:
    writers.writerow(line)
csvfile.close()

```