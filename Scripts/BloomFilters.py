#Construction des blooms filters

import struct
import socket
import time
import hashlib
import binascii
import bitarray
import random
import bitcoin

class BloomFilt(object)

    UPDATE_NONE = 0
    UPDATE_ALL = 1
    UPDATE_P2PUBKEY_ONLY = 2
    UPDATE_MASK = 3

    def baseValues(nbItemsToFilter, falsePosRate):
        nFilterBytes = math.ceil(((-1)/math.log(2)*2nbItemsToFiltermath.log(p))/8) #in bytes
        if nFilterBytes > 36000:
            nFilterBytes = 36000 #Correction the maximum size of the filter
        filter = bitarray(nFilterBytes) #Filter creation
        filter = initFilt(filter, nFilterBytes)

        nHashFuncs = math.ceil((nFilterBytes8)/nbItemsToFilter*math.log(2))
        if nHashFuncs > 50:
            nHashFuncs = 50 #Correction the maximum number of Hash Functions
        nTweak = random.randint(0, 4294967295)


    def initFilt(filter, nFilterBytes):
        i = 0
        while i < nFilterBytes:
            filter[i] = FALSE
            i+=1
        return filter

