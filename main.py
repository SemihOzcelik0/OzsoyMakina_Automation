from machine import Pin
import time

# Rulman Piston Role
rulmanPiston = Pin(16, Pin.OUT)
settimeR = 0

# Kapak Piston Role
kapakPiston = Pin(17, Pin.OUT)
kapaliSure = 300 # Saniye cinsinden kapağı kapalı tutma suresi
acikSure = 5 # Saniye cinsinden kapağı kapalı tutma suresi

# Motor Kontaktor Role
motor = Pin(18, Pin.OUT)
motorDurum = 0
tMotorAcik = 3
tMotorKapali= 60

# Titresim Motoru
tMotor = Pin(19, Pin.OUT)
settimeM = 0

# Rulman Yol Enduktif Sensor
rulmanKisa = Pin(4, Pin.IN)
rulmanUzun = Pin(2, Pin.IN)
settimeK = 0
settime = 0

# Rulman Yuva Enduktif Sensorler
rulman1 = Pin(14, Pin.IN)
rulman2 = Pin(12, Pin.IN)
rulman3 = Pin(8, Pin.IN)
rulman4 = Pin(6, Pin.IN)

# Kapasitif Sensor
robot = Pin(0, Pin.IN)
robotDeger = 0
robotBekle = 0

# Time
zaman = time.time()
simdikiZaman = 0
acik = 0

kapakPiston.value(1)
rulmanPiston.value(1)
motor.value(1)
tMotor.value(1)

while True:
    # Calisma suresi hesaplama
    simdikiZaman = time.time()
    gecenZaman = simdikiZaman - zaman
    
    # Zaman ayarli kapak acma-kapama
    if gecenZaman % (kapaliSure+acikSure) == 0 and acik == 0:
        kapakPiston.value(0)
        #print("Kapak Açıldı")
        acik = 1
        time.sleep(1)
        
    simdikiZaman = time.time() 
    gecenZaman = simdikiZaman - zaman

    if gecenZaman % acikSure == 0 and acik == 1:
        kapakPiston.value(1)
        #print("Kapak Kapandı")
        acik = 0
        time.sleep(1)

    if gecenZaman % tMotorAcik == 0 and tMotor == 0:
        tMotor.value(0)
        tMotor = 1
    elif gecenZaman % tMotorKapali == 0 and tMotor == 1:
        tMotor.value(1)
        tMotor = 0
    
    # Rulmanları Yuvadan Yukseltme
    if rulman2.value() == 1 and rulman2.value() == 1 and rulman3.value() == 1 and rulman4.value() == 1 and robotDeger == 0:
        
        if settimeR == 0:
            rulmanZaman = time.time()
            settimeR = 1
        
        rulmanPistonSure = time.time() - rulmanZaman

        if rulmanPistonSure >= 2: #Rulman yükseltme gecikme süresi
            rulmanPiston.value(0)
            #print("Rulmanlar Yükseldi")
            robotDeger = 1

    else:
        settimeR = 0
    
    # Robot Durum Kontrollu Yuva Indirme
    if robotDeger == 1:
        if robot.value() == 1:
            robotBekle = 1
        
        if robot.value() == 0 and robotBekle == 1:
            rulmanPiston.value(1)
            #print("Rulmanlar İndi")
            robotDeger = 0
            robotBekle = 0
            
    # Motor Calistir-Durdur
    if rulmanKisa.value() == 0 and motorDurum == 0:
        if settimeK == 0:
            kisaSure = time.time()
            settimeK = 1
        
        rulmanKisaSure = time.time() - kisaSure

        if rulmanKisaSure >= 5:
            motor.value(0)
            #print("Motor Aktif")
            motorDurum = 1

    else:
        settimeK = 0
    
    if rulmanUzun.value() == 1 and motorDurum == 1:
        if settime == 0:
            sure = time.time()
            settime = 1
        
        rulmanSure = time.time() - sure

        if rulmanSure >= 5:
            motor.value(1)
            #print("Motor Durdu")
            motorDurum = 0

    else:
        settime = 0
    