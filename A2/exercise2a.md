# AI2 Exercise 2a
#### Group 09: Wilhelm Oskar Ostermann, Marc Steger, Stefan Lepolt

## Representing the Circuit in Boolean Logic

SD =
$
(\neg Ab_{G1} \rightarrow ((\neg A \lor B) \leftrightarrow G_1)) \land
$
$
(\neg Ab_{G2} \rightarrow ((A \lor \neg B) \leftrightarrow G_2)) \land
$
$
(\neg Ab_{G3} \rightarrow ((\neg C \lor D) \leftrightarrow G_3)) \land
$
$
(\neg Ab_{G4} \rightarrow ((C \lor \neg D) \leftrightarrow G_4)) \land
$
$
(\neg Ab_{G5} \rightarrow ((G_1 \land G_2) \leftrightarrow G_5)) \land
$
$
(\neg Ab_{G6} \rightarrow ((G_3 \land G_4) \leftrightarrow G_6)) \land
$
$
(\neg Ab_{G7} \rightarrow ((\neg G_5 \lor \neg G_6) \leftrightarrow G_7))
$

CNF =
$
(Ab_{G1} \lor A \lor G_1) \land
(Ab_{G1} \lor \neg B \lor G_1) \land
(Ab_{G1} \lor \neg G_1 \lor \neg A \lor B) \land
$
$
(Ab_{G2} \lor \neg A \lor G_2) \land
(Ab_{G2} \lor B \lor G_2) \land
(Ab_{G2} \lor \neg G_2 \lor A \lor \neg B) \land
$
$
(Ab_{G3} \lor C \lor G_3) \land
(Ab_{G3} \lor \neg D \lor G_3) \land
(Ab_{G3} \lor \neg G_3 \lor \neg C \lor D) \land
$
$
(Ab_{G4} \lor \neg C \lor G_4) \land
(Ab_{G4} \lor D \lor G_4) \land
(Ab_{G4} \lor \neg G_4 \lor C \lor \neg D) \land
$
$
(Ab_{G5} \lor \neg G_1 \lor \neg G_2 \lor G_5) \land
(Ab_{G5} \lor \neg G_5 \lor G_1) \land
(Ab_{G5} \lor \neg G_5 \lor G_2) \land
$
$
(Ab_{G6} \lor \neg G_3 \lor \neg G_4 \lor G_6) \land
(Ab_{G6} \lor \neg G_6 \lor G_3) \land
(Ab_{G6} \lor \neg G_6 \lor G_4) \land
$
$
(Ab_{G7} \lor G_5 \lor G_7) \land
(Ab_{G7} \lor G_6 \lor G_7) \land
(Ab_{G7} \lor \neg G_7 \lor \neg G_5 \lor \neg G_6)
$