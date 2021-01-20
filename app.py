from gevent import monkey

monkey.patch_socket()

print ('monkey patching done')
worker_class = 'gevent'





