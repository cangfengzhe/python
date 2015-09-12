
# coding: utf-8

# In[1]:

import logging
'''
封装一个log包，方便今后使用
'''

def log(file_name, logger_name = 'root'):
    logger=logging.getLogger(logger_name)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    handler=logging.FileHandler(file_name)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.NOTSET)
    return logger

if __name__ == '__main__':
    logger = log('test.log')
    logger.error('this is error')
    logger.warning('this is warning')


# In[ ]:



