values = [
    False,
    None,
    0,
    0.0,
    "",
    [],
    {},
    (),
    True,
    1,
    "Python",
    [1, 2, 3],
]

for value in values:
    if value:
        print(repr(value), "is truthy")
    else:
        print(repr(value), "is falsy")