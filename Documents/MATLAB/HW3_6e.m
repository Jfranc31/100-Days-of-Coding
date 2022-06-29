clear;
close all;
clc;

Fs = 20000;
n = (1:1024);
x = 5*cos(.2*pi*n) + 4*cos(.205*pi*n);
X = fftshift(fft(x,8192));
omega = ((-8192/2):((8192/2)-1))*2*pi*8192;

plot(omega, abs(X), '-o')
title('|DFT| vs \Omega for 1024 Samples up to 8192')
xlabel('\Omega (rad/sample)')
ylabel('|DFT|')
xlim tight
ylim tight