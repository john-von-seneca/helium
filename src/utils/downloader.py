
import urllib.request
from .cache import *

class Downloader():

	@Cache
	def get(self, url):
		response = urllib.request.urlopen(url).read()
		html = str(response)
		return html
