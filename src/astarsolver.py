'''
Created on Mar 5, 2013

@author: pvicente
'''
from astar_exceptions import FromCityNotFound, GoalCityNotFound
from Queue import PriorityQueue

class Cities_AStarSolver(object):
    def __init__(self, city_map):
        self._cities = city_map
    
    @property
    def cities(self):
        return self._cities
    
    def route(self, from_city, target_city):
        '''
        A-Star algorithm returns (route, cost) tuple
        route: [cityname1, cityname2 ... citynamen]
        cost: cost over route
        '''
        if self.cities[from_city] is None:
            raise FromCityNotFound()
        
        if self.cities[target_city] is None:
            raise GoalCityNotFound
        
        from_city = self.cities[from_city]
        goal_city = self.cities[target_city]
        
        #If goal or from city have not links with other cities there isn't no route
        if len(from_city.links) == 0 or len(goal_city.links) == 0:
            return None, 0
        
        #Helper functions to encapsulate common tasks
        def add_open(city, f_score):
            '''
            Add a city to open priority queue and open_set to retrieve later based on f_score
            '''
            priority_open_set.put_nowait((f_score, city))
            open_set.add(city)
        
        def get_open():
            '''
            Retrieve city with less cost from open set priority queue and remove from open_set 
            '''
            _, city=priority_open_set.get_nowait()
            open_set.remove(city)
            return city
        
        def reconstruct_path(from_city):
            '''
            Returns a tuple (route, cost)
            route: list of city names
            cost: cost to go to from city
            '''
            ret = [from_city.name]
            current_city = came_from.get(from_city.name)
            while not current_city is None:
                ret.insert(0, current_city)
                current_city = came_from.get(current_city)
            return ret, g_score[from_city.name]
        
        def heuristic_cost(from_city, to_city):
            '''
            Heuristic function to manage path finding. Now heuristic function is the euclidean distance from -> to cities
            '''
            return from_city.distance(to_city)
        
        ###Initialize lookup structures
        priority_open_set = PriorityQueue()
        open_set = set()
        closed_set = set()
        came_from = {}
        
        current_fscore = 0 + heuristic_cost(from_city, goal_city)
        add_open(from_city, current_fscore)
        
        g_score={from_city.name: 0}
        f_score={from_city.name: current_fscore}
        
        while len(open_set) > 0:
            current = get_open()
            if current == goal_city:
                return reconstruct_path(current)
             
            closed_set.add(current)
            for neighbor in current.links:
                tentative_g_score = g_score[current.name] + current.distance(neighbor)
                if neighbor in closed_set:
                    if tentative_g_score >= g_score[neighbor.name]:
                        continue
                if not neighbor in open_set or tentative_g_score < g_score[neighbor.name]:
                    came_from[neighbor.name] = current.name
                    g_score[neighbor.name] = tentative_g_score
                    current_f_score = tentative_g_score + heuristic_cost(neighbor, goal_city)
                    f_score[neighbor.name] = current_f_score
                    if not neighbor in open_set:
                        add_open(neighbor, current_f_score)
        
        return None, 0
    
    