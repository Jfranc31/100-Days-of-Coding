%%
N = 60; %Amount of time/points
T = 1;
Px = 0; %Initial value of x
Py = 0; %Initial value of y
Vx = 100; %Initial velocity of x
Vy = 100; %Initial velocity of y
sigx = 5;
sigy = 5;

[q] = gen_state(N,T,Px,Py,Vx,Vy,sigx,sigy);

%%
p = 4;
N = 60; %Amount of time/points
C = eye(p); %Identity matrix
d = [25;10;25;10]; %Noise for the position and velocity of x and y

[y] = measure_state(p,N,C,d,q);

%%
A = [1 T 0 0;0 1 0 0;0 0 1 T;0 0 0 1]; %State Transition matrix
R = eye(p)*0.98; %Identity matrix with forgetting factor

[q_hat] = RLS_estimation(A,y,R);
q_hat(:,1)=[];

%%
hold on
plot(q(1,:),q(3,:),'-r*','DisplayName','Real Position')
plot(y(1,:), y(3,:), '-bo','DisplayName','Measured Position')
plot(q_hat(1,:),q_hat(3,:), '-c^','DisplayName','Estimated Position')
title({('2D Aircraft Trajectory')
    ['Sigma-x = ' num2str(sigx) ' and Sigma-y = ' num2str(sigy)]
    ['D = [' num2str(d(1)) '; ' num2str(d(2)) '; ' num2str(d(3)) '; ' num2str(d(4)) ']']})
xlabel('x position')
ylabel('y position')
hold off
legend('Location','southeast')