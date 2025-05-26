function w = noise_generator(N)
%NOISE_GENERATOR Generates N samples of almost pink noise by filtering a
%white noise process
w_white = randn(N,1);
b = [0.049922035, -0.095993537, 0.050612699, -0.004408786];
a = [1, -2.494956002, 2.017265875, -0.522189400];
w = filter(b,a,w_white);
end