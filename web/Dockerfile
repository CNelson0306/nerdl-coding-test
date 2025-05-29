FROM ubuntu:latest as intermediate

ARG BASE_URL_WEB
ARG BASE_URL_API

ENV BASE_URL_WEB ${BASE_URL_WEB}
ENV BASE_URL_API ${BASE_URL_API}

RUN apt update
RUN apt install -y gettext

ADD ./web/app /tmp/app/
RUN /usr/bin/envsubst < /tmp/app/.env.template > /tmp/app/.env

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get -y install curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_16.x  | bash -
RUN apt-get -y install nodejs

WORKDIR /tmp/app
RUN npm install
RUN npm run build

FROM node:lts-buster

COPY --from=intermediate /tmp/app/build /build
COPY --from=intermediate /tmp/app/.env /

EXPOSE 80

RUN npm install pm2 -g

CMD ["pm2", "serve", "build", "80", "--spa", "--no-daemon"]
