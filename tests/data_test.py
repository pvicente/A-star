'''
Created on Mar 5, 2013

@author: pvicente
'''
from src.data import Node, City, CityMap
from src.data_exceptions import NotValid2DPointFormat, WrongLink, NotCities, \
    NotLinks, NotValidCitiesFormat, NotValidLinksFormat
import unittest

class TestNode(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_str(self):
        '''
        Test calling str operator to perform code
        '''
        n = Node(point2D=(0,0), name='TestNode')
        other = Node(point2D=(1,3), name='OtherTestNode')
        n.addLink(other)
        _ = str(n)
    
    def test_format_exceptions(self):
        '''
        Test raising NotValid2DPointFormat exceptions
        '''
        self.assertRaises(NotValid2DPointFormat, Node, point2D=1)
        self.assertRaises(NotValid2DPointFormat, Node, point2D='a')
        self.assertRaises(NotValid2DPointFormat, Node, point2D={})
        self.assertRaises(NotValid2DPointFormat, Node, point2D=['a', 2, 3])
        self.assertRaises(NotValid2DPointFormat, Node, point2D=(1,'2'))
    
    def test_links_exception(self):
        '''
        Test raising WrongLink
        '''
        n = Node((0,0),'test')
        self.assertRaises(WrongLink, n.addLink, n)
        self.assertRaises(WrongLink,n.addLink, '')
    
    def test_instance(self):
        '''
        Test checking construct of correct instance
        '''
        self.assertIsInstance(Node((1,2)), Node)
        self.assertIsInstance(Node((1.0, 3.5)), Node)
        self.assertIsInstance(Node((1, 2.10)), Node)
    
    def test_equal(self):
        '''
        Tests over equal operator and checking equality over name attribute
        '''
        self.assertNotEqual(Node((0,0)), None)
        self.assertNotEqual(Node((0,0)), 1)
        self.assertEqual(Node((0,0)), Node((1,1)))
        self.assertEqual(Node((0,0),'test'), Node((1,1),'test'))
        self.assertNotEqual(Node((0,0), 'test1'), Node((0,0), 'test2'))
    
    def test_cmp(self):
        '''
        Tests over cmp operator and checking comparisions over name atribute
        '''
        self.assertEqual(cmp(Node((0,0)), 1), -1)
        self.assertEqual(cmp(Node((0,0)), None), -1)
        self.assertEqual(cmp(Node((0,0), 'test'), Node((0,1),'test')), 0)
        self.assertEqual(cmp(Node((0,0), 'test1'), Node((0,1),'test')), cmp('test1', 'test'))
    
    def test_hash(self):
        '''
        Tests over hash attribute checking it over name attribute
        '''
        self.assertEqual(hash(Node((0,0))), hash(''))
        self.assertEqual(hash(Node((0,0), 'test')), hash('test'))
        self.assertNotEqual(hash(Node((0,0))), hash('a'))
        self.assertNotEqual(hash(Node((0,0), 'test')), hash('test2'))
    
    def test_distance(self):
        '''
        Test to checking euclidean distance over 2DPoints
        '''
        origin_points = [(1,1), (1,2),   (0,0),   (0,0), (0,0), (10,10)]
        end_points =    [(1,1), (1,3), (-1,-1), (10,10), (3,4), (3,4)  ]
        distance =      [0    , 1    , 1.4142 , 14.1421, 5    , 9.2195 ]
        for i in xrange(len(origin_points)):
            origin = Node(origin_points[i])
            end = Node(end_points[i])
            self.assertAlmostEqual(origin.distance(end), distance[i], places=4)
    
    
    def test_links(self):
        '''
        Test links are created inside node
        '''
        nodes = {'m': Node((0,0), 'm'), 'b': Node((10,10), 'b'), 'a': Node((4,3), 'a')}
        links = [('m','b'), ('a','m'),('b','m')]
        notlinks = [('b', 'a'), ('m', 'a')]
        
        for origin, end in links:
            nodes[origin].addLink(nodes[end])
        
        for origin, end in links:
            self.assertIn(nodes[end],nodes[origin].links)
        
        for origin, end in notlinks:
            self.assertNotIn(nodes[end], nodes[origin].links)
        
        for node in nodes.values():
            self.assertNotEqual(node.links , set(), msg='%s has not links with other nodes'%(node.name))


class TestCity(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_links(self):
        '''
        Tset links are created in both ways (origin, end) (end, origin)
        '''
        cities={'Madrid': City('Madrid', (0,0)), 'Barcelona': City('Barcelona', (10,10)), 'Albacete': City('Albacete', (3,4))}
        links = [('Madrid', 'Barcelona'), ('Albacete', 'Madrid')]
        notlinks = [('Barcelona', 'Albacete'), ('Albacete', 'Barcelona')]
        
        for origin, end in links:
            cities[origin].addLink(cities[end])
        
        for origin, end in links:
            self.assertIn(cities[end], cities[origin].links)
            self.assertIn(cities[origin], cities[end].links)
        
        for origin, end in notlinks:
            self.assertNotIn(cities[origin], cities[end].links)
        
        for city in cities.values():
            self.assertNotEqual(city.links , set(), msg='%s has not links with other cities'%(city.name))


class TestCityMap(unittest.TestCase):
    def setUp(self):
        self.data = {'cities': {'Madrid': [0,0], 'Barcelona': [10,10], 'Albacete': [3,4]}, 'links': [['Madrid', 'Barcelona'], ['Albacete', 'Barcelona']]}
    
    def test_load_exceptions(self):
        '''
        Testing raising exceptions due to not valid data format
        '''
        self.assertRaises(NotCities, CityMap.load, {})
        self.assertRaises(NotLinks, CityMap.load, {'cities': []})
        self.assertRaises(NotValidCitiesFormat, CityMap.load, {'cities': [], 'links': []})
        self.assertRaises(NotValidCitiesFormat, CityMap.load, {'cities': {1: [1,2]}, 'links': []})
        self.assertRaises(NotValid2DPointFormat, CityMap.load, {'cities': {'name': 'wrongpoint'}, 'links': []})
        self.assertRaises(NotValidLinksFormat, CityMap.load, {'cities': {'name': [1,2]}, 'links': 'wronglink'})
        self.assertRaises(NotValidLinksFormat, CityMap.load, {'cities': {'Madrid': [0,0], 'Barcelona': [10,10]}, 'links': [1,2]})
        self.assertRaises(WrongLink, CityMap.load, {'cities': {'Madrid': [0,0], 'Barcelona': [10,10]}, 'links': [[1,2]]})
    
    def test_load_instance(self):
        '''
        Testing right construction with a valid input format
        '''
        self.assertIsInstance(CityMap.load({'cities': {'Madrid': [0,0], 'Barcelona': [10,10.0]}, 'links': [['Madrid','Barcelona']]}), CityMap)
    
    def check_load_data(self, citymap):
        '''
        Check function to check that input data is being represented correctly
        '''
        for cityname in self.data['cities']:
            city = citymap[cityname]
            self.assertNotEqual(city, None)
            x,y = self.data['cities'][cityname]
            self.assertEqual(city.x, x)
            self.assertEqual(city.y, y)
            related_links = [link for link in self.data['links'] if link[0] == cityname or link[1] == cityname]
            for link in related_links:
                origin, end = link
                if origin != cityname:
                    end = origin
                self.assertIn(end, [c.name for c in city.links])
    
    def test_load_data(self):
        '''
        Test input data
        '''
        citymap = CityMap.load(self.data)
        self.check_load_data(citymap)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)