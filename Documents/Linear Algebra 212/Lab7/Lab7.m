%% Plot a vector in Matlab
a = [2 3 4];
figure
quiver3(0,0,0,a(1),a(2),a(3))
axis equal
xlabel('x')
ylabel('y')
zlabel('z')

%% Projection
P_x = [2 0 0];
figure
quiver3(0,0,0,a(1),a(2),a(3))
hold on
quiver3(0,0,0,P_x(1),P_x(2),P_x(3))
axis equal
xlabel('x')
ylabel('y')
zlabel('z')
title('Figure 1.1')
hold off

P_xy = [2 3 0];
figure
quiver3(0,0,0,a(1),a(2),a(3))
hold on
quiver3(0,0,0,P_xy(1),P_xy(2),P_xy(3))
axis equal
xlabel('x')
ylabel('y')
zlabel('z')
title('Figure 1.2')
hold off

%% Rotation Matrix
figure
x = 30;
Rz = [cosd(x) -sind(x) 0;sind(x) cosd(x) 0;0 0 1];
R1 = Rz * transpose(P_x);
quiver3(0,0,0,R1(1,1),R1(2,1),R1(3,1))
hold on
quiver3(0,0,0,2,0,0)
axis equal
xlabel('x')
ylabel('y')
zlabel('z')
title('Figure 2.1')
hold off

figure
y = 30;
Ry = [cosd(y) 0 sind(y);0 1 0;-sind(y) 0 cosd(y)];
R2 = Ry * transpose(P_x);
quiver3(0,0,0,R2(1,1),R2(2,1),R2(3,1))
hold on
quiver3(0,0,0,P_x(1),P_x(2),P_x(3))
axis equal
xlabel('x')
ylabel('y')
zlabel('z')
title('Figure 2.2')
hold off

%% Image compression by SVD
raw = imread('cameraman.tif');
UFO=imread('UFO.png');

UFO1=255-UFO;
raw(60:95,171:251)=raw(60:95,171:251)+UFO1;
raw(60:95,171:251)=raw(60:95,171:251)-UFO1;

figure
imshow(raw)
drawnow;
title('Figure 3.1 Cameraman VS UFO')


raw = imread('cameraman.tif');

A=single(raw);
%I=uint8(A);
%imshow(I);
[U,S,V] = svd(A);
%A_new=U*S*V';
%imshow(uint8(A_new));

figure
subplot(2,2,1)
imshow(raw);
title('raw')

S2=[S(:,1:2) zeros(256,256-2)];
A_2=U*S2*V';

subplot(2,2,2)
imshow(uint8(A_2));
title('n=2')

S32=[S(:,1:32) zeros(256,256-32)];
A_32=U*S32*V';

subplot(2,2,3)
imshow(uint8(A_32))
title('n=32')

S128=[S(:,1:128) zeros(256,256-128)];
A_128=U*S128*V';

subplot(2,2,4)
imshow(uint8(A_128))
title('n=128')