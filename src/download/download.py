import pafy

class Download:

    '''This function gets video details and downloads audio, it gets video url from google api'''

    def getDetails(url):
        # url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
        video = pafy.new(url)
        file_size = video.get_filesize()

        '''Get the best audio file for download'''
        bestaudiodownload = video.getbestaudio()
        return video.title,url,video.author,video.duration,video.viewcount,video.likes