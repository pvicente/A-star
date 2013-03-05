A-star
======

Solving A-Star Algorithm for a city map.

###First version structure
* **astarcmd**: Executable from command line
* **testall.bash**: Perfom all tests defined in test folder
* **examples**: folder with example configuration files
* **src**: folder with source files
* **tests**: folder with tests files

###Use case
```
>>./astarcmd examples/basic_citymap.map -o Madrid -e Albacete
Route: ['Madrid', 'Barcelona', 'Albacete'] with cost 23.361680081 has been detected wiht A-Star Algorithm in map defined in examples/basic_citymap.map

```

###astarcmd

Executes from command line with:

```
>>./astarcmd -h
usage: astarcmd [-h] [-V] [-o ORIGIN] [-e END] file

astarcmd -- resolves finding paths in road maps with A-Star algorithm

  Created by Pedro Vicente on 2013-03-05.
  Copyright 2013. All rights reserved.
  
  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0
  
  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE

positional arguments:
  file                  path to file with roadmap

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -o ORIGIN, --origin ORIGIN
                        origin of route.From city
  -e END, --end END     end of route. Goal city
```

###Configuration files
Defined in json format

In folder examples there is an example of input file:
```
>>ls examples/*
examples/basic_citymap.map
```




