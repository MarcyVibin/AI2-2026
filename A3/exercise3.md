# AI2 Exercise 3
#### Group 09: Wilhelm Oskar Ostermann, Marc Steger, Stefan Lepolt

## Exercise 1: planning in PDDL

### Modelling in PDDL
#### Domain File
The Domain File explains the environment. So theres no instantiating only definitions of what exists in the environment. For each type there is only one: ```location```. Bathroom, entrance, kitchen, the roads, all map to their own location. The predicates are split into 4 groups, the location types, the carrying states, the task completion states and the navigation logic. The last part of the Domain File consists of all the different actions our robot can perform. Those are implemented as defined by the assignment sheet.

#### Problem File
In the problem file objects are defined first. They create location objects, e.g. entrance, center, roads. Connections in PDDL are directional and since our graph is undirected, we map all connections back and forth, i.e. from A to B and from B to A. Hence there is a mapping of Figure 1 in the Assignment sheet from every connection for all the locations, instantiated in ```:init```. The target location types are defined in our init as well. Each location that could be a target location (everything other than roads) gets its own target location. We also set our starting battery level to 2 and our starting time to 1.
For our target we set states to ````dinner-served && medicine-placed && laundry-done && chatted-with-owner``` also as stated in the assignment.

### Solve and provide a plan

0.0: (move entrance charging-station1)
1.0: (charge charging-station1)
2.0: (move charging-station1 entrance)
3.0: (move entrance bathroom)
4.0: (do-laundry bathroom)
5.0: (move bathroom entrance)
6.0: (move entrance road1)
7.0: (move road1 center)
8.0: (move center road3)
9.0: (move road3 market)
10.0: (buy-groceries market)
11.0: (move market road3)
12.0: (move road3 center)
13.0: (move center road1)
14.0: (move road1 entrance)
15.0: (move entrance kitchen)
16.0: (prepare-dinner kitchen)
17.0: (move kitchen entrance)
18.0: (move entrance dining-room)
19.0: (serve-dinner dining-room)
20.0: (chat-with-owner dining-room)
21.0: (move dining-room entrance)
22.0: (move entrance charging-station1)
23.0: (charge charging-station1)
24.0: (move charging-station1 entrance)
25.0: (move entrance road1)
26.0: (move road1 center)
27.0: (move center road2)
28.0: (move road2 pharmacy)
29.0: (fetch-medicine pharmacy)
30.0: (move pharmacy road2)
31.0: (move road2 center)
32.0: (move center road1)
33.0: (move road1 entrance)
34.0: (move entrance bathroom)
35.0: (place-medicine bathroom)

### Would you use such a robot?

I think a robot like SuBot would be useful for the practical part of
running a household such as getting medicine, preparing meals, and handling everyday tasks, actions where automation can mean more independence for people who have difficulties coping with them, e.g. the elderly or people with limited mobility. For those purposes a robot would be a gamechanger.

I am more sceptical about the idea of addressing loneliness by a robot. A
system that "chats with the owner" can provide routine and an illusion of socila interaction, for someone who would have no other options to talk, that is not nothing. But I would see it only as a better than nothing solution, not a serious replacement for human contact. Lonely people are longing for another person, and a scripted interaction can't provide that. The problem I see is that if a robot might be accepted as a "good enough" choice, it could quietly reduce the pressure to provide real human care. So I would understand the robot as a tool and view the relationship mimicking feature as a somewhat curious but limited byproduct. 



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
