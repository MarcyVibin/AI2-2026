domain parsed
problem parsed
grounding..
grounding time: 35
aibr preprocessing
|f|:20
|x|:2
|a|:31
|p|:0
|e|:0
h1 setup time (msec): 10
 g(n)= 3.0 h(n)=31.0
 g(n)= 5.0 h(n)=25.0
 g(n)= 7.0 h(n)=22.0
 g(n)= 13.0 h(n)=21.0
 g(n)= 16.0 h(n)=18.0
 g(n)= 17.0 h(n)=13.0
 g(n)= 16.0 h(n)=9.0
 g(n)= 17.0 h(n)=8.0
 g(n)= 18.0 h(n)=7.0
 g(n)= 19.0 h(n)=5.0
 g(n)= 27.0 h(n)=4.0
 g(n)= 28.0 h(n)=3.0
 g(n)= 29.0 h(n)=2.0
 g(n)= 30.0 h(n)=1.0
 g(n)= 31.0 h(n)=0.0
problem solved

found plan:
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

plan-length:36
metric (search):31.0
planning time (msec): 73
heuristic time (msec): 38
search time (msec): 68
expanded nodes:690
states evaluated:841
number of dead-ends detected:270
number of duplicates detected:491
