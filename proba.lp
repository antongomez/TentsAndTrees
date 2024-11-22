% Define el tamaño del tablero (3x3)
size(3).

row(1..3).

% Generamos las coordenadas del tablero
cell(X, Y) :- size(N), X = 1..N, Y = 1..N.

% Una celda puede contener un árbol (tree) o estar vacía (vacío implícito si no es un árbol)
{ tree(X, Y) : cell(X, Y) }.

row(1, 3). % La fila 1 debe tener 1 árbol
row(2, 2). % La fila 2 debe tener 2 árboles
row(3, 3). % La fila 3 debe tener 1 árbol

% Restricción dinámica: asegura que el número de árboles en cada fila cumpla con el predicado row(F, N)
:- row(F, N), not N { tree(F, Y) : cell(F, Y) } N.

% Para facilitar la visualización en la salida, definimos cómo se imprimen las celdas
#show tree/2.
