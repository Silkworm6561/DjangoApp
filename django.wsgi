import os, sys
virtual_env = os.path.expanduser('~/venv37')
activate_this = os.path.join(virtual_env, 'bin/activate')
exec(open(activate_this).read(), dict(__file__=activate_this))
sys.path.insert(0, os.path.expanduser('~/domains/j65516585.myjino.ru/hello_world/hello_world'))
from wsgi.py import application