import os 
os.system ('cls')

kata = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
lain = ['twen', 'thir', 'fif']

def numbers(x):
    if x < 11 :
        return kata[x]
    elif x < 20 :
        temp = x % 10
        if temp == 1 :
            return 'eleven'
        elif temp == 2 :
            return 'twelve'
        elif temp == 3 :
            return lain[1] + 'teen'
        elif temp == 5 :
            return lain[2] + 'teen'
        else :
            return kata[temp] + 'teen'
    elif x < 100 :
        if x // 10 == 2 : 
            return lain[0] + 'ty ' + (numbers(x % 10) if x % 10 != 0 else ' ')
        if x // 10 == 3 :
            return lain[1] + 'ty ' + (numbers(x % 10) if x % 10 != 0 else ' ')
        if x // 10 == 5 :
            return lain[2] + 'ty ' + (numbers(x % 10) if x % 10 != 0 else ' ')
        else :
            return kata[x // 10] + 'ty ' + (numbers(x % 10) if x % 10 != 0 else ' ')
    elif x < 1000 :
        return kata[x // 100] + ' hunderds and ' + (numbers(x % 100) if x % 100 != 0 else ' ')
    elif x < 1000000 :
        return numbers(x // 1000) + ' thousands, ' + (numbers(x % 1000) if x % 1000 != 0 else ' ')    
    elif x < 1000000000 :
        return numbers(x // 1000000) + ' millions, ' + (numbers(x % 1000000) if x % 1000000 != 0 else ' ')
    elif x < 1000000000000 :
        return numbers(x // 1000000000) + ' billions, ' + (numbers(x % 1000000000) if x % 1000000000 != 0 else ' ')


while True:
    os.system ('cls')
    try :
        y = int(input('number ? '))
    except :
        print('Tolong masukan angka!!')
        os.system('pause')
    else :
        print(f'{y} = {numbers(y)}')
        os.system('pause')