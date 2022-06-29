clear;
close all;
clc;

Fs = 20000;
T = 1/Fs;
t = (1:1024)*T;
x = 5*cos(2*pi*2000*t) + 4*cos(2*pi*2050*t);
X = fftshift(fft(x));
omega = ((-1024/2):((1024/2)-1))*2*pi*1024;

plot(omega, abs(X), '-o')
title('|DFT| vs \Omega for 1024 Samples' )
xlabel('\Omega (rad/sample)')
ylabel('|DFT|')
xlim tight
ylim tight