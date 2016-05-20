#Authors: Zaher Abdul Azeez
""" All the data structure related classes of bella are implemented here. 
Bella has results in Dicts and classes related to manipulating Dicts are here.
Dicts are converted to JSON to handle over to javascript
JSON handling classes are implemnted here
"""
import json
import copy
from collections import Counter
import numpy
from pprint import pprint


class MasterDataFrame(object):
	"""Master Data frame: A List of lists. Each list contains dictionaries with key value pairs containing location specific data.
	Instantiate with a data frame from iterative_look up from bella_explorer
	"""
	def __init__(self,data_frame):
		self.data_frame = data_frame

	def minimize(self):
		df = self.data_frame
		temp = []
		
		for i in range(len(df)):
			temp.append([df[i][0],df[i][1]])

		return temp

	def write_json_file(self,filename):
		min_file_name = "min_"+filename
		min_data_frame = self.minimize()

		with open(filename, 'w') as outfile:
			json.dump(self.data_frame, outfile)

		with open(min_file_name,'w') as outfile:
			json.dump(min_data_frame, outfile)

	def properties(self):
		data = self.data_frame
		nums = []
		for each in range(len(data)):
			temp_dict = data[each][1]
			nums.append(temp_dict[temp_dict.keys()[0]])

		minim = min(nums)
		maxim = max(nums)
		avrg = numpy.mean(nums)
		med= numpy.median(nums)
		counts = Counter(nums)
		modes = counts.most_common()

		print ("Minimum: %f" %minim)
		print ("Maximum: %f" %maxim)
		print ("Mean: %f" %avrg)
		print ("Median: %f" %med)
		print ("counts:")
		print (counts)
		print ("modes:")
		print (modes)




		

