# Simulation eines Ampelsystems

## Description
Simulation des Verhaltens einer Verkehrsampel (python). Es gibt den Zustand der Ampel und dessen Wechsel (rot, gelb. grün) zurück

## Features
- Class Definition einer Ampel-Klasse, mit folgenden Zusatänden: Rot, RotGelb, Grün, Gelb
- Möglichleit Ampelzustand zu setzten oder wiederzugeben
- Automatisches Umschalten 
- Ausgabe des Zustandes als Tupel (rot, gelb, grün)

## Methoden
- def_init_ : initialisiert die Ampel mit Zustand 'rot'
- setZustand(z) :setzt den Zusatnd z auf (rot, rotgelb, grün, gelb)
- schalten() : schaltet die ampel zum nächsten Zustand
- getLampen() : Gibt den Zustand als Tupel zurück
