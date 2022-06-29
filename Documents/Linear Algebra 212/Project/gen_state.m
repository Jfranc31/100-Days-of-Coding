function [q] = gen_state(N,T,Px,Py,Vx,Vy,sigx,sigy)
    
    px = zeros(1,N+1); %Make array for values of x
    py = zeros(1,N+1); %Make array for values of y
    q = zeros(4,N+1); %Make matrix for values of q
    x_n = zeros(4,N+1); %Make matrix for values of x_n
    
    px(:,1) = Px; %Initialize first value of array for x
    py(:,1) = Py; %Initialize first value of array for y
    
    q(:,1) = [px(1);Vx;py(1);Vy]; %Initialize first values of q matrix
    
    A = [1 T 0 0;0 1 0 0;0 0 1 T;0 0 0 1]; %State Transition matrix
    
    X = randn([4 (N+1)]); %Random values
    x_n(:,1) = [X(1,1);X(2,1);X(3,1);X(4,1)]; %Initialize first values of x_n matrix
    
    B = [0 0 0 0;0 sigx 0 0;0 0 0 0;0 0 0 sigy]; %Matrix to affect the x and y velocities
    
    for n = 2:N+1
        q(:,n) = A*q(:,n-1) + B*x_n(:,n-1); %Equation for time-varying state vector and noise to the velocity
        x_n(:,n) = [X(1,n);X(2,n);X(3,n);X(4,n)]; %Goes to next value of x_n
    end
    
end