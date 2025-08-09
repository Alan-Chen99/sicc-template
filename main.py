from rich import print
from sicc import *
from sicc import functions as f


@program(loop=True)
def main():
    d = Device("StructureGlassDoor", "Door0")
    print("hello from trace time:", d)
    d["On"] = True
    yield_()


if __name__ == "__main__":
    main.cli()
