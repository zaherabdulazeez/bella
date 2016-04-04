# Authors: Zaher Abdul Azeez

"""
All location related classes of bella are implemented here. This module samples location points on a city,
decodes these location to addresses 
"""

class LocationSampler(object):
	"""Samples or probes latitudes and longitudes """
	def __init__(self, loc_centre, stepsize=200.0, bounds):
		""" Instantiate Bellas Location Sampler with starting centre point - loc_centre- a dict with lat & long,
		sampling stepsize in meters and bounds - a dict with lat and long
		"""
		self.centre = loc_centre
		self.start_lat = self.centre['lat']
		self.start_long = self.centre['long']
		self.stepsize = stepsize
		self.stop_lat = bounds.lat
		self.stop_long = bounds.long

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
	
	def sample(self):
		"""The sampling method of Location Sampler"""
		step = self._convert_step()


