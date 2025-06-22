%AR1 correlate an input by using an autoregressive (AR) process of order 1
%
%   x_ar=ar1(x) correlates the signal x by using an AR(1) process
%
%   INPUT
%   x       - Input signal
%
%   OUTPUT
%   x_ar    - Correlated output signal
%
function x_ar = ar1(x)

    %Define the correlation coefficient.
    corr = 0.9;
    
    %Initialize the correlated signal.
    x_ar(1) = x(1);
    
    %Perform the correlation
    for i=2:length(x)
        %Calculate x_ar(i) depending on the actual value of x and the pervious value
        %of x_ar.
        x_ar(i,:) = x(i) + corr*x_ar(i-1);
    end
end