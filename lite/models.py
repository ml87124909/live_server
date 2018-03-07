#coding:utf-8
from django.db import models
from lib.util import *
# Create your models here.
import django.utils.timezone as timezone
from lib.image_save import *

#企业信息
class Lite(models.Model):
    app_id =  models.CharField(max_length=100, verbose_name=u'AppID',null=True,blank=True)
    secret_key = models.CharField(max_length=100, verbose_name=u'SecretKey',null=True,blank=True)

    class Meta:
        verbose_name_plural = verbose_name = u'机构展示信息'

    def __unicode__(self):
        return '%s' % (self.name)

#7 图片库
class FileLibrary(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'名称',null=True,blank=True)
    url = models.CharField(max_length=1000, verbose_name=u'云地址',null=True,blank=True)
    style = models.IntegerField(u'类别',default=IMAGE_COVER,choices=IMAGE_STYLE.items(),)
    local_path = models.ImageField(u'图标',upload_to='static/img/')
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    class Meta:
        verbose_name_plural = verbose_name = u'图库'

    def __unicode__(self):
        return '%s' % (self.id)

    def save(self):
        ImageSave(self,FileLibrary)


class User(models.Model):
    # models.ImageField()
    app =  models.ForeignKey( Lite, verbose_name=u'所属小程序',null=True,blank=True)
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
    create_time = models.DateTimeField(u'创建时间',default = timezone.now,null=True,blank=True)

    phone = models.CharField(max_length=40, verbose_name=u'手机',null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'用户_基本信息'
        # app_label = string_with_title(u'api', u"23421接口")

    def __unicode__(self):
        return '%s' % (self.id)

#企业信息
class Company(models.Model):
    name =  models.CharField(max_length=100, verbose_name=u'名称',null=True,blank=True)
    phone = models.CharField(max_length=40, verbose_name=u'手机',null=True,blank=True)
    introduction = models.CharField(max_length=500, verbose_name=u'个人简介',default="",null=True,blank=True)
    address = models.CharField(max_length=200, verbose_name=u'地址',default="",null=True,blank=True)
    latitude = models.FloatField(verbose_name=u'精度',default=0)
    longitude = models.FloatField(verbose_name=u'维度',default=0)
    class Meta:
        verbose_name_plural = verbose_name = u'机构展示信息'

    def __unicode__(self):
        return '%s' % (self.name)
