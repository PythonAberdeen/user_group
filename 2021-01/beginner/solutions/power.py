def parse_power_log(fn="../power.txt"):
    with open(fn) as f:
        log = [float(l.split()[3]) for l in f if l]
    return log

def on_off_points(log, cutoff):
    for i in range(1, len(log)):
        if log[i] < cutoff and log[i-1] > cutoff:
            print(f"Switch off at {i}")
        if log[i] > cutoff and log[i-1] < cutoff:
            print(f"Switch on at {i}")

def average(l):
    return sum(l) / len(l)

if __name__=="__main__":
    log = parse_power_log()
    avg = average(log)
    on_off_points(log, avg)
    on_vals = [p for p in log if p > avg]
    off_vals = [p for p in log if p < avg]
    lights_curr = average(on_vals) - average(off_vals)
    print(f"Average current draw for lights: {lights_curr:.3f}A ({12*lights_curr:.3f}W)")
    
        
