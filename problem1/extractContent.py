import re

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

s_split = s.split('\n')

# p = re.compile("</?.*|>")
#
# m = p.findall(s)
#
# print(m)

# for word in m:
#     s = s.replace(word, '')
#
# print(s)



    # for word_index in range(len(line)):
    #     if len(line) <= 0:
    #         break
    #
    #     if line[word_index] == '<':
    #         switch = True
    #     elif line[word_index] == '>':
    #         switch = False
    #
    #     if switch is True:
    #         line = line.replace(line[word_index], '')

