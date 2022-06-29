% Quadratic Value  
a = input('a = '); %Input value for a
b = input('b = '); %Input value for b
c = input('c = '); %Input value for c
fprintf('\n')
Answer1 = ((-b)+((b^2-4*a*c))^0.5)/(2*a); %Positive value for quadratic
Answer2 = ((-b)-((b^2-4*a*c))^0.5)/(2*a); %Negative value for quadratic
disp(['x is: ',num2str(Answer1),' & ',num2str(Answer2)]) %Show both values