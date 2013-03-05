'''
Created on Mar 5, 2013

@author: pvicente
'''
from data_exceptions import NotValid2DPointFormat,WrongLink
from math import sqrt

class Node(object):
    '''
    Node object with 2D coordinates and related links with other nodes.
    Equality and comparision operators are performed over name attribute.
    '''
    def __init__(self, point2D, name=''):
        if not isinstance(point2D, tuple) and not isinstance(point2D, list):
            raise NotValid2DPointFormat(name,point2D)
        
        if len(point2D) != 2:
            raise NotValid2DPointFormat(name, point2D)
        
        for value in point2D:
            if not type(value) in (int, float):
                raise NotValid2DPointFormat(name, point2D)
        
        self._name = str(name)
        self._x = point2D[0]
        self._y = point2D[1]
        self._links = set()
    
    @property
    def name(self):
        return self._name
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def links(self):
        return self._links
    
    def distance(self, node):
        '''Euclidean distance wiht other node'''
        
        if not isinstance(node, Node):
            return 0
        x = self.x - node.x
        y = self.y - node.y
        return sqrt(x*x + y*y)
    
    def addLink(self, node):
        if not isinstance(node, Node):
            raise WrongLink(self.name, node)
        
        if self == node:
            raise WrongLink(self.name, node.name)
        
        self._links.add(node)
    
    def __cmp__(self, node):
        '''
        Compare only names. Must be present if hash is defined
        '''
        if not isinstance(node, Node):
            return -1
        return cmp(self.name, node.name)
    
    def __eq__(self, node):
        '''
        Compare only names. Usefull to == comparision, must be defined with hash
        '''
        if not isinstance(node, Node):
            return False
        return self.name == node.name
    
    def __hash__(self):
        '''
        Hash over name. Usefull to insert Nodes in sets.
        '''
        return hash(self.name)
    
    def __str__(self):
        return "<%s-(%s,%s)->%s>"%(self.name, self.x, self.y, [link.name for link in self.links])
    
    def __repr__(self):
        return str(self)


class City(Node):
    '''
    City object with double link behaviour when addLink is performed.
    Other behaviour inherited from Node
    '''
    def __init__(self, name, point2D):
        super(City, self).__init__(point2D, name)
    
    def addLink(self, city):
        '''
        A road map doesn't have directed nodes and a double link is performed between nodes
        '''
        Node.addLink(self, city)
        
        if not self in city.links:
            city.addLink(self)



