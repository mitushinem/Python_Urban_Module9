def all_variants(text):
    for index in range(len(text)):
        for i in range(len(text)):
            elem = text[i:i + index + 1]
            if len(elem) == index + 1:
                yield elem


a = all_variants("abcd")
for i in a:
    print(i)
