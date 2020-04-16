import numpy
import cv2
import random
import math


# (g,b,r)
# (x,y)

def help():
    print()
    print("Visit the site for complete guide")
    print("SHORT GUIDE:")
    print("Keyboard Commands:")
    print(" N- New phasor")
    print(" P- Plot")
    print(" Q- Quit or Exit window")
    print(" S- Save")
    print(" V- View all phasors")
    print(" +- Add two phasors")
    print(" -- Subtract two phasors")
    print(" *- Multiply two phasors")


def save():
    print()
    print("Name with which the file is to be saved")
    fileName = input()
    cv2.imwrite(fileName, fr)

# def click_event(event,x,y,flag,param):
#     if event==cv2.EVENT_
#         text=str(x)+' '+str(y)
#         font=cv2.FONT_HERSHEY_SIMPLEX
#         cv2.putText(fr,text,(x,y),font,0.3,(7,132,231),1)
#         cv2.imshow('frame',fr)

def draw():
    cv2.setMouseCallback('Phasor Dream', click_event)


def plot():
    global nph
    global fr
    print()
    print("To plot a particular phasor, press '1'.")
    print("To plot all the phasors, press '2'.")
    mode = input()
    # for i in p.keys():
    #     print((c[0] + p[i][0], c[1] - p[i][1]))
    #     fr = cv2.arrowedLine(fr, c,(c[0] + p[i][0], c[1] - p[i][1]), (255, 255, 255), 1)
    # cv2.imshow("Phasor Dream", fr)
    # To plot one phasor
    if mode == '1':
        try:
            print("Phasor to be plotted")
            pln = input()
            print("Press 1 to plot on edge of other phasor.")
            print("Press 2 to plot at origin")
            plotOn = input()
            # To plot on edge of other phasor
            if plotOn == '1':
                print("Plot on the edge of phasor:")
                print(p)
                ed = input()
                try:
                    (b, g, r) = (int(255 * random.random()), int(255 * random.random()), int(255 * random.random()))
                    fr = cv2.arrowedLine(fr, (int(c[0] + p[ed][0]), int(c[1] - p[ed][1])),
                                         (int(c[0] + p[ed][0] + nph[pln][0]), int(c[1] - p[ed][1] - nph[pln][1])),
                                         (b, g, r), 1)
                    fr = cv2.putText(fr, pln, (int(c[0] + p[ed][0] + nph[pln][0]), int(c[1] - p[ed][1] - nph[pln][1])),
                                     cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                     (b, g, r), 1)
                except:
                    print("Phasor requested to plot may not exist")
                    print("Press H for Help")
            # To plot on origin
            else:
                (b, g, r) = (int(255 * random.random()), int(255 * random.random()), int(255 * random.random()))
                fr = cv2.arrowedLine(fr, c, (int(c[0] + nph[pln][0]), int(c[1] - nph[pln][1])), (b, g, r), 1)
                fr = cv2.putText(fr, pln, (int(c[0] + nph[pln][0]), int(c[1] - nph[pln][1])), cv2.FONT_HERSHEY_SIMPLEX,
                                 0.5,
                                 (b, g, r), 1)
            del (nph[pln])
        except KeyError:
            print("Phasor requested to plot may not exist")
            print("Press H for Help")
    # To plot all the phasors
    else:
        for i in nph.keys():
            (b, g, r) = (int(255 * random.random()), int(255 * random.random()), int(255 * random.random()))
            fr = cv2.arrowedLine(fr, c, (int(c[0] + nph[i][0]), int(c[1] - nph[i][1])), (b, g, r), 1)
            fr = cv2.putText(fr, i, (int(c[0] + nph[i][0]), int(c[1] - nph[i][1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                             (b, g, r), 1)
        nph = {}
    cv2.imshow("Phasor Dream", fr)
    print(p)


# except:
# print("Press H for Help")

# def undo():


def add():
    try:
        print()
        print("Adds First phasor to the second")
        print("First phasor")
        aph1 = input()
        print("Second phasor")
        aph2 = input()
        print("Name the sum")
        aname = input()
        p[aname] = (p[aph1][0] + p[aph2][0], p[aph1][1] + p[aph2][1])
        nph[aname] = (p[aph1][0] + p[aph2][0], p[aph1][1] + p[aph2][1])
    except:
        print("Enter the name of the phasor not its value")
        print("Press H for Help")


def sub():
    try:
        print()
        print("Substracts the second phasor from the first")
        print("First phasor")
        aph1 = input()
        print("Second phasor")
        aph2 = input()
        print("Name the difference")
        aname = input()
        p[aname] = (round(p[aph1][0] - p[aph2][0],3), round(p[aph1][1] - p[aph2][1],3))
        nph[aname] = (round(p[aph1][0] - p[aph2][0],3), round(p[aph1][1] - p[aph2][1],3))
    except:
        print("Enter the name of the phasor not its value")
        print("This function substracts second phasor from the first")
        print("Press H for Help")


def mul():
    try:
        print()
        print("Multiplies First phasor and the second")
        print("First phasor")
        aph1 = input()
        print("Second phasor")
        aph2 = input()
        print("Name the product")
        aname = input()
        p[aname] = (
            p[aph1][0] * p[aph2][0] - p[aph1][1] * p[aph2][1], p[aph1][0] * p[aph2][1] + p[aph1][1] * p[aph2][0])
        nph[aname] = (
            p[aph1][0] * p[aph2][0] - p[aph1][1] * p[aph2][1], p[aph1][0] * p[aph2][1] + p[aph1][1] * p[aph2][0])
    except:
        print("Enter the name of the phasor not its value")
        print("Press H for Help")


def newPhasor():
    print("Name of the phasor:")
    name = input()
    print("Press 1 for r,Theta(deg) format")
    print("Press 2 for a+jb format")
    mode = input()
    i = [0, 0]
    if mode == "1":
        try:
            print("Phasor in r Theta(deg) format")
            pol = input().strip().split()
            i[0] = round(float(pol[0]) * math.cos(float(pol[1]) * math.pi / 180), 3)
            i[1] = round(float(pol[0]) * math.sin(float(pol[1]) * math.pi / 180), 3)
        except:
            print("Phasor not in specified format")
            print("Press H for Help")
    else:
        print("Phasor in a+jb format")
        try:
            np = input().strip().split("j")
            np[0] = np[0].strip()
            np[1] = np[1].strip()
            if np[0][len(np[0]) - 1] == "+":
                np[0] = np[0][:len(np[0]) - 1]
                np[1] = np[1][:len(np[1])]
                i[0] = round(float(np[0]), 3)
                i[1] = round(float(np[1]), 3)
                # try:
                #     if name in p.keys():
                #         print("Reassigning a phasor which already exists with the same name")
                #     nph[name] = (i[0], i[1])
                #     p[name] = (i[0], i[1])
                # except KeyError:
                #     print("Try giving a different name for your phasor")
                #     print("Press H for Help")
            if np[0][len(np[0]) - 1] == "-":
                np[0] = np[0][:len(np[0]) - 1]
                np[1] = np[1][:len(np[1])]
                i[0] = round(float(np[0]), 3)
                i[1] = -1 * round((float(np[1])), 3)
        except:
            print("The phasor entered not in a+jb format")
            print("Press H for Help")
    try:
        if name in p.keys():
            print("Reassigning a phasor which already exists with the same name")
        nph[name] = (i[0], i[1])
        p[name] = (i[0], i[1])
        print(p)
    except KeyError:
        print("Try giving a different name for your phasor")
        print("Press H for Help")


frl = 1001
frb = 701
fr = numpy.zeros((frb, frl, 3), numpy.uint8)
c = (frl // 2, frb // 2)
fr = cv2.line(fr, (c[0], 0), (c[0], frb), (9, 9, 9), 1)
fr = cv2.line(fr, (0, c[1]), (frl, c[1]), (9, 9, 9), 1)
nph = {}
p = {}
while True:
    cv2.imshow("Phasor Dream", fr)
    if cv2.waitKey(0) == ord('n'): newPhasor()
    if cv2.waitKey(0) == ord('h'): help()
    if cv2.waitKey(0) == ord('s'): save()
    if cv2.waitKey() == ord('q'):
        cv2.destroyAllWindows()
        break
    if cv2.waitKey(0) == ord('p'): plot()
    if cv2.waitKey(0)==ord('d'): draw()
    # if cv2.waitKey(0)==ord('z'):undo()
    if cv2.waitKey(0) == ord('+'): add()
    if cv2.waitKey(0) == ord('-'): sub()
    if cv2.waitKey(0) == ord('v'): print("\n" + str(p))
    if cv2.waitKey(0) == ord('*'): mul()
