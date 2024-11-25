% SPDX-FileCopyrightText: 2024 Eliseo Pita Vilariño and Antón Gómez López
% SPDX-FileContributor: Antón Gómez López
% SPDX-FileContributor: Eliseo Pita Vilariño
%
% SPDX-License-Identifier: MIT

#program display.
#const csize=31.
&display{window,h=S,w=S,caption="Tents & trees"} :- S=csize*N+1, dim(N).
image("pics/tree.png",X,Y) :- tree(X,Y).
image("pics/tent.png",X,Y) :- tent(X,Y).
image("pics/grass.png",X,Y) :- dim(N),X=0..N-1,Y=0..N-1,not tent(X,Y), not tree(X,Y).
&display{image=I,x=X1,y=Y1} :- image(I,X,Y),X1=Y*csize,Y1=X*csize.