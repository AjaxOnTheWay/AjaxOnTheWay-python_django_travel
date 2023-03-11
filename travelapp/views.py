from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
# Create your views here.
def demo(request):
    obj = Place.objects.all()
    return render(request,"index.html",{'result':obj})
# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res = x+y
#     res2 = x-y
#     res3 = x*y
#     res4 = x/y
#     return render(request,"result.html",{'addition':res,
#                                          'Subtraction':res2,
#                                          'multiplication':res3,
#                                          'division':res4})