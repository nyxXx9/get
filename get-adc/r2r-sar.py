import r2r_adc as adc
import adc_plot as plot
import time

ADC = adc.R2R_ADC(3.3)
voltages = []
times = []
duration = 3.0

try:
    start_time = time.time()
    while (time.time() - start_time < duration):
        value = ADC.get_sar_voltage()
        current_time = time.time()-start_time

        voltages.append(value)
        times.append(current_time)
        
    plot.plot_voltage_vs_time(times, voltages, ADC.dynamic_range*1.1)
    plot.plot_sampling_period_hist(times)
finally:
    ADC.deinit()
