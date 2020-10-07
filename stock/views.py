from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def base(request):
    # html ="<html><body>Welcome to KKK</body></html>"
    #  return HttpResponse(html)
   
    return render(request, 'frontend/base.html')

def index(request):
    return render(request, 'frontend/index.html')
def About(request):
    return render(request, 'frontend/About.html')
def Contact(request):
    return render(request, 'frontend/Contact.html')

