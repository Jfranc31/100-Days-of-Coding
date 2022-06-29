[y_0,x_0] = poly_equi(0,3,-5.1,5.0,0.2);
[y_1,x_1] = poly_equi(1,[3 2],-5.1,5.0,0.2);
[y_2,x_2] = poly_equi(2,[3 2 2],-5.1,5.0,0.2);

figure
subplot(3,1,1)
plot(x_0,y_0)
xlabel('x values')
ylabel('y values')
subplot(3,1,2)
plot(x_1,y_1)
xlabel('x values')
ylabel('y values')
subplot(3,1,3)
plot(x_2,y_2)
xlabel('x values')
ylabel('y values')

[y,x,xm,min_max] = poly(1,-2,4,0.1);
figure
plot(x,y)
hold on
xline(xm, ':r', 'LineWidth',2)
yline(min_max, ':m', 'LineWidth',2)
xlabel('x values')
ylabel('y values')
