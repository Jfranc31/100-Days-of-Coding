% function [x,t0] = LS_estimation(A,b)
%     
%     N = 100;
%     
%     x = ones(3,N);
%     x(:,1) = b;
%     
%     for i = 2:N
%         x(:,i) = (A' * A)^(-1) * A' * b;
%         b = x(:,i);
%     end
%     t0 = (A' * A)^(-1) * A' * b;
%     
%     x=fliplr(x);
% end

function [xhat] = LS_estimation(A,b)
%This function will take a matrix A and a vector b. It will use the 
%%least squares method to fit a line that best fits these pieces of data
%%onto each other

At = (A.'); %%This creates the transpose of A
Inverse = inv(At*A); %%I used the normal equation here to find the parameters
xhat= Inverse * (At*b); %%of the line of best fit


end