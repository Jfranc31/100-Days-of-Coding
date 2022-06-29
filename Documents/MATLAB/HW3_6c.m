clear;
close all;
clc;

Fs = 20000;
n = (1:64);
x = 5*cos(0.2*n) + 4*cos(0.205*pi*n);
X = fftshift(fft(x,2048));
omega = ((-2048/2):((2048/2)-1))*2*pi*2048;

plot(omega, abs(X), '-o')
title('|DFT| vs \Omega for 64 Samples to 2048')
xlabel('\Omega (rad/sample)')
ylabel('|DFT|')
xlim tight
ylim tight