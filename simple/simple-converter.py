# coding: utf-8
import os
import sys
from glob import glob
from PIL import Image

# 終了ワード
exit_words:tuple[str] = ('', 'exit', 'quit', 'stop')
# 変換対応 拡張子
extensions:tuple[str] = ('png', 'jpg')

# パスを入力
print('画像のあるディレクトリパスを選択してください')
src:str = input('> ')

# 終了ワード --> 終了
if src in exit_words:
    sys.exit()

# パスが存在しない --> 終了
if not os.path.exists(src):
    input('パスが存在しません...')
    sys.exit()

# 画像を集める
os.chdir(src)
targets:list[str] = []
for extension in extensions:
    targets += glob(f'*.{extension}')

# 無い --> 終了
if not targets:
    input('画像ファイルがありません...')
    sys.exit()

# webp フォルダが無ければ、その場に作る
if not os.path.exists('./webp/'):
    os.mkdir('webp')

# 進捗用 変数
length:int = len(targets)
progress:int = 0
failed:list[str] = []

# ファイルを変換して保存
for path in targets:
    dst:str = path.rsplit('.', 1)[0] + '.webp'
    try:
        img = Image.open(path)
        img.save(f'./webp/{dst}')
    except Exception as e:
        failed.append(path)
        print(e)
    progress += 1
    print(f'\rConverting... {progress}/{length} files', end='')
if failed:
    print('以下のファイルの変換に失敗しました...')
    for path in failed:
        print(f'  {path}')

print(f'指定フォルダに "webp" フォルダを作成しました')
