from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def result(request,keyword):
    
    return render(request,index)