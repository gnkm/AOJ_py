# Aizu Online Judge Problems

## Problems

- [Aizu Online Judge](https://judge.u-aizu.ac.jp/onlinejudge/index.jsp)
- [Aizu Online Judge beta](https://onlinejudge.u-aizu.ac.jp/home) (ベータ版)

### Create virtual env

```
asdf install python pypy3.9-7.3.10
poetry env use $HOME/.asdf/installs/python/pypy3.9-7.3.10/bin/python
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
pytest xxx.py --exitfirst
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
