cat > /etc/rc.local <<EOL
#!/bin/sh -e
(sudo python /usr/local/bin/jfe -s -v -D)&
return 0
EOL

git clone https://github.com/yasir1brahim/jfe.git

chmod +x jfe/*

cd jfe 

sudo ln -sf $(pwd)/jfe /usr/local/bin/jfe

sudo reboot
