## Lista de Emails ##
print('Selecione o destinatário:')
print()
print('A - INV-SaaSReceptionSQL@Sovos.com           VM 02')
print('B - INV-InHouseReceptionSQL@Sovos.com        VM 03')
print('C - INV-SaaSReceptionOracle@Sovos.com        VM 05')
print('D - INV-InHouseReceptionOracle@Sovos.com     VM 06')
print('E - INV-SaasReceptionLATAM@sovos.com         VM 08')
print('F - INV-InHouseReceptionLATAM@sovos.com      VM 09')
print('G - INV-InHouseReceptionTF@sovos.com         VM 14')
print('H - INV-SaaSReceptionTF@sovos.com            VM 19')
print('I - INV-SaaSReceptionINV@sovos.com           VM 22')



print()
destinatario = input('Digite a opção correspondente ao destinatário: ')
destinatario = destinatario.lower()
while destinatario not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'):
    print('Não entendi')
    destinatario = input('Digite a opção correspondente ao destinatário: ')
    destinatario = destinatario.lower()

if destinatario == "a":
    destinatario = 'INV-SaaSReceptionSQL@Sovos.com'
if destinatario == "b":
    destinatario = 'INV-InHouseReceptionSQL@Sovos.com'
if destinatario == "c":
    destinatario = 'INV-SaaSReceptionOracle@Sovos.com'
if destinatario == "d":
    destinatario = 'INV-InHouseReceptionOracle@Sovos.com'
if destinatario == "e":
    destinatario = 'INV-SaasReceptionLATAM@sovos.com'
if destinatario == "f":
    destinatario = 'INV-InHouseReceptionLATAM@sovos.com'
if destinatario == "g":
    destinatario = 'INV-InHouseReceptionTF@sovos.com'
if destinatario == "h":
    destinatario = 'INV-SaaSReceptionTF@sovos.com'
if destinatario == "i":
    destinatario = 'INV-SaaSReceptionINV@sovos.com'
    
print('Você escolheu o email '+ str(destinatario) )