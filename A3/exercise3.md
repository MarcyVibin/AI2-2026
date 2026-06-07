# AI2 Exercise 3
#### Group 09: Wilhelm Oskar Ostermann, Marc Steger, Stefan Lepolt

## Exercise 1: planning in PDDL

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

## Exercise 2: Bayesian Networks

#### D-Separation 
**DAG a**:
$$
A \rightarrow B, A \rightarrow C, B \rightarrow D, C \rightarrow D 
$$
**Valve types**:
Sequential valves: $A \rightarrow B \rightarrow D$, $A \rightarrow C \rightarrow D $
Divergent valve: $B \leftarrow A \rightarrow C$
Convergent valve: $B \rightarrow D \leftarrow C$

**Which valves are closed?**

I(A, Z, B) - never blocked, no independence
I(A, Z, C) - never blocked, no independence
I(A, Z, D) - blocked if $B,C \in Z$, both paths (through B and C) need to be blocked
I(B, Z, C) - blocked if $A \in Z$
I(B, Z, D) - never blocked, no independence
I(C, Z, D) - never blocked, no independence

**DAG b**:
$$
A \rightarrow B, A \rightarrow D, B \rightarrow C, C \rightarrow D 
$$
**Valve types**:
Sequential valves: $A \rightarrow B \rightarrow C$, $B \rightarrow C \rightarrow D $
Divergent valve: $B \leftarrow A \rightarrow D$
Convergent valve: $A \rightarrow D \leftarrow C$

**Which valves are closed?**

I(A, Z, B) - never blocked, no independence
I(A, Z, C) - blocked if $B \in Z$
I(A, Z, D) - one direct path that cant be blocked, no independence
I(B, Z, C) - never blocked, no independence
I(B, Z, D) - blocked if $A,C \in Z$ both paths (through A and C) need to be blocked
I(C, Z, D) - never blocked, no independence

#### Marginal Probabilities
P(A) = P(w1) + P(w2) + P(w3) + P(w4) + P(w5) + P(w6) + P(w7) + P(w8)
P(A) = 0.0192 + 0.0288 + 0.0864 + 0.3456 + 0.024 + 0.036 + 0.012 + 0.048
P(A) = 0.6
P(B) = 0.64
P(C) = 0.244
P(D) = 0.289

#### Conditional Probability Tables
DAG a:
Independency I(B, {A}, C), this means $P(B | A,C) \overset{!}{=} P(B | A)$
$P(B | A) = \frac{P(A,B)}{P(A)} = \frac{0.48}{0.6} = 0.8$
$P(B | A,C) \frac{P(A,B,C)}{P(A,C)} = \frac{0.048}{0.108} = 0.4444$
The probabilites are not the same so the independency is violated, which means the table is not a representation of DAG a.

DAG b:
Independency I(A, {B}, C), this means $P(A | B,C) \overset{!}{=} P(A | B)$
$P(A | B) = \frac{P(A,B)}{P(B)} = \frac{0.48}{0.64} = 0.75$
$P(A | B,C) = \frac{P(A,B,C)}{P(B,C)} = \frac{0.048}{0.064} = 0.75$
This independency is not violated.
$\rightarrow$ the DAG for the table, because DAG a is not. To actually show this DAG corresponds to the table I would have to shwow all independencies hold but the assignment didn't ask for that.

**CPT**:
**A**:
P(A)
0.6

**B**:
A----| P(B | A)
true | 0.8
false| 0.4

**C**:
B----| P(C | B)
true | 0.1
false| 0.5

**D**:
A----|C----| P(D | A,C)
true |true | 0.4
true |false| 0.2
false|true | 0.5
false|false| 0.3

#### More on D-Separation
Figure 3(a) can be modified so that I({A}, {D}, {C}) holds by removing the edge $B \rightarrow D$. The independency was not satisfied because $D \in Z$ was a decendant of B, but now it is cut off so the independency holds.

Figure 4(b) is not a DAG, it contains the circle $A \rightarrow B \rightarrow D \rightarrow A$.