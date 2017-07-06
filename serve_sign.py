#!/usr/bin/env python

import SocketServer as ss
import struct
import os
from binascii import hexlify
import hashlib
from subprocess import Popen, PIPE


class Handler(ss.StreamRequestHandler):

    def handle(self):
        put = self.wfile.write

        put('Signature service, please send a message\n')
        msg = self.rfile.readline()[:-1]
        msghash = hashlib.sha256(msg).hexdigest()
        print('signing %s from %s' % (msg, self.client_address))

        process = Popen(['./sign', msghash], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()

        if stderr != '':
            put(stderr)
        else:
            put(stdout)


class ReusableTCPServer(ss.ForkingMixIn, ss.TCPServer):
    allow_reuse_address = True

if __name__ == '__main__':
    HOST, PORT = ('0.0.0.0', 1111)
    ss.TCPServer.allow_reuse_address = True
    server = ReusableTCPServer((HOST, PORT), Handler)
    server.serve_forever()
