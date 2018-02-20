# -*- coding: utf-8 -*-


from django.conf.urls import url
from lite.views import *



urlpatterns = [

    url(r'^card/all/$', CardGetAll.as_view()),
    url(r'^my/example/$', MyExample.as_view()),



    #365天初始化
    # url(r'^day/index/$', DayIndex.as_view()),

    #我的初始化
    url(r'^my/index/$', MyIndex.as_view()),
    url(r'^my/set/clock/$', MySetClock.as_view()),
    url(r'^my/set/logo/$', MySetLogo.as_view()),

    #上传文件
    url(r'^upload/get/token/$', UploadGetToken.as_view()),
    url(r'^upload/callback/$', UploadCallback.as_view()),
    #
    # #用户登录
    # url(r'^user/login/$', UserLogin.as_view()),

    # 闪卡
    url(r'^user/login/$', UserLogin.as_view()),

    url(r'^card/add/char$', CardAddChar.as_view()),
    url(r'^card/get_list/$', CardGetListByUserID.as_view()),
    url(r'^card/set/level_id/$', CardSetByLevelID.as_view()),
    url(r'^card/set/tag_id/$', CardSetByTagID.as_view()),

    url(r'^tag/add/$', TagAdd.as_view()),
    # url(r'^tag/delete/$', TagAdd.as_view()),
    # url(r'^tag/get_list/$', TagAdd.as_view()),
    # url(r'^tag/update/$', TagAdd.as_view()),
]