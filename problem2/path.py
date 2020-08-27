import sys

print('경로 분해 : ', end=' ')
print(sys.path[0].split('\\'))

print()

print('디렉터리 경로와 현재경로 : ', end=' ')
path_list = sys.path[0].split('\\')
pwd = path_list.pop()

print('\\'.join(path_list), end='\t')
print(f'{pwd}')