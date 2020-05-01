from django.shortcuts import render
from django.http import HttpResponse
from .models import router





def home(request):
    router1 = router()
    router1.name = 'router 1'
    router1.id = '01'
    router1.d_speed = '123'
    router1.u_speed = '234'
    router1.graph_img  = 'wireless_speeds_May_31_20_55_.png'

    context = {'router1':router1}

    return render(request, 'wireless_web/home.html',context)
# render(request arg, path to templates, context(data))
def about(request):
    return render(request, 'wireless_web/about.html')