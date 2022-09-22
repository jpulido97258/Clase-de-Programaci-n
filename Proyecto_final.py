#Programa ciberseguridad
print("Acaba de ejecutar un programa para ver que tan expuesta esta usted en el mundo digital")
print("")
print ("Antes de comenzar debe estar deacuerdo con la politica de privacidad")
print("")
print('Escriba "Si" si esta deacuerdo de lo contrario escriba "No" o retirese del programa')
answer = input('Escriba aqui su respuesta:')

a= "Si"
b= "No"

if answer == a:
  print("Muy bien, entonces comencemos")
  print()
  print('¿Algun amigo o conocido tiene la contraseña de alguna de tus redes sociales?')
  
  answer1 = input('Escriba "Si" o escriba "No":')
  print()
  
  if answer1== a:
    print("¿La contraseña de sus redes sociales son iguales todas?")
    answer2 = input('Escriba "Si" o escriba "No":')
    
    if answer2== a:
      print("¿La contraseña de su correo es la misma que la de sus redes sociales?")
      answer4= input('Escriba "Si" o escriba "No":')
      
      if answer4 == a:
        print('¿Su contraseña esta relacionada a algo de usted, como: numero de documento fecha de nacimiento o nombre?')
        answer7=input('Escriba "Si" o escriba "No":')
        
        if answer7==a:
          print('¿Cambia su contraseña periodicamente?')
          answer8= input('Escriba "Si" o escriba "No":')
          
          if answer8 ==a:
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer9=input('Escriba "Si" o escriba "No":')
            
            if answer9==a:
              print("El nivel de exposicion es de:25% ")
            elif answer9==b:
              print('El nivel de exposicion es de:20%')
            else:
              print("No se entendio su respuesta")
          elif answer8==b:  
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer28=input('Escriba "Si" o escriba "No":')
            
            if answer28==a:
              print("El nivel de exposicion es de:60% ")
            elif answer28==b:
              print('El nivel de exposicion es de:100%')
            else:
              print("No se entendio su respuesta")
          else:
            b= "No"
        elif answer7 == b:
            print('¿Cambia su contraseña periodicamente?')
            answer10= input('Escriba "Si" o escriba "No":')
            if answer10 ==a:
             print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
             answer11=input('Escriba "Si" o escriba "No":')
            
             if answer11==a:
              print("El nivel de exposicion es de: 15%")
             elif answer11==b:
              print('El nivel de exposicion es de:30%')
             else:
              print("No se entendio su respuesta") 
            elif answer10 ==b:
             print("¿Su contraseña tiene caracteres especiales como:*,#,$,etc.?")
             answer12=input('Escriba "Si" o escriba "No":')
            
             if answer12==a:
              print("El nivel de exposicion es de: 30% ")
             elif answer12==b:
              print('El nivel de exposicon es de:50%')
             else:
              print("No se entendio su respuesta")
            else:
             print("no se entendio su respuesta")
        else:
          print("No se entendio su respuesta")


          
      elif answer4 == b:
        print ('¿La contraseña de los sitios web mas importantes para usted tienen alguna relacion con su nombre, fecha de nacimiento o numero de identificacion?')
        answer13 = input('Escriba "Si" o escriba "No":')
                
        if answer13==a:
          print('¿Cambia su contraseña periodicamente?')
          answer14= input('Escriba "Si" o escriba "No":')
          
          if answer14 ==a:
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer33=input('Escriba "Si" o escriba "No":')
            
            if answer33==a:
              print("El nivel de exposicion es de:10% ")
            elif answer33==b:
              print('El nivel de exposicion es de:15%')
            else:
              print("No se entendio su respuesta")

              
          elif answer14==b:
           print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
           answer29=input('Escriba "Si" o "No"')
           if answer29==a:
              print("El nivel de exposicion es de:15% ")
           elif answer29==b:
              print('El nivel de exposicion es de:30%')
           else:
              print("No se entendio su respuesta")   
          else:
            print("No se entendio su respuesta")
        elif answer13==b:
          print('¿Cambia su contraseña periodicamente?')
          answer30= input('Escriba "Si" o escriba "No":')
          
          if answer30 ==a:
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer31=input('Escriba "Si" o escriba "No":')
            
            if answer31==a:
              print("El nivel de exposicion es de: 20%")
            elif answer31==b:
              print('El nivel de exposicion es de:25%')
            else:
              print("No se entendio su respuesta") 
              
          elif answer30 ==b:
            print("¿Su contraseña tiene caracteres especiales como:*,#,$,etc.?")
            answer32=input('Escriba "Si" o escriba "No":')
            
            if answer32==a:
              print("El nivel de exposicion es de: 25%")
            elif answer32==b:
              print('El nivel de exposicon es de:50%')
            else:
              print("No se entendio su respuesta")
          else:
            print("no se entendio su respuesta")
        else:
          print("No se entendio su respuesta")

          
        
    elif answer2 == b:
      print ("¿La contraseña de su correo es la misma que la de alguna de sus redes sociales?")
      answer18= input('Escriba "Si" o escriba "No":')
      
      if answer18 == a:
        print('¿Su contraseña esta relacionada a algo de usted, como: numero de documento fecha de nacimiento o nombre?')
        answer19=input('Escriba "Si" o escriba "No":')
        
        if answer19==a:
          print('¿Cambia su contraseña periodicamente?')
          answer20= input('Escriba "Si" o escriba "No":')
          
          if answer20 ==a:
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer21=input('Escriba "Si" o escriba "No":')
            
            if answer21==a:
              print("El nivel de exposicion es de: 15%")
            elif answer21==b:
              print('El nivel de exposicion es de:20%')
            else:
              print("No se entendio su respuesta")
          elif answer20 ==b:
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer34=input('Escriba "Si" o escriba "No":')
            
            if answer34==a:
              print("El nivel de exposicion es de: 20%")
            elif answer34==b:
              print('El nivel de exposicion es de:35%')
            else:
              print("No se entendio su respuesta")
          else:
            print("No se entendio su respuesta")
        elif answer19==b:
          print('¿Cambia su contraseña periodicamente?')
          answer22= input('Escriba "Si" o escriba "No":')
          
          if answer22 ==a:
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer23=input('Escriba "Si" o escriba "No":')
            
            if answer23==a:
              print("El nivel de exposicion es de:10% ")
            elif answer23==b:
              print('El nivel de exposicion es de:15%')
            else:
              print("No se entendio su respuesta") 
              
          elif answer22 ==b:
            print("¿Su contraseña tiene caracteres especiales como:*,#,$,etc.?")
            answer24=input('Escriba "Si" o escriba "No":')
            
            if answer24==a:
              print("El nivel de exposicion es de:20% ")
            elif answer24==b:
              print('El nivel de exposicon es de:25%')
            else:
              print("No se entendio su respuesta")
          else:
            print("no se entendio su respuesta")
        else:
          print("No se entendio su respuesta")
            
      elif answer18== b:
        print ('¿La contraseña de los sitios web mas importantes para usted tienen alguna relacion con su nombre, fecha de nacimiento o numero de identificacion?')
        answer25 = input('Escriba "Si" o escriba "No":')
                
        if answer25==a:
          print('¿Cambia su contraseña periodicamente?')
          answer26= input('Escriba "Si" o escriba "No":')
          
          if answer26 ==a:
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer27=input('Escriba "Si" o escriba "No":')
            
            if answer27==a:
              print("El nivel de exposicion es de:10% ")
            elif answer27==b:
              print('El nivel de exposicion es de:20%')
            else:
              print("No se entendio su respuesta")
          elif answer26==b:
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer35=input('Escriba "Si" o escriba "No":')
            
            if answer35==a:
              print("El nivel de exposicion es de:20% ")
            elif answer35==b:
              print('El nivel de exposicion es de:30%')
            else:
              print("No se entendio su respuesta")
          else:
            print("No se entendio su respuesta")
        elif answer25==b:
          print('¿Cambia su contraseña periodicamente?')
          answer15= input('Escriba "Si" o escriba "No":')
          
          if answer15 ==a:
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer16=input('Escriba "Si" o escriba "No":')
            
            if answer16==a:
              print("El nivel de exposicion es de: 10%")
            elif answer16==b:
              print('El nivel de exposicion es de:20%')
            else:
              print("No se entendio su respuesta") 
              
          elif answer15 ==b:
            print("¿Su contraseña tiene caracteres especiales como:*,#,$,etc.?")
            answer17=input('Escriba "Si" o escriba "No":')
            
            if answer17==a:
              print("El nivel de exposicion es de:10% ")
            elif answer17==b:
              print('El nivel de exposicon es de: 15%')
            else:
              print("No se entendio su respuesta")
          else:
            print("no se entendio su respuesta")
        else:
          print("No se entendio su respuesta")
      
    else:
      print("no se entendio su respuesta")


#---------------------------------------------


    
  elif answer1==b:
    print("¿La contraseña de sus redes sociales son iguales todas?")
    answer36 = input('Escriba "Si" o escriba "No":')
    
    if answer36== a:
      print("¿La contraseña de su correo es la misma que la de sus redes sociales?")
      answer37= input('Escriba "Si" o escriba "No":')
      
      if answer37 == a:
        print('¿Su contraseña esta relacionada a algo de usted, como: numero de documento fecha de nacimiento o nombre?')
        answer38=input('Escriba "Si" o escriba "No":')
        
        if answer38==a:
          print('¿Cambia su contraseña periodicamente?')
          answer39= input('Escriba "Si" o escriba "No":')
          
          if answer39==a:
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer40=input('Escriba "Si" o escriba "No":')
            
            if answer40==a:
              print("El nivel de exposicion es de:15% ")
            elif answer40==b:
              print('El nivel de exposicion es de:30%')
            else:
              print("No se entendio su respuesta")
          elif answer39==b:  
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer41=input('Escriba "Si" o escriba "No":')
            
            if answer41==a:
              print("El nivel de exposicion es de: 10%")
            elif answer41==b:
              print('El nivel de exposicion es de:15%')
            else:
              print("No se entendio su respuesta")
          else:   
            print("No se entendio su respuesta")
        elif answer38==b:
          print('¿Cambia su contraseña periodicamente?')
          answer42= input('Escriba "Si" o escriba "No":')
          
          if answer42 ==a:
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer43=input('Escriba "Si" o escriba "No":')
            
            if answer43==a:
              print("El nivel de exposicion es de:10% ")
            elif answer43==b:
              print('El nivel de exposicion es de:20%')
            else:
              print("No se entendio su respuesta") 
              
          elif answer42 ==b:
            print("¿Su contraseña tiene caracteres especiales como:*,#,$,etc.?")
            answer44=input('Escriba "Si" o escriba "No":')
            
            if answer44==a:
              print("El nivel de exposicion es de: 25%")
            elif answer44==b:
              print('El nivel de exposicon es de:35%')
            else:
              print("No se entendio su respuesta")
          else:
            print("no se entendio su respuesta")
        else:
          print("No se entendio su respuesta")


          
      elif answer37 == b:
        print ('¿La contraseña de los sitios web mas importantes para usted tienen alguna relacion con su nombre, fecha de nacimiento o numero de identificacion?')
        answer45 = input('Escriba "Si" o escriba "No":')
                
        if answer45==a:
          print('¿Cambia su contraseña periodicamente?')
          answer46= input('Escriba "Si" o escriba "No":')
          
          if answer46 ==a:
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer47=input('Escriba "Si" o escriba "No":')
            
            if answer47==a:
              print("El nivel de exposicion es de: 30% ")
            elif answer47==b:
              print('El nivel de exposicion es de: 50%')
            else:
              print("No se entendio su respuesta")

              
          elif answer46==b:
           print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
           answer48=input('Escriba "Si" o "No"')
           if answer48==a:
              print("El nivel de exposicion es de: 25% ")
           elif answer48==b:
              print('El nivel de exposicion es de: 30%')
           else:
              print("No se entendio su respuesta")   
          else:
            print("No se entendio su respuesta")
        elif answer45==b:
          print('¿Cambia su contraseña periodicamente?')
          answer49= input('Escriba "Si" o escriba "No":')
          
          if answer49==a:
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer50=input('Escriba "Si" o escriba "No":')
            
            if answer50==a:
              print("El nivel de exposicion es de: 10% ")
            elif answer50==b:
              print('El nivel de exposicion es de: 15%')
            else:
              print("No se entendio su respuesta") 
              
          elif answer49 ==b:
            print("¿Su contraseña tiene caracteres especiales como:*,#,$,etc.?")
            answer51=input('Escriba "Si" o escriba "No":')
            
            if answer51==a:
              print("El nivel de exposicion es de: 35% ")
            elif answer51==b:
              print('El nivel de exposicon es de: 45%')
            else:
              print("No se entendio su respuesta")
          else:
            print("no se entendio su respuesta")
        else:
          print("No se entendio su respuesta")

          
        
    elif answer36 == b:
      print ("¿La contraseña de su correo es la misma que la de alguna de sus redes sociales?")
      answer52= input('Escriba "Si" o escriba "No":')
      
      if answer52 == a:
        print('¿Su contraseña esta relacionada a algo de usted, como: numero de documento fecha de nacimiento o nombre?')
        answer53=input('Escriba "Si" o escriba "No":')
        
        if answer53==a:
          print('¿Cambia su contraseña periodicamente?')
          answer54= input('Escriba "Si" o escriba "No":')
          
          if answer54 ==a:
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer55=input('Escriba "Si" o escriba "No":')
            
            if answer55==a:
              print("El nivel de exposicion es de: 20%")
            elif answer55==b:
              print('El nivel de exposicion es de: 45%')
            else:
              print("No se entendio su respuesta")
          elif answer54 ==b:
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer56=input('Escriba "Si" o escriba "No":')
            
            if answer56==a:
              print("El nivel de exposicion es de: ")
            elif answer56==b:
              print('El nivel de exposicion es de:')
            else:
              print("No se entendio su respuesta")
          else:
            print("No se entendio su respuesta")
        elif answer53==b:
          print('¿Cambia su contraseña periodicamente?')
          answer57= input('Escriba "Si" o escriba "No":')
          
          if answer57 ==a:
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer58=input('Escriba "Si" o escriba "No":')
            
            if answer58==a:
              print("El nivel de exposicion es de: 25% ")
            elif answer58==b:
              print('El nivel de exposicion es de: 35%')
            else:
              print("No se entendio su respuesta") 
              
          elif answer57 ==b:
            print("¿Su contraseña tiene caracteres especiales como:*,#,$,etc.?")
            answer59=input('Escriba "Si" o escriba "No":')
            
            if answer59==a:
              print("El nivel de exposicion es de: 60% ")
            elif answer59==b:
              print('El nivel de exposicon es de: 80%')
            else:
              print("No se entendio su respuesta")
          else:
            print("no se entendio su respuesta")
        else:
          print("No se entendio su respuesta")
            
      elif answer52== b:
        print ('¿La contraseña de los sitios web mas importantes para usted tienen alguna relacion con su nombre, fecha de nacimiento o numero de identificacion?')
        answer60 = input('Escriba "Si" o escriba "No":')
                
        if answer60==a:
          print('¿Cambia su contraseña periodicamente?')
          answer61= input('Escriba "Si" o escriba "No":')
          
          if answer61 ==a:
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer62=input('Escriba "Si" o escriba "No":')
            
            if answer62==a:
              print("El nivel de exposicion es de: ")
            elif answer62==b:
              print('El nivel de exposicion es de:')
            else:
              print("No se entendio su respuesta")
          elif answer61==b:
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer63=input('Escriba "Si" o escriba "No":')
            
            if answer63==a:
              print("El nivel de exposicion es de: ")
            elif answer63==b:
              print('El nivel de exposicion es de:')
            else:
              print("No se entendio su respuesta")
          else:
            print("No se entendio su respuesta")
        elif answer60==b:
          print('¿Cambia su contraseña periodicamente?')
          answer64= input('Escriba "Si" o escriba "No":')
          
          if answer64 ==a:
            print("Su contraseña tiene caracteres especiales como:*,#,$,etc.")
            answer65=input('Escriba "Si" o escriba "No":')
            
            if answer65==a:
              print("El nivel de exposicion es de: 0% ")
            elif answer65==b:
              print('El nivel de exposicion es de: 5%')
            else:
              print("No se entendio su respuesta") 
              
          elif answer64==b:
            print("¿Su contraseña tiene caracteres especiales como:*,#,$,etc.?")
            answer66=input('Escriba "Si" o escriba "No":')
            
            if answer66==a:
              print("El nivel de exposicion es de: 5% ")
            elif answer66==b:
              print('El nivel de exposicon es de: 10%')
            else:
              print("No se entendio su respuesta")
          else:
            print("no se entendio su respuesta")
        else:
          print("No se entendio su respuesta")

      
    else:
      print("no se entendio su respuesta")
  else:
    print ("no se entendio su respuesta") 
    
elif answer == b:
  print("Gracias por su tiempo")
else:
  print("no se entendio su respuesta")