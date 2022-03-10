from time import sleep
print(':-' * 45)
print('{:^45}'.format('CALCULO DO IMC'))
print(':-' * 45)
print('Dados do paciente')
nome = str(input('Nome: ')).upper().strip()
altura = float(input('Altura: '))
peso = float(input('Massa (peso(kg)): '))
calculo = peso / (altura**2)
imc = calculo
print(':-' * 45)
print('Calculando o IMC...')
print(':-' *45)
sleep(3)
print('{:^45}'.format('Resultado'))
print(':-' * 45)
sleep(1)
print(f'{nome} seu IMC é {imc:.1f}')
if imc <= 16.9:
          print('Você está MUITO ABAIXO DO PESO!')
          print('Possíveis riscos à sua saúde: ')
          sleep(3)
          print('''[1]Queda de cabelo
[2]Infertilidade
[3]Ausência mestrual''')
          print('CUIDE-SE!')
elif imc <= 18.4:
          print('Você está ABAIXO DO PESO!')
          print('Possíveis riscos à sua saúde: ')
          print('''[1]Fadiga
[2]Stress
[3]Ansiedade''')
          print('CUIDE-SE!')
elif imc <= 24.9:
          print('Peso NORMAL!')
          print('PARABENS! Você tem um risco menor para doenças cardíacas e vasculares.')
          print('Continue se cuidando. Mantenha sempre uma alimentação SAUDÁVEL!')
elif  imc <=30:
          print('Você está ACIMA DO PESO!')
          print('Possíveis riscos à sua saúde: ')
          print('''[1]Fadiga
[2]Má circulação
[3]Varizes''')
          print('CUIDE-SE!')
elif imc <=35:
          print('Você está com OBESIDADE GRAU I!')
          print('Possíveis riscos á saúde: ')
          print('''[1]Diabetes
[2]Angina
[3]Infarto
[4]Aterosclerose''')
          print('Procure um MÉDICO!')
elif imc <=40:
          print('Você está com OBESIDADE GRAU II !')
          print('Possíveis riscos á saúde: ')
          print('''[1]Apneia do sono
[2]Falta de ar''')
          print('Procure um MÉDICO!')
else:
           print('Você está com OBESIDADE GRAU III !')
           print('Você corre os seguintes riscos: ')
           print('''[1]Refluxo
[2]Dificuldade para se mover
[3]Escaras
[4]Diabetes
[5]Infarto
[6]AVC''')
           print('Procure um MÉDICO o quanto antes!')
                    
                    
                    
                    
          
