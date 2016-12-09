from os.path import dirname, join

def read():
  with open(join(dirname(__file__), 'bgwords')) as f:
    return set([unicode(s, 'utf8') for s in f.read().split()])
