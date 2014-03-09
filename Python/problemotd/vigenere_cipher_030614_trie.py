import itertools
import word_utils
import string
def decipher(key, msg, alphabet=string.ascii_lowercase):
    alphabet_len = len(alphabet)
    key_len = len(key)
    d = { c:i for i,c in enumerate(alphabet)}
    d_rev = {key : val for val, key in d.items()}
    key = key.lower()
    msg = msg.lower()
    key_d = { i:d[c] for i,c in enumerate(key) }
    real_msg = []
    for i,c in enumerate(msg):
        real_msg.append(d_rev[(d[c] - key_d[(i % key_len)]) % alphabet_len])

    return ''.join(real_msg)

def crack(msg, alphabet=string.ascii_lowercase, max_len=5):
    # generate keys:
    print 'generating keys...'
    possible_keys = []
    for i in xrange(1, max_len+1):
        for key in [''.join(key) for key in list(itertools.product(alphabet, repeat=i))]:
            possible_keys.append(key)
    print 'done.'

    for key in possible_keys:
        possible_ans = decipher(key, msg)
        possible_breakdowns = word_utils.break_sentence(possible_ans)
        if len(possible_breakdowns) != 0:
            print 'key:', key, '\ndeciphered:', possible_ans, '\nbreakdowns:', possible_breakdowns
            return possible_breakdowns

if __name__ == '__main__':
    crack('ZEJFOKHTMSRMELCPODWHCGAW', max_len=5)