'''Clock Hands

Write a program to find the minimum angle between two hands on a 24 hour clock. For instance, the angle at 6:00 is 90 degrees and the angle at 18:00 is also 90 degrees. At 6:17 the degree is 7.75 and at 18:17 it's 172.25.

For fun, program this one up in a language you've never used before. Here is a list of esoteric languages to help you decide. There are some truly interesting languages on that list. Feel free to use a "standard" language as well if there's one out there that you've been looking to learn.
'''

def clock_24h_hands_min_angle(time):
    # hour_hand_degrees_per_hour = 360/24 = 15
    # hour_hand_degree_per_minute = 360/24/60 = 0.25 
    # minute_hand_degree_per_minute = 360/60 = 6
    hour, minutes = map(float, time.split(':', 2))
    ans = abs((hour*15 + minutes*0.25) - (minutes * 6))
    return min(360-ans, ans)

print clock_24h_hands_min_angle('6:17')