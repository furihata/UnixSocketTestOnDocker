# UnixSocketTestOnDocker

## 何をするものか

Docker 上で Unix domain socket を使う場合、指定したファイルパスがホスト側のドライブをマウントしたものであった場合に、環境によって正しく動作しないのではないか？ というのを確認するものです。

具体的には、```Windows の Docker Desktop を Hyper-V で動かしている場合``` だけ動作しないのではないかと考えています。

## 確認方法

まず Docker イメージを作成します。
テスト用ファイルを入れています。

```
docker build -t test-ubuntu .
```

ホスト側のドライブをマウントしてコンテナを起動します。
```d:\tmp\socktest``` という部分は適宜変更して下さい。

```
docker run -v d:\tmp\socktest:/var/tmp/socktest -it test-ubuntu
```

この状態で

```
# cd /root
# python3 receiver.py
```

上記のようにレシーバーを起動すると、ホスト側の環境によってエラーが出たり出なかったりするようです。
Windowsのファイルシステム上に Unix domain socket のファイルが作れないためではないかと思っていますが、ドキュメント上で具体的にこれを説明している部分を見つけられませんでした。
もしご存知の方がおられましたら教えていただけると嬉しいです。

## 補足

これは sender.py で入力したテキストを receiver.py が受け取るサンプルです。
プロセス間通信を ```/tmp/socktest/testsock.sock``` というパスを使って Unix domain socket を使って行っています。
この ```/tmp/socktest``` というディレクトリをホスト側のドライブをマウントしたものに変更すると、環境によってはエラーになるのではと考えています。

雑に作成しているため、エラー処理などは端折られています。また終了後に testsock.sock ファイルは消えないので自分で消す必要があります。

