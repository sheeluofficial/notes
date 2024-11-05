# Orphan and Zombie Processes

## Overview
Orphan and zombie processes both involve scenarios where a child process is not properly handled by its parent process. They differ based on the state of the child process and how the operating system handles them.

## Key Definitions
- **Orphan Process**: A running child process whose parent has terminated.
- **Zombie Process**: A terminated child process that remains in the process table because the parent has not called `wait()` to retrieve its exit status.

## Differences Between Orphan and Zombie Processes
| Aspect                | Orphan Process                                | Zombie Process                           |
|-----------------------|-----------------------------------------------|------------------------------------------|
| **State of Child**    | Still running                                 | Terminated                               |
| **Parent's Action**   | Parent terminates before the child finishes   | Parent does not call `wait()` after child finishes |
| **Adopted By `init`** | Yes, when the parent terminates               | Yes, if the parent terminates without calling `wait()` |
| **Resource Usage**    | Uses CPU and memory as it continues to run    | Only occupies a process table entry      |

## How They Are Created
1. **Orphan Process**:
   - **Scenario**: The parent process terminates while the child process is still running.
   - **Result**: The child process becomes an orphan and is adopted by the `init` process.
   - **Example**: Parent exits immediately without waiting for the running child.

2. **Zombie Process**:
   - **Scenario**: The child process terminates but the parent process does not call `wait()` to read its exit status.
   - **Result**: The child becomes a zombie, occupying a slot in the process table.
   - **Example**: Child finishes execution but remains in a zombie state until the parent calls `wait()`.

## Handling by the `init` Process
- **Orphan Processes**: `init` process adopts orphan processes and continues to manage them until they finish execution.
- **Zombie Processes**: If a parent exits without cleaning up zombies, `init` adopts these zombies and calls `wait()` to remove them from the process table.

## Common Scenarios
1. **Parent Does Not Call `wait()`**:
   - If the child process finishes and the parent remains running without calling `wait()`, the child becomes a zombie.
   - If the parent eventually exits, the zombie is adopted and cleaned up by the `init` process.

2. **Parent Exits Before the Child**:
   - If the parent exits while the child is still running, the child becomes an orphan.
   - The orphaned child is adopted by the `init` process, which ensures it runs to completion.

## Why Different Names and Handling
- **Zombie Process**:
  - Named "zombie" because it is already dead but still exists in the process table.
  - Represents a lack of cleanup after the child has finished.
  - Exists until the parent calls `wait()` or until the parent itself terminates.

- **Orphan Process**:
  - Named "orphan" because it loses its parent while still alive.
  - The system adopts the running orphan to prevent unmanageable processes.
  - Continues execution under the management of the `init` process.

## Summary
- Both **orphans** and **zombies** involve the parent failing to handle the child properly.
- **Orphans**: Created when the parent exits before the child finishes; adopted by `init`.
- **Zombies**: Created when the child finishes but the parent does not call `wait()`; if the parent exits, `init` cleans up the zombie.
- The **init** process plays a crucial role in managing both orphaned and zombie processes to ensure system stability.

