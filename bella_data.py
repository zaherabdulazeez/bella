#Authors: Zaher Abdul Azeez
""" All the data structure related classes of bella are implemented here. 
Bella has results in Dicts and classes related to manipulating Dicts are here.
Dicts are converted to JSON to handle over to javascript
JSON handling classes are implemnted here
"""
import json



class MasterDataFrame(object):
	"""Master Data frame: List of dictionaries to be converted to JSON.
	Instantiate with a list of keys that the dict would have
	"""
	def __init__(self,keylist):
		self.sub_dict = dict.fromkeys(keylist,)

	def add_key(key):

class JSONObject(object):
	"""The full json data frame where data from all the bella classes are aggregated"""
	def __init__(self, arg):
		

