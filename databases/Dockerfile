FROM mysql:5.7

WORKDIR /usr/app/src

ENV MYSQL_ROOT_PASSWORD 1111

COPY ./init-sql /docker-entrypoint-initdb.d

CMD ["mysqld"]