function [x,y,z] = const_state_3D(N,T,Px,Vx,Ax,Py,Vy,Ay,Pz,Vz,Az)
    
    px = zeros(1,N+1);
    vx = zeros(1,N+1);
    
    py = zeros(1,N+1);
    vy = zeros(1,N+1);
    
    pz = zeros(1,N+1);
    vz = zeros(1,N+1);
    
    q = zeros(9,N+1);
    
    px(1) = Px;
    vx(1) = Vx;
    ax = ones(1, N+1)*Ax;
    
    py(1) = Py;
    vy(1) = Vy;
    ay = ones(1, N+1)*Ay;
    
    pz(1) = Pz;
    vz(1) = Vz;
    az = zeros(1, N+1)*Az;
    
    q(:,1) = [px(1);vx(1);ax(1);py(1);vy(1);ay(1);pz(1);vz(1);az(1)];
    
    A = [1 T (T^2/2) 0 0 0 0 0 0;0 1 T 0 0 0 0 0 0;0 0 1 0 0 0 0 0 0;...%State Transition Matrix
        0 0 0 1 T (T^2/2) 0 0 0;0 0 0 0 1 T 0 0 0;0 0 0 0 0 1 0 0 0;...
        0 0 0 0 0 0 1 T  (T^2/2);0 0 0 0 0 0 0 1 T;0 0 0 0 0 0 0 0 1];
    
    for n = 2:N+1
        px(n) = .5 * T.^2 * ax(1) + T * vx(n-1) + px(n-1); %Equation for position of x
        vx(n) = T * ax(1) + vx(n-1); %Equation for velocity of x
        
        py(n) = .5 * T.^2 * ay(1) + T * vy(n-1) + py(n-1); %Equation for position of y
        vy(n) = T * ay(1) + vy(n-1); %Equation for velocity of y
        
        pz(n) = .5 * T.^2 * az(1) + T * vz(n-1) + pz(n-1); %Equation for position of z
        vz(n) = T * az(1) + vz(n-1); %Equation for velocity of z
        
        q(:,n) = A*q(:,n-1); %Equation for time-varying state vector of x,y,z
    end
    x = q(1:3,:);
    y = q(4:6,:);
    z = q(7:9,:);
end
