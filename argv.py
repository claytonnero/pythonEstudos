from sys import argv
from os import system

__autor__ = """
Clayton nero silva
"""

email = "neroclayton@gmail.com"
    

def msn(msn):
    return f"\n{msn}"

if len(argv) > 0:
    nome = argv[0]
    system("clear")
    if "-a" in argv[1]:
        system("clear")
        print(f"{__autor__} \n{email}")

    if "-h" in argv[1]:
        system("clear")
        print("\npagina de ajuda")
        print(msn("esta mensagem passada pela função nsn"))
