dongvatanco(de).
dongvathungdu(chosoi).
dongvatanthit(X):-dongvathungdu(X).
dongvat(X):-dongvatanthit(X); dongvatanco(X).
an(X, thit):-dongvatanthit(X).
an(X, co):-dongvatanco(X).
an(X, Y):-dongvatanthit(X),dongvatanco(Y).
thucuong(nuoc).
uong(X, Y):-dongvat(X),thucuong(Y).
tieuthu(X, Y):-((an(X, Y),not(uong(X, Y)));(uong(X, Y), not(an(X, Y)))), dongvat(X).



/*

?- dongvathungdu(X).
X = chosoi.

?- tieuthu(chosoi, Y).
Y = thit ;
Y = de ;
Y = nuoc ;
false.

*/
