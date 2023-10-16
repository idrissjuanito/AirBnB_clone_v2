#!/usr/bin/env bash
# bash script install nginx and ready server to servee
if [[ ! -d /data ]]; then
	mkdir -p /data/web_static/{releases,shared}
	mkdir -p "/data/web_static/releases/test"
fi
if [[ -L "/data/web_static/current" ]]
then
	rm "/data/web_static/current"
fi
ln -s "/data/web_static/releases/test" /data/web_static/current
chown -R ubuntu:ubuntu /data/

which nginx
if [[ $? -eq 1 ]]; then
	apt-get update
	apt install -y curl gnupg2 ca-certificates lsb-release \
			debian-archive-keyring
	Download and save the NGINX signing key:
	curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor \
	| tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null
	OS=$(lsb_release -is | tr '[:upper:]' '[:lower:]') RELEASE=$(lsb_release -cs)
	echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
	http://nginx.org/packages/${OS} ${RELEASE} nginx" \ | tee /etc/apt/sources.list.d/nginx.list
	apt-get update
    apt-get install -y nginx
    nginx
fi
sed -i "/location \/ {/i\ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/; \n\t}" \
	/etc/nginx/conf.d/default.conf
nginx -s reload
