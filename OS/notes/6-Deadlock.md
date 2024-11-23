# Deadlock: Definition and Basics

## What is a Deadlock?
A **deadlock** occurs in a system when a group of processes are waiting indefinitely for resources that are held by each other. This leads to a situation where none of the processes can proceed.

### Example in Real Life
Imagine two cars are on a narrow bridge from opposite directions:
1. Both cars refuse to back up, each waiting for the other to move.
2. Neither car can proceed, resulting in a deadlock.

### Example in Computer Systems
Consider two processes:
1. **Process P1** is holding **Resource R1** and requests **Resource R2**.
2. **Process P2** is holding **Resource R2** and requests **Resource R1**.
Neither process can proceed, resulting in a deadlock.

---

## Four Necessary Conditions for Deadlock
Deadlock occurs only if all four of the following conditions hold simultaneously:

1. **Mutual Exclusion**
   - At least one resource must be held in a non-shareable mode.
   - Example: A printer can only be used by one process at a time.

2. **Hold and Wait**
   - A process holding at least one resource is waiting to acquire additional resources held by other processes.
   - Example: Process A holds a printer and waits for a scanner.

3. **No Preemption**
   - Resources cannot be forcibly taken from a process holding them. They must be released voluntarily.
   - Example: Process B won’t release a file lock unless it finishes its task.

4. **Circular Wait**
   - A set of processes form a circular chain where each process waits for a resource held by the next process.
   - Example: Process A → Process B → Process C → Process A (each waiting for the next).

---

## Resource Allocation Graph (RAG)

### Single Instance Example
A **Resource Allocation Graph (RAG)** represents processes, resources, and their relationships.

- Nodes:
  - Processes: Represented as circles (e.g., P1, P2).
  - Resources: Represented as squares (e.g., R1, R2).

- Edges:
  - Request Edge: Directed from a process to a resource (e.g., P1 → R1).
  - Allocation Edge: Directed from a resource to a process (e.g., R1 → P1).

### Example

```plaintext
Processes: P1, P2
Resources: R1, R2

P1 → R1 (Request Edge)
R2 → P1 (Allocation Edge)
P2 → R2 (Request Edge)
R1 → P2 (Allocation Edge)
```
In this graph, there is a cycle: **P1 → R1 → P2 → R2 → P1**.  
This indicates a **deadlock**.

```python 
from collections import defaultdict

# Representing the Resource Allocation Graph
graph = defaultdict(list)

# Add edges
graph["P1"].append("R1")  # P1 requests R1
graph["R1"].append("P2")  # R1 allocated to P2
graph["P2"].append("R2")  # P2 requests R2
graph["R2"].append("P1")  # R2 allocated to P1

# Function to detect cycles in the graph
def detect_cycle(graph):
    visited = set()
    stack = set()

    def dfs(node):
        if node in stack:
            return True  # Cycle detected
        if node in visited:
            return False

        visited.add(node)
        stack.add(node)
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        stack.remove(node)
        return False

    for node in graph:
        if dfs(node):
            return True
    return False

# Check for deadlock
if detect_cycle(graph):
    print("Deadlock detected!")
else:
    print("No deadlock.")
```

---

# Deadlock Prevention

## What is Deadlock Prevention?
Deadlock prevention is a set of techniques used to ensure that at least one of the four necessary conditions for deadlock (Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait) never holds. By breaking one or more of these conditions, deadlocks can be avoided entirely.

---

## Breaking the Four Conditions

### 1. **Preventing Mutual Exclusion**
   - **Approach**: Make resources sharable wherever possible.
   - **Examples**:
     - Use read-only access to shared files for multiple processes.
     - Allow multiple processes to share a resource, such as a database, with proper concurrency control.
   - **Limitation**:
     - Some resources, like printers or tape drives, are inherently non-shareable.

---

### 2. **Preventing Hold and Wait**
   - **Approach 1: Request All Resources at Once**
     - Require processes to request all required resources simultaneously before execution begins.
     - If all resources cannot be granted, the process must release any it holds and try again later.

     **Example**:
     - Process P1 requires R1 and R2. It requests both at the start.
     - If R1 is free but R2 is not, P1 will not acquire R1 until both are available.

     **Advantages**:
     - Simple to implement.
     - Eliminates holding one resource while waiting for others.

     **Disadvantages**:
     - May lead to resource underutilization.
     - Processes might need to wait longer.

   - **Approach 2: Ensure Processes Hold No Resources While Waiting**
     - Require processes to release all currently held resources before requesting new ones.
     - After obtaining all required resources, the process resumes.

     **Example**:
     - Process P2 holds a printer and requests a scanner.
     - P2 must release the printer and try requesting both resources again.

---

### 3. **Preventing No Preemption**
   - **Approach**: Allow resources to be preempted from a process.
   - **Method**:
     - If a process holding resources is denied additional resources, it must release the currently held resources.
     - These released resources are added back to the pool for allocation to other processes.

   **Example**:
   - Process P3 holds R1 and requests R2, but R2 is unavailable.
   - P3 must release R1, making it available for other processes.

   **Advantages**:
   - More efficient resource utilization.

   **Disadvantages**:
   - May lead to increased process overhead due to repeated resource allocation.

---

### 4. **Preventing Circular Wait**
   - **Approach**: Impose a strict ordering on resource requests.
   - **Method**:
     - Assign a unique number to each resource.
     - Require processes to request resources in ascending order of numbering.

     **Example**:
     - Resources: R1 (1), R2 (2), R3 (3).
     - Process P4 can only request R2 after holding R1 and R3 after R2.
     - This eliminates the possibility of a circular chain.

   **Advantages**:
   - Simple and effective in preventing circular dependencies.

   **Disadvantages**:
   - Can complicate resource request logic.
   - Processes may be forced to acquire resources they don’t need immediately.

---

## Example: Circular Wait Prevention in Python

```python
# Resource ordering to prevent circular wait
resources = {"R1": 1, "R2": 2, "R3": 3}  # Assign unique numbers to resources

def request_resources(process, held, requested):
    # Ensure resources are requested in ascending order
    if any(resources[r1] > resources[r2] for r1 in held for r2 in requested):
        print(f"Process {process}: Request denied (violates ordering).")
    else:
        print(f"Process {process}: Request granted.")
        
# Example usage
request_resources("P1", ["R1"], ["R2"])  # Request granted
request_resources("P2", ["R2"], ["R1"])  # Request denied
```
Output:

```arduino
Process P1: Request granted.
Process P2: Request denied (violates ordering).
```

### Summary of Deadlock Prevention  

- **Mutual Exclusion**:  
  Allow resource sharing when possible.  

- **Hold and Wait**:  
  Require processes to request all resources at once or release held resources before requesting new ones.  

- **No Preemption**:  
  Allow preemption of resources from processes.  

- **Circular Wait**:  
  Use resource ordering to eliminate circular dependencies.  

- **Trade-off**:  
  Deadlock prevention often reduces system efficiency or complicates resource management but ensures the system is free of deadlocks.  


---

# Deadlock Avoidance

## What is Deadlock Avoidance?
Deadlock avoidance is a technique to ensure that a system does not enter an unsafe state where deadlocks could occur. Unlike prevention, which eliminates one of the four conditions for deadlock, avoidance allows all conditions but makes resource allocation decisions carefully to avoid potential deadlocks.

---

## Key Concepts in Deadlock Avoidance

### 1. **Safe State**
   - A system is in a **safe state** if there exists a sequence of all processes such that each process can complete its execution without causing a deadlock.
   - If a system is not in a safe state, it is in an **unsafe state**, which may lead to a deadlock.

### 2. **Resource Allocation Decisions**
   - The system dynamically checks whether granting a resource request will leave the system in a safe state.
   - A resource is only allocated if the resulting state is safe.

---

## Banker's Algorithm

The **Banker's Algorithm** is the most commonly used method for deadlock avoidance. It works by simulating resource allocation to ensure the system remains in a safe state.

### Inputs to the Banker's Algorithm
1. **Available Vector**: Number of available instances for each resource.
   - Example: `Available = [3, 3, 2]` (3 of R1, 3 of R2, 2 of R3).
2. **Maximum Matrix**: Maximum demand of each process for each resource.
   - Example:
     ```
     Maximum = [
         [7, 5, 3],  # P1
         [3, 2, 2],  # P2
         [9, 0, 2],  # P3
     ]
     ```
3. **Allocation Matrix**: Current allocation of resources to each process.
   - Example:
     ```
     Allocation = [
         [0, 1, 0],  # P1
         [2, 0, 0],  # P2
         [3, 0, 2],  # P3
     ]
     ```
4. **Need Matrix**: Remaining resources needed by each process.
   - Formula: `Need = Maximum - Allocation`
   - Example:
     ```
     Need = [
         [7, 4, 3],  # P1
         [1, 2, 2],  # P2
         [6, 0, 0],  # P3
     ]
     ```

---

### Algorithm Steps
1. **Check Request**:
   - If a process requests resources, ensure:
     - `Request[i] <= Need[i]` (Request is within maximum demand).
     - `Request[i] <= Available` (Request can be satisfied with current resources).

2. **Simulate Allocation**:
   - Temporarily allocate requested resources to the process.
   - Update `Available`, `Allocation`, and `Need`.

3. **Safety Check**:
   - Check if the system is in a safe state after the allocation.
   - Use the **Safety Algorithm** to determine if all processes can complete.

4. **Grant or Deny**:
   - If the system remains in a safe state, grant the request.
   - Otherwise, deny the request and rollback the changes.

---

## Example: Banker's Algorithm

### Initial State
- **Available**: `[3, 3, 2]`
- **Maximum**:
```python
[ [7, 5, 3], [3, 2, 2], [9, 0, 2], ]
```
- **Allocation**:
```python
[ [0, 1, 0], [2, 0, 0], [3, 0, 2], ]
```
- **Need**:

```python
[ [7, 4, 3], [1, 2, 2], [6, 0, 0], ]
```


### Process P1 Requests `[0, 2, 0]`

1. **Check Request**:
 - `Request <= Need`: `[0, 2, 0] <= [7, 4, 3]` → True.
 - `Request <= Available`: `[0, 2, 0] <= [3, 3, 2]` → True.

2. **Simulate Allocation**:
 - Update `Available`: `[3, 3, 2] - [0, 2, 0] = [3, 1, 2]`.
 - Update `Allocation`: `[0, 1, 0] + [0, 2, 0] = [0, 3, 0]`.
 - Update `Need`: `[7, 4, 3] - [0, 2, 0] = [7, 2, 3]`.

3. **Safety Check**:
 - Use the Safety Algorithm to find a safe sequence:
   - Try to finish each process in order while ensuring enough resources remain for others.

 **Safe Sequence**: P2 → P3 → P1

 - Since a safe sequence exists, the request is **granted**.

---

## Python Implementation: Banker's Algorithm

```python
import numpy as np

# Data setup
available = np.array([3, 3, 2])
maximum = np.array([
  [7, 5, 3],
  [3, 2, 2],
  [9, 0, 2],
])
allocation = np.array([
  [0, 1, 0],
  [2, 0, 0],
  [3, 0, 2],
])
need = maximum - allocation

def is_safe(available, allocation, need):
  work = available.copy()
  finish = [False] * len(need)
  safe_sequence = []

  while True:
      found = False
      for i, (a, n, f) in enumerate(zip(allocation, need, finish)):
          if not f and all(n <= work):
              work += a
              finish[i] = True
              safe_sequence.append(f"P{i + 1}")
              found = True
      if not found:
          break

  if all(finish):
      return True, safe_sequence
  return False, []

# Example: Process P1 requests [0, 2, 0]
request = np.array([0, 2, 0])
process_index = 0  # P1 is at index 0

# Check and simulate allocation
if all(request <= need[process_index]) and all(request <= available):
  available -= request
  allocation[process_index] += request
  need[process_index] -= request

  # Check safety
  safe, sequence = is_safe(available, allocation, need)
  if safe:
      print("Request granted. Safe sequence:", sequence)
  else:
      print("Request denied. Unsafe state.")
      # Rollback
      available += request
      allocation[process_index] -= request
      need[process_index] += request
else:
  print("Request exceeds maximum demand or available resources.")
```

```less
Request granted. Safe sequence: ['P2', 'P3', 'P1']
```
### Summary of Deadlock Avoidance  

- **Deadlock avoidance** ensures that the system does not enter an unsafe state.  
- The **Banker's Algorithm** dynamically checks resource allocation to maintain safety.  
- It requires prior knowledge of maximum resource demands and is not suitable for all systems (e.g., real-time systems).  

---

# Deadlock Detection and Recovery

## What is Deadlock Detection?
Deadlock detection involves monitoring the state of a system to identify deadlocks. It assumes deadlocks might occur and focuses on detecting and resolving them when they arise.

---

## Deadlock Detection in Single-Instance Resources

For systems where each resource has only one instance, deadlocks can be detected using a **Resource Allocation Graph (RAG)**.

### Detection Method
- If a **cycle** exists in the RAG, a deadlock is present.

### Example
Consider the following RAG:
```plaintext
Processes: P1, P2
Resources: R1, R2

P1 → R1 (Request Edge)
R1 → P2 (Allocation Edge)
P2 → R2 (Request Edge)
R2 → P1 (Allocation Edge)
```

This graph has a cycle: P1 → R1 → P2 → R2 → P1.  
**Deadlock Detected.**  

### Deadlock Detection in Multiple-Instance Resources  

When resources have multiple instances, deadlocks are detected using a variation of the Banker's Algorithm.  

#### Key Data Structures  
- **Available**:  
  Vector of available instances for each resource.  
- **Allocation**:  
  Matrix showing the resources currently allocated to each process.  
- **Request**:  
  Matrix showing the remaining resource requests for each process.  

#### Algorithm Steps  

1. **Initialize**:  
   - Work = Available.  
   - Finish = False for all processes.  

2. **Find Process**:  
   - Find an unfinished process P such that Request[P] <= Work.  

3. **Simulate Allocation**:  
   - If found, allocate resources and update:  
     Work = Work + Allocation[P]  
     Mark P as finished (Finish[P] = True).  

4. **Repeat**:  
   - Repeat steps 2–3 until all processes are finished or no such process exists.  

5. **Deadlock Detected**:  
   - If any process remains unfinished, the system is in deadlock, and the unfinished processes are part of the deadlock.  

### Example: Deadlock Detection for Multiple Instances  

#### Initial Data  
- **Available**: [3, 3, 2]  
- **Allocation**:  

```python
[
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2],
]
```
- **Request**:  

```python
[
    [0, 0, 0],
    [2, 0, 2],
    [0, 0, 0],
    [1, 0, 0],
    [0, 0, 2],
]
```

### Steps  

1. **Initialize Work**:  
   Work = [3, 3, 2].  

2. **Find Processes**:  

   - **P0**:  
     Request[0] <= Work → [0, 0, 0] <= [3, 3, 2] → True.  
     - Allocate resources:  
       Work = Work + Allocation[0] = [3, 3, 2] + [0, 1, 0] = [3, 4, 2].  
     - Mark P0 as finished.  

3. **Repeat for P2, P3**:  
   - Continue marking processes as finished by finding suitable requests.  

4. **Remaining Processes**:  
   - Processes P1 and P4 remain unfinished → **Deadlock Detected**.  

### Deadlock Recovery  

Once a deadlock is detected, the system must recover to proceed.  

#### Recovery Techniques  

1. **Process Termination**:  
   - Abort one or more processes involved in the deadlock to break the cycle.  
   - **Options**:  
     - Terminate all processes in the deadlock.  
     - Terminate processes one by one, considering resource utilization.  

2. **Resource Preemption**:  
   - Forcefully take resources from one or more processes and allocate them to others.  
   - **Factors to consider**:  
     - Cost of preempting a resource.  
     - Priority of processes.  
     - Restart preempted processes later.  



### Python Implementation: Deadlock Detection and Recovery
```python
import numpy as np

# Data setup
available = np.array([3, 3, 2])
allocation = np.array([
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2],
])
request = np.array([
    [0, 0, 0],
    [2, 0, 2],
    [0, 0, 0],
    [1, 0, 0],
    [0, 0, 2],
])

# Deadlock detection function
def detect_deadlock(available, allocation, request):
    work = available.copy()
    finish = [False] * len(request)
    deadlocked = []

    while True:
        allocated = False
        for i in range(len(request)):
            if not finish[i] and all(request[i] <= work):
                work += allocation[i]
                finish[i] = True
                allocated = True
        if not allocated:
            break

    for i, done in enumerate(finish):
        if not done:
            deadlocked.append(i)
    return deadlocked

# Detect deadlock
deadlocked_processes = detect_deadlock(available, allocation, request)

if deadlocked_processes:
    print(f"Deadlock detected among processes: {deadlocked_processes}")
else:
    print("No deadlock detected.")
```

Output:

```less
Deadlock detected among processes: [1, 4]
```

### Summary of Deadlock Detection and Recovery  

- **Detection** is performed using:
  - **RAG (Resource Allocation Graph)** for single instances.
  - An **algorithm** (e.g., Banker's Algorithm) for multiple instances.  

- **Recovery methods** include:
  - **Terminating processes**.
  - **Preempting resources**.
# Methods for Handling Deadlocks

## Overview
Deadlocks can be addressed using the following strategies:
1. **Deadlock Prevention**: Design the system so that one of the necessary conditions for deadlock cannot occur.
2. **Deadlock Avoidance**: Dynamically allocate resources to ensure the system never enters an unsafe state.
3. **Deadlock Detection and Recovery**: Allow deadlocks to occur but detect and resolve them when they do.
4. **Ignore the Problem**: In some systems (e.g., UNIX or Windows), deadlocks are ignored and assumed to be rare.

This section focuses on a holistic understanding of these approaches.

---

## 1. Deadlock Prevention
   - Prevent one or more of the necessary conditions for deadlock.
   - **Advantages**:
     - Simple and effective.
   - **Disadvantages**:
     - Reduces system resource utilization.

**Recap**: Breaking the conditions:
- **Mutual Exclusion**: Make resources shareable when possible.
- **Hold and Wait**: Force processes to request all resources at once or release held resources before requesting new ones.
- **No Preemption**: Allow resources to be forcibly taken from processes.
- **Circular Wait**: Impose a strict resource request order.

---

## 2. Deadlock Avoidance
   - Dynamically check resource allocation requests to prevent unsafe states.
   - **Techniques**:
     - **Banker’s Algorithm**: Ensures the system remains in a safe state.
   - **Advantages**:
     - Effective in avoiding deadlocks without reducing concurrency.
   - **Disadvantages**:
     - High overhead due to continuous state checking.
     - Requires processes to declare maximum resource requirements in advance.

---

## 3. Deadlock Detection and Recovery
   - Allow deadlocks to occur and resolve them when detected.
   - **Detection**:
     - Use algorithms based on the Resource Allocation Graph (RAG) for single-instance resources.
     - Use request and allocation matrices for multiple-instance resources.
   - **Recovery**:
     - Terminate processes.
     - Preempt resources.

   **Advantages**:
     - Flexible and can be applied after deadlocks occur.
   **Disadvantages**:
     - May cause process termination or significant delays.

---

## 4. Ignoring Deadlocks
   - Deadlocks are assumed to be rare and are ignored by the system.
   - Used in systems like UNIX, Linux, and Windows.
   - **Advantages**:
     - Simple and requires no extra resources.
   - **Disadvantages**:
     - Deadlocks may persist indefinitely, affecting system reliability.

---

## Comparison of Strategies

| Strategy                | Complexity | Resource Utilization | Deadlock Possibility | Overhead |
|-------------------------|------------|-----------------------|-----------------------|----------|
| **Prevention**          | Low        | Low                   | None                  | Low      |
| **Avoidance**           | High       | Medium                | None                  | High     |
| **Detection & Recovery**| Medium     | High                  | Possible              | Medium   |
| **Ignoring Deadlocks**  | Very Low   | High                  | High                  | Very Low |

---

## Practical Considerations
1. **System Type**:
   - Real-time systems often use prevention or avoidance.
   - General-purpose systems may rely on detection or ignore deadlocks.
2. **Resource Constraints**:
   - Systems with abundant resources may opt for detection and recovery.
3. **Criticality of Processes**:
   - Mission-critical systems prefer prevention or avoidance to ensure reliability.

---



