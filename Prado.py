'''
REPOSITORY LINK:
https://github.com/TurnipGuy30/Prado
REQUIRED MODULES:
python -m pip install brainfuck
python -m pip install brainfuck_interpreter
'''
import brainfuck,os,webbrowser
os.system('color 0a')
cls=lambda:os.system('cls')
z=0
while z==0:
    e=0
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
    elif x=='1' or x=='3' or x=='5':#COMPLETE
        print('')
        print('Enter blank line when done.')
        print('')
        if x=='1' or x=='3':
            print('Prado code:')
        elif x=='4' or x=='5':
            print('BF code:')
        elif x=='2' or x=='6':
            print('Text:')
        else:
            cls()
            break
        f=''
        y=' '
        while y!='':
            y=input('> ')
            if y!='':
                f+=y
        if f!='':
            if x=='1' or x=='3':#1#3
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
            elif x=='2' or x=='4' or x=='6':#2#4#6
                if x=='2' or x=='6':
                    try:
                        cls()#f = Text -> BF
                    except:
                        e=1
                if x=='2' or x=='4':
                    cls()#f = BF -> Prado
                cls()
                print('')
                if e==0:
                    print(f'{f}')
                else:
                    print('Failed!')
            elif x=='5':#5
                cls()
                print('')
                try:
                    print(f'"{brainfuck.evaluate(f)}"')
                except:
                    print('Failed!')
        else:
            cls()
            print('')
            print('Failed!')
    elif x=='7':
        z=1
    else:
        cls()
        print('')
        print('Invalid!')
