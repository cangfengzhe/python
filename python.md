## python学习

### 修改编码方式

```python
#! /usr/bin/env python 
# -*- coding: utf-8 -*- 
import sys 
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入 
sys.setdefaultencoding('utf-8') 
```
