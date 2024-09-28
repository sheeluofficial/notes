1. Windows Operating System
  1. Kernel Architecture:
    - Hybrid Kernel: Combines elements of both microkernel and monolithic kernel architectures. Provides more flexibility in performance and extensibility.
    - Components:
    - Executive: Manages core system services like process/thread management, memory, I/O.
    - Kernel: Handles low-level operations like context switching, synchronization, interrupt handling.
    - Hardware Abstraction Layer (HAL): Provides a layer of abstraction between hardware and the OS, ensuring compatibility across diverse hardware.
  2. Memory Management:
    - Virtual Memory Manager (VMM): Implements paging and virtual memory through demand paging. It uses a two-level paging system for efficient memory allocation.
    - Address Space Layout Randomization (ASLR): Provides security by randomizing the address space positions of key data areas.
  3. File Systems:
    - NTFS (New Technology File System): Supports large volumes, file-level security, encryption (EFS), and compression. It uses a journaling feature to protect against file system corruption.
    - ReFS (Resilient File System): Designed for high-resiliency and improved data integrity. It is optimized for fault tolerance and large datasets.
  4. Process Scheduling:
    - Preemptive Multitasking: Ensures high-priority tasks get more CPU time. Uses a priority-based, preemptive scheduling model.
    - Windows Scheduler: Implements a quantum-based system where each thread is assigned a time slice (quantum) to run. The thread with the highest priority is selected for execution.
  5. Security Model:
    - User Account Control (UAC): Limits applications to standard privileges unless an administrator allows elevated rights.
    - Security Reference Monitor (SRM): Central part of the Windows security model that enforces access control and auditing.
    - BitLocker: Full disk encryption for protecting data on Windows devices.
2. macOS (Based on Darwin OS)
  1. Kernel Architecture:
    - XNU Kernel (X is Not Unix): Hybrid kernel combining elements of the Mach microkernel and components from FreeBSD (monolithic kernel).
    - Mach Layer: Handles IPC (inter-process communication), tasks, and memory management.
    - BSD Layer: Provides UNIX-like interfaces, POSIX compliance, file systems, and networking.
  2. Memory Management:
    - Virtual Memory: Implements demand paging using a unified buffer cache for memory and file I/O.
    - Shared Memory: macOS uses shared memory regions for better communication between processes, often used by GUI and multimedia applications.
  3. File Systems:
    - APFS (Apple File System): Optimized for flash and solid-state drives (SSD). Supports snapshots, clones, encryption, and space sharing.
    - HFS+: The legacy file system used before APFS, still supported for backward compatibility.
  4. Process Scheduling:
    - Priority-Based Scheduling: Like Windows, macOS uses a priority-based scheduling algorithm with dynamic thread priority.
    - Grand Central Dispatch (GCD): Provides a high-level API for managing concurrent operations by submitting tasks to dispatch queues, which dynamically assigns tasks to threads.
  5. Security Model:
    - System Integrity Protection (SIP): Prevents potentially malicious software from modifying protected system files.
    - Keychain: A secure storage system for sensitive information like passwords, encryption keys, and certificates.
    - Sandboxing: Isolates applications to limit their access to system resources, enhancing security.
3. Linux (Ubuntu, Fedora, Debian, etc.)
  1. Kernel Architecture:
    - Monolithic Kernel: The Linux kernel is monolithic, meaning most services like device drivers and file system management are part of the kernel itself.
    - Loadable Kernel Modules (LKMs): Allow parts of the kernel to be loaded or unloaded dynamically, providing flexibility without recompiling the kernel.
  2. Memory Management:
    - Demand Paging: Uses a paging system where only needed parts of a program are loaded into memory.
    - Transparent Huge Pages (THP): Automatically optimizes memory usage by using large memory pages to reduce overhead.
    - Swapping: Linux swaps out pages of memory to disk (swap space) when physical memory is full.
  3. File Systems:
    - ext4 (Fourth Extended File System): The default file system for many Linux distributions, it supports journaling, large files, and extended attributes.
    - Btrfs (B-tree File System): Advanced file system with features like snapshots, checksums for data integrity, and transparent compression.
    - XFS: High-performance file system optimized for parallel I/O.
  4. Process Scheduling:
    - Completely Fair Scheduler (CFS): Uses a balanced tree data structure (red-black tree) to maintain fairness in allocating CPU time to processes. It provides low latency and high throughput.
    - Real-Time Scheduling: Linux supports real-time scheduling policies (e.g., SCHED_FIFO, SCHED_RR) for critical tasks with strict timing requirements.
  5. Security Model:
    - Mandatory Access Control (MAC): Implemented through security modules like SELinux and AppArmor to enforce access policies beyond traditional UNIX permissions.
    - Capabilities: Linux splits root’s privileges into fine-grained capabilities, allowing processes to perform specific privileged operations without being root.
4. Android Operating System (Linux-Based)
  1. Kernel Architecture:
    - Modified Linux Kernel: Android uses a modified Linux kernel but with different drivers and components optimized for mobile devices.
    - Binder IPC: Provides efficient inter-process communication between apps, enabling Android’s application sandboxing model.
  2. Memory Management:
    - Low Memory Killer: Android uses a low-memory killer to free up resources by terminating less essential background apps when memory is low.
    - Zygote Process: A system-wide shared process that preloads common classes and resources, which new applications can fork from for faster startup.
  3. File Systems:
    - ext4: Android primarily uses the ext4 file system for internal storage.
    - YAFFS2: Historically used for NAND flash devices, now mostly replaced by ext4.
    - F2FS (Flash-Friendly File System): Used in some devices for better performance on NAND flash memory.
  4. Process Scheduling:
    - Priority-Based Scheduling: Android uses a priority-based scheduling model with real-time priorities for critical system processes like multimedia rendering.
    - CFS: Since Android is Linux-based, it inherits the CFS for general process scheduling.
  5. Security Model:
    - Sandboxing: Each application runs in its own sandbox, separated from other apps and the system.
    - SELinux: Enforces mandatory access controls to restrict what apps and services can do on the system.
    - Permissions: Android uses a user-granted permissions model, where apps must request access to specific system resources at runtime.
5. iOS Operating System (Based on Darwin OS)
  1. Kernel Architecture:
    - XNU Kernel (like macOS): Combines Mach and BSD components, but with additional mobile-optimized features.
    - Kernel Extensions (kexts): Dynamically loaded modules that extend kernel functionality, used for device drivers and security.
  2. Memory Management:
    - Automatic Reference Counting (ARC): iOS uses ARC to manage memory allocation and deallocation for objects, improving performance and reducing memory leaks.
    - Shared Memory: iOS uses shared memory regions for fast communication between apps, especially useful in multimedia processing.
  3. File Systems:
    - APFS (Apple File System): Same as macOS, optimized for NAND storage. Supports encryption, snapshots, and cloning.
    - Data Partitioning: iOS uses a partitioned system where user data and system data are separated for better security.
  4. Process Scheduling:
    - Cooperative Multitasking: Earlier versions of iOS used cooperative multitasking where applications would yield control of the CPU. Modern versions use preemptive multitasking.
    - Real-Time Scheduling: Critical processes like UI rendering and audio playback are given real-time priority.
  5. Security Model:
    - Secure Boot Chain: Verifies the integrity of every component from the bootloader to the OS to ensure the system hasn’t been tampered with.
    - App Sandboxing: Similar to Android, but iOS enforces stricter app isolation and communication rules.
    - Data Protection: Uses file-level encryption, with encryption keys tied to the user’s passcode.
1. Comparison of Technical Features

| **Feature**           | **Windows**                               | **macOS**                                    | **Linux**                                 | **Android**                               | **iOS**                                   |
|-----------------------|-------------------------------------------|---------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
| **Kernel**            | Hybrid (monolithic + microkernel)         | XNU (hybrid: Mach + BSD)                    | Monolithic                               | Linux-based                              | XNU (hybrid: Mach + BSD)                  |
| **File System**        | NTFS, ReFS                               | APFS, HFS+                                  | ext4, Btrfs, XFS                         | ext4, F2FS                               | APFS                                      |
| **Scheduling**        | Quantum-based, priority preemptive        | Priority preemptive, GCD                    | Completely Fair Scheduler (CFS)          | CFS, real-time scheduling                | Real-time priority, preemptive multitasking |
| **Memory Management** | Paging, ASLR, VMM                        | Virtual memory, shared memory               | Paging, Swapping, THP                    | Low memory killer, Zygote                | ARC, shared memory                       |
| **Security**          | UAC, BitLocker, SRM                      | SIP, Keychain, Sandboxing                   | SELinux, MAC (AppArmor, SELinux)         | SELinux, sandboxing, permissions         | Secure Boot, sandboxing, data protection |
