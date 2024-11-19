# CPU Scheduling Algorithms

## 1. First-Come, First-Served (FCFS)

### Characteristics:
- Non-preemptive.
- Processes are scheduled based on their arrival time.
- Works on a simple FIFO (First-In-First-Out) basis.

### Advantages:
- Simple to implement: Only requires a basic queue.
- Fair in terms of order: The first process to arrive is the first to get CPU time.
- No starvation: Every process eventually gets executed.

### Disadvantages:
- Convoy effect: A long process can delay all subsequent shorter processes.
- High waiting time: Shorter processes suffer if a long process arrives first.

### Example:
Consider three processes, P1, P2, and P3, with arrival and burst times as follows:

| Process | Arrival Time | Burst Time |
| ------- | -------------|------------|
| P1      | 0            | 8          |
| P2      | 1            | 4          |
| P3      | 2            | 2          |

Execution order (FCFS): P1 → P2 → P3

**Gantt Chart:**
| P1 | P1 | P1 | P1 | P1 | P1 | P1 | P1 | P2 | P2 | P2 | P2 | P3 | P3 | 0 1 2 3 4 5 6 7 8 9 10 11 12 13


**Average Waiting Time:**
- P1: 0, P2: 7, P3: 9  
- Total = (0 + 7 + 9) / 3 = **5.33 ms**

---

## 2. Shortest Job First (SJF)

### Characteristics:
- Non-preemptive.
- The process with the shortest burst time is executed next.
- Optimal for minimizing average waiting time if all burst times are known in advance.

### Advantages:
- Minimizes average waiting time compared to FCFS.
- Efficient in batch processing where the jobs' burst times are predictable.

### Disadvantages:
- Difficult to predict burst times: Not practical in real-time systems where burst times are unknown.
- Starvation: Longer processes can be postponed indefinitely if shorter jobs keep arriving.

### Example:
| Process | Arrival Time | Burst Time |
| ------- | -------------|------------|
| P1      | 0            | 8          |
| P2      | 1            | 4          |
| P3      | 2            | 2          |

Execution order (SJF): P3 → P2 → P1

**Gantt Chart:**
| P3 | P3 | P2 | P2 | P2 | P2 | P1 | P1 | P1 | P1 | P1 | P1 | P1 | P1 | 0 1 2 3 4 5 6 7 8 9 10 11 12 13

**Average Waiting Time:**
- P1: 6, P2: 2, P3: 0  
- Total = (6 + 2 + 0) / 3 = **2.67 ms**

---

## 3. Shortest Remaining Time First (SRTF)

### Characteristics:
- Preemptive version of SJF.
- If a new process arrives with a shorter remaining time than the current running process, it preempts the CPU.

### Advantages:
- Better average waiting time than SJF due to preemption.
- Ideal for systems with varying process lengths.

### Disadvantages:
- Frequent context switches: High overhead due to preemption.
- Starvation: Long processes may suffer from being preempted repeatedly.

### Example:
| Process | Arrival Time | Burst Time |
| ------- | -------------|------------|
| P1      | 0            | 8          |
| P2      | 1            | 4          |
| P3      | 2            | 2          |

Execution order (SRTF): P1 → P3 → P2 → P1

**Gantt Chart:**
| P1 | P1 | P3 | P3 | P2 | P2 | P2 | P2 | P1 | P1 | P1 | P1 | 0 1 2 3 4 5 6 7 8 9 10 11 

**Average Waiting Time:**
- P1: 7, P2: 2, P3: 0  
- Total = (7 + 2 + 0) / 3 = **3 ms**

---

## 4. Priority Scheduling

### Characteristics:
- Each process is assigned a priority.
- The process with the highest priority is selected for execution.
- Can be preemptive or non-preemptive. If two processes have the same priority, FCFS is used.

### Advantages:
- Allows prioritization of important tasks (e.g., system processes over user tasks).
- Can implement aging to prevent starvation.

### Disadvantages:
- Starvation: Low-priority processes may never get CPU time if higher-priority tasks keep arriving.

### Example:
| Process | Arrival Time | Burst Time | Priority |
| ------- | -------------|------------|----------|
| P1      | 0            | 8          | 3        |
| P2      | 1            | 4          | 1        |
| P3      | 2            | 2          | 2        |

Execution order (Priority): P2 → P3 → P1

**Gantt Chart:**
| P2 | P2 | P2 | P2 | P3 | P3 | P1 | P1 | P1 | P1 | P1 | P1 | P1 | P1 | 0 1 2 3 4 5 6 7 8 9 10 11 12 13

**Average Waiting Time:**
- P1: 6, P2: 0, P3: 4  
- Total = (6 + 0 + 4) / 3 = **3.33 ms**

---

## 5. Round Robin (RR)

### Characteristics:
- Time-sharing scheduling algorithm.
- Each process is given a fixed time quantum or time slice.
- Preemptive scheduling.

### Advantages:
- Fairness: Each process gets an equal share of the CPU in turn.
- Good response time: Ideal for time-sharing systems.

### Disadvantages:
- Depends on time quantum: Too short, frequent context switches; too long, behaves like FCFS.

### Example:
Assume time quantum is 4ms.

| Process | Arrival Time | Burst Time |
| ------- | -------------|------------|
| P1      | 0            | 8          |
| P2      | 1            | 4          |
| P3      | 2            | 2          |

Execution order (Round Robin): P1 → P2 → P3 → P1

**Gantt Chart:**
| P1 | P1 | P1 | P1 | P2 | P2 | P2 | P2 | P3 | P3 | P1 | P1 | P1 | P1 | 0 1 2 3 4 5 6 7 8 9 10 11 12 13

**Average Waiting Time:**
- P1: 4, P2: 5, P3: 6  
- Total = (4 + 5 + 6) / 3 = **5 ms**

---

## 6. Multi-Level Queue Scheduling (MLQS)

### Characteristics:
- Processes are divided into different priority queues.
- Each queue has its own scheduling algorithm.

### Advantages:
- Separation of process types: High-priority processes are treated differently from lower-priority ones.

### Disadvantages:
- Rigid structure: Processes cannot move between queues.

### Example:
Consider three priority queues:
- Queue 1 (interactive, time quantum 4ms, RR)
- Queue 2 (system, FCFS)
- Queue 3 (batch, FCFS)

| Process | Burst Time | Queue Type  |
| ------- | -----------|-------------|
| P1      | 3          | Interactive |
| P2      | 8          | System      |
| P3      | 12         | Batch       |

Execution order: P1 → P2 → P3

**Gantt Chart:**
| P1 | P2 | P2 | P2 | P2 | P2 | P2 | P2 | P2 | P3 | P3 | P3 | P3 | P3 | P3 | P3 | P3 | P3 | P3 | P3 | P3 | 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21

**Average Waiting Time:**
- P1: 0ms, P2: 3ms, P3: 8ms  
- Total = (0 + 3 + 8) / 3 = **3.67ms**

---

## 7. Multi-Level Feedback Queue Scheduling (MLFQ)

### Characteristics:
- Dynamic version of MLQS.
- Processes can move between queues based on their behavior and CPU usage.

### Advantages:
- Flexible: Processes can be demoted or promoted based on their usage, leading to better performance.
- Suitable for general-purpose systems where process characteristics vary widely.

### Disadvantages:
- Complex to implement: Requires tuning of multiple parameters like queue behavior, time quanta, and promotion/demotion rules.

**Conclusion:**
Different scheduling algorithms are suitable for different types of systems. FCFS is simple but inefficient in many cases, while SJF/SRTF minimizes waiting time but can lead to starvation. Priority scheduling adds another layer of complexity by allowing higher-priority tasks to be served first. RR is ideal for fairness in time-sharing systems. MLQS and MLFQ are more advanced algorithms that offer more flexibility but come with increased complexity.
