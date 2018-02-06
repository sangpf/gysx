# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.
class ProjectManager(models.Manager):
    # def get_queryset(self):
    #     return super(ProjectManager,self).get_queryset().filter(invId != None)
    def addProject(cls,invId,title,summary,client,responsibility,comment,type,status,cTime,bTime,eTime):
        project = cls.model()
        project.invId = invId
        project.title = title
        project.summary = summary
        project.client = client
        project.responsibility = responsibility
        project.comment = comment
        project.type = type
        project.status = status
        project.cTime = cTime
        project.bTime = bTime
        project.eTime = eTime
        return project

class Project(models.Model):
    invId = models.IntegerField(default= None)
    title = models.CharField(max_length = 100) #项目标题
    summary = models.CharField(max_length = 100) #项目简介
    client = models.CharField(max_length = 200) #委托单位
    responsibility = models.CharField(max_length = 200) #项目负责人
    type = models.IntegerField(default = None)
    status = models.IntegerField(default = None)
    cTime = models.DateTimeField(db_column='cTime')
    bTime = models.DateTimeField(db_column='bTime')
    eTime = models.DateTimeField(db_column='eTime')
    comment = models.CharField(max_length = 200)

    # 自定义管理器
    projectManager = ProjectManager()
    # 默认管理器
    objects = models.Manager()

    class Meta:
        db_table = 'project'

# class BookInfo(models.Model):
#     btitle=models.CharField(max_length=20)
#     bpub_date=models.DateTimeField(db_column='pub_date')
#     bread=models.IntegerField(default=0)
#     bcommet=models.IntegerField(null=False)
#     isDelete=models.BooleanField(default=False)
#     class Meta:
#         db_table='bookinfo'

# Id	int	10
# invId	int	10
# title	varchar	200
# type	tinyint	2
# cTime	TIMESTAMP	6
# bTime	TIMESTAMP	6
# eTime	TIMESTAMP	6
# status	tinyint	2
# summary	varchar	200
# client	varchar	100
# responsibility	varchar	100
# comment	varchar	100


