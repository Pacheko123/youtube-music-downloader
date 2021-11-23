from django.shortcuts import render
from pafy.pafy import new
from download.download import Download
from search.search import GoogleSearch

# Create your views here.
def index(request):
    return render(request,"index.html")

def result(request,keyword):
    newsearch = GoogleSearch()
    url = newsearch.search(keyword)

    
    downloadVideo= Download()
    downloadVideo.getDetails(keyword)
    return render(request,index)