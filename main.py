from class_mon.py import mon
from class_data_class.py import data_class
from class_move.py import move
from class_spcies.py import species



def main():
    data_class = data_class(r".\mon.csv",r".\move.csv")
    
    mon1 = mon(0,data_class)




    print("hellow world")

    



if __name__ == "__main__":
    main()