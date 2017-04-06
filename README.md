#Docker installation:

https://docs.docker.com/engine/installation/

# docker-python-app
This is a docker python app image

#to build the app 
docker build -t track-python-app .

#to run with log 
 docker run —name    logging-01 -t -d -v $(pwd):/tmp  -w /tmp  -p 5000:5000 track-python-app

#to see process 
docker ps or docker stats

#TO ssh  into the container 
sudo docker exec -it <containerid>  bash

#
curl 127.0.0.1:5000 -v
