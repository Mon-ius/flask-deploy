export CF_Key={{KEY}}
export CF_Email={{EMAIL}}

apt install socat -y
mkdir /etc/nginx/certs
wget -O -  https://get.acme.sh | sh

~/.acme.sh/acme.sh --force --issue -d "*.{{domain}}" -d "{{domain}}" --dns dns_cf \
--cert-file /etc/nginx/certs/site.crt \
--key-file /etc/nginx/certs/site.key \
--fullchain-file /etc/nginx/certs/fullchain.crt \
--ca-file /etc/nginx/certs/ca.crt 
