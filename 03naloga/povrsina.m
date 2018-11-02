function vsota=povrsina(x)
vektor_velikost=size(x);
n=vektor_velikost(2);
dt=1/n;
vsota=(sum(x)-0.5*(x(1)+x(n)))*dt;
end