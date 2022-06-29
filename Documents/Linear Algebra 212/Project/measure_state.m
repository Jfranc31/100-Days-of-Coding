function [y] = measure_state(p,N,C,d,q)
    % p = number of sensors
    % N = number of whatever
    % C = pxN sensor matrix that forms linear combinations of the state elements
    % d = Noise vector
    
    % Returns:
    % y = sensor measurements
    
    y = zeros(p,1); %Make matrix for values of y

    w = zeros(p,1); %Make matrix for values of w
    
    W = randn([4 (N+1)]); %Random values
    w(:,1) = [W(1,1);W(2,1);W(3,1);W(4,1)]; %Initialize first values of w matrix
    
    D = diag(d); %Identity matrix with d values diagonally placed
    y(:,1) = C*q(:,1) + D*w(:,1); %Initialize first values of y matrix
 
    
    for n = 2:N+1
        w = [W(1,n);W(2,n);W(3,n);W(4,n)]; %Goes to next value of w
        y(:,n) = C*q(:,n) + D*w; %Equation for time-varying state vector and noise to the position and velocity
    end
    
end