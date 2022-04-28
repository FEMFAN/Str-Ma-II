from CoolProp.CoolProp import PropsSI
#Zustand 5 (Eintritt Turbine)
rho_4 = PropsSI('D','T',800,'P',11.5e6,'water')
h_4 = PropsSI('H','T',800,'P',11.5e6,'water')
s_4 = PropsSI('S','T',800,'P',11.5e6,'water')
print rho_4, h_4, s_4

#Zustand 5 (Eintritt Turbine)
rho_5 = PropsSI('D','T',798,'P',11e6,'water')
h_5 = PropsSI('H','T',798,'P',11e6,'water')
s_5 = PropsSI('S','T',798,'P',11e6,'water')
print rho_5, h_5, s_5

#Zustand 6' (Austritt Turbine (isentrop))
h_6_s = PropsSI('H','P',5000,'S',s_5,'water')
print h_6_s

#Zustand 6 (Austritt Turbine)
rho_6 = PropsSI('D','P',5000,'H',2.2308e6,'water')
T_6 = PropsSI('T','P',5000,'H',2.2308e6,'water')
s_6 = PropsSI('S','P',5000,'H',2.2308e6,'water')
print rho_6, T_6, s_6

#Zustand 0 (Austritt Kondensator) Annahme:isotherme kondensierung
rho_0 = PropsSI('D','P',4900,'T',T_6,'water')
h_0 = PropsSI('H','P',4900,'T',T_6,'water')
s_0 = PropsSI('S','P',4900,'T',T_6,'water')
print rho_0, h_0, s_0

#Zustand 1' (AUstritt Pumpe (isentrop))
h_1_s = PropsSI('H','P',12e6,'S',s_0,'water')
print h_1_s

#Zustand 1 (Austritt Pumpe)
rho_1 = PropsSI('D','P',12e6,'H',6557645.72,'water')
s_1 = PropsSI('S','P',12e6,'H',6557645.72,'water')
T_1 = PropsSI('T','P',12e6,'H',6557645.72,'water')
print rho_1,s_1,T_1
