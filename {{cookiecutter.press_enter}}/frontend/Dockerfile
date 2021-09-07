FROM node:14-stretch-slim

ARG APP_HOME=/app
WORKDIR ${APP_HOME}
COPY ./package.json ${APP_HOME}
RUN npm install && npm cache clean --force

ENV PATH ./node_modules/.bin/:$PATH

COPY . ${APP_HOME}
RUN npm run build
