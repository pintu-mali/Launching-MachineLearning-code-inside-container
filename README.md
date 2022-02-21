# Task4.1 : Create a machine learning code in python to accept command line input
Use Dockerfile to build the image with the python code
Create the container and give the input while launching the container so that container gives output and then stops.

Follow the below steps

step 1 : Create a separate folder
      
      #mkdir /task/
      
step 2 : Create a Machine learning code in it
      
      #vim machinelearning.py
      Copy paste the code provided
      
step 3 : Download the dataset provided

step 4 : Create a Dockerfile
      
      #vim Dockerfile
      Copy paste the code provided
      
step 5 : Build the image by the following command
      
      #docker Build /task/ -t pythoncode
      here /task/ is the folder name and pythoncode is the image name we are creating

step 6 : Create a container from the image
      
      #docker run -it pythoncode
      
Basic Requirements : Docker-ce and python must be installed
THAT'S IT!
   
