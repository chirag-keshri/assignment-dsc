def reverse(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))
print(reverse("Rinkiya ke papa"))