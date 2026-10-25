Python 3.15.1 (v3.15.1:c37e74cb6bc, Oct 20 2026, 23:21:44) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
>>> name = input("Enter file:")
... if len(name) < 1:
...     name = "mbox-short.txt"
... handle = open(name)
... 
... many= dict()
... 
... 
... for line in handle:
...     if not line.startswith("From "):
...         continue
... 
...     wds = line.split()
...     time = wds[5]
...     hour = time.split(":")[0]
...     many[hour] = many.get(hour, 0) + 1
... 
... for hour, count in sorted(many.items()):
