function [U] = my_elimination(Matrix_A)
    [n,m]=size(Matrix_A);
    U = zeros(n,m);
    U(1,:) = Matrix_A(1,:);
    if Matrix_A(1,1) > Matrix_A(2,1)
        if Matrix_A(1,1) == 0
            Matrix_A(1,1) = 1;
        end
        mul1 = Matrix_A(2,1) / Matrix_A(1,1);
        Matrix1 = -mul1 * Matrix_A(1,:);
        U(2,:) = Matrix1 + Matrix_A(2,:);
        if U(2,1) ~= 0
            U(2,:) = 0;
            if Matrix_A(2,1) == 0
                Matrix_A(2,1) = 1;
            end
            mul1 = Matrix_A(1,1) / Matrix_A(2,1);
            Matrix1 = -mul1 * Matrix_A(2,:);
            U(2,:) = Matrix1 + Matrix_A(1,:);
        end
        if Matrix_A(3,1) == 0
            Matrix_A(3,1) = 1;
        end
        mul2 = Matrix_A(3,1) / Matrix_A(1,1);
        Matrix2 = -mul2 * Matrix_A(1,:);
        U(3,:) = Matrix2 + Matrix_A(3,:);
        if U(2,:) == 0
            U(2,:) = U(3,:);
            U(3,:) = 0;
        else
            mul3 = U(3,2) / U(2,2);
            Matrix3 = -mul3 * U(2,:);
            U(3,:) = Matrix3 + U(3,:);
        end
    else
        if Matrix_A(1,1) == 0
            Matrix_A(1,1) = 1;
        end
        mul1 = Matrix_A(2,1) / Matrix_A(1,1);
        Matrix1 = -mul1 * Matrix_A(1,:);
        U(2,:) = Matrix1 + Matrix_A(2,:);
        if Matrix_A(1,1) == 0
            Matrix_A(1,1) = 1;
        end
        mul2 = Matrix_A(3,1) / Matrix_A(1,1);
        Matrix2 = -mul2 * Matrix_A(1,:);
        U(3,:) = Matrix2 + Matrix_A(3,:);
        if U(2,2) == 0
            U(2,2) = 1;
        end
        mul3 = U(3,2) / U(2,2);
        Matrix3 = -mul3 * U(2,:);
        U(3,:) = Matrix3 + U(3,:);
    end
end