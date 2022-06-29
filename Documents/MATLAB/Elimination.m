% Elimination upper triangle
function [U] = Elimination(Matrix_A)
    % Initialize matrix
    [n,m]=size(Matrix_A);
    U = zeros(n,m);
    r2 = 1;
        
    if Matrix_A(1,r2) == 0 %case for (1,1) and (2,1) are zero
        if Matrix_A(2,r2) ~=0
            x = Matrix_A(1,:);
            y = Matrix_A(2,:);
            Matrix_A(1,:) = y;
            Matrix_A(2,:) = x;
        elseif Matrix_A(3,r2) ~= 0 %case for (1,1) and (3,1) is zero
            a = Matrix_A(1,:);
            b = Matrix_A(3,:);
            Matrix_A(1,:) = b;
            Matrix_A(3,:) = a;
        end
    end
    
    if Matrix_A(1,r2) == 0 && Matrix_A(2,r2) == 0 && Matrix_A(3,r2) == 0 %If first column is all zeros
%         Matrix_A = Matrix_A(Matrix_A~=0); % Changing matrix size
%         Matrix_0 = zeros(n,m-1);
%         Matrix_0(:,1) = Matrix_A(1:3);
%         Matrix_0(:,2) = Matrix_A(4:6);
%         Matrix_A = Matrix_0;
%         U = zeros(n,m-1);
%         U(1,:) = Matrix_A(1,:);
        r2 = 2;
    end
    
    U(1,:) = Matrix_A(1,:); %First row of U is same as Matrix_A
    if Matrix_A(1,r2) > Matrix_A(2,r2)
        if Matrix_A(1,r2) == 0 %Make sure we don't divide by 0
            Matrix_A(1,r2) = 1;
        end
        mul1 = Matrix_A(2,r2) / Matrix_A(1,r2); %Find value for second row for U
        Matrix1 = -mul1 * Matrix_A(1,:);
        U(2,:) = Matrix1 + Matrix_A(2,:);
        if U(2,1) ~= 0 %If first on row 2 of U is not zero, set row 2 back to 0
            U(2,:) = 0;
            if Matrix_A(2,r2) == 0 %Make sure we don't divide by 0
                Matrix_A(2,r2) = 1;
            end
            mul1 = Matrix_A(1,r2) / Matrix_A(2,r2); %Find the value for the second row for U
            Matrix1 = -mul1 * Matrix_A(2,:);
            U(2,:) = Matrix1 + Matrix_A(1,:);
        end
        if Matrix_A(3,r2) == 0 %Make sure we don't divide 0 by a number
            Matrix_A(3,r2) = 1;
        end
        mul2 = Matrix_A(3,r2) / Matrix_A(1,r2); %Find value for third row for U
        Matrix2 = -mul2 * Matrix_A(1,:);
        U(3,:) = Matrix2 + Matrix_A(3,:);
        if U(2,:) == 0 %If second row of U is zero, change it with the third row
            U(2,:) = U(3,:);
            U(3,:) = 0;
        end
        if U(3,r2+1) ~= 0 %If second on third row is not a zero
            mul3 = U(3,r2+1) / U(2,r2+1); %Find value for third row of U
            Matrix3 = -mul3 * U(2,:);
            U(3,:) = Matrix3 + U(3,:);
        end
    else %If Matrix_A first row, first space, is less than Matrix_A second row, first space
        mul1 = Matrix_A(2,r2) / Matrix_A(1,r2); %Find the value for the second row of U
        Matrix1 = -mul1 * Matrix_A(1,:);
        U(2,:) = Matrix1 + Matrix_A(2,:);
        if Matrix_A(1,r2) == 0 %Make sure we don't divide by 0
            Matrix_A(1,r2) = 1;
        end
        mul2 = Matrix_A(3,r2) / Matrix_A(1,r2); %Find the value for the third row of U
        Matrix2 = -mul2 * Matrix_A(1,:);
        U(3,:) = Matrix2 + Matrix_A(3,:);
        if U(2,r2+1) == 0 %Make sure we don't divide by 0
            U(2,r2+1) = 1;
        end
        mul3 = U(3,r2+1) / U(2,r2+1); %Find the value for the third row of U
        Matrix3 = -mul3 * U(2,:);
        U(3,:) = Matrix3 + U(3,:);
    end
end
