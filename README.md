# docker-python-app
This is a docker python app image
#Docker installation:
https://docs.docker.com/engine/installation/

#to build the app 
docker build -t track-python-app .

#to run with log 
 docker run —name    logging-01 -t -d -v $(pwd):/tmp  -w /tmp  -p 5000:5000 track-python-app

#to see process 
docker ps or docker stats

#To ssh  into the container 
sudo docker exec -it <containerid>  bash

#To Create an image  with latest tag
docker tag fb37732d54a9 aramaraj/docker-python-app:latest

#To Push Docker image to hub
docker push aramaraj/docker-python-app


<img src='/dockerpush.png' title='Docker push to Hub' width='' alt='Docker push to Hub' />

<img src='/dockerhub.png' title='Docker push to Hub' width='' alt='Docker push to Hub' />




#
curl 127.0.0.1:5000 -v
