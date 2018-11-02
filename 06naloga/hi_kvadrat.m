y=[41.6 , 37.7875 , 36.4975 , 35.785 , 34.53 , 42.345 , 39.5375 , 37.3525 , 36.36 , 33.915];
temp=[100 ,  161 , 227 , 270 , 362 , 90 , 149 , 206 , 247 , 352];
moc=[545 , 602 , 538 , 550 , 522 , 276 , 275 , 274 , 274 , 272];
napaka=[0.16 , 0.16 , 0.16 , 0.16 , 0.16 , 0.28 , 0.28 , 0.28 , 0.28 , 0.28];

L=length(napaka);

napaka=power(napaka,2)/power(L,2);



velikost=size(y);
n=velikost(2);
A=[ones(1,n);temp;power(temp,3);power(temp,4);moc; power(moc,2);power(moc,3)].';

b=y.';
c=napaka.';
[x,stdx,mse,S]= lscov(A,b,power(c,0.5));

fprintf('x:\n');
disp(x);

fprintf('stdx\n');
disp(stdx);

fprintf('mse\n');
disp(mse);

fprintf('s\n');
disp(S);

fprintf('fit tocke:\n');
tocke=A*x;
disp(tocke)

vsota=0;
for i=1:n
    delna=power(((tocke(i)-y(i))/napaka(i)),2);
    vsota=vsota+delna;
end

disp(vsota);