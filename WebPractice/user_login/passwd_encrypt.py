'''
使用sha1加密
'''
import hashlib
pwd = 'jihaibo'
m = hashlib.sha1()
m.update(pwd.encode('utf-8'))
print (m.hexdigest())