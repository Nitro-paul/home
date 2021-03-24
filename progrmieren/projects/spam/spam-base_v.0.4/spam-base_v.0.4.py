from tkinter import *
def startSpamm():
    parameterFenster = Tk()
    parameterFenster.title("Einstellen der Parameter")
    spamTextEingeben = Entry(parameterFenster)
    spamTextEingeben.pack()
    wiederholungenEingeben = Entry(parameterFenster)
    wiederholungenEingeben.pack()
    spamschutzwartezeitEingeben = Entry(parameterFenster)
    spamschutzwartezeitEingeben.pack()
    newLineEingabe = Entry(parameterFenster)
    newLineEingabe.pack()
    newLineEingabeZählen = Entry(parameterFenster)
    newLineEingabeZählen.pack()
    def speichernAuto():
        with open('autosave.txt','w') as autosaveFile:
            autosaveFile.write(spamTextEingeben.get())
            autosaveFile.write("\n")
            autosaveFile.write(wiederholungenEingeben.get())
            autosaveFile.write("\n")
            autosaveFile.write(spamschutzwartezeitEingeben.get())
            autosaveFile.write("\n")
            autosaveFile.write(newLineEingabe.get())
            autosaveFile.write("\n")
            autosaveFile.write(newLineEingabeZählen.get())
            autosaveFile.write("\n")
            print("saved in autosave.txt in C:\\Users\*username*")
    def saveAs():
        speicherDialog = Tk()
        speicherDialog.title("save as/speichern unter")
        saveManEntry = Entry(speicherDialog)
        describeSaveAsLabel = Label(speicherDialog,text="<- gib den namen unter dem die Parameter gespeichert werden sollen ein, z.b. hallo.txt.")
        saveManEntry.pack(side=LEFT)
        describeSaveAsLabel.pack(side=LEFT)
        def saveAsButtonPressed():
            with open(saveManEntry.get(),'w') as manusaveFile:
                manusaveFile.write(spamTextEingeben.get())
                manusaveFile.write("\n")
                manusaveFile.write(wiederholungenEingeben.get())
                manusaveFile.write("\n")
                manusaveFile.write(spamschutzwartezeitEingeben.get())
                manusaveFile.write("\n")
                manusaveFile.write(newLineEingabe.get())
                manusaveFile.write("\n")
                manusaveFile.write(newLineEingabeZählen.get())
                manusaveFile.write("\n")
            print("saved with name",saveManEntry.get(),"in C:\\Users\*username*")
        SaveAsButton = Button(speicherDialog,text="Save",command=saveAsButtonPressed)
        SaveAsButton.pack(side=LEFT)
    def SpamAutoSave():
        with open("autosave.txt",'r') as autosaveFileRead:
            import pyautogui
            import time
            import math
            wiederholungen = int(autosaveFileRead.readlines()[2])
            print(wiederholungen,"pribnbnj")
            g = 0
            print("suche einen den platz, wo du den text eingeben willst und clicke diesen")
            print("starten in")
            print("5")
            time.sleep(1)
            for t in reversed(range(1,5)):
                print(t)
                time.sleep(1)
            time.sleep(1)
            print("abflug")
            for g in range(0,wiederholungen):
                f = autosaveFileRead.readlines()[1]
                a = 1
                for word in f:
                    pyautogui.typewrite(word)
                    time.sleep(int(autosaveFileRead.readlines()[3]))
                    if (int(autosaveFileRead.readlines()[4]) == 0):
                        return
                    else:
                        if (int(autosaveFileRead.readlines()[4]) == 1):
                            pyautogui.press('enter')
                        if (int(autosaveFileRead.readlines()[4]) == 2):
                            if (word == " "):
                                pyautogui.press('enter')
                        if (int(autosaveFileRead.readlines()[4]) == 3):
                            if (a == int(autosaveFileRead.readlines()[4])):
                                pyautogui.press('enter')
                                a = 1
                            else:
                                a = a + 1
                        if (int(autosaveFileRead.readlines()[4]) == 4):
                            if (a == int(autosaveFileRead.readlines()[5])):
                                pyautogui.press('enter')
                                a = 1
                            else:
                                if (word == " "):
                                    a = a + 1
                        if (int(autosaveFileRead.readlines()[4]) == 5):
                            if (word == int(autosaveFileRead.readlines()[5])):
                                pyautogui.press('enter')
            print("text wurde" , wiederholungen ,"mal eingegeben")
    def spam():
        import pyautogui
        import time
        import math
        wiederholungen = int(wiederholungenEingeben.get())
        g = 0
        print("suche einen den platz, wo du den text eingeben willst und clicke diesen")
        print("starten in")
        print("5")
        time.sleep(1)
        for t in reversed(range(1,5)):
            print(t)
            time.sleep(1)
        time.sleep(1)
        print("abflug")
        for g in range(0,wiederholungen):
            f = str(spamTextEingeben.get())
            a = 1
            for word in f:
                pyautogui.typewrite(word)
                time.sleep(int(spamschutzwartezeitEingeben.get()))
                if (int(newLineEingabe.get()) == 0):
                    return
                else:
                    if (int(newLineEingabe.get()) == 1):
                        pyautogui.press('enter')
                    if (int(newLineEingabe.get()) == 2):
                        if (word == " "):
                            pyautogui.press('enter')
                    if (int(newLineEingabe.get()) == 3):
                        if (a == int(newLineEingabeZählen.get())):
                            pyautogui.press('enter')
                            a = 1
                        else:
                            a = a + 1
                    if (int(newLineEingabe.get()) == 4):
                        if (a == int(newLineEingabeZählen.get())):
                            pyautogui.press('enter')
                            a = 1
                        else:
                            if (word == " "):
                                a = a + 1
                    if (int(newLineEingabe.get()) == 5):
                        if (word == int(newLineEingabeZählen.get())):
                            pyautogui.press('enter')
        print("text wurde" , wiederholungen ,"mal eingegeben")
    parameterAnwenden = Button(parameterFenster, text = "Parameter anwenden und Starten", command = spam)
    parameterAnwenden.pack()
    loadConfigAutoButton = Button(parameterFenster,text="Parameter aus autosave.txt laden und starten",command=SpamAutoSave)
    loadConfigAutoButton.pack()
    parameterSpeichernButton = Button(parameterFenster,text="Parameter Speichern",command=speichernAuto)
    parameterSpeichernButton.pack(side=LEFT)
    parameterManuSpeichernButton = Button(parameterFenster,text="Parameter speichern unter",command=saveAs)
    parameterManuSpeichernButton.pack(side=RIGHT)
def zeigeErklärung1():
    print("erklährung Erstes textfeld: in das erste eingabefeld wird der dext eingegeben, der automatisirt ausgegeben werden soll. Neue zeilen[enter] werden nicht berücksichtigt, dies kann aber durch andere funktionen ersetzt werden.")
def zeigeErklärung2():
    print("erklährung Zweites textfeld: in diesem feld wird angegeben, wie oft das automatische ausgeben passieren soll. In diesem feld dürfen keine Buchstaben oder zhlen kleiner 0 stehen! dieses programm hat keine schutzfunktionen gegen falsche bedinung.")
def zeigeErklärung3():
    print("erklährung Drittes textfeld: Manche programme können zu schnelle eingaben nicht verarbeiten oder markieren den zu schnell eingebenden benutzer als aspam. um dieses problem zu beheben, kann in diesem feld eingegeben werden, wie lange zwischen den einzelnen eingegebenen Buchstaben gewartet werden soll. sie maßeinheit ist sekunden. In diesem feld dürfen keine Buchstaben oder zhlen kleiner 0 stehen! dieses programm hat keine schutzfunktionen gegen falsche bedinung.")
def zeigeErklärung4():
    print("erklährung Viertes textfeld: in diesem textfeld kann man die funktionen für neue zeilen einstellen.")
    print("Eine eingabe der Zahl Null[0] bedeutet, dass nur in einer zeile ausgegeben wird.")
    print("Eine eingabe der Zahl Einz[1] bedeutet, dass nach jedem buchstaben einen neue zeile kmmt.")
    print("Eine eingabe der Zahl Zwei[2] bedeutet, dass bei jedem lerzeichen[space[ ]] eine neue zeile kommt.")
    print("Eine eingabe der Zahl Drei[3] bedeutet, dass immer nach der in zeile vier angegebenen anzahl von zeichen eine neue zeile kommt")
    print("Eine eingabe der zahl Vier[4] Bedeutet, dass immer nach der in felf 4 angegebenen menge von leerzeichen/wörtern eine neue zeile kommt.")
    print("Eine eingabe der Zahl Fünf[5] Bedeutet, dass immer bei dem in zeile 4 angegebenem zeichen einleerzeichen kommt.")
    print("In diesem feld dürfen keine Buchstaben oder zhlen kleiner 0 oder größer 5 stehen! dieses programm hat keine schutzfunktionen gegen falsche bedinung.")
def zeigeErklärung5():
    print("die Fünfte zeile fungirt als beschreibungszeile zu zeile 4 bei nichtbenutzung mit Null[0] ausfüllen. In diesem feld dürfen keine Buchstaben oder zhlen kleiner 0 stehen! dieses programm hat keine schutzfunktionen gegen falsche bedinung.")
def openHeplp():
    HilfeFenster = Tk()
    HilfeFenster.title("Hilfe/Help")
    HelpLabel1 = Label(HilfeFenster, text = "um dieses programm nutzen zu können, muss das Terminal und das fenster")
    HelpLabel3 = Label(HilfeFenster, text = "einstellen der parameter geöffnet seien.")
    HelpLabel2 = Label(HilfeFenster, text = "Das Programm kann nicht mit falschen Eingaben arbeiten.")
    HelpLabel4 = Label(HilfeFenster, text = "Bei Fragen, Bugs etc. an die unten stehende Emailadresse schreiben.")
    freeLabel1 = Label(HilfeFenster, text = " ")
    contactLabel = Label(HilfeFenster, text = "Email:   info@nitropaul.de ")
    contactLabe2 = Label(HilfeFenster, text = "Quelle:  nitropaul.de/downloads")
    infoLabel1 = Label(HilfeFenster, text = "version 0.2 stand 2020.12.30")
    HelpLabel1.pack()
    HelpLabel3.pack()
    HelpLabel2.pack()
    HelpLabel4.pack()
    freeLabel1.pack()
    contactLabel.pack()
    contactLabe2.pack()
    freeLabel1.pack()
    infoLabel1.pack()
einleitungFenster = Tk()
einleitungFenster.title("Einleitung")
einleitungText = Label(einleitungFenster, text = "dieses programm kann automatisirt text ausgeben.")
einleitungText.pack()
einleitungErsteZeile = Button(einleitungFenster, text = "zeige erklärung zu Erstem eingabefed", command = zeigeErklärung1)
einleitungErsteZeile.pack()
einleitungZweiteZeile = Button(einleitungFenster, text = "zeige erklärung zu Zweitem eingabefeld", command = zeigeErklärung2)
einleitungZweiteZeile.pack()
einleitungDritteZeile = Button(einleitungFenster, text = "zeige erklärung zu drittem eingabefeld", command = zeigeErklärung3)
einleitungDritteZeile.pack()
einleitungVierteZeile = Button(einleitungFenster, text = "zeige erklärung zu Viertem eingabefeld", command = zeigeErklärung4)
einleitungVierteZeile.pack()
einleitungFünfteZeile = Button(einleitungFenster, text = "zeige erklärung zu Fünftem eingabefeld", command = zeigeErklärung5)
einleitungFünfteZeile.pack()
startUsing = Button(einleitungFenster, text = "start", command = startSpamm)
startUsing.pack()
HelpButton = Button(einleitungFenster, text = "hilfe/help", command = openHeplp)
HelpButton.pack()
mainloop()