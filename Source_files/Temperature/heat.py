
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------
""" |      |        |      |      |      | 
    | fuel | buffer | IPyC | SiC  | OPyC |
    |      |        |      |      |      |
"""
#-----------------------------------------------
#
#----------------------------
# Boundary Conditions
#----------------------------
T_out = 1200    # Celsius
Q = 600*pow(10,6)          # MW/m3
#----------------------------
# Geometry dimentions
#----------------------------
d_f = 250*pow(10,-6)    # meter
d_buf = d_f + 100*pow(10,-6)  # meter
d_ipyc = d_buf + 40*pow(10,-6)  # meter
d_sic = d_ipyc + 35*pow(10,-6)   # meter
d_opyc = d_sic + 40*pow(10,-6)  # meter

#---------------------------
# Conductivity at 1200C
#---------------------------
k_f = 2.08     # W/m*C
k_buf = 1.3    # W/m*C
k_ipyc = 5.2   # W/m*C
k_sic =35.7    # W/m*C
k_opyc = 5.2   # W/m*C
#---------------------------

def temp_dist(r):
    if r>= 0 and r<= d_f:
        return T_out + ((d_opyc - d_sic)/(k_opyc*d_opyc*d_sic) + 
                           (d_sic - d_ipyc)/(k_sic*d_sic*d_ipyc) +
                           (d_ipyc -d_buf)/(k_ipyc*d_buf*d_ipyc) +
                           (d_buf -d_f)/(k_buf*d_buf*d_f) + 
                           (d_f**2 - r**2)/(2*k_f*d_f**3))*Q*d_f**3
                        
    elif r > d_f and r <= d_buf:
        return T_out + ((d_opyc - d_sic)/(k_opyc*d_opyc*d_sic) + 
                           (d_sic - d_ipyc)/(k_sic*d_sic*d_ipyc) +
                           (d_ipyc -d_buf)/(k_ipyc*d_buf*d_ipyc) +
                           (d_buf -r)/(k_buf*d_buf*r))*Q*d_f**3
   
    elif r > d_buf and r <= d_ipyc:
        return T_out + ((d_opyc - d_sic)/(k_opyc*d_opyc*d_sic) + 
                           (d_sic - d_ipyc)/(k_sic*d_sic*d_ipyc) +
                           (d_ipyc -r)/(k_ipyc*r*d_ipyc))*Q*d_f**3
   
    elif r > d_ipyc and r <= d_sic:     
        return T_out + ((d_opyc - d_sic)/(k_opyc*d_opyc*d_sic) + 
                           (d_sic - r)/(k_sic*d_sic*r))*Q*d_f**3 
    
    elif r > d_sic and r <= d_opyc:     
        return T_out + ((d_opyc - r)/(k_opyc*d_opyc*r))*Q*d_f**3
    else:
        return False

# print(d_f, d_buf, d_sic)

dr = 5*pow(10,-6)
r= pow(10,-7)
rad = []
step_num = int(d_opyc/dr)
temp = []
for i in range(0, step_num):
    temp.append(temp_dist(r))
    rad.append(r*pow(10,3))
    r+=dr
#print(len(rad),len(temp))

plt.plot(rad,temp)
plt.xlabel("TRISO radius, cm")
plt.ylabel("Temperature, Celsius")
plt.title("Temperature distribution in TRISO (T=1200C)")
plt.savefig('fig2.png', dpi = 150)
plt.show()




