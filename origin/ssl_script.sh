export CF_Key={{KEY}}
export CF_Email={{EMAIL}}

sudo apt install socat -y

sudo wget -O -  https://get.acme.sh | sh

sudo ~/.acme.sh/acme.sh --force --issue -d "*.{{domain}}" -d "{{domain}}" --dns dns_cf \
--cert-file /etc/nginx/certs/site.crt \
--key-file /etc/nginx/certs/site.key \
--fullchain-file /etc/nginx/certs/fullchain.crt \
--ca-file /etc/nginx/certs/ca.crt 
