## Код
```
sum_elements([], 0).
sum_elements([X|Xs], Sum) :- 
    sum_elements(Xs, Rest),
    Sum is X + Rest.
```
## Ввод-вывод

```
sum_elements([1, 2, 3, 4], Sum).
Sum = 10.

sum_elements([5, 10, 15], Sum).
Sum = 30.

sum_elements([], Sum).
Sum = 0.
```
