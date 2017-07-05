def py_generator_split(sentence):
    for word in sentence.split(" "):
        yield word

foo = py_generator_split('baby let me iterate ya')

print foo.next()
print foo.next()

# sentence = 'baby let me iterate ya'
# foo = (word for word in sentence.split(" "))

# print foo.next()
