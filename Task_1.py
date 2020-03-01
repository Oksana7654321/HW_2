print ("1.Zen in capital letters:")

Zen_of_Python = """Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.
Readability counts.\nSpecial cases aren't special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one—and preferably only one—obvious way to do it.\nAlthough that way may not be obvious at first unless you're Dutch.
Now is better than never.\nAlthough never is often better than right now.\nIf the implementation is hard to explain, it's a bad idea.\nIf the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea—let's do more of those!"""

a = Zen_of_Python.upper()
print(a)

print("2.Count the words frequency")

b = Zen_of_Python.count('better')
print("'Better' is used " + str(b) + " times in Python Zen")

c = Zen_of_Python.count('never')
print("'Never' is used " + str(c) + " times in Python Zen")

d = Zen_of_Python.count('is')
print("'Is' is used " + str(d) + " times in Python Zen")

print ("3. Replacing 'i' with '&'")

e = Zen_of_Python.replace("i", "&")
print(e)