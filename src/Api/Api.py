from Api.ApiRequest import ApiRequest

'''
Does the API request to get the planets 
'''
api = ApiRequest("https://api.le-systeme-solaire.net/rest/bodies")

planets = api.request({"filter":"isPlanet,eq,true", "order":"perihelion,asc"})['bodies']

'''
Add inital velocities value (orbital speed)
'''
velocities = [47400, 35000, 29800, 24100, 13100, 9700, 6800, 5400]
for p in planets:
    p['velocity'] = velocities[planets.index(p)]

'''
Does the API request to get the sun
'''
sun = api.request({"filter":"id,eq,soleil"})['bodies'][0] 

'''
Does the API request to get the moon
'''
moon = api.request({"filter":"id,eq,lune"})['bodies'][0] 
moon['velocity'] = 1022



