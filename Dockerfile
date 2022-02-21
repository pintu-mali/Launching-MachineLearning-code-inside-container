FROM centos
WORKDIR cd /etc/yum.repos.d/
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
RUN yum update -y
RUN yum install python3 -y
RUN pip3 install -U pip
RUN pip3 install -U setuptools
RUN pip3 install pandas
RUN pip3 install keras
RUN pip3 install tensorflow
RUN pip3 install scikit-learn
RUN pip3 install numpy
#RUN yum install ncurses -y
COPY machinelearning.py /machinelearning.py
COPY weight-height.csv /dataset.csv
CMD python3 /machinelearning.py
