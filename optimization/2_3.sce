function z = f(x1, x2)
    z = (x1-2).^2 + (x2-5).^2;
endfunction
[X1, X2]=meshgrid(-100:1:100, -100:1:100);
Z=f(X1, X2);

mesh(X1, X2, Z);
xgrid;

function w=fv(z)
    w = (z(1)-2).^2 + (z(2)-5).^2;
endfunction
z0=[1 0];
[zmin fmin]=fminsearch(fv, z0)
disp(zmin)
