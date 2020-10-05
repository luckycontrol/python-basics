class Point:

    count_of_instance = 0   # self 없이 클래스 영역에 선언
    # 모든 인스턴스가 공유하는 객체

    # 생성자 -> 여러가지 생성자에 대응하는 단 한개의 생성자를 만들어야 함
    # 주로 객체의 초기화 담당
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        Point.count_of_instance += 1


    # 소멸자
    def __del__(self):
        Point.count_of_instance -= 1

    # (일반 사용자용)
    def __str__(self):
        return f"x = {self.x}, y = {self.y}, count_of_instance = {self.count_of_instance}"

    # repr 함수를 호출하면 반환되는 문자열 포맷
    # eval 함수를 이용해 해당 객체를 복원할 수 있는 용도의 문자열 (개발자용)
    def __repr__(self):
        return f"Point({self.x}, {self.y})"


    # def __enter__(self): # with ~ as 구문이 시작될 때
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb): # with ~ as 구문이 종료될 때
    #     return self

    def __add__(self, other):
        # Point(x, y) + other
        if isinstance(other, (int, float)): # other의 타입을 체크
            return Point(self.x + other, self.y + other)
        elif isinstance(other, Point): # other가 Point
            return Point(self.x + other.x, self.y + other.y)
        else:
            return self + other


    def __sub__(self, other):
        # Point(x, y) - other
        if isinstance(other, (int, float)):
            return Point(self.x - other, self.y - other)
        elif isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            return self - other


    def __eq__(self, other):
        # Point(x, y) == other
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return self == other


    # 역이행 연산자
    # other + Point(x, y)
    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return Point(self.x + other, self.y + other)
        return self + other

    def set_x(self, x): # 인스턴스 메서드의 첫 번째 인자는 self
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def draw(self):
        print(f"점 ({self.x}, {self.y})를 그렸습니다.")

    @classmethod
    def get_count_of_instance(cls): # cls -> 클래스 객체의 참조 주소
        return cls.count_of_instance

    # class namespace 안쪽에 있을 뿐
    # class 멤버와는 전혀 연관없음
    @staticmethod
    def static_method():
        print("static method 호출")


# 상속
# 부모로부터 멤버를 물려받은 이후, 필요한 부분만 추가 구현
# 부모가 가진 메서드를 재정의한다
class ColorPoint(Point):    # 부모가 Point인 서브클래스
    def __init__(self, x=0, y=0, color="black"):
        # 부모(super)의 생성자를 호출
        super().__init__(x, y)  # 부모 생성자 호출
        self.color = color

    def draw(self):
        print(f"{self.color} 색 점({self.x}, {self.y})를 그렸습니다.")

    def __str__(self):  # 출력 포맷 변경
        return f"ColorPoint({self.x}, {self.y}), {self.color}"

