import random
import time
import ak_pb2
from itertools import cycle


def xor(s, k):
  return_me = ''
  k = hex(k)[2:]
  bytes = cycle([int(str(a)+str(b), 16) for a,b in zip(k[0::2], k[1::2])])
  pairs = zip(s, bytes)
  for c,i in pairs:
    return_me += unicode( ord(c) ^ i )
  return return_me


def frame_maker(id):
  datas = ["Th---i-s -i-s s-o-me---- -da---ta", "T----H-I--S i----s- SOME- d----a-ta", "t-HIS i--S- sOME ---d----AT-A", "this- is som-e data", "T----HIS---IS- SOME -DA-TA-----"]
  frame = ak_pb2.Frame()
  frame.msg_id = id
  frame.nonce = int(time.time())
  frame.payload.key = random.randint(1,2**31)
  frame.payload.key_size = 4
  if id == 0xa8:
    frame.payload.data = xor("PUT YOUR SECRET DATA HERE", frame.payload.key)
  else:
    frame.payload.data = xor(random.choice(datas), frame.payload.key)
  frame.payload_len = len(frame.payload.data)
  return frame.SerializeToString()


for i in range(0, 0xff):
  print repr(frame_maker(i))
