# Hum iss program mein ek password checker banayenge jo yeh sunchit karega ki
# humara password strong hai.Pehle user se ek password ka string input lijiye.
# Fir check kariye ki user ka password sakht hai ya nahi. Ek sakht password ko
# yeh sab rule follow karne chaiye:
# 1 Kam se kam uski length 6 honi chaiye
# 2 Jada se jada length 16 se jyada na ho
# 3 Kam se kam ek dollar ka sign ($) hona chaiye
# 4 Kam se kam password mein 2 ya 8 hona chaiye
# 5 Password mein capital A ya capital Z hona chaiye
# Agar password yeh rules follow kar raha hai toh "Strong Password" print karo,
# nahi toh "Weak Password" type karo

ps_wd= input("enter number")
if len(ps_wd)>5 and len(ps_wd)<17:
    if "$" in ps_wd and ("2" in ps_wd or "8" in ps_wd) and ("A" in ps_wd or "Z" in ps_wd):
        print("Strong Password")
    else:
        print("week password")
else:
    print("Weak password")