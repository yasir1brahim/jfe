cat > /etc/rc.local <<EOL
#!/bin/sh -e
(sudo python /usr/local/bin/jfe -s -D -v)&
return 0
EOL

chmod +x jfe/*

cd jfe 

sudo ln -sf $(pwd)/jfe /usr/local/bin/jfe

sudo python /usr/local/bin/jfe -s -D -v
