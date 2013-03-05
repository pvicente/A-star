'''
Created on Mar 5, 2013

@author: pvicente
'''
class FromCityNotFound(Exception):
    def __init__(self, city_name):
        Exception.__init__(self, "From City '%s' not found"%(city_name))

class GoalCityNotFound(Exception):
    def __init__(self, city_name):
        Exception.__init__(self, "Goal City '%s' not found"%(city_name))
