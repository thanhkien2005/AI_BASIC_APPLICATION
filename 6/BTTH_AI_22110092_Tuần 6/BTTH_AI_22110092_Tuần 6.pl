parent(marry, bill).
parent(tom, bill).
parent(tom, liz).
parent(bill, ann).
parent(bill, sue).
parent(sue, jim).
woman(marry).
man(tom).
man(bill).
woman(liz).
woman(sue).
woman(ann).
man(jim).
child(Y, X):-parent(X, Y).
mother(X, Y):-parent(X, Y),woman(X).
grandparent(X, Z):-parent(X,Y),parent(Y,Z).
sister(X, Y):-parent(Z, X),parent(Z,Y),woman(X).

/*
?- parent(jim, X).
false.

?- parent(X, jim).
X = sue.

?- parent(marry, X),parent(X, part).
false.

?- parent(marry, X),parent(X, Y),parent(Y, jim).
X = bill,
Y = sue.

?- parent(X, bill).
X = marry ;
X = tom.

?- child(X, marry).
X = bill.

?- grandparent(X, sue).
X = marry ;
X = tom ;
false.

*/



