# Text Parsing #

This task will look at parsing the data in some text files. 

## Current log ##

`power.txt` has some readings of the current being drawn from the PSU while I was testing some lights. 

Pull put the current values from the log. 

Figure out when the lights were on and when they were off. 

What was the average current draw of the lights?

## FPGA board power/temp log ##

The 4 `.log` files are logs of readings for the power and temperature sensors of an FPGA board. 

Write code to parse these log files.

Turn the timestamps into `datetime` objects.

Calculate the power used by the board for each log point (`power = current * voltage`).

Plot graphs of the power and temperatures.

### Errors ###

`20210107-test.log` and `20210108-test.log` include some error messages from when the USB connection to the FPGA was being used by other processes and the logging couldn't access it. Does you code handle these error messages? If not fix it so it does. 

## Timing checks ##

When building images for an FPGA there are a number of rules for the timing of signals. In the Intel tool chain there are tools to check that these rules are being followed but they don't output a nice pass/fail signal, rather files like `timing_report_1.txt` and `timing_report_2.txt`. 

Write a script to check all the `slack` and `tns` values in these reports for any values below 0. If you find any report the `Type` for that clock and the negative value(s). If everything is OK then display a message to say that. 

### Exit code ###

The usage for this script was in a CI pipeline to indicate if a build had completed successfully or had timing errors. The normal method of indicating errors for this is the return code of called process. Make your script give an exit code of 0 when there are no timing errors and a non-zero exit code when there are. 
