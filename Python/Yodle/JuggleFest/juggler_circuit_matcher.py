__author__ = 'Shay Weiss'

''' what we have here is obviously a small generalization of the stable marriage problem, where instead having each
    girl (circuit) accept just one suitor (juggler), each accepts a total of |jugglers|/|circuits| jugglers.

    The base code was taken from: http://rosettacode.org/wiki/Stable_marriage_problem
    and was modified to accommodate the new requirements (that's why code is a bit fugly)
'''

import copy
import input_file_parser

circuits, jugglers = input_file_parser.parse_input_file("juggle_fest_example.txt")

def jugglers_to_jugglers_prefers(jugglers):
    jugglers_prefers = {}
    for juggler in jugglers:
        jugglers_prefers[juggler.name] = juggler.circuit_preferences
    return jugglers_prefers

def circuits_to_circuits_prefers(circuits, jugglers):
    circuits_prefer = {}
    for circuit in circuits:
        circuits_prefer[circuit.name] = circuit.calc_preference_list(jugglers)
    return circuits_prefer

guy_prefers_demo = {
 'abe':  ['abi', 'eve', 'cath', 'ivy', 'jan', 'dee', 'fay', 'bea', 'hope', 'gay'],
 'bob':  ['cath', 'hope', 'abi', 'dee', 'eve', 'fay', 'bea', 'jan', 'ivy', 'gay'],
 'col':  ['hope', 'eve', 'abi', 'dee', 'bea', 'fay', 'ivy', 'gay', 'cath', 'jan'],
 'dan':  ['ivy', 'fay', 'dee', 'gay', 'hope', 'eve', 'jan', 'bea', 'cath', 'abi'],
 'ed':   ['jan', 'dee', 'bea', 'cath', 'fay', 'eve', 'abi', 'ivy', 'hope', 'gay'],
 'fred': ['bea', 'abi', 'dee', 'gay', 'eve', 'ivy', 'cath', 'jan', 'hope', 'fay'],
 'gav':  ['gay', 'eve', 'ivy', 'bea', 'cath', 'abi', 'dee', 'hope', 'jan', 'fay'],
 'hal':  ['abi', 'eve', 'hope', 'fay', 'ivy', 'cath', 'jan', 'bea', 'gay', 'dee'],
 'ian':  ['hope', 'cath', 'dee', 'gay', 'bea', 'abi', 'fay', 'ivy', 'jan', 'eve'],
 'jon':  ['abi', 'fay', 'jan', 'gay', 'eve', 'bea', 'dee', 'cath', 'ivy', 'hope'],

 'abe2':  ['abi', 'eve', 'cath', 'ivy', 'jan', 'dee', 'fay', 'bea', 'hope', 'gay'],
 'bob2':  ['cath', 'hope', 'abi', 'dee', 'eve', 'fay', 'bea', 'jan', 'ivy', 'gay'],
 'col2':  ['hope', 'eve', 'abi', 'dee', 'bea', 'fay', 'ivy', 'gay', 'cath', 'jan'],
 'dan2':  ['ivy', 'fay', 'dee', 'gay', 'hope', 'eve', 'jan', 'bea', 'cath', 'abi'],
 'ed2':   ['jan', 'dee', 'bea', 'cath', 'fay', 'eve', 'abi', 'ivy', 'hope', 'gay'],
 'fred2': ['bea', 'abi', 'dee', 'gay', 'eve', 'ivy', 'cath', 'jan', 'hope', 'fay'],
 'gav2':  ['gay', 'eve', 'ivy', 'bea', 'cath', 'abi', 'dee', 'hope', 'jan', 'fay'],
 'hal2':  ['abi', 'eve', 'hope', 'fay', 'ivy', 'cath', 'jan', 'bea', 'gay', 'dee'],
 'ian2':  ['hope', 'cath', 'dee', 'gay', 'bea', 'abi', 'fay', 'ivy', 'jan', 'eve'],
 'jon2':  ['abi', 'fay', 'jan', 'gay', 'eve', 'bea', 'dee', 'cath', 'ivy', 'hope']}

gal_prefers_demo = {
 'abi':  ['bob', 'bob2', 'fred', 'fred2', 'jon', 'jon2', 'gav', 'gav2', 'ian', 'ian2', 'abe', 'abe2', 'dan', 'dan2', 'ed', 'ed2', 'col', 'col2', 'hal', 'hal2'],
 'bea':  ['bob', 'bob2', 'abe', 'abe2', 'col', 'col2', 'fred', 'fred2', 'gav', 'gav2', 'dan', 'dan2', 'ian', 'ian2', 'ed', 'ed2', 'jon', 'jon2', 'hal', 'hal2'],
 'cath': ['fred', 'fred2', 'bob', 'bob2', 'ed', 'ed2', 'gav', 'gav2', 'hal', 'hal2', 'col', 'col2', 'ian', 'ian2', 'abe', 'abe2', 'dan', 'dan2', 'jon', 'jon2'],
 'dee':  ['fred', 'fred2', 'jon', 'jon2', 'col', 'col2', 'abe', 'abe2', 'ian', 'ian2', 'hal', 'hal2', 'gav', 'gav2', 'dan', 'dan2', 'bob', 'bob2', 'ed', 'ed2'],
 'eve':  ['jon', 'jon2', 'hal', 'hal2', 'fred', 'fred2', 'dan', 'dan2', 'abe', 'abe2', 'gav', 'gav2', 'col', 'col2', 'ed', 'ed2', 'ian', 'ian2', 'bob', 'bob2'],
 'fay':  ['bob', 'bob2', 'abe', 'abe2', 'ed', 'ed2', 'ian', 'ian2', 'jon', 'jon2', 'dan', 'dan2', 'fred', 'fred2', 'gav', 'gav2', 'col', 'col2', 'hal', 'hal2'],
 'gay':  ['jon', 'jon2', 'gav', 'gav2', 'hal', 'hal2', 'fred', 'fred2', 'bob', 'bob2', 'abe', 'abe2', 'col', 'col2', 'ed', 'ed2', 'dan', 'dan2', 'ian', 'ian2'],
 'hope': ['gav', 'gav2', 'jon', 'jon2', 'bob', 'bob2', 'abe', 'abe2', 'ian', 'ian2', 'dan', 'dan2', 'hal', 'hal2', 'ed', 'ed2', 'col', 'col2', 'fred', 'fred2'],
 'ivy':  ['ian', 'ian2', 'col', 'col2', 'hal', 'hal2', 'gav', 'gav2', 'fred', 'fred2', 'bob', 'bob2', 'abe', 'abe2', 'ed', 'ed2', 'jon', 'jon2', 'dan', 'dan2'],
 'jan':  ['ed', 'ed2', 'hal', 'hal2', 'gav', 'gav2', 'abe', 'abe2', 'bob', 'bob2', 'jon', 'jon2', 'col', 'col2', 'ian', 'ian2', 'fred', 'fred2', 'dan', 'dan2']}

def check(engaged):
    inverse_engaged = dict((v,k) for k,v in engaged.items())
    for she, he in engaged.items():
        she_likes = gal_prefers[she]
        she_likes_better = she_likes[:she_likes.index(he)]
        he_likes = guy_prefers[he]
        he_likes_better = he_likes[:he_likes.index(she)]
        for guy in she_likes_better:
            guys_girl = inverse_engaged[guy]
            guy_likes = guy_prefers[guy]
            if guy_likes.index(guys_girl) > guy_likes.index(she):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (she, guy, he, guys_girl))
                return False
        for gal in he_likes_better:
            girls_guy = engaged[gal]
            gal_likes = gal_prefers[gal]
            if gal_likes.index(girls_guy) > gal_likes.index(he):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (he, gal, she, girls_guy))
                return False
    return True

def matchmaker(guy_prefers, gal_prefers):
    guys = sorted(guy_prefers.keys())
    gals = sorted(gal_prefers.keys())
    guys_per_girl = len(guys)/len(gals)
    free_guys = guys[:]

    engaged  = {}
    for gal in gals:
        engaged[gal] = []

    guy_prefers2 = copy.deepcopy(guy_prefers)
    gal_prefers2 = copy.deepcopy(gal_prefers)

    while free_guys:
        guy = free_guys.pop(0)
        guy_preference_list = guy_prefers2[guy]
        for gal in guy_preference_list:
            fiances = engaged[gal]
            if not len(fiances) == guys_per_girl:
                # There's still room for another fiance
                engaged[gal].append(guy)
                print(" %s is now engaged to %s" % (guy, gal))
                break
            else:
                # The bounder proposes to a fully engaged lass!
                match_found = False
                gals_preferences_list = gal_prefers2[gal]
                for fiance in fiances:
                    if gals_preferences_list.index(fiance) > gals_preferences_list.index(guy):
                    # She prefers new guy
                        fiances.remove(fiance)
                        fiances.append(guy)
                        print("  %s dumped %s for %s" % (gal, fiance, guy))
                        # Ex is now free
                        free_guys.append(fiance)
                        match_found = True
                        break
                if match_found: break
    return engaged


'''print('\nEngagements:')
engaged = matchmaker(jugglers_prefers, circuits_prefer)

print('\nCouples:')
print('  ' + ',\n  '.join('%s is engaged to %s' % couple
                          for couple in sorted(engaged.items())))
print()'''


'''print('Engagement stability check PASSED'
      if check(engaged) else 'Engagement stability check FAILED')

print('\n\nSwapping two fiances to introduce an error')
engaged[gals[0]], engaged[gals[1]] = engaged[gals[1]], engaged[gals[0]]
for gal in gals[:2]:
    print('  %s is now engaged to %s' % (gal, engaged[gal]))
print()
print('Engagement stability check PASSED'
      if check(engaged) else 'Engagement stability check FAILED')
'''