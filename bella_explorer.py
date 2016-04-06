# Authors: Zaher Abdul Azeez
""" Given a location or a collection of locations, this module has classes that handle these locations 
and explore the nearby areas
"""

from keys import GMAPS_SERVER_KEY
import googlemaps
from time import sleep

gmaps = googlemaps.Client(key ='AIzaSyDIGV_bW2xhoC8ovYrV_cfOSavGqDGMaOo')

class RadarExplorer(object):
	""" This class does a radar search of all the places around a given a list of locations a given radius and optional name/keyword.
	"""
	#extend the functionality 
	def __init__(self, loc_centre_list, radius):
		self.location_list = loc_centre_list
		self.radius = radius
		self.food_data_frame = []
		self.health_data_frame = []
		self.school_data_frame = []
		
	def _single_explore(self,client=gmaps, location=None, radius=None, keyword=None, name= None, type=None):
		clientobj = client
		radar_res = clientobj.places_radar(location=location, radius=self.radius, type=type, keyword= keyword, name= name)
		return radar_res

	def _single_place_lookup(self,place_id,client=gmaps):
		clientobj = client
		lookup_res = clientobj.place(place_id)
		return lookup_res

	
	def iterative_food_lookup(self):
		sampled_list = self.location_list
		for each in sampled_list:
			#perform radar search
			# single_radar_res = {'results':[{'place_id':each},{'place_id':each},{'place_id':each}]}
			single_radar_res = self._single_explore(location=each, type='restaurant')
			#find the number of food
			num_food = len(single_radar_res['results'])
			#find the place_id
			place_id_list = []
			for k in range(num_food):
				place_id_list.append(single_radar_res['results'][k]['place_id'])

			item = self.make_list(location=each,num_food=num_food, place_id_list=place_id_list)
			self.food_data_frame.append(item)
			sleep(1)

	def iterative_health_lookup(self):
			sampled_list = self.location_list
			for each in sampled_list:
				#perform radar search
				single_radar_res = self._single_explore(location=each, type='hospital')
				num_hospital = len(single_radar_res['results'])
				#find the place_id
				place_id_list = []
				for k in range(num_hospital):
					place_id_list.append(single_radar_res['results'][k]['place_id'])

				item = self.make_health_list(location=each,num_hospital=num_hospital, place_id_list=place_id_list)
				self.health_data_frame.append(item)
				sleep(1)
	
	def iterative_school_lookup(self):
			sampled_list = self.location_list
			for each in sampled_list:
				#perform radar search
				single_radar_res = self._single_explore(location=each, type='school')
				num_school = len(single_radar_res['results'])
				#find the place_id
				place_id_list = []
				for k in range(num_school):
					place_id_list.append(single_radar_res['results'][k]['place_id'])

				item = self.make_school_list(location=each,num_school=num_school, place_id_list=place_id_list)
				self.school_data_frame.append(item)
				sleep(1)

	def make_food_list(self,location,num_food,place_id_list):
		temp_l = [{'location':location },{'num_of_food':num_food },{'place_id_list':place_id_list}]
		return temp_l

	def make_health_list(self,location,num_hospital,place_id_list):
		temp_l = [{'location':location },{'num_of_hospitals':num_hospital },{'place_id_list':place_id_list}]
		return temp_l

	def make_school_list(self,location,num_school,place_id_list):
		temp_l = [{'location':location },{'num_of_schools':num_school },{'place_id_list':place_id_list}]
		return temp_l
