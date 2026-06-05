### Modelling in PDDL
#### Domain File
The Domain File explains the environment. So theres no instantiating only defining of what the environment exist. For types there is only one: ```location```. So bathroom, entrance, kitchen, the roads, will all map to a its own location. The predicates are split into 4 groups, being the location types the carrying states the task completion states and the navigation logic. The last part of the Domain File are all the different actions our robot can take. Those are also just implemented as per definition of the assignment sheet.

#### Problem File
In the problem file, first the objects are defined. Those just create Location Objects (entrance, center, roads...). Connections in PDDL are directional and since our graph is undirected, we map ever connection from A to B and from B to A. Therefore theres a mapping of Figure 1 in the Assignment sheet of every connection for all the locations which is instantized in ```:init```. The goal location types are also defined in our init. So each location that could be a goal location (everything other than roads) gets its own goal location. We also set our starting battery level to 2 and our starting time to 1.
For our goal we set our and states to ````dinner-server && medicine-delivered && laundry-done && chatted-with-owner``` also as stated in the assignment.

### Solve and provide a plan

...

### Would you use such a robot?

...