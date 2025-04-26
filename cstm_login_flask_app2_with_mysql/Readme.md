Hello, This example is an 3 tier application where we have implemented the docker-compose.

To run this application in containers, Follow below steps:

1. Have 1 ec2 instance (t2.micro is fine).
2. Once after the instance is up run below commands
    sudo apt update && sudo apt install -y docker.io
    sudo apt update && sudo apt install -y curl jq
    export LATEST_COMPOSE_VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
    sudo curl -L "https://github.com/docker/compose/releases/download/${LATEST_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
3. After running above commands verify if docker and docker-compose are installed or not.
    docker -version
    docker-compose -version
4. After verification is completed run the below command to start the containers
    sudo docker-compose up