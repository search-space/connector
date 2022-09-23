#!/bin/bash

mkdir keys
cd keys

rm *.pem

# 1. Generate CA's private key and self-signed certificate
openssl req -x509 -newkey rsa:4096 -days 365 -nodes -keyout ca-key.pem -out ca-cert.pem \
	    -subj "/C=JP/ST=Tokyo/L=Shibuya/O=Search Space/OU=HQ/CN=*.searchspace.cloud/emailAddress=team@searchspace.cloud"

echo "CA's self-signed certificate"
openssl x509 -in ca-cert.pem -noout -text

# 2. Generate web server's private key and certificate signing request (CSR)
openssl req -newkey rsa:4096 -nodes -keyout server-key.pem -out server-req.pem \
	    -subj "/C=JP/ST=Tokyo/L=Shibuya/O=Search Space/OU=HQ/CN=*.searchspace.cloud/emailAddress=team@searchspace.cloud"

# 3. Use CA's private key to sign web server's CSR and get back the signed certificate
openssl x509 -req -in server-req.pem -days 60 -CA ca-cert.pem -CAkey ca-key.pem -CAcreateserial -out server-cert.pem


# 4. Generate client's private key and certificate signing request (CSR)

openssl req -newkey rsa:4096 -nodes --keyout client-key.pem -out client-req.pem \
	    -subj "/C=JP/ST=Tokyo/L=Shibuya/O=Search Space/OU=HQ/CN=*.searchspace.cloud/emailAddress=team@searchspace.cloud"

# 5. Use CA's private key to sign web clients's CSR and get back the signed certificate
openssl x509 -req -in client-req.pem -days 60 -CA ca-cert.pem -CAkey ca-key.pem -CAcreateserial -out client-cert.pem



echo "Server's signed certificate"
openssl x509 -in server-cert.pem -noout -text

echo "Client's signed certificate"
openssl x509 -in client-cert.pem -noout -text

chmod +r client-key.pem
chmod +r server-key.pem
chmod +r ca-key.pem

cp ca-cert.pem     ../../misc/squid/volumes/ssl/
cp ca-key.pem     ../../misc/squid/volumes/ssl/
cp client-cert.pem ../../misc/squid/volumes/ssl/
cp client-key.pem  ../../misc/squid/volumes/ssl/

cp ca-cert.pem     ../../misc/nginx/volumes/ssl/
cp ca-key.pem      ../../misc/nginx/volumes/ssl/
cp server-cert.pem ../../misc/nginx/volumes/ssl/
cp server-key.pem  ../../misc/nginx/volumes/ssl/

sudo mkdir -p /etc/docker/certs.d
sudo chown -R $USER:$USER /etc/docker

cp ca-cert.pem /etc/docker/certs.d

cd ..
