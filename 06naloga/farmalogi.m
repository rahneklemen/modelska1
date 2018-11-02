A=importdata('farmakoloski.dat');
A.data;
disp(A.data);
x_data=A.data(:,1);
y_data=A.data(:,2);

disp(x_data);
disp(y_data);
x=1./x_data;
y=1./y_data;

velikost=size(y);
n=velikost(1);
disp(n);

enke=ones(n,1);
disp(enke);
matrika=[x,enke];
b = regress(y,matrika);
fprintf('fit koeficienti');
disp(b);

a=polyfit(x,y,1);
rez=polyval(a,x);
disp(a);
fprintf('%f, %f',a(1),a(2));


plot(x,y,'d',x,rez);


disp(matrika\y)