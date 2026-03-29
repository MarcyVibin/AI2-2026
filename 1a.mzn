% skeleton for now

var 1..4: x1;
var 1..3: x2;

constraint x1 > x2;
constraint x2 = 3;

solve satisfy;

output ["x1= ", show(x1), ", x2= ", show(x2)];