
from googleapiclient.discovery import build
from pprint import PrettyPrinter
import pafy

class GoogleSearch:
    def search(keyword):
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
            return video.title,videoUrl,video.author,video.duration,video.viewcount,video.likes,bestaudiodownload
            
        