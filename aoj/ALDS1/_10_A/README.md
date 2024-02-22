# 10_A : Fibonacci Number

https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_10_A

## パフォーマンスの比較

### 実装方法

- `mycode_01.py`: Dynamic programming を自分で実装
- `mycode_02.py`: `lru_cache` を使用

### 結論

`lru_cache` を使うのがよい。

### 実験

```
hyperfine -r 100 --ignore-failure python ALDS1/_10_A/mycode.py < ALDS1/_10_A/input_02.txt
```

output is the following.

```
Benchmark 1: python
  Time (mean ± σ):       8.2 ms ±   0.6 ms    [User: 6.3 ms, System: 1.3 ms]
  Range (min … max):     7.7 ms …  12.9 ms    100 runs
```

```
hyperfine -r 100 --ignore-failure python ALDS1/_10_A/mycode_02.py < ALDS1/_10_A/input_02.txt
```

output is the following.

```
Benchmark 1: python
  Time (mean ± σ):       8.3 ms ±   0.3 ms    [User: 6.4 ms, System: 1.4 ms]
  Range (min … max):     7.7 ms …   9.7 ms    100 runs
```
