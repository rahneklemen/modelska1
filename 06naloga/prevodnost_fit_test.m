y=[41.6 , 37.7875 , 36.4975 , 35.785 , 34.53 , 42.345 , 39.5375 , 37.3525 , 36.36 , 33.915];
temp=[100 ,  161 , 227 , 270 , 362 , 90 , 149 , 206 , 247 , 352];
moc=[545 , 602 , 538 , 550 , 522 , 276 , 275 , 274 , 274 , 272];
napaka=[0.16 , 0.16 , 0.16 , 0.16 , 0.16 , 0.28 , 0.28 , 0.28 , 0.28 , 0.28];



velikost=size(y);
n=velikost(2);
H=[ones(1,n);temp;power(temp,3);power(temp,4);moc; power(moc,2);power(moc,3)].';

r=y.';
d=napaka.';
p = lin_reg_error(H,r,power(d,1));

disp(p);

vsota=0;
for i=1:n
    delna=power(((tocke(i)-y(i))/napaka(i)),2);
    vsota=vsota+delna;
end

disp(vsota);