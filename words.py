# coding: utf8
from os.path import dirname, join
alphabet = u'абвгдежзийклмнопрстуфхцчшщъьюя'

def read():
  with open(join(dirname(__file__), 'bgwords')) as f:
    return (unicode(s, 'utf8') for s in f.read().split())
