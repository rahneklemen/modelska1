y=[41.6 , 37.7875 , 36.4975 , 35.785 , 34.53 , 42.345 , 39.5375 , 37.3525 , 36.36 , 33.915]';
y_napake=[0.16 , 0.16 , 0.16 , 0.16 , 0.16 , 0.28, 0.28, 0.28, 0.28, 0.28];
moc=[545 , 602 , 538 , 550 , 522 , 276 , 275 , 274 , 274 , 272];

temp=[100 ,  161 , 227 , 270 , 362 , 90 , 149 , 206 , 247 , 352];

velikost=size(temp);

n=velikost(2);
enke=ones(1,n);
A=enke;
n=4;
m=3;

for i=1:n
    if i~=2
        B=A;
        A=[B;power(temp,i)];
    end
        
end

for i=1:m
    B=A;
    A=[B;power(moc,i)];
end

B=A';
A=B;
[b,m,r,rint,R]=regress(y,A);
disp(b);
fprintf('%10.10f \n',b);
fprintf('R=\t%10.10f \n',r);

disp(rint);
disp(R);

y2=A*b;
velikost=size(temp);

n=velikost(2);
goodness=hi_kvadrat(x,y',y_napake,y2');
disp(goodness);

b=A\y;
b=(A'*A)^(-1)*A'*y_napake;
disp(b);