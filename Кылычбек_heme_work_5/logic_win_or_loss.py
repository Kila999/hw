from __main__ import valuta

def winner(result):
    print(f'    Победа за тобой! выйгрыш составил: {result} {valuta}')
    print(f'    У тебя на счету: {money}')

def losser(result):
    print(f'    К сожалению, проигрыш: {result} {valuta}')
    print(f'    У тебя на счету: {money}')
    print('    Нужно отыграться!')