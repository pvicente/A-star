'''
Created on Mar 5, 2013

@author: pvicente
'''

class NotValid2DPointFormat(Exception):
    def __init__(self, cityname, point2D):
        super(NotValid2DPointFormat, self).__init__("2DPoint '%s' of city '%s' has a wrong format. It must have the following format -> [int or float, int or float]. Ex: [1, 2.1]", 
                                                    point2D, cityname)

class WrongLink(Exception):
    def __init__(self, origin, end):
        super(WrongLink, self).__init__("Link '%s->%s' is wrong. Please check ('%s', '%s') are valid names of cities"%(origin, end, origin, end))

class ValidFormatException(Exception):
    format_example = '{"cities": {"cityname-1": 2DPoint, ... , "cityname-n": 2DPoint}, "links": [["cityname-1", "cityname-2"], ["cityname-n-1", "cityname-n"]] }'
    example = '{"cities": {"Madrid": [0, 0], "Barcelona": [10, 10], "Albacete": [3, 4]}, "links": [["Madrid", "Barcelona"], ["Albacete", "Barcelona"]] }'
    
    def __init__(self, *args, **kwargs):
        super(ValidFormatException, self).__init__(*args, **kwargs)

class NotCities(ValidFormatException):
    def __init__(self, *args, **kwargs):
        super(NotCities, self).__init__('Not cities section. It should have the key cities like the following format ->%s. Ex: %s'%(self.format_example, self.example))

class NotValidCitiesFormat(ValidFormatException):
    def __init__(self, *args, **kwargs):
        super(NotValidCitiesFormat, self).__init__('Not valid cities format. It should have the following format -> %s. Ex: %s'%(self.format_example, self.example))
        
class NotLinks(ValidFormatException):
    def __init__(self, *args, **kwargs):
        super(NotLinks, self).__init__('Not links section. It should have the key links like the following format-> %s. Ex: %s'%(self.format_example, self.example))

class NotValidLinksFormat(ValidFormatException):
    def __init__(self, *args, **kwargs):
        super(NotValidLinksFormat, self).__init__('Not valid links format. It should have the following format -> %s. Ex: %s'%(self.format_example, self.example))