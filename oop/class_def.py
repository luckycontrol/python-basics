# 클래스 정의 테스트
# 가장 최상위 클래스는 Object
class MyString:
    pass


print("===== MyString class")
a = MyString() # 인스턴스화
print(type(a))

print("a의 클래스 확인: ", a.__class__)
print("MyString의 부모 확인: ", MyString.__bases__) # 여러 부모로부터 상속을 받을 수 있다.

print("a의 구성요소: ", dir(a))
print("object의 구성 요소: ", dir(object))