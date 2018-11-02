n=10;
x=zeros(1,n);
options = optimset('MaxFunEvals',1000000000000000000000000,'MaxIter',100000000000000);
[optimalna,minim]=fminsearch(@hitrost,x,options);


