%%% grid defined in instance.asp %%%

%%% Adjacent (horizontal vertical and diagonal allowed) is exactly the same in the powerpoint %%%
adjacent(R1, C1, R2, C2) :- row(R1), col(C1), row(R2), col(C2), R1 - R2 <= 1, R2 - R1 <= 1, C1 - C2 <= 1, C2 - C1 <= 1.

%%% Cells that are allowed to have light bulbs (_ means any value) %%%
allowed(R, C) :- adjacent(R, C, Rwall, Cwall), wall(Rwall, Cwall, _).

%%% Guess light bulb placement %%%
{placeLightBulb(R, C)} :- row(R), col(C), not wall(R, C, _), allowed(R, C).

%%% cell is blocked %%%
blockedByCol(C, R1, R2) :- wall(Rwall, C, _), row(R1), row(R2), Rwall > R1, Rwall < R2.
blockedByCol(C, R1, R2) :- wall(Rwall, C, _), row(R1), row(R2), Rwall > R2, Rwall < R1.

blockedByRow(R, C1, C2) :- wall(R, Cwall, _), col(C1), col(C2), Cwall > C1, Cwall < C2.
blockedByRow(R, C1, C2) :- wall(R, Cwall, _), col(C1), col(C2), Cwall > C2, Cwall < C1.

%%% cell is lit up %%%
litUp(R,C) :- placeLightBulb(R, C).
litUp(R,C) :- placeLightBulb(R2, C), row(R), R != R2, not blockedByCol(C, R, R2).
litUp(R,C) :- placeLightBulb(R, C2), col(C), C != C2, not blockedByRow(R, C, C2).

%%% constraint: every non wall cell is lit up %%%
:- row(R), col(C), not wall(R, C, _), not litUp(R, C).
