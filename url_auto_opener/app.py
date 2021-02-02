import os
import webbrowser
import time

file_name = input("Sisesta failinimi: ")
f = open(file_name, encoding = "UTF-8")
num_lines = sum(1 for line in open(file_name))

countsek = 6 #mitu sekundit on alla laadimise alustamiseks aega
continue_sek = 20 #mitme sekundi järel avatakse uus link

print("There are " + str(num_lines) + " entities in file " + file_name + " to be exported!")
time.sleep(2)

check = input('To continue, press "y": ')
if check == 'y':

    print("Creditinfo export is starting in " + str(countsek-1) + " seconds!")
    for sek in range(countsek):

        print(sek)
        time.sleep(1)
        
    counter = 1 #counter loopi jaoks
    breaker = 0

    for nr in range(num_lines):
        for url in f:
            time.sleep(1)
            print("Avan "  + str(counter) + "/" + str(num_lines) + " URLi: " + url);
            time.sleep(1)
            webbrowser.open(url, new=2)
            print("Avatud!")
            time.sleep(continue_sek)
            counter +=1
        f.close()

else:
    print("Export katkestatud!")

#os.system("taskkill /im chrome.exe /f")
