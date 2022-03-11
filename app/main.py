'''
REPOSITORY LINK:
https://github.com/PradoLang/Prado
'''
import brainfuck,os
os.system('color 0a')
cls=lambda:os.system('cls')
def letter_to_brainfuck(letter):
    num=ord(letter)
    return '+' * (num // 10) + '[>++++++++++<-]>' + '+'*(num%10)
def brainfuck_print(letter_list):
    return ''.join([i+'.>\n'for i in letter_list])
a=['1','2','3','4','5','6']
z=0
while z==0:
    e=0
    x=''
    x=input('\nWhat would you like to do?\n1. Prado to text\n2. Text to Prado\n3. Prado to BF\n4. BF to Prado\n5. BF to text\n6. Text to BF\n7. Exit\n\n»')
    cls()
    if x in a:
        print('\nEnter blank line when done.\n')
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
            y=input('»')
            if y!='':
                if f=='':
                    f=y
                else:
                    f+=f'\n{y}'
        if f!='':
            if x=='1' or x=='3':#1#3
                cls()
                if x=='1' or x=='3':
                    n=256
                    for i in range(n):
                        n-=1
                        f=f.replace(f'x{str(n)}','>'*(n)).replace(f'y{str(n)}','<'*(n)).replace(f'+{str(n)}','+'*(n)).replace(f'-{str(n)}','-'*(n)).replace(str(n),'+'*(n))
                    f=f.replace('\n','').replace(' ','').replace('=','.').replace('(','[').replace(')',']').replace('x','>').replace('y','<').replace('z',',').replace('<>','').replace('><','')
                    print('')
                    if f!='':
                        if x=='3':
                            print(f'{f}')
                        elif x=='1':
                            try:
                                if '\n' in f:
                                    print(f'{brainfuck.evaluate(f)}')
                                else:
                                    print(f'{brainfuck.evaluate(f)}')
                            except:
                                print('Failed!')
                    else:
                        print('Failed!')
            elif x=='2' or x=='4' or x=='6':#2#4#6
                if x=='2' or x=='6':
                    try:
                        f=brainfuck_print([letter_to_brainfuck(i) for i in list(f)]).replace('\n','')
                    except:
                        e=1
                if x=='2' or x=='4':
                    n=256
                    for i in range(n-1):
                        f=f.replace('>'*(n),f'x{str(n)}').replace('<'*(n),f'y{str(n)}').replace('+'*(n),f'+{str(n)}').replace('-'*(n),f'-{str(n)}')
                        n-=1
                    f=f.replace('>','x').replace('<','y').replace('\n','').replace(' ','').replace('.','\n=').replace('\n=\n','\n=xy\n').replace('[','(').replace(']',')').replace(',','z').replace('=+','=').replace('(+','(').replace('+)','+1)').replace('+\n','+1\n)').replace('-)','-1)').replace('-\n','-1\n)').replace('\n)=','\n=')
                    if f[0]=='+':
                        f=f[1:]
                    if f[len(f)-1]=='=':
                        f+='xy'
                    elif f[len(f)-1]=='x':
                        f+='y'
                cls()
                print('')
                if e==0:
                    if '\n' in f:
                        print(f'{f}')
                    else:
                        print(f'{f}')
                else:
                    print('Failed!')
            elif x=='5':#5
                cls()
                print('')
                try:
                    if '\n' in f:
                        print(f'{brainfuck.evaluate(f)}')
                    else:
                        print(f'{brainfuck.evaluate(f)}')
                except:
                    print('Failed!')
        else:
            cls()
            print('\nFailed!')
    elif x==str(int(a[len(a)-1])+1):
        z=1
    else:
        cls()
        print('\nInvalid!')
