FROM php:8-fpm

WORKDIR /app

RUN docker-php-ext-install mysqli

COPY . .

EXPOSE 8989

CMD [ "php", "-S", "0.0.0.0:8989" ]