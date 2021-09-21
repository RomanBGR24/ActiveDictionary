# django & gunicorn

FROM python:3.8.12-alpine

RUN mkdir -p /home/app
RUN addgroup -S app && adduser -S app -G app
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME && \
    mkdir $APP_HOME/staticfiles && \
    mkdir $APP_HOME/staticfiles/admin && \
    mkdir $APP_HOME/staticfiles/main_app

WORKDIR $APP_HOME

# install postgresql dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint
COPY ./entrypoint.sh .

# copy project
COPY . $APP_HOME

RUN chown -R app:app $APP_HOME
USER app

ENTRYPOINT ["/home/app/web/entrypoint.sh"]
