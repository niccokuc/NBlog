from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

# from django.http import HttpResponse
# import datetime
#
# def home(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)