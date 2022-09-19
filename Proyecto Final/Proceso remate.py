print('Comencemos con el proceso de remate')
print('Vas a necesitar la ayuda de un compañero que te levante el balon y un aro')
print('Vas a colocar el aro en zona 1 del campo contrario y vas a realizar a rematar 3 balones dirigidos  al aro, 3 remates por punta, 3 remates por centro y 3 remates por opuesto')

BalRin11=int(input('¿Cuántos balones cayeron dentro del aro, cuando atacabas por punta?'))
BalRin12=int(input('¿Cuántos balones cayeron dentro del aro,cuando atacabas por centro? '))
BalRin13=int(input('¿Cuántos balones cayeron dentro del aro,cuando atacabas por opuesto? '))
BalRin1=int(BalRin11+BalRin12+BalRin13)

print('Ahora coloca el aro en zona 6 del campo contrario, repite el número de remates')

BalRin21=int(input('¿Cuántos balones cayeron dentro del aro, cuando atacabas por punta?'))
BalRin22=int(input('¿Cuántos balones cayeron dentro del aro,cuando atacabas por centro? '))
BalRin23=int(input('¿Cuántos balones cayeron dentro del aro,cuando atacabas por opuesto? '))
BalRin2=int(BalRin21+BalRin22+BalRin23)

print('Ahora coloca el aro en zona 5 del campo contrario, repite el número de remates')

BalRin31=int(input('¿Cuántos balones cayeron dentro del aro, cuando atacabas por punta?'))
BalRin32=int(input('¿Cuántos balones cayeron dentro del aro,cuando atacabas por centro? '))
BalRin33=int(input('¿Cuántos balones cayeron dentro del aro,cuando atacabas por opuesto? '))
BalRin3=int(BalRin31+BalRin32+BalRin33)
Prescicion1=float(BalRin1*0.4)
Prescicion2=float(BalRin2*0.3)
Prescicion3=float(BalRin3*0.3)

EfectividadRemate=int(((BalRin11+BalRin12+BalRin13+BalRin21+BalRin22+BalRin23+BalRin31+BalRin32+BalRin33)*100)/27)
PresicionRemate=int((Prescicion1+Prescicion2+Prescicion3)*10)
print(EfectividadRemate, PresicionRemate)