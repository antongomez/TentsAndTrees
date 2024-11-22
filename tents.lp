% Define the adjacent cells
adj(0, 1). adj(1, 0). adj(0, -1). adj(-1, 0).

% Generate only one tent within next to a tree
1 { belongs_to(TX, TY, X, Y) : TX = X + DX, TY = Y + DY, adj(DX, DY), row(TX, _), col(TY, _), not tree(TX,TY) } 1 :- tree(X, Y).
tent(X, Y) :- belongs_to(X, Y, _, _).

% Not the same tent belongs to two trees
:- belongs_to(X, Y, X1, Y1), belongs_to(X, Y, X2, Y2), tent(X, Y), tree(X1, Y1), tree(X2, Y2), (X1, Y1) != (X2, Y2).

% Tents cannot be adjacent to each other (including diagonals)
:- tent(X1, Y1), tent(X2, Y2), DX=-1..1, DY=-1..1, X2 = X1 + DX, Y2 = Y1 + DY, (DX, DY) != (0, 0).

% The number of tents in each row and column must match with the indicated number
:- row(X, N), N != { tent(X, Y) : col(Y, _) }.
:- col(Y, N), N != { tent(X, Y) : row(X, _) }.


#show dim/1.
#show tree/2.
#show tent/2.