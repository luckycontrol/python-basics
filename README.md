# PYTHON - BASICS

> 기억하고 싶은 것들

## Input과 string 비교
> [problem4의 no_4](https://github.com/luckycontrol/python-basics/blob/master/problem3/no_4.py)에서 확인한 issue
```python
if user_input.isdigit() or user_input.lower() != "y" and user_input.lower() != "n":
```
위는 입력받은 input이 정수, 'y', 'n'이면 반복문을 나가는 조건문
위의 'y'와 'n'을 확인하는 조건문을  
```python
user_input.lower() != "y" or user_input.lower() != "n"
```
위와 같이 작성하면 **타입비교만 수행** 하며 무조건 True을 반환.

따라서 or가 아닌 **and**로 작성 해야함

## lambda - map / filter / reduce
> **map, filter, reduce** 라이브러리로 생성된 lambda 함수를 실행

```python
from functools import reduce

# map - lambda : 두 arr을 맵핑해서 덧셈 수행
print(list(map(lambda x, y: x + y, arr1, arr2)))

# filter - lambda : arr1에서 짝수를 거르고 출력
print(list(filter(lambda x: x % 2 == 0, arr1)))

# reduce - lambda : arr1 내 모든 수의 합 
print(reduce(lambda x, y: x + y, arr1))
```

## Python Float 연산
> 하드웨어에서 계산되는 2진 부동소수점을 이해할 필요가 있다.

1.0 + 2.0 연산을 수행할 경우, 3.0이 아닌 3.0000004가 출력된다.
이는 연산이나 하드웨어적인 버그가 아니다. 
- 하드웨어는 2진 부동소수점으로 연산을 수행한다.
- Python 인터프리터는 하드웨어에서 계산한 수를 10진수에 근사하게 출력한다.

> 보기 좋게 출력하기 위해서 **round()** 를 이용한다.
```python
# 각각의 진수에 맞게 수를 반올림
float_number = 2.754259040

round(float_number, 10)
round(float_number, 2)
round(float_number, 7)

``` 