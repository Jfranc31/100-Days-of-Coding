% Matrix vector operation
A = [4 -1 2];
B = [2 -2 -1];
c = A .* B.';

% Elimination
C = A.' .* A;
C_noise = C;
C_noise(1,2) = C_noise(1,2) - 0.0001;
C_noise(2,3) = C_noise(2,3) - 0.0001;

U1 = my_elimination(C);
U2 = my_elimination(magic(3));
U3 = my_elimination(eye(3));
disp(U1)
disp(U2)
disp(U3)

