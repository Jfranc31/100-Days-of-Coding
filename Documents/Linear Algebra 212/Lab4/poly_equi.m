function [y,x] = poly_equi(power,coeffs,xmin,xmax,del_x)
%
% USAGE: [y,x] = poly_equi(power,coeffs,xmin,xmax,del_x);
%
% Inputs: power = an integer specifying the highest power of the polynomial
% coeffs = a row vector of the polynomial's coefficients
% xmin = the desired minimum x value for evaluation
% xmax = the desired maximum x value for evaluation
% del_x = the desired spacing between the x values
%
% Output: x = a row vector of the x values
% y = a row vector of the y values
%
% Operation: if coeffs = [C_0 C_1 C_2 ... C_p], where p = power, this
% function computes
% In equation form, not in matlab syntax: y = C_0 + C_1x + C_2x^2 + ... +
% C_px^p
% First, generate the x values as a row vector
x = xmin:del_x:xmax; % this uses MATLAB's colon operator to generate
% equally spaced points at a spacing of del_x
for n=0:power
 % Loop through the powers in the polynomial
 % and compute a row vector for each of the terms in the polynomial
 % and put that row vectro into each row of matrix X
 X(n+1,:)=coeffs(n+1)*x.^n; % note use of "n+1" for indexing - matlab
 % can't index using "0"
end
% You now have a matrix X who's nth row is C_n*x.^n
% The x values run across this matrix, the power value runs down this matrix
% Now to create the values of y we have to add the rows together:
if power>0
 y=sum(X);
else
 y=X;
end