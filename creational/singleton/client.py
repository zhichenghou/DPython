from singleton import *

s1 = Singleton.get_instance()
s2 = Singleton.get_instance()

if s1 is s2:
    print "in singleton pattern"