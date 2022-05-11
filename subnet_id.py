def twopower(bit):       
    return 2**bit
     
def no_host_subnet(cf):
    bit=int(cf/8)
    nb=cf-(8*bit)
    hb=32-cf
    print(f"Network bit is 2's power {nb} which is {twopower(nb)}")
    print(f"host bit is 2's power {hb} which is {(twopower(hb)-2)}")

def subnetid(cf):
    bit=int(cf/8)
    nb=cf-(8*bit)
    s=0
    count=7
    for _ in range(0,nb):
        s+=(2**count)
        count=count-1    
    return s

def ipt(ip,cf):
    bit=int(cf/8)
    subid=ip
    count=0
    for i in range(bit,4):
        if count==0:
            subid[i]=subnetid(cf)&subid[i]
            count=count+1
        else:    
            subid[i]=0
    return subid  

ip=input("enter ip ")
cf=int(input("enter cf value "))
a=[]
b=[]
a.append(ip.split("."))
for i in range(0,len(a[0])):
    b.append(int(a[0][i]))

if b[0]>0 and b[0]<=127:
    print('\n')
    print("class A")
    no_host_subnet(cf)
    sid=ipt(b,cf)
    print(f"subnet id is {sid[0]}.{sid[1]}.{sid[2]}.{sid[3]}")

elif b[0]>=128 and b[0]<=191:
    print('\n')
    print("class B")
    no_host_subnet(cf)
    sid=ipt(b,cf)
    print(f"subnet id is {sid[0]}.{sid[1]}.{sid[2]}.{sid[3]}")

elif b[0]>=192 and b[0]<=223:
    print('\n')
    print("class C") 
    no_host_subnet(cf)
    sid=ipt(b,cf)
    print(f"subnet id is {sid[0]}.{sid[1]}.{sid[2]}.{sid[3]}")

else:
    print("out of range")      