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