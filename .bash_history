docker ps
docker ps -a
sudo docker run -d   --name jenkins   -p 8080:8080 -p 50000:50000   -v jenkins_home:/var/jenkins_home   jenkins/jenkins:lts
sudo docker ps
sudo docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
sudo apt update
docker run -d   --name jenkins   -p 8080:8080 -p 50000:50000   -v jenkins_home:/var/jenkins_home   jenkins/jenkins:lts
sudo usermod -aG docker $USER
newgrp docker
