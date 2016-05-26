
import urllib.request as ur
from http.cookiejar import MozillaCookieJar
from .cache import *

class Downloader():
	USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0'
	HEADERS = {'User-Agent': USER_AGENT}
	def __init__(self):
		self.cjar = MozillaCookieJar()
		self.headers = Downloader.HEADERS
		self.opener = ur.build_opener(ur.HTTPCookieProcessor(self.cjar))

	@Cache
	def get(self, url):
		response = ur.urlopen(url).read()
		html = str(response)
		return html

	@Cache
	def get2(self, url):
		request = ur.Request(url = url,
							  headers=self.headers)
		response = self.opener.open(request).read()
		
		html = str(response)
		return html
