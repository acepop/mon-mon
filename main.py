from class_mon.py import mon
from class_mon_apidia.py import mon_apidia
from class_move.py import move






def main():
    mon_apidia = mon_apidia(r".\mon.csv",r".\move.csv")
    mon1 = mon(0,mon_apidia)




    print("hellow world")

    



if __name__ == "__main__":
    main()