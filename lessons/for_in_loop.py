xs: list[str] = ["a", "b", "c"]

"""While Loop example with item definition"""
i: int = 0
while i < len(xs):
    item: str = xs[i]
    print(item)
    i += 1

"""For Loop Example"""
for item in xs:
    print(item)
