from random import randint

secret=randint(0,100)
guess=int(input('Veuillez entrer un nombre entre 0 et 100 : '))
attempts=1
while secret != guess:
    #if secret > guess:
    #    print('C\'est plus')
    #else:
    #    print('C\'est moins')

    info = 'C\'est plus' if secret>guess else 'C\'est moins'
    print(info)

    guess=int(input('Veuillez entrer un nombre entre 0 et 100 : '))
    attempts+=1
print(f'Bravo, vous avez trouvé le nombre secret en {attempts} essai(s)')
#hjiheo
