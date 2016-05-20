# Authors: Zaher Abdul Azeez

"""
All location related classes of bella are implemented here. This module samples location points on a city,
decodes these location to addresses 
"""

class LocationSampler(object):
	"""Samples or probes latitudes and longitudes """
	def __init__(self, loc_centre, bounds, stepsize=200.0):
		""" Instantiate Bellas Location Sampler with starting centre point - loc_centre- a dict with lat & long,
		sampling stepsize in meters and bounds - a dict with length and breadth in meters, length = breadth for radius 
		Ex: bounds = {'rectangle':{'length':10000,'breadth':50000 }}
		"""
		self.centre = loc_centre
		self.start_lat = self.centre['lat']
		self.start_long = self.centre['long']
		self.stepsize = stepsize
		if 'radius' in bounds:
			self.bound_radius = bounds['radius']
		elif 'rectangle' in bounds:
			self.rect_length = bounds['rectangle']['length']
			self.rect_breadth = bounds['rectangle']['breadth']
		
	def _convert_step(self):
		"""Converts stepsize to degrees of latitude and longitude. Note that we assume that each degree of 
		latitude and longitude correspond to a fixed distance in the conversion. Thought this is almost approx. true for latitudes,
		it is not true for longitudes. As we move to the poles the longitudes come closer.   
		"""
		_lat_factor = 1.0/111000  # one degree lat ~ 111000 km
		_long_factor = 1.0/111321 # valid at equator only
		# long_var = (111321.0/90.0)(90.0 - self.start_lat)
		# long_step = 1/long_var
		lat_step = self.stepsize*_lat_factor
		long_step = self.stepsize*_long_factor
		step = {'lat':lat_step, 'long':long_step }
		return step
	
	def rectangle_sample(self):
		"""The rectangular sampling method of Location Sampler. Returns a list of lists of lat-long samples"""
		step = self._convert_step()
		num_steps = {}
		try:
			num_steps['lat'] = int(round(abs(self.rect_length/self.stepsize))) 
			num_steps['long'] = int(round(abs(self.rect_breadth/self.stepsize)))
		except:
			print ("LocationSampler rectangle_sample bounds is a dict of the form {'rectangle':{'length':10000,'breadth':50000 }}")
		
		sample = []
		#in the following loop. a better sampling has to be implemented. Say we have a starting centre and the length and breadth of the rect
		#We have to sample data around the given starting centre in the given 
		for i in range(int(num_steps['lat']+1)):
			for j in range(int(num_steps['long']+1)):
				temp = []
				temp.append(self.start_lat + (i*step['lat']))
				temp.append(self.start_long + (j*step['long']))
				# temp ={'geometry':{'lat':None,'long':None}}
				# temp['geometry']['lat'] = self.start_lat + (i*step['lat'])
				# temp['geometry']['long'] = self.start_long + (j*step['long'])
				sample.append(temp)

		return sample

	def circle_sample(self):
		""" Circular Sampling method of Location Sampler """
		# implement later