$ cd
$ mkdir bin
$ cd bin
$ curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
$ chmod +x wp-cli.phar
$ alias 'wp=/opt/php-7.2.6/bin/php ~/bin/wp-cli.phar'
$ source source ~/.bashrc
