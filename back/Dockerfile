FROM python:3.8-alpine

ENV APP_ROOT /usr/src/app
WORKDIR $APP_ROOT

RUN apk update && \
    apk add --update --no-cache git openssh-client nodejs npm && \
    npm i -g yarn && \
    yarn global add serverless

COPY ./requirements.txt ./
COPY ./package.json ./
RUN pip install -r requirements.txt && \
    yarn install

EXPOSE 5000

CMD ["sls", "wsgi", "serve", "--host", "0.0.0.0"]
