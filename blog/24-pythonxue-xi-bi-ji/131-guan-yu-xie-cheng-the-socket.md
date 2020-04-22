# 关于协程

The sockets are still synchronous / blocking with merely gevent.pawn().
The way to solve it is to use gevent monkey patch to patch all from the begining so that it could capture the socket status (poll / select).
Or directly use gevent.sleep() to force worker sleep and initiate another worker.
