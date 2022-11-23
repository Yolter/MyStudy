phrase = "Don't panic!"
plist = list(phrase)

print(phrase)
print(plist)

new_phrase = plist[1:8]
new_phrase.remove("'")
new_phrase.insert(2, new_phrase.pop(3))
new_phrase.insert(4, new_phrase.pop())
plist = ''.join(new_phrase)

print(new_phrase)
print(plist)
