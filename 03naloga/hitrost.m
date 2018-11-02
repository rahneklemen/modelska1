
%------------------------------------------funkcija-hitrost------------------------------
function skupaj = hitrost(v,v0,lamda)
format long;
vektor_velikost=size(v);
n=vektor_velikost(2);
dt=1/n;
vK=v0;

vsota1=0;
vsota2=0;
for i=1:n
    if i==1
        delna=0.5*((v0-v(i))/dt)^2;
    elseif i>1 && i<n
        delna=((v(i)-v(i-1))/dt)^2;
    else
        v(i)=vK;
        delna=0.5*((v(i)-v(i-1))/dt)^2;
    end
    vsota1=vsota1+delna;
end

for i=1:n
    if i==1
        delna=0.5*v0;
    elseif i>1 && i<n
        delna=v(i);
    else
        delna=0.5*v(i);
    end
    vsota2=vsota2-lamda*delna;
end
% vsota3=0;
% 
% for i=1:n
%     if i==1
%         delna=0.5*v0;
%     elseif i>1 && i<n
%         delna=v(i);
%     else
%         delna=0.5*v(i);
%     end
%     vsota3=vsota2-lamda*delna;
% end

skupaj=vsota1+vsota2;
end

    