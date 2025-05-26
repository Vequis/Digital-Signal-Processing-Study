function ns_play_speech_signal;

%**************************************************************************
% Get all necessary variables
%**************************************************************************

main_data = get(gcf,'UserData');

%**************************************************************************
% Compute the length of the signal in seconds
%**************************************************************************

len_sec = length(main_data.signals.s) / main_data.f_s;

%**************************************************************************
% Set bottom axis as drawing destination
%**************************************************************************

tag_axes_top    = 'demo_ns_axes_top';
tag_axes_bottom = 'demo_ns_axes_bottom';

%**************************************************************************
% Start sound output
%**************************************************************************

soundsc(main_data.signals.s,main_data.f_s);

%**************************************************************************
% Update line in the lower axis
%**************************************************************************

tic;
while (toc < len_sec)
    t = toc;
    set(gcf,'CurrentAxes',findobj('Tag',tag_axes_top)); 
    set(main_data.axes_top.plot_handle_1,'XData',[t t]);
    set(gcf,'CurrentAxes',findobj('Tag',tag_axes_bottom)); 
    set(main_data.axes_bottom.plot_handle_1,'XData',[t t]);    
    drawnow;
end;

set(main_data.axes_top.plot_handle_1,'XData',[-1 -1]);
set(main_data.axes_bottom.plot_handle_1,'XData',[-1 -1]);
drawnow;