import click
import time
import os
import platform
import core.install as install
import core.exceptions as exception
from pathlib import Path

# commands
@click.command()
@click.option('--cpp', is_flag=True, help="Creates a C++ project.")
@click.option('--debug', is_flag=True, help="Debugs/Runs your C++ project.")
@click.option('--version', is_flag=True, help="Shows latest version of vdk.")
@click.option('--device', is_flag=True, help="Used to outputs platform information.")
@click.option('--lib', is_flag=True, help="Shows a list of available libraries.")
@click.option('--update', is_flag=True, help="Upgrades to the latest version.")
@click.option('-i', 'package_name', help="Installs Libraries/Packages")

def cli(cpp, debug, version, device, lib, update, package_name):
    if cpp:
        path = Path("project/main.cpp")
        def createProject():
            print("Creating project...")
            
            install.install("cpp_project")

            print("Project created.")

        # detects if project folder already exists
        if path.is_file():
            f = open("project/main.cpp", "r")
            f.close()
            
            exception.message("warning", "You already have a main.cpp file in your project, running this command again may rewrite the entire file. Continue?")
            a = input("(y/n) > ")

            if a == "y":
                createProject()
            elif a == "n":
                return False
            else:
                return True

        else:
            createProject()


    elif debug:
        try:
            d = open("project/main.cpp")
            d.close
        except FileNotFoundError:
            print("C++ project not created yet, use \u001b[0;1mvdk --cpp\u001b[0m to create one.")
        else:
            os.system("g++ project/main.cpp")
            os.system("./a.out")

    elif version:
        print("""VDK: \u001b[32;1mv1.0.0\u001b[0m""")
        print("Click: \u001b[32;1m7.1.2\u001b[0m")
        print("Pip3: \u001b[32;1m21.3.1\u001b[0m")
        print("")
        print("Status: \u001b[36;1mUp To Date\u001b[0m")

    elif device:
        print(platform.platform())

    elif lib:
        print(
            "\u001b[36;1mvdk.h\u001b[0m --- No info \t \u001b[36;1mvython\u001b[0m --- A VDK python library.")
        print('Use \u001b[0;1m-i (library name)\u001b[0m to install a library.')

    elif update:
        print("\u001b[36mUpdating...\u001b[0m")
        os.system("python3 -m pip install --upgrade pip")
        os.system("python3 -m pip install click")

    elif package_name:
        if package_name == "vdk.h":
            path = Path("project/lib/vdk.h")

            if path.is_file():
                print("'vdk.h' is already installed.")
            else:
                install.install("vdk.h")
                print("Library installed.")

        elif package_name == "vython":
            print("\u001b[32;1m[Installing Library]\u001b[0m")

            os.system("mkdir lib")

            libr = open("lib/vython.py", "w+")
            libr.write("""def hello(name):
    return 'Hello ' + name""")
            libr.close()

            print("\u001b[32;1m[Installed Library]\u001b[0m")
            
            f = open("main.py", "w+")
            f.write("""""")
            f.close()

        else:
            exception.message("error", f"No Such Package: {package_name}")

if __name__ == "__main__":
    cli()
