"""
Given a dictionary of alphabetic keys and numeric values, sort the dictionary
based on values.
"""
sortme = {"a": 3, "c": 4, "b": 1}

sortme_sorted = sorted(sortme.items(), key=lambda (k, v): v)

print(dict(sortme_sorted))

"""
Alternative to write from above
Given a dictionary of alphabetic keys and numeric values, sort the dictionary
based on values.
"""
sortme = {"a": 3, "c": 4, "b": 1}

sortme_sorted = sorted(sortme.items(), key=lambda (key, val): sortme.get(key))

print(dict(sortme_sorted))

"""
Alternative to write from above
Given a dictionary of alphabetic keys and numeric values, sort the dictionary
based on the keys.
"""
sortme = {"a": 3, "c": 4, "b": 1}

sortme_sorted = sorted(sortme.items(), key=lambda (key, val): key)

print(dict(sortme_sorted))
