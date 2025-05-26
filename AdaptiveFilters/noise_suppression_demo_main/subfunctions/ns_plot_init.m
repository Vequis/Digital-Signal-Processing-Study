function dp_plot_init(plot_nr);

main_data = get(gcf,'UserData');

sim_active_tmp       = main_data.sim_active;
main_data.sim_active = 0;
set(gcf,'UserData',main_data);

if (plot_nr == 1)
    tag_axes                                  = 'demo_ns_axes_top';
    set(gcf,'CurrentAxes',findobj('Tag',tag_axes));
    plot_method                               = main_data.axes_top.plot_method;
    main_data.axes_top.index                  = 0;
    main_data.axes_top.plot_method_changed    = 0;
else
    tag_axes                                  = 'demo_ns_axes_bottom';
    set(gcf,'CurrentAxes',findobj('Tag',tag_axes)); 
    plot_method                               = main_data.axes_bottom.plot_method;
    main_data.axes_bottom.index               = 0;
    main_data.axes_bottom.plot_method_changed = 0;
end;

handle_1 = 0;
handle_2 = 0;

switch plot_method
    
    case 's_time'                       
        cla;  
        max_abs = max(abs([main_data.signals.s; main_data.signals.y; main_data.signals.s_dach]));
        t = (0:(length(main_data.signals.s)-1)) / main_data.f_s;
        plot(t,main_data.signals.s,'LineWidth',1);
        axis([0 length(main_data.signals.s)/main_data.f_s+eps -1.1*max_abs-eps 1.1*max_abs+eps])                
        handle_1 = line([-1 -1],[-1.2*max_abs-eps 1.2*max_abs+eps]);
        set(handle_1,'Color','k');
        set(handle_1,'LineWidth',2);
        %set(handle_1,'EraseMode','xor');                        
        grid on;  
        xlabel('Time in seconds');    
        legend('Undistorted speech signal - s(n)')
        
    case 's_tf'        
        cla;  
        [spec f t] = specgram(main_data.signals.s,512,main_data.f_s,hanning(512),512-64);
        imagesc(t,f/1000,20*log10(abs(spec)+eps));
        axis xy;     
        set(gca,'CLim',[-80 40]);
        handle_1 = line([-1 -1],[0 main_data.f_s]);
        set(handle_1,'Color','k');
        set(handle_1,'LineWidth',2);
        %set(handle_1,'EraseMode','xor');                        
        grid on;  
        xlabel('Time in seconds');
        ylabel('Frequency in kHz');
        legend('Undistorted speech signal - s(n)');
        
    case 'y_time'                       
        cla;  
        max_abs = max(abs([main_data.signals.s; main_data.signals.y; main_data.signals.s_dach]));
        t = (0:(length(main_data.signals.y)-1)) / main_data.f_s;
        plot(t,main_data.signals.y,'LineWidth',1);
        axis([0 length(main_data.signals.y)/main_data.f_s+eps -1.1*max_abs-eps 1.1*max_abs+eps])                
        handle_1 = line([-1 -1],[-1.2*max_abs-eps 1.2*max_abs+eps]);
        set(handle_1,'Color','k');
        set(handle_1,'LineWidth',2);
        %set(handle_1,'EraseMode','xor');                        
        grid on;  
        xlabel('Time in seconds');    
        legend('Microphone signal - y(n)')  
        
    case 'y_tf'        
        cla;  
        [spec f t] = specgram(main_data.signals.y,512,main_data.f_s,hanning(512),512-64);
        imagesc(t,f/1000,20*log10(abs(spec)+eps));
        axis xy;     
        set(gca,'CLim',[-80 40]);
        handle_1 = line([-1 -1],[0 main_data.f_s]);
        set(handle_1,'Color','k');
        set(handle_1,'LineWidth',2);
        %set(handle_1,'EraseMode','xor');                        
        grid on;  
        xlabel('Time in seconds');
        ylabel('Frequency in kHz');
        legend('Microphone signal - y(n)');        
        
    case 's_dach_time'                       
        cla;  
        max_abs = max(abs([main_data.signals.s; main_data.signals.y; main_data.signals.s_dach]));
        t = (0:(length(main_data.signals.y)-1)) / main_data.f_s;
        plot(t,main_data.signals.s_dach,'LineWidth',1);
        axis([0 length(main_data.signals.y)/main_data.f_s+eps -1.1*max_abs-eps 1.1*max_abs+eps])                
        handle_1 = line([-1 -1],[-1.2*max_abs-eps 1.2*max_abs+eps]);
        set(handle_1,'Color','k');
        set(handle_1,'LineWidth',2);
        %set(handle_1,'EraseMode','xor');                        
        grid on;  
        xlabel('Time in seconds');    
        legend('Output signal');    
        
    case 's_dach_tf'        
        cla;  
        [spec f t] = specgram(main_data.signals.s_dach,512,main_data.f_s,hanning(512),512-64);
        imagesc(t,f/1000,20*log10(abs(spec)+eps));
        axis xy;     
        set(gca,'CLim',[-80 40]);
        handle_1 = line([-1 -1],[0 main_data.f_s]);
        set(handle_1,'Color','k');
        set(handle_1,'LineWidth',2);
        %set(handle_1,'EraseMode','xor');                        
        grid on;  
        xlabel('Time in seconds');
        ylabel('Frequency in kHz');
        legend('Output signal');            
        
end;

drawnow;

if (plot_nr == 1)
    main_data.axes_top.plot_handle_1 = handle_1;
    main_data.axes_top.plot_handle_2 = handle_2;
else
    main_data.axes_bottom.plot_handle_1 = handle_1;
    main_data.axes_bottom.plot_handle_2 = handle_2;    
end;

set(gca,'Tag',tag_axes);


main_data.sim_active = sim_active_tmp;
set(gcf,'UserData',main_data);