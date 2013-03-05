'''
Created on Mar 5, 2013

@author: pvicente
'''
import unittest
from src.data import CityMap
from src.astarsolver import Cities_AStarSolver

class TestAStar(unittest.TestCase):
    def setUp(self):
        pass
    
    @classmethod
    def get_cost(cls, a_star, route):
        '''
        Returns the cost of a route adding distances over cities in route
        '''
        if len(route)<=1:
            return 0
        
        cities = [a_star.cities[city] for city in route]
        current_city = cities[0]
        cost = 0
        
        for city in cities[1:]:
            cost += current_city.distance(city)
            current_city=city
        return cost
    
    def test_no_route(self):
        '''
        Test no route has been founded
        '''
        data = {u'cities': {u'Madrid': [0,0], u'Barcelona': [10,10], u'Albacete': [3,4]}, u'links': [[u'Madrid', u'Barcelona']]}
        a_star = Cities_AStarSolver(CityMap.load(data))
        self.assertEqual(a_star.route(from_city='Barcelona', target_city='Albacete'), (None,0))
    
    def test_solve_1(self):
        '''
        Simple test solving easy city map
        '''
        data = {u'cities': {u'Madrid': [0,0], u'Barcelona': [10,10], u'Albacete': [3,4]}, u'links': [[u'Madrid', u'Barcelona'], [u'Albacete', u'Barcelona']]}
        short_route = ['Madrid', 'Barcelona', 'Albacete']
        a_star = Cities_AStarSolver(CityMap.load(data))
        
        check_res = (short_route, self.get_cost(a_star, short_route))
        self.assertEqual(a_star.route(from_city='Madrid', target_city='Albacete'), check_res)
    
    def test_solve_2(self):
        '''
        Simple test solving another easy city map
        '''
        data = {u'cities': {u'Madrid': [0,0], u'Barcelona': [10,10], u'Albacete': [3,4]}, u'links': [[u'Madrid', u'Barcelona'], [u'Madrid', u'Albacete']]}
        short_route = ['Barcelona', 'Madrid', 'Albacete']
        a_star = Cities_AStarSolver(CityMap.load(data))
        
        check_res = (short_route, self.get_cost(a_star, short_route)) 
        self.assertEqual(a_star.route(from_city='Barcelona', target_city='Albacete'), check_res)
    
    def test_solve_3(self):
        '''
        Simple test solving a more complex city map
        '''
        data = {u'cities': {u'Madrid': [0,0], u'Guadalajara':[1,2], u'Albacete':[-1,-3], u'Murcia': [-1,-5]},
                u'links': [ ['Madrid', 'Guadalajara'], ['Madrid', 'Albacete'], ['Guadalajara', 'Murcia'],['Albacete', 'Murcia'], ['Guadalajara', 'Albacete'] ]}
        short_route=['Madrid', 'Albacete', 'Murcia']
        a_star = Cities_AStarSolver(CityMap.load(data))
        
        check_res = (short_route, self.get_cost(a_star, short_route))
        self.assertEqual(a_star.route(from_city='Madrid', target_city='Murcia'), check_res)

if __name__ == '__main__':
    unittest.main(verbosity=2)