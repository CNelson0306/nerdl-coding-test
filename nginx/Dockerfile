FROM byjg/nginx-extras

COPY ./nginx/default.template /tmp/default.template
CMD ["/bin/sh", "-c", "envsubst < /tmp/default.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"]

EXPOSE 80
