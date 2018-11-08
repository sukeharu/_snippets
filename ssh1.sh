$ mkdir ~/.ssh
$ chmod 600 ~/.ssh
$ cp ~/Downloads/<id>.key ~/.ssh/<id>_rsa # ~/Downloads...はダウンロードしたファイルのパスとファイル名。コピー先ファイル名のid_<id>_rsaは何でもよいが、半角。拡張子なし
$ chmod 400 <id>_rsa
