


if vlan in nativevlan99:
     print("las vlans son iguales y cumplen con el requerimiento")
else:
    print("las vlans son diferentes y no cumplen con el requerimiento")
if vlan in nativevlan200:
  print("las vlans son iguales y cumplen con el requerimiento")
else:
    print("las vlans son diferentes y no cumplen con el requerimiento")



    acl_number = int(input("numero de acl: "))
if 1 <=acl_number <= 99:
    print("acl estandar")
elif 100 <= acl_number <= 199:
    print("acl extendida")
else:
    print("numero no corresponde a una acl")  
vlan = int(input("numero de vlan:" ))
nativevlan99 = [10,20,30,99]
nativevlan200 = [40,50,60,200]
# javiera_vergara
