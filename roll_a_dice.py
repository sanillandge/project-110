import random

r="y"

while r=="y":
    num=random.randint(1,6)
    if num==1:
        print("[-----]") 
        print("[     ]") 
        print("[  0  ]") 
        print("[     ]") 
        print("[-----]")
    
    if num==2:
        print("[-----]") 
        print("[0    ]") 
        print("[     ]") 
        print("[    0]") 
        print("[-----]")
    if num==3:
        print("[-----]") 
        print("[0   0]") 
        print("[     ]") 
        print("[  0  ]") 
        print("[-----]")
    if num==4:
        print("[-----]") 
        print("[0   0]") 
        print("[     ]") 
        print("[0   0]") 
        print("[-----]")
    if num==5:
        print("[-----]") 
        print("[0   0]") 
        print("[  0  ]") 
        print("[0   0]") 
        print("[-----]")
    if num==1:
        print("[-----]") 
        print("[0 0 0]") 
        print("[     ]") 
        print("[0 0 0]") 
        print("[-----]")

    r=input("enter Y or N")
    print("\n")
    