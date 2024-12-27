import os
import sys

def main():

    root_process = os.getpid()
    print(f"Root Process 0 with ID: {root_process}")

    for i in range(4): #Level 1 children
        pid=os.fork()
        if pid == 0:  #child
            pid = os.getpid()
            ppid = os.getppid()
            print(f"Child[1.{i+1}] with ID: {pid} and its Parent ID: {ppid}")
            for j in range(3): #Level 2 children
                eggoniaPid = os.fork()
                if eggoniaPid == 0:
                    eggoniaPid = os.getpid()
                    eggoniaNum = (i * 3) + (j + 1)
                    print(f"Child[2.{eggoniaNum}] with ID: {eggoniaPid} and its Parent ID: {os.getppid()}")
                    if eggoniaNum % 2 == 1 :
                        for k in range(2): #Level 3 children
                            diseggonaPid = os.fork()
                            if diseggonaPid == 0:
                                diseggonaPid = os.getpid()
                                diseggonaNum = (((eggoniaNum + 1) // 2) * 2) + k - 1
                                print(f"Child[3.{diseggonaNum}] with ID: {diseggonaPid} and its Parent ID: {os.getppid()}")
                                if diseggonaNum % 2 == 0 :
                                    for m in range(1): #Level 4 children
                                        triseggonaPid = os.fork()
                                        if triseggonaPid == 0:
                                            triseggonaPid = os.getpid()
                                            triseggonaNum = diseggonaNum // 2
                                            print(f"Child[4.{triseggonaNum}] with ID: {triseggonaPid} and its Parent ID: {os.getppid()}")
                                        else:
                                            os.wait()
                                os._exit(0)
                            else:
                                os.wait()
                    os._exit(0)
                else:
                    os.wait()
            os._exit(0)
        else: #parent
            os.wait()
    return 0

if __name__ == "__main__":
    os._exit(main())
