# Aizu Online Judge Problems

## Problems

- [Aizu Online Judge](https://judge.u-aizu.ac.jp/onlinejudge/index.jsp)
- [Aizu Online Judge beta](https://onlinejudge.u-aizu.ac.jp/home) (ベータ版)

### Create virtual env

2022/07/09 時点の AOJ の Python バージョンは 3.6.3 だが、M1 Mac には pyenv で古いバージョンをインストールできないため異なるバージョンを使用する。

```
anyenv install pyenv
pyenv install 3.8.13
poetry env use $HOME/.anyenv/envs/pyenv/versions/3.8.13/bin/python
```

### Prepare

```
poetry shell
poetry install
```

### Execute

```
python xxx.py < input.txt
```

### Run tests

```
pytest xxx.py
```

### Exit virtual env

```
exit
```

## Template file

cf. [https://github.com/gnkm/cheetsheet/tree/master/python/online_judge](https://github.com/gnkm/cheetsheet/tree/master/python/online_judge)

## File name rule

- `mycode.py`: I wrote
- `example_answer_0X.py`: other's answer
