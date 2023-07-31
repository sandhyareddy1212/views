from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
def fbv_string(request):
    return HttpResponse('this is CBV sting')


def fbv_temp(request):
    return render(request,'fbv_temp.html')




class cbv_string(View):
    def get(self,request):
        return HttpResponse("<h1> this is cbv_string</h1>")


class cbv_temp(View):
    def get(self,request):
        return render(request,'cbv_temp.html')