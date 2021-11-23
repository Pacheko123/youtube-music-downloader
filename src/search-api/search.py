
from googleapiclient.discovery import build
from pprint import PrettyPrinter

class GoogleSearch:
    def search(keyword):
        api_key="AIzaSyC38udAOc03YcEXO41SwnqxPJEjpaxudio"

        youtube = build('youtube','v3',developerKey = api_key)
        print(type(youtube))

        request = youtube.search().list(q=keyword,part='snippet',type='video')
        print(type(request))
        res = request.execute()
        for item in res['items']:
            videoId=item['snippet']['id.videoId']
            videoUrl = "https://www.youtube.com/watch?v="+videoId 
            return videoUrl

        pp = PrettyPrinter()
        pp.pprint(res)
        