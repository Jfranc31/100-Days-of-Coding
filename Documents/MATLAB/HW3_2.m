w = -20:.01:20;
X = .5*((1-.5*exp(-1i*(w+4))))+(1./(1-.5*exp(-1i*(w-4))));

subplot(2,1,1)
plot(w,abs(X))
grid
xlabel('\Omega (rad/sec)')
ylabel('|x(\Omega)|')

subplot(2,1,2)
plot(w,angle(X))
grid
xlabel('\Omega (rad/sec')
ylabel('<X(\Omega) (rad)')