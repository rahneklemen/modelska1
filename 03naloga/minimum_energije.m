%število nabojev (najboljše poljubno spreminjati):
n=12;


koti=ones(2,n);
for i =1:n
    koti(1,i)=2*pi/n*(i-1);
    koti(2,i)=pi/4*(i-0);
end

options = optimset('MaxFunEvals',1000000000000000000000000,'MaxIter',100000000000000);
[resitev,minim]=fminsearch(@energija,koti,options);
%tale metoda naj bi bila Neadel-Mead Simplex


%prikaz rešitve (prva vrsta kot fi, druga vrsta za kot theta. stolpec je i-ti naboj)
disp(resitev);

%se sprememba v kartezicne koordinate
z = cos(resitev(2,:));
x=z;
y=z;

x2=x;
y2=y;
z2=z;

%transforamcija, da je vedno en naboj na vrhu sfere.
%transformacijske matrike:
B=roty(-resitev(2,1)*180/pi);
C=rotz(-resitev(1,1)*18/pi);

A=B*C;

%pa se enacbe za transformacijo:
for i = 1:n
    x(i)=cos(resitev(1,i))*sin(resitev(2,i));
    y(i) = sin(resitev(1,i))*sin(resitev(2,i));
    
    x2(i)=A(1,1)*x(i)+A(1,2)*y(i)+A(1,3)*z(i);
    y2(i)=A(2,1)*x(i)+A(2,2)*y(i)+A(2,3)*z(i);
    z2(i)=A(3,1)*x(i)+A(3,2)*y(i)+A(3,3)*z(i);
end

%tocke za sfero:
[x1,y1,z1]=sphere(30);
%plot nabojev na sfero:
figure; surf(x1,y1,z1,'FaceAlpha', 0.4); hold on; scatter3(x2,y2,z2,100,'filled','red'), hold on; title(['N = ',num2str(n)]);

%---------------------------od tu naprej risanje grafa. odvisnost energije
%od stevila nabojev------------------------------------------------------
% dolzina=20;
% 
% energije=zeros(1,dolzina);
% naboj=energije;
% 
% 
% for i =1:dolzina
%     naboj(i)=i;
%     
%     koti=ones(2,i);
%     for j =1:i
%         koti(1,j)=2*pi/i*(j-1);
%         koti(2,j)=pi/4*(j-0);
%     end
%     
% 
%     options = optimset('MaxFunEvals',1000000000000000000000000,'MaxIter',100000000000000);
%     [resitev,minim]=fminsearch(@energija,koti,options);
%     energije(i)=minim;
% end
% 
% plot(naboj,energije);

    





