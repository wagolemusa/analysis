Python 2.7.6 (default, Oct 26 2016, 20:30:19) 
[GCC 4.8.4] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> sl = set()
>>> sl.add(1)
>>> sl.update([1,2,3])
>>> print si

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print si
NameError: name 'si' is not defined
>>> print sl
set([1, 2, 3])
>>> sl.add(4)
>>> print sl
set([1, 2, 3, 4])
>>> s2 = set([4,5,6])
>>> print s2
set([4, 5, 6])
>>> sl.union(s2)
set([1, 2, 3, 4, 5, 6])
>>> sl.intersection(s2)
set([4])
>>> 7 in sl
False
>>> 4 in sl
True
>>> 
