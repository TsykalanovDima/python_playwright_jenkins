FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv curl && \
    pip3 install --break-system-packages --upgrade pip && \
    pip3 install --break-system-packages playwright && \
    playwright install --with-deps

USER jenkins
