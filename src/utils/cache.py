import os

class Cache(object):
	def __init__(self, fun):
		self.fun = fun
		self.cache = {}
		self.location = os.path.abspath('.') + '/data/cache/'
		self._read_cache()
		print(self.location)

	def __get__(self, obj, objtype):
		"""Support instance methods."""
		import functools
		return functools.partial(self.__call__, obj)

	def _read_cache(self):
		pass

	def __call__(self, *args, **kwargs):
		key	 = str(args) + str(kwargs)
		print('key: ', key)
		try:
			return self.cache[key]
		except KeyError:
			self.cache[key] = rval = self.fun(*args, **kwargs)
			print(type(rval))
			return rval
		except TypeError: # incase key isn't a valid key - don't cache
			return self.fun(*args, **kwargs)
	
