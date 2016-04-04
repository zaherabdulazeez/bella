# Authors: Zaher Abdul Azeez
""" Given a location or a collection of locations, this module has classes that handle these locations 
and explore the nearby areas
"""

from keys import GMAPS_SERVER_KEY
import googlemaps

gmaps = googlemaps.Client(key = GMAPS_SERVER_KEY)

class RadarExplorer(object):
	""" This class does a radar search of all the places around a given particular and a given radius
	"""
	def __init__(self, loc_centre, radius):
		self.location = loc_centre
		self.radius = radius

		

