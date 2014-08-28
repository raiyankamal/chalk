import random
import chalk

L = [ x/2 if x%2==0 else x*3+1 for x in range(0,12)]
# chalk.draw(L)

LL = [ [ m for m in range(2*l, 2*l+3) ] for l in range(0,12)]
# chalk.draw(LL)

names = [
'Kein Pardon',
'Kein Platz fr Gerold',
'Kein Sex ist auch keine Lsung',
'Keine Angst Liebling, ich pass schon auf',
'Keiner hat das Pferd geksst',
'Keiner liebt mich',
'Keinohrhasen',
'Keiros Cat',
'La Prima Donna',
'La Primeriza',
'La Prison De Saint-Clothaire',
'La Puppe',
'La Pjara',
'La Pergola de las Flores',
]
#chalk.draw(names)

x = random.randint(0,1000)
# chalk.draw(x)