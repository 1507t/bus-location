# Introduce
https://bus-location.1507t.xyz で表示される車番が実際のものと異なる場合の変換規則について記述します。

# Schema

1行目にはヘッダを記述します。
```
system,real
```

2行目以降には実際の変換規則を記述します。
```
123,abc
456,def
...
```

> [!NOTE]
> system_number列はヘッダ行を除いて昇順ソートされている必要があります。

## Example

システム上で`0123`となっている車両の実際の車番が`xyz`である場合の例を示します。
```
system,real
0123,xyz
```
