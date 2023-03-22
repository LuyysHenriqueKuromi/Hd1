import pygame
força = int(input('Digite a força do seu personagem: '))
modfor = (força - 10) // 2
proficiencia = int(input('Digite o bônus de proficiência do seu personagem: '))
#destreza = int(input('Digite a destreza do seu personagem: '))
#moddes = (destreza - 10) // 2
#constituição = int(input('Digite a constituição do seu personagem: '))
#modcon = (constituição - 10) // 2
#inteligencia = int(input('Digite a inteligência do seu personagem: '))
#modint = (inteligencia - 10) // 2
#sabedoria = int(input('Digite a sabedoria do seu personagem: '))
#modsab = (sabedoria - 10) // 2
#carisma = int(input('Digite o carisma do seu personagem: '))
#modcar = (carisma - 10) // 2
#print('{}\n{}\n{}\n{}\n{}\n{}'.format(modfor, moddes, modcon, modint, modsab, modcar))
acerto = random.randint(1,20) + proficiencia
print(acerto)
dano = random.randint(1,3) + modfor
print(dano)