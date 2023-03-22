larg = float(input('Digite a largura de uma parede em metros: '))
alt = float(input('Digite a altura de uma parede em metros: '))
área = larg * alt
print('Sua parede tem a dimenção de {}x{} e sua área é de {}m². \nPara pintar essa parede, você precisará de {}l de tinta'.format(larg, alt, área, área/2))
#cada 1l de tinta pinta uma área de 2m²