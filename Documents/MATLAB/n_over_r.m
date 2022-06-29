% ( n over r) (n!/((n-r)! * r!))
n = input('n = '); %Input value for n
r = input('r = '); %Input value for r
b = 1; %Initial value for b
d = 1; %Initial value for d
f = 1; %Initial value for f
y = n-r; %Initial value for y
for i = 1:n
   a = i * b; %Value for a
   b = a; %New value for b
end
for j = 1:r
   c = j * d; %Value for c
    d = c; %New value for d
end
for k = 1:y
   e = k * f; %Value for e
   f = e; %New value for f
end

answer = b / (d * f); %Value for answer
fprintf('\n')
disp(['Value is: ',num2str(answer)]) %Show value for answer