'''
1-byte 0xxxxxxx
2-byte 110xxxxx 10xxxxxx
3-byte 1110xxxx 10xxxxxx 10xxxxxx
4-byte 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

Shortest possible
U+10FFFF 0x10FFFF
100001111111111111111

# pseudo code
def validate_utf8(stream):
    iterate over bytes in stream
    if in middle of parsing a more than one byte character:
        1) validte that it starts with 10xxxxxx
        2) aggregate the payload for the byte
    if its the last part of the character:
        make sure, after aggregation that it doesnt violate shortest possible
    else:
        start parsing and determine how many bytes are we parsing

        3) if its the last part of a 4-byte character than validate that its not bigget tha 0x10FFFF
'''
def validate_utf8(byte_stream):
  minimum_per_byte_legnth = {2:(0b1 << 7) , 3: (0b1 << 11) , 4:(0b1 << 16)}
  is_parsing = False
  aggregator = None

  remanining_bytes_to_parse = None
  for byte in byte_steram: # assumption
    if not is_parsing:
     # determine the number of bytes in this character
     mask = (0b11111 << 3) # 11111000
     num_byte_sig = byte & mask
     if (num_byte_sig & 0b10000) == 0:
        pass
     elif num_byte_sig == 0b11110:
        # were parsing 4-byte character
        is_parsing = 4
        aggregator = byte & 0b111
        remanining_bytes_to_parse = 3
     elif (num_byte_sig & 0b11110) == 0b11100:
        # were parsing 3-byte character
        is_parsing = 3
        aggregator = byte & 0b1111
        remanining_bytes_to_parse = 2
     elif (num_byte_sig & 0b11100) == 0b11000:
        # were parsing 2-byte character
        is_parsing = 2
        aggregator = byte & 0b11111
        remanining_bytes_to_parse = 1
     else:
        return False
    else:
      if byte & (0b11 << 6) != 0b10000000:
        return False
      aggregator = (aggregator << 6) | (byte & 0b00111111)
      remanining_bytes_to_parse -= 1
      if remanining_bytes_to_parse == 0:
        # validate we dont break the shortest possible rule
        if aggregator < minimum_per_byte_legnth[is_parsing]:
          return False
        if is_parsing == 4 and aggregator > 0b100001111111111111111:
          return False
        if_parsing = False

  return True
