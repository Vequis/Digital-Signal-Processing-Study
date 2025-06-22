%PRED_ERROR_FILTER calculate the prediction error filter  
%
%   [e, pred_error_gain, h_pef] = pred_error_filter(x, N) calculates the
%   prediction error filter of order N for the signal x and returns the
%   error signal e, the prediction error gain and the predition error coefficients
%
%   INPUT
%   x                   - Input signal
%   N                   - Prediction Order
%
%   OUTPUT
%   e                   - Error signal (Output of the filter)
%   pred_error_gain     - Prediction error gain
%   h_pef               - Prediction error coefficients
%
function [e, pred_error_gain, h_pef] = pred_error_filter(x, N)

    %Calculate the auto-correlation of x
    r_xx = xcorr(x, N, 'biased');
    
    %Calculate the prediction coefficients
    a = calculate_pred_coeffs(r_xx(N+1:end), N);
    
    %Define the prediction error coefficients
    h_pef = [1;-a];
    
    %Calculate the error signal (output of the filter) 
    e=conv(x(1:end-N), h_pef);
    
    %Calculate the prediction error gain
    pred_error_gain = var(x)/var(e);
end