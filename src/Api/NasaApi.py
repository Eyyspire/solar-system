from astroquery.jplhorizons import Horizons
import astropy.units as u
import datetime

class NasaApi:
    """Allows to get intial positions and velocities of bodies relatively to the sun, according to the starting date
    """
    
    def __init__(self, name, date):
        self.correspondances = {
            "Mercury" : 199,
            "Venus" : 299,
            "Earth" : 399,
            "Mars" : 499,
            "Jupiter": 599,
            "Saturn": 699,
            "Uranus": 799, 
            "Neptune": 899,
            "Sun": 10,
            "Moon" : 301
        }
        self.obj = Horizons(id=str(self.correspondances[name]), location='500@0', epochs={'start':date.strftime("%Y-%m-%d"), 'stop':(date + datetime.timedelta(days=1)).strftime("%Y-%m-%d"), 'step':'1d'})

    def initial_conditions_request(self):
        # Interroger l'API pour les positions de la planète
        vectors = self.obj.vectors()

        return vectors


