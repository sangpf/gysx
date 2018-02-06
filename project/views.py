# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from .models import *
import time

# Create your views here.

# 跳转到添加项目测试页面
def add_project_page(request):
    return render(request, 'project/addProject.html')

# 添加项目
def add_project(request):
    invId = request.POST['invId']
    title = request.POST['title']
    summary = request.POST['summary']
    client = request.POST['client']
    responsibility = request.POST['responsibility']
    # comment = request.POST['comment']
    type = request.POST['type']
    status = request.POST['status']
    # localtime = time.asctime(time.localtime(time.time()))
    # 格式化成2016-03-20 11:45:39形式
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    cTime = localtime
    bTime = localtime
    eTime = localtime

    add_project = Project.projectManager.addProject(invId, title, summary, client, responsibility,'haha',
                                                    type, status,cTime ,bTime, eTime)
    add_project.save()
    return HttpResponse('success ')

# 项目列表查询
def list_project(request):
    # id = request.GET['id']
    # title = request.GET['title']
    # title = request.GET.get('title','title default')  # 有默认值
    id = request.GET.get('id')
    title = request.GET.get('title')

    project_list = Project.objects.all()
    if id != None:
        project_list = project_list.filter(invId__exact=id)
    if title != None:
        project_list = project_list.filter(title = title)

    # project_list = Project.objects.filter(invId__exact=id).filter(title=title)
    project_list_serialize = serializers.serialize('json', project_list)
    return HttpResponse(project_list_serialize)
    # context = {'id':id, 'title':title}
    # return JsonResponse(context)

# 修改
def update_project(request):
    context = {'success': False, 'msg': 'error msg'}
    id = request.POST.get('id')
    invId = request.POST.get('invId')
    title = request.POST.get('title')
    summary = request.POST.get('summary')
    client = request.POST.get('client')
    responsibility = request.POST.get('responsibility')
    type = request.POST.get('type')
    status = request.POST.get('status')
    if id == None:
        context['msg'] = 'no id error '
        return JsonResponse(context)
    objects_filter = Project.objects.filter(pk=id)
    try:
        if invId != None:
            objects_filter.update(invId=invId)
        if title != None:
            objects_filter.update(title=title)
        if summary != None:
            objects_filter.update(summary=summary)
        if client != None:
            objects_filter.update(client=client)
        if responsibility != None:
            objects_filter.update(responsibility=responsibility)
        if type != None:
            objects_filter.update(type=type)
        if status != None:
            objects_filter.update(status=status)
    except Exception as e:
        print (e)
        context['msg'] = 'exception happen'
        return JsonResponse(context)
    context['success'] = True
    context['msg'] = 'success'
    return JsonResponse(context)

# 根据id查询一个
def get_project_id(request):
    context = {'success': False, 'msg': 'error msg'}
    id = request.GET.get('id')
    if id == None:
        context['msg'] = 'get id is null'
        return JsonResponse(context)
    project = Project.objects.get(pk=id)
    data = {}
    data['id'] = project.id
    data['invId'] = project.invId
    data['title'] = project.title
    data['summary'] = project.summary
    data['responsibility'] = project.responsibility
    data['type'] = project.type
    data['client'] = project.client
    data['status'] = project.status
    # 返回页面渲染数据
    return render(request, 'project/addProject.html', data)
    # 返回json格式数据
    # context['success'] = True
    # context['msg'] = 'success'
    # context['data'] = data
    # return JsonResponse(context)


