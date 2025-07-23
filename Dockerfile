FROM jenkins/jenkins:lts

USER root

RUN	apt update && apt install -y python3 python3-venv python3-pip vim && \
    apt autoremove && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python

USER jenkins
