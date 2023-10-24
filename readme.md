# これはなに

`.png` と `.jpg` を `.webp` に変換してくれる簡易ツールです。
ほんとにそれだけです。

# ダウンロード

1. 右上の、きみどり色の`<>Code`というボタンを押します。
2. `Download Zip` のボタンを押します。

# 実行方法

## 実行ファイル (.exe) で動かす

準備中です。

## Pythonで動かす

1.  Pythonをインストールします
2.  Pythonに"Pillow"をインストールします
  ```cmd
  python -m pip install Pillow
  ```
3.  `simple` か `multi-thread` のどちらかにある`.py` ファイルを実行します
  ```cmd
  python simple-converter.py
  ```
  もしくは
  ```cmd
  python mt-converter.py
  ```

# ディレクトリの違い

### シンプル版 `simple`

昨日シンプル版。  
はじめてのPythonの解読の練習にどうぞ。

### マルチスレッド版 `multi-thread`

マルチスレッド版。  
こっちの方が処理が早いはずです。
