FROM centos
WORKDIR cd /etc/yum.repos.d/
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
RUN yum update -y
RUN yum install python3 -y
RUN pip3 install scikit-learn
RUN pip3 install numpy
COPY machinelearning.py /machinelearning.py
CMD python3 /machinelearning.py
