function [y,x, xm, min_max] = poly(a,b,c,z)
%
%USAGE [y,x,xm,min_max] = poly(a,b,c,z);
%
%Inputs: a = Coefficient for x^2
% b = Coefficient for x
% c = an integer
% z = spacing for x axis
%
%Output: x = a row vector of the x values
% y = a row vector of the y values
% xm = The x value of the min/max
% min_max = The y value of the min/max
%
% Operation: if a,b,c, and z equal a value, then the function computes
%
% First, generate x value for the min/max
xm = -b / (2 * a); % Equation for finding the min/max

x = xm-5:z:xm+5; % Equally spaced points at a spacing of z
yf = @(x, a, b, c) a*x.^2 + b*x + c; % Function for a quadratic
y = yf(x,a,b,c); % Gives the values for the y for each x

min_max = yf(xm,a,b,c); % Takes values to give the value of the min/max

disp(['x value where the min/max occurs is ', num2str(xm)]) % Displays the 
% string that gives the value for the x
disp(['value of the min/max is ', num2str(min_max)]) % Displys the string
% that gives the value for the min/max
end