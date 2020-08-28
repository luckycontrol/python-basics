# 딕셔너리 컴프리헨션

s = 'This is test sentence'

print({i:j for i, j in enumerate(s.split())})