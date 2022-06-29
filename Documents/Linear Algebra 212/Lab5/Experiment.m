%% Write a few simple test MATLAB functions
A = [2 4 6 9 1 10 3 12 8 7];
B = [1 2 3 4 5 6 7 8 9 10];
for x = 1:10
    if all(A<B)
        disp('All good')
    elseif any(A(x)<B(x))
        disp(['x = ',num2str(x),' Good'])
    else
        disp('No good')
    end
end

fprintf('\n')

C = [1 1 1 0 1 0 0 1 0 1 1 0 1 0 1];
D = [1 0 1 0 0 1 0 1 1 0 1 0 1 1 1];
for x = 1:15
    y = C(x) | D(x);
    if y == 1
        disp('There is a 1')
    else
        disp('There is no 1')
    end
end
%% Write a simple MATLAB function that illustrates how the error command works
Count = 0;
while true
    x = input('Please input a positive number: ');
    if x>=0
        Count = Count + 1;
    elseif x<0
        error('Value of input variable x must be positive. Re-run with positive x value')
    end
    y = 10;
    disp(y)
end

        