x = str(input('digite algo: ')).upper().strip()
print(f'a letra "A" aparece: {x.count("A")} vezes')
print(f'a letra "A" aparece pela primeira vez em: {x.find("A")+1}')
print(f'a letra "A" aparece pela última vez em: {x.rfind("A")+1}')
