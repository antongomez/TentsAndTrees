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

% Generate all the posible tents within the board next to a tree
tent(X1, Y1) :- 
    tree(X, Y),
    X1 = X + DX, 
    Y1 = Y + DY,
    DX = -1..1,
    DY = -1..1,
    (DX = 0; DY = 0), % Permite solo movimientos horizontales o verticales
    row(X1), col(Y1),
    not tree(X1, Y1).


#show dim/1.
#show tree/2.
#show tent/2.

% ..t...
% .t....
% t....t
% ......
% ....t.
% t...t.