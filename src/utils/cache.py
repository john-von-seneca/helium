import os
import hashlib
import csv


class Cache(object):
	def __init__(self, fun):
		self.fun = fun
		self.location = os.path.abspath('.') + '/data/cache/'
		self.file_keys = self.location + 'keys.csv'
		self._read_cache()

	def __get__(self, obj, objtype):
		"""Support instance methods."""
		import functools
		return functools.partial(self.__call__, obj)

	def _read_cache(self):
		self.cache = {}
		for key, val_md5 in csv.reader(open(self.file_keys)):
			self.cache[key] = open(self.location + val_md5, 'r').read()

	def __call__(self, *args, **kwargs):
		# the first arg is the object id, shouldn't include that in the key
		key	 = str(args[1:]) + str(kwargs)
		try:
			return self.cache[key]
		except KeyError:
			print('key ', key, ' not found ... ')
			self.cache[key] = rval = self.fun(*args, **kwargs)
			self._append_key(key, rval)
			return rval
		except TypeError: # incase key isn't a valid key - don't cache
			return self.fun(*args, **kwargs)
	

	def _append_key(self, key, val):
		csv_writer = csv.writer(open(self.file_keys, "a"))
		val_md5 = hashlib.md5(val.encode('utf-8')).hexdigest()
		csv_writer.writerow([key, val_md5])
		with open(self.location + val_md5, 'w+') as file_val:
			file_val.write(val)
