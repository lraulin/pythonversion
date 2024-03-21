# pythonversion

For a recent code test. The function compares versions given as strings.

Not how I submitted it, as the test wouldn't let me check documentation. So I used a traditional for-loop, which isn't very Pythonic, and I suspected there was a more elegant way I could have done it using zip. Normal zip truncates to the length of the shortest list. But it turns out itertools.zip_longest is exactly what I wanted.
