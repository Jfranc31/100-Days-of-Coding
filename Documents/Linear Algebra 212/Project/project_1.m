%%
N = 60; %Amount of time/points
T = 1;
Px = 0; %Initial value of x
Py = 0; %Initial value of y
Vx = 100; %Initial velocity of x
Vy = 100; %Initial velocity of y
sigx = 0;
sigy = 0;

[q] = gen_state(N,T,Px,Py,Vx,Vy,sigx,sigy);

%%
figure
plot(q(1,:), q(3,:), '-r*')
hold on
xlabel('x position')
ylabel('y position')
str = sprintf('2D Aircraft Trajectory with Sigma-x = %d and Sigma-y = %d', sigx, sigy);
title(str)
hold off

%%
N = 60; %Amount of time/points
T = 1;
Px = 0; %Initial value of x
Py = 0; %Initial value of y
Vx = 100; %Initial velocity of x
Vy = 100; %Initial velocity of y
sigx = 5;
sigy = 10;

[q] = gen_state(N,T,Px,Py,Vx,Vy,sigx,sigy);

%%
figure
plot(q(1,:), q(3,:), '-r*')
hold on
xlabel('x position')
ylabel('y position')
str = sprintf('2D Aircraft Trajectory with Sigma-x = %d and Sigma-y = %d', sigx, sigy);
title(str)
hold off