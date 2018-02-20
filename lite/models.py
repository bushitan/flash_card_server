#coding:utf-8
from django.db import models

from lite.lib.util import *

# Create your models here.
IDENTIFY_STATUS = {
    0: u"未提交",
    1: u'已提交',
    2: u'审核不通过',
    3: u'审核通过',
}
class User(models.Model):
    # models.ImageField()
    logo = models.CharField(max_length=300, verbose_name=u'logo链接',default="",null=True,blank=True)
    # logo = models.ImageField(max_length=150, verbose_name=u'logo链接',null=True,blank=True)
    name =  models.CharField(max_length=100, verbose_name=u'名称',null=True,blank=True)
    nick_name =  models.CharField(max_length=100, verbose_name=u'微信昵称',null=True,blank=True)
    wx_id =  models.CharField(max_length=100, verbose_name=u'微信号',null=True,blank=True)

    wx_open_id = models.CharField(max_length=50, verbose_name=u'微信OpenID',null=True,blank=True)
    wx_session_key = models.CharField( max_length=128,verbose_name=u'微信SessionKey',null=True,blank=True)
    wx_expires_in = models.FloatField( verbose_name=u'微信SessionKey过期时间',null=True,blank=True)
    session = models.CharField (max_length=128, verbose_name=u'Django的session',null=True,blank=True)
    expires = models.FloatField( verbose_name=u'Django的session过期时间',null=True,blank=True)
    uuid =  models.CharField(max_length=32, verbose_name=u'uuid标识',null=True,blank=True)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True,null=True,blank=True)

    phone = models.CharField(max_length=40, verbose_name=u'手机',null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'用户_基本信息'
        # app_label = string_with_title(u'api', u"23421接口")

    def __unicode__(self):
        return '%s' % (self.id)



import django.utils.timezone as timezone
class Image(models.Model):
    user = models.ForeignKey(User,verbose_name=u'用户',null=True,blank=True)
    # file_name =  models.CharField(max_length=50, verbose_name=u'图片名称',null=True,blank=True)
    url = models.CharField(max_length=300, verbose_name=u'地址',default="",null=True,blank=True)
    # content =  models.CharField(max_length=1000, verbose_name=u'内容',null=True,blank=True)
    # style = models.IntegerField(u'类型',default=IMAGE,choices=FILE_STYLE.items())
    create_time = models.DateTimeField(u'创建时间',default = timezone.now,null=True,blank=True)

    class Meta:
        verbose_name_plural = verbose_name = u'图片'
    def __unicode__(self):
        return '%s' % (self.id)

class Tag(models.Model):
    user = models.ForeignKey(User,verbose_name=u'用户',null=True,blank=True)
    name =  models.CharField(max_length=100, verbose_name=u'名称',null=True,blank=True)

    class Meta:
        verbose_name_plural = verbose_name = u'标签'
    def __unicode__(self):
        return '%s' % (self.id)



class Card(models.Model):
    user = models.ForeignKey(User,verbose_name=u'用户',null=True,blank=True)
    tag = models.ForeignKey(Tag,verbose_name=u'标签',null=True,blank=True)

    level = models.IntegerField(u'背面类型',default=STRANGER,choices=LEVEL.items())

    face_title =  models.TextField(max_length=50, verbose_name=u'正面生词',null=True,blank=True)

    back_style = models.IntegerField(u'背面类型',default=IMAGE,choices=BACK_STYLE.items())
    back_summary =  models.CharField(max_length=50, verbose_name=u'背面摘要',null=True,blank=True)
    back_explain =  models.TextField(max_length=50, verbose_name=u'背面解释',null=True,blank=True)
    back_image = models.ForeignKey(Image,verbose_name=u'图片',null=True,blank=True)

    create_time = models.DateTimeField(u'创建时间',default = timezone.now,null=True,blank=True)

    class Meta:
        verbose_name_plural = verbose_name = u'单词卡'
        ordering = ['-create_time']
    def __unicode__(self):
        return '%s' % (self.id)
















