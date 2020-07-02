FROM node:14.5.0-alpine

ENV APP_ROOT /usr/src/app
WORKDIR $APP_ROOT

RUN yarn global add @vue/cli

COPY ./package*.json ./
RUN yarn install

EXPOSE 8080

CMD ["yarn", "run", "serve"]
