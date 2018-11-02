function energija = energija(x)
%vsota = energija(x)
%funkcija, ki izracuna energijo (brez konstant: samo 1/(r_i-r_j)) nabojev porazdeljene po sferi, z radijem
%r=1, ter koti fi(prva vrstica x-a) in kot theta(druga vrstica x-a)
v=size(x);
n=v(2);
zacetek=0;

for i =1:n
    for j =1:i
        if i~=j
            delno=1/(sqrt(abs(2-2*sin(x(2,i))*sin(x(2,j))*cos(x(1,i)-x(1,j))-2*cos(x(2,i))*cos(x(2,j)))));
            zacetek=zacetek+delno;
        end
           
    end
end
energija=zacetek;
