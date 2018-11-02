function zakljucek = bisekcija(x, spodnja,zgornja)

lamda=(spodnja+zgornja)/2;
v0=5;

f = @(x)hitrost(x,v0,lamda);

options = optimset('MaxFunEvals',1000000000000000000000000,'MaxIter',100000000000000);
x = fminsearch(f,x,options);
omejitev=povrsina(x);
fprintf('povrsina:%d \tlamda:%0.20f \n',omejitev,lamda);



if omejitev>1
    fprintf('povrsina vecja\n');
    zakljucek=bisekcija(x,spodnja,lamda);
elseif omejitev<0.995
    fprintf('povrsina manjsa\n');
    zakljucek=bisekcija(x,lamda,zgornja);
else
    zakljucek=x;
    disp(x);
end

end

