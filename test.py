# from bella_location import LocationSampler
# from bella_explorer import RadarExplorer 
# from pprint import pprint
# import json

# center = {'lat':18.969344,'long':72.826709 }
# bounds = {'rectangle':{'length':7000,'breadth':4000 }}

# sampler = LocationSampler(center,bounds,250.0)

# sampled_list = sampler.rectangle_sample()
# print len(sampled_list)

# cen = [19.132637,72.913157]
###############################################################
# explorer = RadarExplorer(sampled_list, 250)
# explorer.iterative_food_lookup()
# food_data = explorer.data_frame
# with open('food_data.json','w') as outfile:
# 	json.dump(food_data, outfile)

##############################################################
# health_explorer = RadarExplorer(sampled_list, 1000)
# health_explorer.iterative_health_lookup()
# health_data = health_explorer.health_data_frame

# with open('health_data.json','w') as outfile:
# 	json.dump(health_data, outfile)


##############################################################

# school_explorer = RadarExplorer(sampled_list, 1000)
# school_explorer.iterative_school_lookup()
# school_data = school_explorer.school_data_frame

# with open('school_data.json','w') as outfile:
# 	json.dump(school_data, outfile)

#############################################################

# def minimizer(df):
# 	temp = df
# 	for k in range(len(temp)):
# 		del df[k][-1]
# 	return temp

# def dump_food(df):
# 	tm = minimizer(df)
# 	with open('health_min.json','w') as outfile:
# 		json.dump(tm, outfile)

#####################################

nums = []
# print nums

for each in range(len(data)):
	nums.append(data[each][1]['num_of_schools'])
print min(nums)
print max(nums)
from collections import Counter
count = Counter(nums)
print count
