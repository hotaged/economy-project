FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

WORKDIR /etc/nginx/conf.d
RUN mkdir "staticfiles"
RUN mkdir "mediafiles"