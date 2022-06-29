% Data = load('Lab10_data');
% 
% A = [1 0.1 0.005;0 1 0.1;0 0 1];
% b = [Data.p_without_noise(100,2);9.9;1];
% [x,t0] = LS_estimation(A,b);
% 
% figure
% plot(Data.p_without_noise(:,2), '-*','DisplayName','Original Data')
% hold on
% plot(x(1,:),'DisplayName','Estimated Position')
% xlabel('Time Index')
% ylabel('Position')
% title('Position for Without Noise')
% hold off
% legend
% fprintf('Estimated without Noise');
% fprintf('\n')
% fprintf(['p[0]: ',num2str(t0(1))]);
% fprintf('\n')
% fprintf(['v[0]: ',num2str(t0(2))]);
% fprintf('\n')
% fprintf(['a[0]: ',num2str(t0(3))]);
% fprintf('\n')
% 
% fprintf('\n')
% 
% A = [1 0.1 0.005;0 1 0.1;0 0 1];
% b = [Data.p_with_noise(100,2);9.9;1];
% [x,t0] = LS_estimation(A,b);
% 
% figure
% plot(Data.p_with_noise(:,2),'-*','DisplayName','Original Data')
% hold on
% plot(x(1,:),'DisplayName','Estimated Position')
% xlabel('Time Index')
% ylabel('Position')
% title('Position for With Noise')
% legend
% hold off
% fprintf('Estimated with Noise');
% fprintf('\n')
% fprintf(['p[0]: ',num2str(t0(1))]);
% fprintf('\n')
% fprintf(['v[0]: ',num2str(t0(2))]);
% fprintf('\n')
% fprintf(['a[0]: ',num2str(t0(3))]);
% fprintf('\n')

%%%No Noise %%%%
Data= load("Lab10_data.mat"); %%Load in the data
Nonoise= Data.p_without_noise; %%take the struct as the b value
A1= ones(100,3); %%Establishes the A matrix
Time= Nonoise(:,1);
Timesq= Time.^2;
A1(:,2)= Time;
A1(:,3)= Timesq;
B1=Nonoise(:,2); 
x1= LS_estimation(A1,B1);%%uses the function
%%Line of best fit graph%%
a= (x1(3));
v= (x1(2));%%establishes acceleration, velocity and position as parts of x hat
p= (x1(1));
bestfit= zeros(1,100);
n=1;
 for t= 0:.1:9.9 %%evaluates the line of best fit from 0 to 9.9 seconds
     quad = ((a)*(t^2))+ (v*t) + p;
     bestfit(:,n)= quad;
     n=n+1;
 end
figure 
hold on;
plot(Nonoise(:,1),Nonoise(:,2),'r:'); %%plots the original graph
plot(Nonoise(:,1),bestfit,'b-'); %%plots the best fit line
legend('Best fit','Original')
title('Plotting the Line of Best Fit with No Noise')
hold off;
disp('At Time =0 ');
disp(['Acceleration : ' num2str(x1(3))]); %%shows the value at t=0
disp(['Velocity : ' num2str(x1(2))]);
disp(['Position : ' num2str(bestfit(1))]);
fprintf('\n')
%%%Noise included%%%%
Noise=Data.p_with_noise;
A2= ones(100,3);
At2= A2.';
Time= Nonoise(:,1);
Timesq= Time.^2;
A2(:,2)= Time;
A2(:,3)= Timesq;
B2=Noise(:,2);
x2= LS_estimation(A2,B2);
%%Line of best fit Noise graph%%
a2= (x2(3));
v2= (x2(2));
p2= (x2(1));
bestfit2= zeros(1,100);
n=1;
 for t= 0:.1:9.9
     quad = ((a2)*(t^2))+ (v2*t) + p2;
     bestfit2(:,n)= quad;
     n=n+1;
 end
figure 
hold on;
plot(Noise(:,1),Noise(:,2),'r:');
plot(Noise(:,1),bestfit2,'b-');
legend('Best fit','Original')
title('Plotting the Line of Best Fit with Noise')
hold off;
disp('At Time =0 ');
disp(['Acceleration : ' num2str(x2(3))]); %%shows the value at t=0 for the noise graph
disp(['Velocity : ' num2str(x2(2))]);
disp(['Position : ' num2str(bestfit2(1))]);