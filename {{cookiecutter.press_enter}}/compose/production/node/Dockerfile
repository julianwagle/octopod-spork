FROM node:14-stretch-slim
ARG APP_HOME=/app
WORKDIR ${APP_HOME}/frontend
COPY ./frontend/package.json /app/frontend
RUN npm install && npm cache clean --force
COPY . ${APP_HOME}
RUN npm run build
ENV PATH ./frontend/node_modules/.bin/:$PATH