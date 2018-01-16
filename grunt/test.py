from yattag import Doc

doc, tag, text = Doc().tagtext()
a1 = [1, 2, 3]
a2 = [4, 5, 6]
d = {'a1': a1, 'a2': a2}
with tag('html'):
    with tag('body'):
        with tag('p', id = 'main'):
            for key in d.keys():
                if key == 'a1':
                    with tag('p'):
                        text('a1 = %s' % d[key])
                elif key == 'a2':
                    with tag('p'):
                        text('a2 = %s' % d[key])
                else:
                    text('someother test')

result = doc.getvalue()
print result
