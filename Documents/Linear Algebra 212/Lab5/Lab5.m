[Rab] = R_Ladder_Fixed([2 1 3],[2 3 4]);
disp(Rab)

[R] = R_Ladder_Inf(5,3,10);
disp(R)
plot(R)
xlabel('number of stages')
ylabel('result of R')