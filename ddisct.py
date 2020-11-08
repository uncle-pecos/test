from collections import defaultdict

#defaultdict([default_factory[, ...]])

cnt = defaultdict(lambda : 0)
for i in "fdsafasdf":
    cnt[i] += 1
print(cnt.items())