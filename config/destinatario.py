## Lista de Emails ##
print()
print('Selecione o destinatário:')
print('A - INV-SaaSReceptionINV@sovos.com')
print('B - INV-SaaSReceptionTF@sovos.com ')
print()
destinatario = input('Digite a opção correspondente ao destinatário: ')
destinatario = destinatario.lower()
while destinatario not in ('a', 'b'):
    print('Eita caralho, não entendi')
    destinatario = input('Digite a opção correspondente ao destinatário: ')
    destinatario = destinatario.lower()

if destinatario == "a":
    destinatario = 'INV-SaaSReceptionINV@sovos.com'
if destinatario == "b":
    destinatario = 'INV-SaaSReceptionTF@sovos.com'
    
print('Você escolheu o email '+ str(destinatario) +' seu vacilão')