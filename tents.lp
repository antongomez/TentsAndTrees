% Define the adjacent cells
adj(0, 1). adj(1, 0). adj(0, -1). adj(-1, 0).

% Generate only one tent within next to a tree
% 1 {tent(X1, Y1)} 1 :- 
%     tree(X, Y),
%     X1 = X + DX, 
%     Y1 = Y + DY,
%     adj(DX, DY),
%     row(X1, _), col(Y1, _),
%     not tree(X1, Y1).
1 { belongs_to(TX, TY, X, Y) : TX = X + DX, TY = Y + DY, adj(DX, DY), row(TX, _), col(TY, _), not tree(TX,TY) } 1 :- tree(X, Y).
tent(X, Y) :- belongs_to(X, Y, _, _).

% Not the same tent belongs to two trees
:- belongs_to(X, Y, X1, Y1), belongs_to(X, Y, X2, Y2), tent(X, Y), tree(X1, Y1), tree(X2, Y2), (X1, Y1) != (X2, Y2).



#show dim/1.
#show tree/2.
#show tent/2.