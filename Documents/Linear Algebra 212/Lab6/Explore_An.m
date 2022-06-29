D = [0.8 0.2;0.4 0.6];
D3 = zeros(2,2,100);
figure
for i = 1:100
    D3(:,:,i) = D^i;
    plot(i,D3(1,1,i),'sr',i,D3(1,2,i),'db',i,D3(2,1,i),'pk',i,D3(2,2,i),'hg')
    title('D to the power 1~100')
    hold on
end
hold off
%%
E = [0.7 0.2;0.4 0.6];
E3 = zeros(2,2,100);
figure
for i = 1:100
    E3(:,:,i) = E^i;
    plot(i,E3(1,1,i),'sr',i,E3(1,2,i),'db',i,E3(2,1,i),'pk',i,E3(2,2,i),'hg')
    title('E to the power 1~100')
    hold on
end
hold off
%%
F = [0.9 0.2;0.4 0.6];
F3 = zeros(2,2,100);
figure
for i = 1:100
    F3(:,:,i) = F^i;
    plot(i,F3(1,1,i),'sr',i,F3(1,2,i),'db',i,F3(2,1,i),'pk',i,F3(2,2,i),'hg')
    title('F to the power 1~100')
    hold on
end
hold off
