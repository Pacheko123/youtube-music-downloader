from django.shortcuts import render
from googleapiclient.discovery import build
from pprint import PrettyPrinter
import pafy
# from download.download import Download
# from search.search import GoogleSearch

# Create your views here.
def index(request):
    return render(request,"index.html")

def result(request,keyword):
        api_key=""

        youtube = build('youtube','v3',developerKey = api_key)
        print(type(youtube))

        request = youtube.search().list(q=keyword,part='snippet',type='video')
        print(type(request))
        res = request.execute()
        for item in res['items']:
            videoId=item['snippet']['id.videoId']
            videoUrl = "https://www.youtube.com/watch?v="+videoId 
            
            # url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
            video = pafy.new(videoUrl)
            file_size = video.get_filesize()

            '''Get the best audio file for download'''
            bestaudiodownload = video.getbestaudio()
            print(type(video))

        # return video.title,videoUrl,video.author,video.duration,video.viewcount,video.likes,bestaudiodownload
        return render(request,index,video)

def download(request):
    pass
            