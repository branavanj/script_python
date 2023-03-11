import subprocess


print("""
  ______ _____ _____  ________          __     _      _      
 |  ____|_   _|  __ \|  ____\ \        / /\   | |    | |     
 | |__    | | | |__) | |__   \ \  /\  / /  \  | |    | |     
 |  __|   | | |  _  /|  __|   \ \/  \/ / /\ \ | |    | |     
 | |     _| |_| | \ \| |____   \  /\  / ____ \| |____| |____ 
 |_|    |_____|_|  \_\______|   \/  \/_/    \_\______|______|
                                                                                                                         
""")

port = int(input("Entrez le port à ouvrir : "))

if port > 99999: 
    print("Erreur ! Veuillez mettre un autre ports ")

else:
    result = subprocess.call(["sudo","iptables", "-A", "INPUT", "-p", "tcp", "--dport", str(port), "-j", "ACCEPT"])
    if result !=0:
        print("Une erreur s'est produite lors de l'ouverture du port")
    else:
        print("Le port", port, "a été ouvert avec succès")



