def fcfs_scheduling(processes, arrival_time, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculating waiting time
    for i in range(1, n):
        waiting_time[i] = burst_time[i-1] + waiting_time[i-1]

    # Calculating turnaround time
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    # Display results
    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

# Example usage:
processes = [1, 2, 3]
arrival_time = [0, 1, 2]
burst_time = [10, 5, 8]

fcfs_scheduling(processes, arrival_time, burst_time)
