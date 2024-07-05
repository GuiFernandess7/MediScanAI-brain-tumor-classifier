#!/bin/sh

set -e

echo "Substituindo variáveis de ambiente..."
envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf

echo "Iniciando o Nginx..."
nginx -g 'daemon off;'