%CALCULATE_PRED_COEFFS calculate predictor coefficients
%
%   [a,E_min] = calculate_pred_coeffs(r_xx,N) calculates the predictor
%   coefficients a using the Levinson-Durbin-Recursion up to the order N 
%   for a given auto-correlation function r_xx.
%
%   INPUT
%   r_xx    - Auto-correlation function (vector)
%   N       - Prediction order N
%
%   OUTPUT
%   a       - Prediction coefficients
%   E_min   - Error signal power (minimum) for each recursions setp
%

function [a, E_min] = calculate_pred_coeffs(r_xx, N)
    %GENERAL REMARK: MATLAB matrix indices start at 1, not at 0!
    %Extend the length of r_xx to N if it is smaller 
    if length(r_xx) <= N
        r_xx(N+1) = 0;
    end                        
    
    %Initialization of the Levinson-Durbin-Recursion
    a(1) = r_xx(2)/r_xx(1); %First index in Matlab: 1 not 0!
    E_min = zeros(1,N);
    E_min(1) = r_xx(1);
    
    %Levinson-Durbin-Recursion (iterative) up to order N
    for i=2:N
        %Calculate parcor (reflection) coefficient
        parcor = (r_xx(i+1) - r_xx(2:i)'*a(end:-1:1))/(r_xx(1)-r_xx(2:i)'*a);
        %Calculate new prediction coefficients
 
        a = a - parcor*a(end:-1:1);
        a(i,:) = parcor;
        %Calculate new error power (minimum)
        E_min(i) = E_min(i-1)*(1-abs(parcor).^2);
    end
end