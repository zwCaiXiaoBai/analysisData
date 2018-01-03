import urllib
# from urllib.request import *
#from urllib.request import urlopen


class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            return None
        response = urllib.urlopen(url)
        if response.getcode()!=200:
            return None
        return response
