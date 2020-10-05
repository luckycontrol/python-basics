# PYTHON - BASICS

> 기억하고 싶은 것들

## 심볼 테이블 ( Symbol Table )
> 파이썬에서 객체의 이름과 주소를 딕셔너리 형태로 저장하는 것을 '심볼 테이블' 이라고 한다.

### 심볼 테이블이란,
1. 변수의 이름과 데이터의 주소를 저장하는 테이블
2. Global table과 Local table이 있다.
3. 테이블 내용은 딕셔너리 형태.

> Local Table은 객체가 존재하는동안 일시적으로 존재하다 사라진다.

심볼테이블이 존재한다는 것은 객체의 확장이 가능하다는 것이다.
> 내장 함수는 심볼테이블이 존재하지 않고, 내장 클래스의 객체는 심볼테이블이 존재하지만 확장 불가능하다.

 ![screensh](/SymbolTable.PNG)
 
### 객체 비교,
20글자 이하의 문자열, -5 ~ 256 내의 값은 Optimization를 위하여 이미 해당 값의 객체가 생성되었다면, 그 값으로 연결시켜준다.  
리스트와 튜플의 경우 값이 같아도 다른 객체를 참조한다.    
```python
i1 = 10
i2 = 10
print(i1 is i2) # True

s1 = "Hello"
s2 = "Hello"
print(s1 is s2) # True

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2) # False

i1 = 256
i2 = 255 + 1
print(i1 is i2) # True

i1 = 257
i2 = 256 + 1
print(i1 is i2) # False

i1 = 257
i2 = 257
print(i1 is i2) # True
```

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

## Python Regex ( 정규식 )
> [자주 사용하는 문자 클래스]  

[0-9] 또는 [a-zA-Z] 등은 무척 자주 사용하는 정규 표현식이다. 이렇게 자주 사용하는 정규식은 별도의 표기법으로 표현할 수 있다. 다음을 기억해 두자.  
**\d** - 숫자와 매치, [0-9]와 동일한 표현식이다.  
**\D** - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.  
**\s** - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.  
**\S** - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.  
**\w** - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.  
**\W** - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.  
대문자로 사용된 것은 소문자의 반대임을 추측할 수 있다.  


> **Raw String**을 사용하는 이유  
정규식 Raw String

만약 백슬래시 두개를 표현해야 한다면 ex) \\\
```python
p = re.complie('\\\\section') 
```  
과 같이 불편할것이다.  
따라서 Raw String을 사용하여 다음과 같이 표현한다.
```python
p = re.complie(r'\\section')
```  

## Python Float 연산
**[problem3의 no_2](https://github.com/luckycontrol/python-basics/blob/master/problem3/no_2.py) 참조**
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

## Python Virtual Environment ( Isolation Tool )
> 하나의 파이썬 설치가 모든 응용프로그램의 요구 사항을 충족시켜 줄 수 없다.  
>A는 1.0 버전이 필요하지만, B는 2.0이 필요한 경우..

**가상환경 설치 방법**
1. 프로젝트 폴더 생성 후 진입
2. python3 -m venv [가상환경이름] ex) python3 -m venv venv
3. source [가상환경이름]/bin/activate  
  
위 작업 이후 쉘이 (venv) $python3로 변경됨  
  
deactivate 으로 환경 나가기

> pip로 패키지 관리  

[serach], [install], [uninstall], [freeze]등의 부속명령어가 있다.  
```commandline
pip install novas
```  
패키지 이름 뒤에 **==** 과 버전 번호를 붙여 특정 버전의 패키지를 설치할 수 있다.
```commandline
pip install requests==2.6.0
```  
패키지를 최신 버전으로 업그레이드 하기
```commandline
pip install --upgrade [패키지이름]
```
가상환경에 설치된 패키지 목록 표시
```commandline
pip list
```

## Python DB 연결 (MariaDB)
> 파이썬과 MariaDB 연결

1. PyMySQL 모듈 설치
2. 파이썬과 DB 연결  
```python
import pymysql

# db connection 열기
db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='passwd',
    db='db',
    charset='utf8',
    autocommit=True
)

# cursor object로 db와의 작업을 수행한다.
cursor = db.cursor()
# show tables 쿼리 실행
cursor.execute("show tables")
# fetchall()로 모든 테이블 정보를 Fetch
data = cursor.fetchall()

print(data)

db.close()
```
