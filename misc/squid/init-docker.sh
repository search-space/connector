#!/bin/bash

docker-compose -f docker-compose_initial.yml up -d --build

docker-compose ps

docker exec -it forward-proxy /usr/lib/squid/security_file_certgen -c -s /var/lib/squid/ssl_db -M 20MB

docker cp forward-proxy:/var/lib/squid/ssl_db ./volumes/

docker-compose -f docker-compose_initial.yml stop
