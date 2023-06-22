function str=precision(h)
    pt = h.data;
    str=msprintf('X:%.11f\nY:%.11f', pt(1),pt(2))
endfunction

w = 0:0.00001:0.02

// степень колебательности системы
m = 0.22;

s = -m*w + sqrt(-1)*w

// передаточная функция
W = 53.0 ./ (10300.0 * s.^2 + 203.8 * s + 1) .* exp(-110 .* s);

W_inv = 1 ./ W

c0 = w * (m.^2 + 1) .* imag(W_inv)
c1 = m * imag(W_inv) - real(W_inv)

show_window(1);

plot(c1, c0);

xgrid()
