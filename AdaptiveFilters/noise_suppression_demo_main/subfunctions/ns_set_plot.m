function ns_set_plot(val,axes_nr);

main_data = get(gcf,'UserData');

if (axes_nr == 1)
    switch val
        case 1
            main_data.axes_top.plot_method = 's_time';
        case 2
            main_data.axes_top.plot_method = 's_tf';
        case 3
            main_data.axes_top.plot_method = 'y_time';
        case 4
            main_data.axes_top.plot_method = 'y_tf';
        case 5
            main_data.axes_top.plot_method = 's_dach_time';
        case 6
            main_data.axes_top.plot_method = 's_dach_tf';
    end;
    set(gcf,'UserData',main_data);
    ns_plot_init(1);
else
    switch val
        case 1
            main_data.axes_bottom.plot_method = 's_time';
        case 2
            main_data.axes_bottom.plot_method = 's_tf';
        case 3
            main_data.axes_bottom.plot_method = 'y_time';
        case 4
            main_data.axes_bottom.plot_method = 'y_tf';
        case 5
            main_data.axes_bottom.plot_method = 's_dach_time';
        case 6
            main_data.axes_bottom.plot_method = 's_dach_tf';
    end;
    set(gcf,'UserData',main_data);
    ns_plot_init(2);    
end;

