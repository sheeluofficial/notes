def sjf_non_preemptive(processes, arrival_time, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completed = [False] * n
    
    # Sort by burst time, if equal by arrival time
    processes = sorted(list(zip(processes, arrival_time, burst_time)), key=lambda x: (x[2], x[1]))

    # Calculate waiting time and turnaround time
    current_time = 0
    for i in range(n):
        pid, at, bt = processes[i]
        
        if current_time < at:
            current_time = at
            
        waiting_time[i] = current_time - at
        current_time += bt
        turnaround_time[i] = waiting_time[i] + bt
    
    # Display results
    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        pid, at, bt = processes[i]
        print(f"{pid}\t{at}\t\t{bt}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

# Example usage:
processes = [1, 2, 3]
arrival_time = [0, 1, 2]
burst_time = [7, 4, 1]

sjf_non_preemptive(processes, arrival_time, burst_time)
