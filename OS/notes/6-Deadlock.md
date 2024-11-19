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