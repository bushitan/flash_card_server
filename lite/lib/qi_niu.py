# -*- coding: utf-8 -*-
from django.http import HttpResponse
# import qiniu
import qiniu


from  flash_card_server.settings  import *
from flash_card_server.settings import (QINIU_ACCESS_KEY,
                                 QINIU_SECRET_KEY,
                                 QINIU_BUCKET_NAME)

assert QINIU_ACCESS_KEY and QINIU_SECRET_KEY and QINIU_BUCKET_NAME
import sys
import os
import logging
# logger
logger = logging.getLogger(__name__)

class QiNiu():
    def getToken(self,file_name):
        q = qiniu.Auth(QINIU_ACCESS_KEY, QINIU_SECRET_KEY)
        key = file_name
        policy = {
            "callbackUrl":QINIU_CALLBACK_URL,
            "callbackBody":QINIU_CALLBACK_BODY,
            "callbackHost":QINIU_CALLBACK_HOST,
            "fsizeLimit": QINIU_FSIZE_LIMIT,
        }
        token = q.upload_token(QINIU_BUCKET_NAME,key = key,policy = policy)
        return token,key

    def delete(self,key):
        # try:
            #初始化Auth状态
        q = qiniu.Auth(QINIU_ACCESS_KEY, QINIU_SECRET_KEY)
        #初始化BucketManager
        bucket = qiniu.BucketManager(q)
        #删除bucket_name 中的文件 key  #你要测试的空间， 并且这个key在你空间中存在
        ret, info = bucket.delete(QINIU_BUCKET_NAME, key)
        print(info)
            # return True
        # except Exception as e:
        #     print 'error',e
        #     return False


# policy = {
#     # "callbackUrl":"http://120.27.97.33/upload/token/",
#     "callbackUrl":"https://www.12xiong.top/upload/token/",
#     "callbackBody":"key=$(key)&hash=$(etag)&w=$(imageInfo.width)&h=$(imageInfo.height)&duration=$(avinfo.video.duration)&fsize=$(fsize)&vw=$(avinfo.video.width)&vh=$(avinfo.video.height)",
#     "callbackHost":"120.27.97.33",
#     "fsizeLimit": 6815744,
#     # "mimeLimit": "image/png"
# }