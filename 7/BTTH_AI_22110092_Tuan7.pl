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
Sử dụng logic vị từ để biểu diễn các phát biểu:
a. Dê là động vật ăn cỏ.
DongVatAnCo(De).
b. Chó sói là động vật hung dữ.

DongVatHungDu(ChoSoi).
c. Động vật hung dữ là động vật ăn thịt.

∀x DongVatHungDu(x) → DongVatAnThit(x).
d. Động vật ăn thịt thì ăn thịt.

∀x DongVatAnThit(x) → An(x, Thit).
e. Động vật ăn cỏ thì ăn cỏ.
∀x DongVatAnCo(x) → An(x, Co).

f. Động vật ăn thịt thì ăn các động vật ăn cỏ.
∀x ∃y DongVatAnThit(x) ⋀ DongVatAnCo(y) → An(x, y).

g. Động vật ăn thịt và động vật ăn cỏ đều uống nước.
∀x DongVat(x), ThucUong(Nuoc) → Uong(x, Nuoc).
Vì động vật hung dữ là động vật ăn thịt nên ta có thể gộp lại thành DongVat(x)

 h. Một động vật tiêu thụ cái mà nó uống hoặc cái mà nó ăn.

∀x ∃y DongVat(x) ⋀ [[An(x, y) ⋀ ¬Uong(x, y)] ⋁ [Uong(x, y) ⋀ ¬An(x, y)]] → TieuThu(x, y)

*/
