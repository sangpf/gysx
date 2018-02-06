# -*- coding: UTF-8 -*-
from django.db import models,connection

class UserManager(models.Manager):
    def get_queryset(self):
        return super(UserManager,self).get_queryset().filter(isValid = 0)

    def addUser(cls,name,wxAccounts,wxName,account,telephone,ugender,uhobby):
        user = cls.model()
        user.name = name
        user.wxAccounts = wxAccounts
        user.wxName = wxName
        user.account = account
        user.telephone = telephone
        user.ugender = ugender
        user.uhobby = uhobby
        return user

class User(models.Model):
    # id
    wxAccounts = models.CharField(max_length = 20)
    wxName = models.CharField(max_length = 20)
    account = models.CharField(max_length = 20)
    passWord = models.CharField(max_length = 20)
    role = models.IntegerField(default=0)
    name = models.CharField(max_length = 20)
    img = models.CharField(max_length = 200)
    gender = models.IntegerField(default=0)
    identity = models.CharField(max_length = 20)
    bankCard = models.CharField(max_length = 50)
    station = models.IntegerField(default=0)
    telephone = models.CharField(max_length = 20)
    isValid = models.IntegerField(default=1)
    comment = models.CharField(max_length = 20)

    class Meta:
        db_table = 'investigator'

    # 默认管理器
    objects = models.Manager()  # The default manager.
    # 自定义管理器
    userManager = UserManager()

    @classmethod
    def addUser(cls,wxAccounts,wxName,account):
        user = cls(wxAccounts = wxAccounts, wxName = wxName, account = account)
        user.passWord = 123456
        user.telephone = 188789
        return user


