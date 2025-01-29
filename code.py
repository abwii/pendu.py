import random as r
from turtle import *
# from PIL import Image

    # Affichage du pendu
f = 1
def faux () :
    if f == 1 :
        up()
        goto(0,0)
        down()
        forward(100)
    elif f == 2 :
        up()
        goto(20,0)
        left(90)
        down()
        forward(100)
    elif f == 3 :
        up()
        right(90)
        down()
        forward(60)
    elif f == 4 :
        up()
        goto(20,80)
        down()
        left(45)
        forward(28.284271247461900976033774484194) #théorème de pytagore pour connaitre la longeur de la poutre diagonale
    elif f == 5 :
        up()
        goto(80,100)
        right(135)
        down()
        forward(20)
    elif f == 6 :
        up()
        right(90)
        down()
        for i in range (45) :
            forward(1)
            left(8)
    elif f == 7 :
        up()
        left(90)
        forward(15)
        down()
        forward(20)
    elif f == 8 :
        up()
        goto(80,45)
        left(30)
        down()
        forward(15)
    elif f == 9 :
        up()
        goto(80,45)
        right(60)
        down()
        forward(15)
    elif f == 10 :
        up()
        goto(80,60)
        left(60)
        down()
        forward(15)
    elif f == 11 :
        up()
        goto(80,60)
        right(60)
        down()
        forward(15)
        up()
        goto(0,0)
        left(125)
        input("Appuyez sur une touche pour fermer")
    else :
        print("Erreur") #laisse pas cette ligne, c'est experimental, ou bien met "vous avez perdu le mec est mort xD"

    # Code du pendu
jouer = "Y"
if jouer =='Y':
    fi = open('dico.txt.txt','r')
    fi2 = open('mot5l.txt', 'w')

    n=r.randint(1,4976)

    for mot in fi :

        if len(mot) == 6 :
            fi2.write(mot)

    fi2.close()


    fi2 = open('mot5l.txt', 'r')
    for i in range(n):
        mot = fi2.readline()


    characters = "\n"

    for i in range(len(characters)):
        mot = mot.replace(characters[i],"")


    mot_devine = '-'*len(mot)

    print (mot_devine)
    print (mot)

    cpt=0
    list = []
    while mot != mot_devine:
        lettre = input("Entrez une lettre : "  )
        if mot.find(lettre) == -1 :
                print ("La lettre ",lettre," n'est pas dans le mot")
                cpt = cpt+1
                list.append(lettre)
                faux()
                f = f+1


        if cpt ==11:
            print("T'as perdu man")
            exit()

        for i in range (len(mot)):
            if lettre == mot[i]  :
                mot_devine = mot_devine[:i]+lettre+mot_devine[i+1:]
            if lettre == mot :
                mot_devine = mot
        print(mot_devine)
        print ("Les lettres qui ne sont pas dans le mot sont : ", list )
    if mot == mot_devine :
        print('Le mot etait bien',mot)

fi2.close()
fi.close()