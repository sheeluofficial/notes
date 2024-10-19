def sjf_non_preemptive_with_avg(processes, arrival_time, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    # Sorting processes based on burst time, if equal by arrival time
    processes = sorted(list(zip(processes, arrival_time, burst_time)), key=lambda x: (x[2], x[1]))

    # Calculate waiting and turnaround time
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

    # Calculate average waiting and turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

# Example usage:
processes = [1, 2, 3, 4]
arrival_time = [0, 1, 2, 3]
burst_time = [6, 2, 8, 3]

sjf_non_preemptive_with_avg(processes, arrival_time, burst_time)
