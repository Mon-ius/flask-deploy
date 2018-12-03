sudo mkdir /etc/nginx/certs
sudo /home/monius/Documents/code/flask-deploy/b.com/b.com.sh
sudo /home/monius/Documents/code/flask-deploy/b.com/b.com.run
sudo cp /home/monius/Documents/code/flask-deploy/b.com/b.com.conf /etc/nginx/sites-enabled/
sudo cp /home/monius/Documents/code/flask-deploy/b.com/b.com.conf /etc/nginx/sites-available/
sudo cp /home/monius/Documents/code/flask-deploy/b.com/b.com.service /etc/systemd/system/
sudo systemctl enable b.com.service
sudo systemctl start b.com.service
