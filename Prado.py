import brainfuck,os,webbrowser
os.system('color 0a')
cls=lambda:os.system('cls')
z=0
while z==0:
    x=''
    print('')
    print('What would you like to do?')
    print('1. Prado to text')
    print('2. Text to Prado')
    print('3. Prado to BF')
    print('4. BF to text')
    print('5. Text to BF')
    print('6. Exit')
    print('')
    x=input('> ')
    cls()
    if x=='2':
        print('')
        print('Coming soon!')
    elif x=='1' or x=='3':
        s=0
        while s==0:
            print('')
            file=input('Path to \'.pdn\' file: ')
            try:
                r=open(file,'r')
            except:
                cls()
            else:
                s=1
        cls()
        f=r.read()
        r.close()
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
        print('')
        if f!='':
            if x=='3':
                print(f'{f}')
            elif x=='1':
                print(f'"{brainfuck.evaluate(f)}"')
            else:
                cls()
    elif x=='4':
        cls()
        try:
            print('')
            bf=brainfuck.evaluate(input('BF code: '))
        except:
            print('Failed!')
        else:
            if bf!='':
                cls()
                print('')
                print(f'"{bf}"')
            else:
                cls()
    elif x=='5':
        print('')
        print('Coming soon!')
    elif x=='6':
        z=1
    else:
        cls()
        print('')
        print('Invalid!')
print('')
input('Press Enter to exit.')
