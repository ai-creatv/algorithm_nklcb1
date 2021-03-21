# Python

## 학습 목표

- 자주 사용되는 Python 문법을 Review한다.
- Python로 프로그래밍할 때, 좋은 습관/나쁜 습관들을 알아본다.
- Python Reference를 활용하는 방법을 이해한다.

## Python 주요 문법 Review

- 다양한 방식의 for문

  ```python
  a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  for i in range(10):
      print(a[i])
  ```

  ```python
  a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  for elem in a:
      print(elem)
  ```

- 함수의 구현 및 함수 클로저

  ```python
  def solution(x, y):
      return x + y
  ```

  ```python
  def outer(n):
      def inner(x):
          return x + n
      return inner
  ```

  ```python
  def outer():
      outer_sum = 0
      def inner(x):
          nonlocal outer_sum # 외부 값을 수정하기 위해 필요
          outer_sum += x
          return outer_sum
      return inner
  ```

- List Comprehension
  - for문에 비해 빠르게 동작하는 장점이 있음

  ```python
  a = [x for x in range(10)]
  ```

- Generator
  - 미리 값을 만들어두지 않기 때문에 메모리를 적게 사용

  ```python
  a = (x for x in range(10))
  ```

- Dictionary Comprehension
  - 딕셔너리도 지능형 리스트처럼 구현 가능

  ```python
  a = {key:key**2 for key in range(10)}
  ```

- Lambda expression

  ```python
  print((lambda x: x**2)(10))
  ```

- 삼항 연산자

  ```python
  b = 20
  a = 1 if b > 0 else -1
  ```

- map 함수

  ```python
  a = [x for x in range(10)]
  a = list(map(lambda x: x**10, a))
  ```

- filter 함수

  ```python
  a = [x for x in range(100)]
  a = list(filter(lambda x: x % 2, a))
  ```

- 클래스의 구현

  ```python
  class Foo:
      cls_var = 10  # 클래스 멤버 변수

      def __init__(self, x):
          self.x = x  # 인스턴스 멤버 변수

      def method(self, y):  # 인스턴스 메소드
          return self.x + y

      @classmethod
      def cls_method(cls, z):  # 클래스 메소드
          return cls.cls_var + z

      @staticmethod
      def static_method(k):  # 스태틱 메소드
          return k
  ```

## 좋은 습관/나쁜 습관

- 좋은 습관
  - 변수 명을 정할 때에는 의미가 있는 이름으로 결정
  - 변수, 클래스 명 등은 컨벤션을 지켜서 일정하게 구현 (ClassName, method_name, var_name, CONST_NAME, ...)
  - PEP-8을 지켜서 가독성 좋은 코드 작성
  - map, filter 등을 이용하여 함수형 프로그래밍을 적절하게 채용

- 나쁜 습관
  - C언어처럼 구현하는 습관 (항상 for문으로 모든 것을 처리)
    - Python은 for문으로 처리할 경우 속도가 느리고 코드의 가독성이 떨어짐
  - 신기한 코드
    - 나만 알아볼 수 있는 신기한 코드는 적절하지 않음
  - 무조건 짧은 코드
    - Short code 자체도 의미는 있으나, 일반적으로는 사용하지 않음
  - 무조건 내가 구현
    - 기본 파이썬 라이브러리에 구현된 것은 import해서 쓰는 편이 좋다.
  - 무조건 최적화
    - 최적화 vs. 가독성 사이에 trade-off 관계가 있을 경우, 상황에 맞게 결정한다.

## Python References

- <https://docs.python.org/3/>
- <https://devdocs.programmers.co.kr/python/>
