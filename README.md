# Containerized_ServerStatMonitorApp

## How to run the Application:
 - Make sure docker and docker compose are downloaded on your Linux/unix based machine.
 - Create a directory on your machine and cd into it.
 - Clone the repo into the directory
 - Run the command
   ```shell
    docker-compose up --build
   ```
 - Open your browser on port 5000, i.e. localhost:5000/ (if running on localhost)

 ## Tech Stack
 - Linux/Unix OS (RHEL was used in this particular project)
 - Docker & docker-compose (RHEL based systems):
   - update yum and download the yum config manager by:```shell yum update && yum install yum-utils ```
   - on RHEL just do: ```shell sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo ```
   
