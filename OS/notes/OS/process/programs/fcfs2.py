def fcfs_scheduling_with_avg(processes, arrival_time, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    
    # First process
    completion_time[0] = burst_time[0]
    turnaround_time[0] = completion_time[0] - arrival_time[0]
    waiting_time[0] = turnaround_time[0] - burst_time[0]
    
    # Calculating completion, turnaround, and waiting time for each process
    for i in range(1, n):
        completion_time[i] = completion_time[i - 1] + burst_time[i]
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]

    # Display results
    print("Process\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{completion_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    # Calculate average waiting and turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

# Example usage:
processes = [1, 2, 3, 4]
arrival_time = [0, 1, 2, 3]
burst_time = [6, 2, 8, 3]

fcfs_scheduling_with_avg(processes, arrival_time, burst_time)
