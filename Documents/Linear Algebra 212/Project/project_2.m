%%
N = 60; %Amount of time/points
T = 1;
Px = 0; %Initial value of x
Py = 0; %Initial value of y
Vx = 100; %Initial velocity of x
Vy = 100; %Initial velocity of y
sigx = 1;
sigy = 10;

[q] = gen_state(N,T,Px,Py,Vx,Vy,sigx,sigy);

%%
p = 4;
N = 60; %Amount of time/points
C = eye(p); %Identity matrix
d = [25;10;25;10]; %Noise for the position and velocity of x and y

[y] = measure_state(p,N,C,d,q);

%%
figure
plot(q(1,:),q(3,:), '-r*','DisplayName','Real Position')
hold on
plot(y(1,:), y(3,:), '-bo','DisplayName','Measured Position')
title({('Sensor Measurement of a 2D Aircraft Trajectory')
    ['Sigma-x = ' num2str(sigx) ' and Sigma-y = ' num2str(sigy)]
    ['D = [' num2str(d(1)) '; ' num2str(d(2)) '; ' num2str(d(3)) '; ' num2str(d(4)) ']']})
xlabel('x position')
ylabel('y position')
hold off
legend('Location','southeast')

xdifference = q(1,:)-y(1,:);
xvdifference = q(2,:)-y(2,:);
ydifference = q(3,:)-y(3,:);
yvdifference = q(4,:)-y(4,:);

%%
figure
subplot(2,1,1)
plot(xdifference,'-r*','DisplayName','X-Values')
hold on
plot(ydifference,'-bs','DisplayName','Y-Values')
title('Difference Between Real and Measured Values for Position')
xlabel('Time')
xlim([0 60])
ylabel('Position (m)')
hold off
legend

subplot(2,1,2)
plot(xvdifference,'-m^','DisplayName','Xv-Values')
hold on
plot(yvdifference,'-gp','DisplayName','Yv-Values')
title('Difference Between Real and Measured Values for Velocity')
xlabel('Time')
xlim([0 60])
ylabel('Velocity (m/s)')
hold off
legend