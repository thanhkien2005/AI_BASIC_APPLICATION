% Đổ đầy bình Y
fillY(Y, Vy, NewY, X, X) :-
    Y < Vy, NewY is Vy.

% Đổ hết nước trong bình X
emptyX(Y, Y, X, Vx, NewX) :-
    X > 0, NewX is 0.

% Rót nước từ bình Y sang bình X
pourYtoX(Y, X, Vy, Vx, NewY, NewX) :-
    Y > 0, X < Vx,
    Transfer is min(Y, Vx - X),
    NewY is Y - Transfer,
    NewX is X + Transfer.

% Rót nước từ bình X sang bình Y
pourXtoY(Y, X, Vy, Vx, NewY, NewX) :-
    X > 0, Y < Vy,
    Transfer is min(X, Vy - Y),
    NewX is X - Transfer,
    NewY is Y + Transfer.

% Kiểm tra điều kiện dừng
goal(Y, X, Z) :-
    Y =:= Z; X =:= Z.

% Một bước chuyển trạng thái
step(Y, X, Vy, Vx, NewY, NewX) :-
    fillY(Y, Vy, NewY, X, NewX);
    emptyX(Y, NewY, X, Vx, NewX);
    pourYtoX(Y, X, Vy, Vx, NewY, NewX);
    pourXtoY(Y, X, Vy, Vx, NewY, NewX).

% Giải bài toán
solve(Y, X, Vy, Vx, Z, Visited, Path) :-
    goal(Y, X, Z),                     % Nếu đạt mục tiêu
    reverse([(Y, X) | Visited], Path); % Lưu đường đi
    step(Y, X, Vy, Vx, NewY, NewX),    % Thực hiện bước tiếp theo
    \+ member((NewY, NewX), Visited),  % Tránh lặp trạng thái
    solve(NewY, NewX, Vy, Vx, Z, [(Y, X) | Visited], Path).

% Hàm khởi tạo
start(Vy, Vx, Z, Path) :-
    solve(0, 0, Vy, Vx, Z, [], Path).
/*
?- start(5, 3, 4, Path).
Path = [(0, 0), (5, 0), (2, 3), (2, 0), (0, 2), (5, 2), (4, 3)].
?- start(7, 3, 1, Path).
Path = [(0, 0), (7, 0), (4, 3), (4, 0), (1, 3)].
?- start(6, 2, 5, Path).
False.

*/
