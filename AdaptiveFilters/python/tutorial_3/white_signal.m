%WHITE_SIGNAL generate a white signal
%
%   x = white_signal(M) generates a white signal of lenght M with
%   (sigma_x)^2 = 1
%
%   INPUT
%   M       - Length of the signal
%
%   OUTPUT
%   x       - White signal
function x = white_signal(M)

    %Compute white signal.
    x = ((rand(1,M)-0.5)*2*sqrt(3))';
    
end
