def run():
    subs = ['I', 'You']
    verbs = ['Play', 'Love']
    objs = ['Hockey', 'Football']

    print([f'{sub} {verb} {obj}' for sub in subs for verb in verbs for obj in objs])

if __name__ == '__main__':
    run()