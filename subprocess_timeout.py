import subprocess

ret = -1
try:
    ret = subprocess.call(['sleep', '10'], timeout=12)
except Exception:
    pass

print(ret)

__author__ = 'yln'
