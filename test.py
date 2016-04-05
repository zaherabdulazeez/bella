from bella_location import LocationSampler
center = {'geometry':{'lat':19.132637,'long':72.913157 }}
bounds =  {'geometry':{'lat':19.2,'long':73.0 }}
e = LocationSampler(center,bounds)
p = e.rectangle_sample()
print p