# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models        #所有的django模型必须继承自他

KIND_CHOICES= (
    ('Python技术', 'Python技术'),
    ('ASP.NET技术', 'ASP.NET技术'),
    
)


# Create your models here.
class Moment(models.Model):     #定义子类
    """
    """
    # 保存消息的内容
    content=models.CharField(max_length=200)
    # 发布人的名字
    user_name=models.CharField(max_length=20,default='匿名')
    # 消息的类型
    # kind=models.CharField(max_length=20)
    kind=models.CharField(max_length=20,choices=KIND_CHOICES,default=KIND_CHOICES[0])