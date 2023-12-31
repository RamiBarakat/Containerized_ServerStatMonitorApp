# Containerized_ServerStatMonitorApp

## How to run the Application:
 - Make sure docker and docker compose are downloaded on your Linux/unix based machine.
 - Create a directory on your machine and cd into it.
 - Clone the repo into the directory.
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
  - In order to view the current statistics, use the following:
     ```shell
     localhost:5000/cpu_now
     ```
     ```shell
     localhost:5000/mem_now
     ```
     ```shell
     localhost:5000/disk_now
     ```
- Note: if the application isn't working properly, try the remove the containers and create them again, as follows
     ```shell
     docker compose down
     ```
     then:
  
     ```shell
     docker compose up
     ```
 ## Logs
 - In order to view any error that might occur with the Flask API or the database, view the log files
   - for the API: flask_app.log
   - for the statistics collection: readstats.log


  
 ## Tech Stack
 - Linux/Unix OS (RHEL was used in this particular project)
 - Docker & docker-compose (RHEL based distributions):
   - update yum and download the yum package config manager by:
     
     ```shell
     yum update && yum install yum-util
      ```
   - on RHEL just do:
     ```shell
     sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
      ```
   
