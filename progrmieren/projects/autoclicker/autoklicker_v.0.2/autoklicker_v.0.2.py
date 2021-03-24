from tkinter import *
import pyautogui
import time
import msvcrt
einstellungenFenster = Tk()
einstellungenFenster.title("Einstelllungen Autoklicker")
wiederholungEingeben = Entry(einstellungenFenster)
wiederholungEingeben.pack(side=LEFT)
pauseEingeben = Entry(einstellungenFenster)
pauseEingeben.pack(side=LEFT)
betweenCounterButton = Entry(einstellungenFenster)
betweenCounterButton.pack(side=LEFT)
def showBeschreibung():
    print("dieses programm kann das drücken der linken maustaste simulieren.")
def showHowTo():
    print("In dem ersten Eingabefeld gibt man an, wie oft Gecklickt werden soll. Wenn 0 eingegeben = EndlessMode")
    print("In dem Zweiten Eingabefeld gibt man an, wie lange zwischen den clicks (in sek) gewartet werden soll.")
    print("In dem dritten Eingabefeld kann 0 angegeben werden, um keinen zähler zu haben, der einem die zeit bis zum nächsten click anzuzeigt, oder es kann 1 angegeben werden, um diesen zähler zu aktivieren.")
    print("[Für dumme: der Button am ende startet und Übernimmt die Eingaben]")
def showInfos():
    beschreibungFenster = Tk()
    beschreibungFenster.title("Infos")
    zeigeBeschreibungButton =  Button(beschreibungFenster, text = "Beschreibung", command = showBeschreibung)
    zeigeBeschreibungButton.pack(side=LEFT)
    zeigeHowToButton = Button(beschreibungFenster, text = "How to use", command = showHowTo)
    zeigeHowToButton.pack(side=LEFT)
    freeLabel = Label(beschreibungFenster)
    freeLabel.pack(side=LEFT)
    def printMail():
        print("info@nitropaul.de")
    def printWeb():
        print("http://nitropaul.de/projekte")
    ContacktEmailButton = Button(beschreibungFenster, text = "Email: info@nitropaul.de", command = printMail)
    ContacktTeleButton = Button(beschreibungFenster, text = "quelle: nitropaul.de/projekte", command = printWeb)
    ContacktEmailButton.pack(side=LEFT)
    ContacktTeleButton.pack(side=LEFT)
def applySettingsButton():
    betweenCounterTogle = int(betweenCounterButton.get())
    for countdown in reversed(range(1,6)):
        print(countdown)
        time.sleep(1)
    wiederholungKontrolle = 0
    clicks = 0
    doClick = True
    while(doClick ==  True):
        pyautogui.click()
        clicks = clicks + 1
        print("click", clicks)
        for betweenCounter in reversed(range(0,int(pauseEingeben.get()))):
            time.sleep(1)
            if (betweenCounterTogle == 1):
                print(betweenCounter)
        if (int(wiederholungEingeben.get()) == 0):
            uselessVarialbe = 0
        else:
            wiederholungKontrolle = wiederholungKontrolle + 1
            if (wiederholungKontrolle == int(wiederholungEingeben.get())):
                doClick = False
    print("Fin")
applySettings = Button(einstellungenFenster,  text = "apply", command = applySettingsButton)
applySettings.pack(side=LEFT)
instgesamtBeschreibung = Button(einstellungenFenster, text = "Infos", command = showInfos)
instgesamtBeschreibung.pack(side=LEFT)
mainloop()