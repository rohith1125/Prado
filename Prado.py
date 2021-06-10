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
    print('4. BF to Prado')
    print('5. BF to text')
    print('6. Text to BF')
    print('7. Exit')
    print('')
    x=input('> ')
    cls()
    if x=='2' or x=='4' or x=='6':#INCOMPLETE
        print('')
        print('Coming soon!')
    elif x=='1' or x=='3' or x=='5':
        print('')
        print('Enter blank line when done.')
        print('')
        print('Code:')
        f=''
        y=' '
        while y!='':
            y=input('> ')
            if y!='':
                f+=y
        if x=='1' or x=='3':
            cls()
            if x=='1' or x=='3':
                n=255
                for i in range(n):
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
                    print('Failed!')
        elif x=='5':
            cls()
            print('')
            try:
                print(f'"{brainfuck.evaluate(f)}"')
            except:
                print('Failed!')
    elif x=='4':
        if bf!='':
            #BF to Prado
            cls()
        else:
            cls()
            print('')
            print('Failed!')
    elif x=='5':
        cls()
        print('')
        bf=input('BF code: ')
        try:
            bf=brainfuck.evaluate(bf)
        except:
            print('Failed!')
        else:
            if bf!='':
                cls()
                print('')
                print(f'"{bf}"')
            else:
                cls()
    elif x=='7':
        z=1
    else:
        cls()
        print('')
        print('Invalid!')
