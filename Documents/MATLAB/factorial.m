% Factorial Value
n = input('Input value for n in n!: '); %Input value for n
b = 1; %Initial value for b
for i = 1:n
   a = i * b; %Value for a
   b = a; %New value for b
   disp(b)
end
fprintf('\n')
disp(['Value is: ',num2str(b)]) %Show value for b