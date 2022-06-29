function [q_hat] = RLS_estimation(A,y,R)
    
    % A is a matrix
    % R is a matrix which has forgetting factors
    % y is measurements from the mesure_state
    % Y is p * (k + 1)
    
    %Returns:
    % q_hat is output as the columns of a matrix 
    
    k = max(size(y)); %Set k to be the number of columns
    q_hat = zeros(min(size(y)),k+1); %Make matrix for values of q_hat
    P(:,:,1) = eye(max(size(A))); %initialize the first covariance matrix
    K = zeros(min(size(y))); %Make matrix for values of K
    q_hat(:,1) = [0;100;0;100]; %Initialize first value of q_hat
    
    
    for n = 2:k+1
        K(:,:,n) = P(:,:,n-1)*A.'*(A*P(:,:,n-1)*A.'+R)^-1; %Kalman Gain
        P(:,:,n) = inv(R) - K(:,:,n)*A*(R^-1) *P(:,:,n-1); %Covariance Matrix
        q_hat(:,n) = q_hat(:,n-1) + K(:,:,n)*(y(:,n-1)-A*q_hat(:,n-1)); %Estimated States
    end
   
end