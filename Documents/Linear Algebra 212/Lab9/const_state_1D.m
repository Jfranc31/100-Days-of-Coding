function [tsv] = const_state_1D(N,T,P,V,Ac)

    p = zeros(1,N+1);
    v = zeros(1,N+1);
    q = zeros(3,N+1);
    
    p(1) = P;
    v(1) = V;
    a = ones(1, N+1)*Ac;
    q(:,1) = [p(1);v(1);a(1)]; %State Vector
    
    A = [1 T (T^2/2);0 1 0;0 0 1]; %State Transition Matrix
    
    for n = 2:N+1
        p(n) = .5 * T.^2 * a(1) + T * v(n-1) + p(n-1); %Equation for position
        v(n) = T * a(1) + v(n-1); %Equation for velocity
        q(:,n) = A*q(:,n-1);%Equation for time-varying state vector
    end
    tsv = q;
end