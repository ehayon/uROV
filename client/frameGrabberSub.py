# -*- coding: utf-8 -*-
"""
framegrabberSub v0.1

Demonstrates how to subscribe to a MJPEG
stream published using 0mq.

Created on Tue Sep 19 21:30:57 2013

@author: Matthew Witherwax (Lemoneer) lemoneer@outlook.com
@copyright: 2013 Matthew Witherwax (framegrabberSub 0.1 implementation)
@license: BSD

                           BSD LICENSE

Copyright (c) 2013, Matthew Witherwax
All rights reserved. 

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

 * Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.

 * Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in
   the documentation and/or other materials provided with the
   distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import zmq
import cv2
from cv2 import cv
import numpy as np

def main():
    """ main method """
    
    # Prepare our context and publisher
    context = zmq.Context(1)
    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://192.168.1.28:9997")
    subscriber.setsockopt(zmq.SUBSCRIBE, "")
    
    cv2.namedWindow("stream")
    
    while True:
        # Read envelope with address
        [address, contents] = subscriber.recv_multipart()
        pic = np.fromstring(contents, np.int8)
        img = cv2.imdecode(pic, cv.CV_LOAD_IMAGE_COLOR)
        cv2.imshow("stream", img)
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC       
            break
     
    cv2.destroyAllWindows()

    # We never get here but it is good form
    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
