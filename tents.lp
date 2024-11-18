% Define the size of the board
#const n = 6.
dim(n).

% % Define the rows and the columns
row(1..n).
col(1..n).

% Define the tents
tree(1, 3).
tree(2, 1).
tree(3, 1). tree(3, 6).

tree(5, 5).
tree(6, 1). tree(6, 5).

% Define the adjacent cells
adj(0, 1). adj(1, 0). adj(0, -1). adj(-1, 0).

% Generate all the posible tents within the board next to a tree
tent(X1, Y1) :- 
    tree(X, Y),
    X1 = X + DX, 
    Y1 = Y + DY,
    adj(DX, DY),
    row(X1), col(Y1).


#show dim/1.
#show tree/2.
#show tent/2.

% ..t...
% .t....
% t....t
% ......
% ....t.
% t...t.