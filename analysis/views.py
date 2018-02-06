from django.shortcuts import render

# Create your views here.
def getImg(request):
    return render(request,'statistics/imgTest.html')


