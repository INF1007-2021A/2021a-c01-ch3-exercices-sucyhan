#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def square_root(a: float) -> float:
    return math.sqrt(a)


def square(a: float) -> float:
    return a ** 2


def average(a: float, b: float, c: float) -> float:
    liste = [a, b, c]
    moyenne = sum(liste) / len(liste)
    return moyenne


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_total=angle_degs+angle_mins/60+angle_secs/3600
    return math.radians(angle_total)

    #pi = 3.1416
    #radian = angle_degs * (pi / 180)
    #radian2 = angle_mins * (pi / 10800)
    #radian3 = angle_secs * (pi / 4.84813681E-6)
    #return radian,  radian2,  radian3


def to_degrees(angle_rads: float) -> tuple:
    degres_total=math.degrees(angle_rads)
    degres=int(degres_total)
    reste_degres=degres_total-degres
    minutes_total=reste_degres*60
    minutes=int(minutes_total)
    reste_minutes=minutes_total-minutes
    secondes_total=reste_minutes*60
    return degres, minutes, secondes_total

    #pi= 3.1416
    #degres = angle_rads * (180 / pi)
    #minutes = angle_rads * (10800 / pi)
    #secondes = angle_rads * (4.84813681E-6 / pi)
    return degres, minutes, secondes

#Tf = Tc x 1.8 + 32
def to_celsius(temperature: float) -> float:
    tf=(temperature-32)/1.8
    return tf


def to_farenheit(temperature: float) -> float:
    tc= temperature*1.8+32
    return tc


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")

    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 180 Celsius en Farenheit: {to_farenheit(180.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
