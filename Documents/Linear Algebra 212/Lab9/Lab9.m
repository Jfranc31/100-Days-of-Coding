[tsv] = const_state_1D(100,0.1,10,0,1);

figure
plot(tsv(1,:))
hold on
title('Position vs. Time')
xlabel('Time')
ylabel('Position')
hold off

figure
plot(tsv(2,:))
hold on
title('Speed vs. Time')
xlabel('Time')
ylabel('Speed')
hold off

figure
plot(tsv(1,:),'DisplayName','Position')
hold on
plot(tsv(2,:),'DisplayName','Speed')
title('Position and Speed vs. Time')
xlabel('Time')
ylabel('Displacement and Distance per time')
hold off
legend

[x,y,z] = const_state_3D(100,0.1,10,0,1,10,0,1,0,10,0);

figure
plot3(x(1,:),y(1,:),z(1,:))
hold on
title('x-position vs y-position vs z-position')
xlabel('x-position')
ylabel('y-position')
zlabel('z-position')
hold off

% figure
% plot3(x(2,:),y(2,:),z(2,:))
% hold on
% title('x-position vs y-position vs z-position')
% xlabel('x-position')
% ylabel('y-position')
% zlabel('z-position')

% figure
% plot3(x(3,:),y(3,:),z(3,:))
% hold on
% title('x-position vs y-position vs z-position')
% xlabel('x-position')
% ylabel('y-position')
% zlabel('z-position')
