#! /usr/bin/env python3

from pathlib import Path


# pathlibの基本。カレントワーキングディレクトリの相対パスを取得
path = Path()
print(path)

# __file__は、実行ファイルのカレントワーキングディレクトリからの相対パスを返す
print(__file__)

# __file__を絶対パスにしたいときは：
path = Path(__file__)
abspath = path.resolve()
print(abspath)

# パスの結合
new_file = abspath / 'new_file.py'
print(new_file)

# new_fileが存在しているかどうかはexists()で調べられる
print(new_file.exists())
