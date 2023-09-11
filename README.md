# Containerized_ServerStatMonitorApp

## How to run the Application:
 - Make sure docker and docker compose are downloaded on your Linux/unix based machine.
 - Create a directory on your machine and cd into it.
 - Clone the repo into the directory
 - For the first time run the command
   ```shell
    docker-compose up --build
   ```
 - After the first time, run the command
    ```shell
   docker compose up
   ```
 - If the application is running on localhowt, then open your browser on port 5000:
    ```shell
   localhost:5000/ (if running on localhost)
    ```
 - In order to view the CPU, Memory, Disk statistics use the following URLs respectively
    ```shell
   localhost:5000/cpu
    ```
    ```shell
   localhost:5000/mem
    ```
   ```shell
   localhost:5000/disk
    ```

 ## Tech Stack
 - Linux/Unix OS (RHEL was used in this particular project)
 - Docker & docker-compose (RHEL based systems):
   - update yum and download the yum package config manager by:
     
     ```shell
     yum update && yum install yum-util
      ```
   - on RHEL just do:
     ```shell
     sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
      ```
   
