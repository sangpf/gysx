# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from django.core import serializers

def index(request):
    return HttpResponse(request.path)

def detail(request,p1,p2,p3):
    return HttpResponse('year:%s, month:%s , day:%s'%(p1,p2,p3))

def getTest1(request):
    return render(request,'booktest/getTest1.html')

# get提交，接收1键1值
def getTest2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a':a1,'b':b1,'c':c1}
    return render(request,'booktest/getTest2.html',context)

# get提交，接收1键多值
def getTest3(request):
    a_list = request.GET.getlist('a')
    context = {'a_list':a_list}
    return render(request,'booktest/getTest3.html',context)

# 跳转到post信息录入页面
def postTest1(request):
    return render(request,'booktest/postTest1.html')

# postt提交
def postTest2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST.get('ugender')
    uhobby = request.POST.getlist('uhobby')
    context = {'uname':uname, 'upwd':upwd, 'ugender':ugender, 'uhobby':uhobby}
    return render(request,'booktest/postTest2.html',context)

# 跳转到添加user页面
def add_user_page(request):
    return render(request,'user/addUser.html')

# 保存user
def add_user(request):
    name = request.POST['name']
    wxAccounts = request.POST['wxAccounts']
    wxName = request.POST['wxName']
    telephone = request.POST['telephone']
    ugender = request.POST['ugender']
    uhobby = request.POST['uhobby']
    account = 465
    user = User.userManager.addUser(name,wxAccounts,wxName,account,telephone,ugender,uhobby)
    user.save()
    context = {'name': name, 'wxAccounts': wxAccounts, 'wxName': wxName,'telephone': telephone,'ugender': ugender, 'uhobby': uhobby}
    return render(request,'user/addUser_test.html',context)

# 条件查询所有user
def get_userList(requeset):
    id = requeset.GET['id']
    account = requeset.GET['account']
    wxAccounts = requeset.GET['wxAccounts']
    if id != None:
        users = User.objects.filter(id__lte=id, account__exact=account)

    users_serialize = serializers.serialize('json', users)
    return HttpResponse(users_serialize)
    # return HttpResponse(users_serialize, content_type="application/json")

    # users = User.objects.filter(id__lte=3)
    # users = User.objects.filter(id__gt=3)
    # users = User.objects.filter(wxAccounts__contains='太')

    # response_data = {}
    # try:
    #     response_data['result'] = 'success'
    #     response_data['message'] = serializers.serialize('json',users)
    # except:
    #     response_data['result'] = 'flase'
    #     response_data['message'] = 'flse message'
    # return JsonResponse(users_serialize)

# 根据主键，查询user
def get_user_id(request,id):
    # user = User.objects.get(pk=1)
    queryset = User.userManager.filter(pk=id)

    user_serialize = serializers.serialize('json', queryset)
    return HttpResponse(user_serialize)

# 删除
def delete_user_id(request,id):
    queryset = User.userManager.filter(pk=id)
    queryset.delete()
    return HttpResponse('delete id : '+id)

# 修改
def update_user(request,id):
    # save方法对单个对象有效
    # user = User.userManager.get(pk=id)
    # user.name = '王菲'
    # user.save()

    # update()方法对于任何结果集（QuerySet）均有效，这意味着你可以同时更新多条记录
    update = User.userManager.filter(pk=id).update(name='中岛美雪')
    return HttpResponse('update success')

