'''
정규식 Raw String

만약 백슬래시 두개를 표현해야 한다면 ex) \\
p = re.complie('\\\\section') 과 같이 불편할것이다.
따라서 Raw String을 사용하여 다음과 같이 표현한다.
p = re.complie(r'\\section')
'''

import re

def run():
    s = """
    <html>
        <body style='background-color:#fff'>
            <h4>Click</h4>
            <a href='http://www.python.org'>Here</a>
            <p>
                To connect to the most powerful tools in the world.
            </p>
        </body>
    </html>
    """

    p = re.compile(r"</?\w*\s?\w*=?'?\w*:?/?/?-?\w*.?\w*.?:?#?\w*'?>")
    m = p.findall(s)

    print(m)

    for word in m:
        s = s.replace(word, '')

    print(s)

if __name__ == '__main__':
    run()