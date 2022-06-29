% EECE 212
% lab 3
% Juan Franco

%TASK 2
load('lab3_data.mat')
D = datenum(2015,1,1:1/24/4:365+1);
D(:,35041) = [];
figure
subplot(2,1,1)
plot(D,E_union)
datetick('x')
ylabel('Energy (kWh)')
title('lab3 task2 2015 Union Energy Usage whole year')

subplot(2,1,2)
plot(D(1:2880),E_union(1:2880));
datetick('x',2,'keepticks')
ylabel('Energy (kWh)')
title('lab3 task2 2015 Union Energy Usage 1st month')

%TASK 3
figure
histogram(E_union,20)
xlabel('Energy(kWh)')
title('2015 Union Energy Usage Histogram')

%TASK 4
figure
s = surf(E_union_matrix);
s.EdgeColor = 'none';
s.FaceAlpha = 0.5;
xlabel('Days')
yticks([1 24 48 72 96])
yticklabels({'00:00','06:00','12:00','18:00','24:00'})
zlabel('kWh')
xlim([1 365])
ylim([1 96])
title('2015 Union Energy Usage 3D representation')

%TASK 5
figure
h = heatmap(E_union_matrix);
grid off
colormap(flipud(autumn));
xlabel('Days')
title('2015 Union Energy Usage Heatmap')