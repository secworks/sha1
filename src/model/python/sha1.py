#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# sha1.py
# ---------
# Simple, pure Python model of the SHA-1 function. Used as a
# reference for the HW implementation. The code follows the structure
# of the HW implementation as much as possible.
#
#
# Author: Joachim Strömbergson
# (c) 2014 Secworks Sweden AB
# 
# Redistribution and use in source and binary forms, with or 
# without modification, are permitted provided that the following 
# conditions are met: 
# 
# 1. Redistributions of source code must retain the above copyright 
#    notice, this list of conditions and the following disclaimer. 
# 
# 2. Redistributions in binary form must reproduce the above copyright 
#    notice, this list of conditions and the following disclaimer in 
#    the documentation and/or other materials provided with the 
#    distribution. 
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT 
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS 
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE 
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, 
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, 
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, 
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#=======================================================================

#-------------------------------------------------------------------
# Python module imports.
#-------------------------------------------------------------------
import sys


#-------------------------------------------------------------------
# Constants.
#-------------------------------------------------------------------


#-------------------------------------------------------------------
# ChaCha()
#-------------------------------------------------------------------
class SHA1():
    def __init__(self, verbose = 0):
        self.verbose = verbose
        self.H = [0] * 5
        self.T = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.W = [0] * 80
        self.k = 0

        
    def init(self):
        self.H = [0x67452301, 0xefcdab89, 0x98badcfe,
                  0x10325476, 0xc3d2e1f0]
        

    def next(self, block):
        self._W_schedule(block)
        self._copy_digest()
        for i in range(80):
            self._sha1_round(i)
        self._update_digest()


    def get_digest(self):
        return self.H


    def _copy_digest(self):
        self.a = self.H[0] 
        self.b = self.H[1] 
        self.c = self.H[2] 
        self.d = self.H[3] 
        self.e = self.H[4] 
    
    
    def _update_digest(self):
        self.H[0] = (self.H[0] + self.a) & 0xffffffff 
        self.H[1] = (self.H[1] + self.b) & 0xffffffff 
        self.H[2] = (self.H[2] + self.c) & 0xffffffff 
        self.H[3] = (self.H[3] + self.d) & 0xffffffff 
        self.H[4] = (self.H[4] + self.e) & 0xffffffff 


    def _sha1_round(self, round):
        if round <= 19:
            self.k = 0x5a827999        
            self.f = self._Ch(self.b, self.c, self.d)

        elif 20 <= round <= 39:
            self.k = 0x6ed9eba1
            self.f = self._Parity(self.b, self.c, self.d)

        elif 40 <= round <= 59:
            self.k = 0x8f1bbcdc
            self.f = self._Maj(self.b, self.c, self.d)

        elif 60 <= round <= 79:
            self.k = 0xca62c1d6
            self.f = self._Parity(self.b, self.c, self.d)

        if self.verbose:
            print("Round %0d" % round)
            print("Round input values:")
            print("a = 0x%08x, b = 0x%08x, c = 0x%08x" % (self.a, self.b, self.c))
            print("d = 0x%08x, e = 0x%08x" % (self.d, self.e))
            print("f = 0x%08x, k = 0x%08x, w = 0x%08x" % (self.f, self.k, self.W[round]))
            
        
        self.T = (self._rotl32(self.a, 5) + self.f + self.e + self.k + self.W[round]) & 0xffffffff
        self.e = self.d
        self.d = self.c
        self.c = self._rotl32(self.b, 30)
        self.b = self.a
        self.a = self.T

        if self.verbose:
            print("Round output values:")
            print("a = 0x%08x, b = 0x%08x, c = 0x%08x" % (self.a, self.b, self.c))
            print("d = 0x%08x, e = 0x%08x" % (self.d, self.e))
            print("")


    def _W_schedule(self, block):
        # Expand the block into 80 words before round operations.
        for i in range(80):
            if (i < 16):
                self.W[i] = block[i]
            else:
                self.W[i] = self._rotl32((self.W[(i - 3)] ^ self.W[(i - 8)] ^
                                          self.W[(i - 14)] ^ self.W[(i - 16)]), 1)
        if (self.verbose):
            print("W after schedule:")
            for i in range(80):
                print("W[%02d] = 0x%08x" % (i, self.W[i]))
            print("")


    def _Ch(self, x, y, z):
        return (x & y) ^ (~x & z)


    def _Maj(self, x, y, z):
        return (x & y) ^ (x & z) ^ (y & z)


    def _Parity(self, x, y, z):
        return (x ^ y ^ z)

    def _rotl32(self, n, r):
        return ((n << r) | (n >> (32 - r))) & 0xffffffff


def compare_digests(digest, expected):
    if (digest != expected):
        print("Error:")
        print("Got:")
        print(digest)
        print("Expected:")
        print(expected)
    else:
        print("Test case ok.")
        
    
#-------------------------------------------------------------------
# main()
#
# If executed tests the ChaCha class using known test vectors.
#-------------------------------------------------------------------
def main():
    print("Testing the SHA-256 Python model.")
    print("---------------------------------")
    print

    my_sha1 = SHA1(verbose=1);

    # TC1: NIST testcase with message "abc"
    TC1_block = [0x61626380, 0x00000000, 0x00000000, 0x00000000, 
                 0x00000000, 0x00000000, 0x00000000, 0x00000000,
                 0x00000000, 0x00000000, 0x00000000, 0x00000000,
                 0x00000000, 0x00000000, 0x00000000, 0x00000018]
    
    TC1_expected = [0xa9993e36, 0x4706816a, 0xba3e2571,
                    0x7850c26c, 0x9cd0d89d]
    
    my_sha1.init()
    my_sha1.next(TC1_block)
    my_digest = my_sha1.get_digest()
    compare_digests(my_digest, TC1_expected)

    

#-------------------------------------------------------------------
# __name__
# Python thingy which allows the file to be run standalone as
# well as parsed from within a Python interpreter.
#-------------------------------------------------------------------
if __name__=="__main__": 
    # Run the main function.
    sys.exit(main())

#=======================================================================
# EOF sha1.py
#=======================================================================
