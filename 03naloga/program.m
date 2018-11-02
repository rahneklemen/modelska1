function program
n=25;
x=ones(1,n);

y1=bisekcija(x,-68.0,-68.7);
y=[5,y1];
fprintf('cel vektor');
disp(y);
disp(y);
velikost=size(y);
n=velikost(2);

t=ones(1,n);
for i =1:n
    t(i)=(i-1)/(n-1);
end
disp(t);
plot(t,y);
end