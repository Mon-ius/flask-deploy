export {{OP1}}
export {{OP2}}

sudo apt install socat -y

sudo wget -O -  https://get.acme.sh | sh

sudo ~/.acme.sh/acme.sh --force --issue -d "*.{{DOMAIN}}" -d "{{DOMAIN}}" --dns {{DNS_OP}} \
--cert-file /etc/nginx/certs/site.crt \
--key-file /etc/nginx/certs/site.key \
--fullchain-file /etc/nginx/certs/fullchain.crt \
--ca-file /etc/nginx/certs/ca.crt 
