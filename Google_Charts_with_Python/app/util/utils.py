from os.path import sep, join

def pjoin(*args, **kwargs):
  return join(*args, **kwargs).replace(sep, '/')