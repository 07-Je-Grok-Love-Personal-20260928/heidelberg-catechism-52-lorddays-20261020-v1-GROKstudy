s=open('src/style.css').read()
assert 'v6 note-marking' not in s
s=s.replace('color:#0b1020;background:linear-gradient(90deg,var(--gold),var(--grat));','color:var(--ink);background:var(--gold);')
a=s.index('mark{background'); b=s.index('.legend{display:flex')
MK=open('v6_marks.css').read()
s=s[:a]+MK+s[b:]+open('v6_tail.css').read()
open('src/style.css','w').write(s)
print('ok')
