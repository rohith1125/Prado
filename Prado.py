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
    if x=='2':
        print('')
        print('Coming soon!')
    elif x=='1' or x=='3':
        print('')
        print('Enter blank line when done.')
        print('')
        print('Prado code:')
        f=''
        y=' '
        while y!='':
            y=input('> ')
            if y!='':
                f+=y
        cls()
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
                cls()
        else:
            cls()
            print('')
            print('Failed!')
    elif x=='4':
        cls()
        print('')
        print('Coming soon!')
        """
        bf=input('BF code: ')
        if bf!='':
            #BF to Prado
            cls()
        else:
            cls()
        """
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
    elif x=='6':
        print('')
        print('Coming soon!')
    elif x=='7':
        z=1
    else:
        cls()
        print('')
        print('Invalid!')
