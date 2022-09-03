FROM python:3.5

#set env
ENV HOME ./app
ENV LOG_LEVEL 'INFO'

#Create HOME dir
RUN mkdir -p ${HOME}
WORKDIR ${HOME}

RUN apt-get update

CMD