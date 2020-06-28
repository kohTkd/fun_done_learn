FROM python:3.8-alpine

ENV APP_ROOT /usr/src/app
WORKDIR $APP_ROOT

RUN apk update && \
    apk add --update --no-cache tzdata git openssh-client openjdk8-jre nodejs npm && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata && \
    npm i -g yarn && \
    yarn global add serverless && \
    pip install pipenv
COPY ./Pipfile ./
COPY ./Pipfile.lock ./
COPY ./package.json ./
RUN pipenv install --dev && \
    yarn install

EXPOSE 5000

ENTRYPOINT ["pipenv", "run"]
CMD ["sls", "wsgi", "serve", "--host", "0.0.0.0"]
