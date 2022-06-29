function [Rk] = R_Ladder_Inf(R,alpha,N)

for x = R
    if length(x) ~= 1
        error('Wrong Length of resistance value')
    end
    if x < 0
        error('Value of the resistance is less than zero')
    end
end

for x = alpha
    if length(x) ~= 1
        error('Wrong Length of alpha value')
    end
    if x < 0
        error('Value of the alpha is less than zero')
    end
end

for x = N
    if length(x) ~= 1
        error('Wrong Length of N value')
    end
    if x < 0
        error('Value of the N is less than zero')
    end
end

Rk = zeros(1,N);
Rk(1) = R + R;
stop = true;
i = 2;
while stop
    Rk(i) = ((Rk(i-1)*R)/(Rk(i-1)+R))+R;
    c = abs(Rk(i) - Rk(i-1));
    if (c > alpha) || (i == N)
        warning('Loop has reached maximum number of iterations') 
        stop = false;
    end
    i = i + 1;
end
Rk = Rk(1:i-1);
end