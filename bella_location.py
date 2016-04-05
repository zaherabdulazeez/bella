# Authors: Zaher Abdul Azeez

"""
All location related classes of bella are implemented here. This module samples location points on a city,
decodes these location to addresses 
"""

class LocationSampler(object):
	"""Samples or probes latitudes and longitudes """
	def __init__(self, loc_centre, bounds, stepsize=200.0):
		""" Instantiate Bellas Location Sampler with starting centre point - loc_centre- a dict with lat & long,
		sampling stepsize in meters and bounds - a dict with lat and long or radius
		"""
		self.centre = loc_centre['geometry']
		self.start_lat = self.centre['lat']
		self.start_long = self.centre['long']
		self.stepsize = stepsize
		if 'radius' in bounds:
			self.bound_radius = bounds['radius']
		elif 'geometry' in bounds:
			self.stop_lat = bounds['geometry']['lat']
			self.stop_long = bounds['geometry']['long']
		else:
			self.bound_radius = None
			self.stop_lat = None
			self.stop_long = None


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
		"""The sampling method of Location Sampler"""
		step = self._convert_step()
		num_steps = {}
		if (self.stop_lat != None) and (self.stop_long != None):
			num_steps['lat'] =int(round(abs((self.stop_lat - self.start_lat)/step['lat']))) 
			num_steps['long'] = int(round(abs((self.stop_long - self.start_long)/step['long'])))

		else:
			num_steps['lat'] = 50
			num_steps['long'] = 50

		
		k = 0
		for i in range(int(num_steps['lat']+1)):
			for j in range(int(num_steps['long']+1)):
				sample[k]['geometry']['lat'] = self.start_lat + (i*step['lat'])
				sample[k]['geometry']['long'] = self.start_long + (j*step['long'])
			k = k + 1

		return sample


			


