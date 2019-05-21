# Code Listing #1

"""
Take an input stream and hash it's contents using MD5 and return the hash digest
"""

# hash_stream.py
from hashlib import sha1
from hashlib import md5

def hash_stream_sha1(stream, chunk_size=4096):
    """ Hash a stream of data using sha1 """
    
    shash = sha1()
    
    for chunk in iter(lambda: stream.read(chunk_size), ''):
        shash.update(chunk.encode('utf-8'))

    return shash.hexdigest()

def hash_stream_md5(stream, chunk_size=4096):
    """ Hash a stream of data using sha1 """
    
    shash = md5()
    
    for chunk in iter(lambda: stream.read(chunk_size), ''):
        shash.update(chunk.encode('utf-8'))

    return shash.hexdigest()

