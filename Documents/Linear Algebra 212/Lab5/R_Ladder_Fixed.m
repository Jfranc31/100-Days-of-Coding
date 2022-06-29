function [Rab] = R_Ladder_Fixed(Rs,Rp)

if length(Rs) ~= length(Rp)
    error('Wrong Length of vector')
end

if any(Rs < 0) || any(Rp < 0)
    error('Value is less than zero')
end

n = length(Rp);
Re = Rp(n);

for i = n:2
    Rk = Rs(i) + Re;
    Re = ((Rk)*(Rp(i-1))/(Rk + Rp(i-1)));
end

Rab = Rs(1) + Re;

end

