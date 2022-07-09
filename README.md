# Aizu Online Judge Problems

## Problems

[Aizu Online Judge](https://judge.u-aizu.ac.jp/onlinejudge/index.jsp)
[Aizu Online Judge beta](https://onlinejudge.u-aizu.ac.jp/home)

### Create virtual env

2022/07/09 時点の AOJ の Python バージョンは 3.6.3 だが、M1 Mac だと pyenv で古いバージョンをインストールできないため異なるバージョンを使用する。

```
anyenv install pyenv
pyenv install 3.8.13
poetry env use $HOME/.anyenv/envs/pyenv/versions/3.8.13/bin/python
```

### Prepare

```
poetry install
poetry shell
```

### Execute

```
python xxx.py < input.txt
```

### Exit virtual env

```
exit
```
