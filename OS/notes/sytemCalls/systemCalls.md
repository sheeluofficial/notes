# System Calls in Operating Systems

## What is a System Call?
A **system call** is a mechanism that provides the interface between a process and the operating system. It allows user-level processes to request services from the operating system's kernel, such as managing hardware resources, file handling, or memory management.

System calls are critical for accessing low-level services provided by the OS, like file handling, process control, and communication between processes.

### Types of System Calls:
System calls are generally categorized into the following types:

1. **Process Control**
   - To manage and control the execution of processes.
   - Examples: process creation, termination, wait for a process, etc.

2. **File Management**
   - To create, read, write, and delete files or directories.
   - Examples: open, close, read, write, delete, etc.

3. **Device Management**
   - To request, release, and control hardware devices (such as I/O devices).
   - Examples: request device, release device, read, write, etc.

4. **Information Maintenance**
   - To maintain and retrieve information about processes, files, devices, or system status.
   - Examples: get process ID, system time, get system info, etc.

5. **Communication**
   - For inter-process communication, using shared memory, message passing, or network communication.
   - Examples: send, receive, shared memory operations, etc.

---

## System Call in Different Operating Systems

### 1. **System Calls in UNIX/Linux**
Linux/Unix provides a rich set of system calls to interact with its kernel. Some of the commonly used system calls are:

#### Process Control
| **System Call** | **Description**                                       | **Commands** |
|-----------------|-------------------------------------------------------|--------------|
| `fork()`        | Creates a new process (child) by duplicating the parent. |  |
| `exec()`        | Replaces the current process image with a new program. |  |
| `exit()`        | Terminates the calling process.                        |  |
| `wait()`        | Waits for a child process to terminate.                |  |
| `kill()`        | Sends a signal to a process to terminate it.           |  |
| `setuid()`      | Sets the user ID of the calling process.               |  |
| `setgid()`      | Sets the group ID of the calling process.              |  |
| `getppid()`     | Returns the parent process ID of the calling process.  | `echo $$` to get parent PID |
| `sched_yield()` | Yields the processor to other threads or processes.    |  |

#### File Management
| **System Call** | **Description**                                       | **Commands** |
|-----------------|-------------------------------------------------------|--------------|
| `open()`        | Opens a file for reading, writing, or both.           |  |
| `close()`       | Closes an opened file descriptor.                     |  |
| `read()`        | Reads data from an opened file.                       |  |
| `write()`       | Writes data to an opened file.                        |  |
| `lseek()`       | Repositions the read/write file offset.               |  |
| `unlink()`      | Deletes a name from the filesystem (removes a file).  |  |
| `dup()`         | Duplicates a file descriptor.                         |  |
| `dup2()`        | Duplicates a file descriptor to a specific value.     |  |
| `truncate()`    | Truncates a file to a specified length.               | `truncate -s <size> <filename>` |
| `fstat()`       | Retrieves status information about an open file.      | `stat <filename>` |

#### Device Management
| **System Call** | **Description**                                       | **Commands** |
|-----------------|-------------------------------------------------------|--------------|
| `ioctl()`       | Manipulates device parameters of special files.       |  |
| `read()`        | Reads data from the device.                           |  |
| `write()`       | Writes data to the device.                            |  |
| `open()`        | Opens a device for communication.                     |  |
| `close()`       | Closes the opened device file descriptor.             |  |
| `mmap()`        | Maps a file or device into memory.                    | `mmap -addr <address> <size>` |
| `munmap()`      | Unmaps a previously mapped region.                    |  |
| `poll()`        | Checks multiple file descriptors for available I/O.   | `poll` in scripts |

#### Information Maintenance
| **System Call** | **Description**                                       | **Commands** |
|-----------------|-------------------------------------------------------|--------------|
| `getpid()`      | Returns the process ID of the calling process.        |  |
| `getuid()`      | Returns the user ID of the calling process.           |  |
| `alarm()`       | Sets an alarm clock for sending a signal after a certain time. |  |
| `sleep()`       | Suspends the process execution for a specific period. |  |
| `getgid()`      | Gets the group ID of the calling process.             | `id -g` |
| `times()`       | Returns time-related information about a process.     | `time <command>` |
| `sysinfo()`     | Retrieves system statistics.                          | `free -m`, `vmstat` |
| `uname()`       | Gets information about the system.                    | `uname -a` |

#### Communication
| **System Call** | **Description**                                       | **Commands** |
|-----------------|-------------------------------------------------------|--------------|
| `pipe()`        | Creates a unidirectional communication channel.       |  |
| `shmget()`      | Allocates a shared memory segment.                    |  |
| `shmat()`       | Attaches the shared memory segment.                   |  |
| `msgsnd()`      | Sends a message to a message queue.                   |  |
| `msgrcv()`      | Receives a message from a message queue.              |  |
| `socketpair()`  | Creates a pair of connected sockets.                  |  |
| `sendmsg()`     | Sends a message on a socket.                          |  |
| `recvmsg()`     | Receives a message from a socket.                     |  |
| `select()`      | Monitors multiple file descriptors.                   |  |

---

### 2. **System Calls in Windows**
Windows provides its own set of system calls, often referred to as **Windows API**. The most important system calls are as follows:

#### Process Control
| **System Call**          | **Description**                                       | **Commands** |
|--------------------------|-------------------------------------------------------|--------------|
| `CreateProcess()`         | Creates a new process (similar to `fork()` in Unix).  |  |
| `ExitProcess()`           | Terminates a process.                                 |  |
| `WaitForSingleObject()`   | Waits until a process finishes or a signal is received. |  |
| `TerminateProcess()`      | Forces a process to terminate.                        |  |
| `GetCurrentProcessId()`   | Retrieves the process identifier (PID).              |  |
| `OpenProcess()`           | Opens an existing process for manipulation.          |  |
| `SetPriorityClass()`      | Sets priority of a process.                          |  |
| `SuspendThread()`         | Suspends execution of a thread in a process.         |  |
| `ResumeThread()`          | Resumes a suspended thread in a process.             |  |

#### File Management
| **System Call**          | **Description**                                       | **Commands** |
|--------------------------|-------------------------------------------------------|--------------|
| `CreateFile()`           | Opens or creates a file.                             |  |
| `ReadFile()`             | Reads data from an opened file.                      |  |
| `WriteFile()`            | Writes data to an opened file.                       |  |
| `CloseHandle()`          | Closes an open file handle.                          |  |
| `DeleteFile()`           | Deletes a file.                                      |  |
| `SetFilePointer()`       | Moves the file pointer for an open file.             |  |
| `FlushFileBuffers()`     | Flushes the buffers of a file to disk.               |  |
| `GetFileInformationByHandle()` | Retrieves information about a file.            |  |

#### Device Management
| **System Call**          | **Description**                                       | **Commands** |
|--------------------------|-------------------------------------------------------|--------------|
| `DeviceIoControl()`      | Sends a control code to a device driver.             |  |
| `ReadFile()`             | Reads data from a device.                            |  |
| `WriteFile()`            | Writes data to a device.                             |  |
| `CreateFile()`           | Opens a device for communication.                    |  |
| `SetupDiGetClassDevs()`  | Retrieves a list of devices for a specified device class. |  |
| `GetVolumeInformation()` | Gets information about a file system and volume. | `wmic volume get` |

#### Information Maintenance
| **System Call**          | **Description**                                       | **Commands** |
|--------------------------|-------------------------------------------------------|--------------|
| `GetSystemTime()`        | Retrieves the current system time.                   |  |
| `GetProcessTimes()`      | Retrieves timing information for a process.          |  |
| `GetExitCodeProcess()`   | Retrieves the termination status of a process.       |  |
| `GetCurrentThreadId()`   | Retrieves the thread identifier (TID).               |  |
| `GetSystemInfo()`        | Retrieves system architecture and configuration.     |  |
| `GlobalMemoryStatusEx()` | Retrieves the status of the system's memory.         |  |
| `GetTickCount()`         | Returns the number of milliseconds since the system started. |  |

#### Communication
| **System Call**          | **Description**                                       | **Commands** |
|--------------------------|-------------------------------------------------------|--------------|
| `CreatePipe()`           | Creates a pipe for inter-process communication.      |  |
| `WriteFile()`            | Writes to the pipe.                                  |  |
| `ReadFile()`             | Reads from the pipe.                                 |  |
| `CreateNamedPipe()`      | Creates a named pipe for communication.              |  |
| `WaitNamedPipe()`        | Waits for a named pipe instance to be available.     |  |
| `ConnectNamedPipe()`     | Waits for a client to connect to a named pipe.       |  |

---

### 3. **System Calls in macOS (BSD)**
macOS, which is built on a Unix-like kernel, uses similar system calls as Linux but has some differences due to the BSD heritage.

#### Process Control
| **System Call**         | **Description**                                       | **Commands** |
|-------------------------|-------------------------------------------------------|--------------|
| `fork()`                | Creates a new process.                                |  |
| `exec()`                | Executes a program in the current process.            |  |
| `exit()`                | Terminates the current process.                       |  |
| `wait()`                | Waits for a process to terminate.                     |  |
| `posix_spawn()`         | Creates and runs a new process.                       |  |
| `killpg()`              | Sends a signal to a process group.                    |  |

#### File Management
| **System Call**         | **Description**                                       | **Commands** |
|-------------------------|-------------------------------------------------------|--------------|
| `open()`                | Opens a file descriptor.                              |  |
| `read()`                | Reads data from an open file.                         |  |
| `write()`               | Writes data to an open file.                          |  |
| `close()`               | Closes an open file descriptor.                       |  |
| `unlink()`              | Deletes a file.                                       |  |
| `flock()`               | Applies or removes a lock on an open file.            |  |
| `rename()`              | Changes the name or location of a file.               |  |

#### Device Management
| **System Call**         | **Description**                                       | **Commands** |
|-------------------------|-------------------------------------------------------|--------------|
| `ioctl()`               | Controls device parameters.                           |  |
| `read()`                | Reads data from a device.                             |  |
| `write()`               | Writes data to a device.                              |  |
| `mount()`               | Mounts a filesystem.                                  | `mount` |
| `umount()`              | Unmounts a filesystem.                                | `umount` |

#### Information Maintenance
| **System Call**         | **Description**                                       | **Commands** |
|-------------------------|-------------------------------------------------------|--------------|
| `getpid()`              | Retrieves the process ID.                             |  |
| `gettimeofday()`        | Retrieves the current time.                           |  |
| `getuid()`              | Retrieves the user ID of the current process.         |  |
| `sysctl()`              | Gets or sets kernel parameters.                       | `sysctl -a` |
| `mach_absolute_time()`  | Retrieves high-resolution timestamp for profiling.    |  |

#### Communication
| **System Call**         | **Description**                                       | **Commands** |
|-------------------------|-------------------------------------------------------|--------------|
| `socket()`              | Creates an endpoint for communication.                |  |
| `bind()`                | Associates a socket with a local address.             |  |
| `send()`                | Sends data through a socket.                          |  |
| `recv()`                | Receives data from a socket.                          |  |
| `setsockopt()`          | Sets options for a socket.                            |  |
| `getsockopt()`          | Retrieves options for a socket.                       |  |

---
