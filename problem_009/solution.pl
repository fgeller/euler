isTriple(X,Y,Z) :-
  XX = X*X,
  YY = Y*Y,
  ZZ = Z*Z,
  ZZ =:= XX + YY,
  1000 is X + Y + Z,
  X < Y,
  Y < Z.
triple(X,Y,Z) :-
  between(1,500,X),
  between(1,500,Y),
  between(1,500,Z),
  isTriple(X,Y,Z).
