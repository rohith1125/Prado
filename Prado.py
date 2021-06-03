import os,webbrowser
os.system('color 0a')
cls=lambda:os.system('cls')
s=0
while s==0:
    file=input('Path to \'.pdn\' file: ')
    try:
        f=open(file,'r')
    except:
        cls()
    else:
        s=1
cls()
f=f.read()
n=99
for i in range(99):
    n-=1
    f=f.replace(f'x{str(n)}','>'*(n))
    f=f.replace(f'y{str(n)}','<'*(n))
    f=f.replace(f'+{str(n)}','+'*(n))
    f=f.replace(f'-{str(n)}','-'*(n))
    f=f.replace(str(n),'+'*(n))
f=f.replace('\n','')
f=f.replace(' ','')
f=f.replace('=','.')
f=f.replace('(','[')
f=f.replace(')',']')
f=f.replace('x','>')
f=f.replace('y','<')
f=f.replace('z',',')
f=f.replace('<>','')
f=f.replace('><','')
try:
    o=open(f'{file[-1:(len(file)-3)]}.bf','x')
    o.write(f'{f}\n')
except:
    print('Could not create file. Output:')
else:
    print('Created \'.bf\'. Output:')
finally:
    print('')
    print(f)
print('')
input('Press Enter to exit.')
