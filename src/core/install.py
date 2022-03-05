import os

def install(library):
    if library == "cpp_project":
        os.system("mkdir project")
        f = open("project/main.cpp", "w+")
        f.write("""#include <iostream>

int main(int argc, char const *argv[])
{
    std::cout << "Hello World" << std::endl;
    return 0;
}""")

        f.close()
    elif library == "vdk.h":
        os.system("mkdir project/lib")
        h_file = open("project/lib/vdk.h", "w+")
        h_file.write("""#ifndef vdk
#define vdk
#include <string>
using namespace std;

string i = "vdk.h";

std::string getOsName() {
    #ifdef _WIN32
        return "Windows 32-bit";
    #elif _WIN64
        return "Windows 64-bit";
    #elif __APPLE__ || __MACH__
        return "Mac OSX";
    #elif __linux__
        return "Linux";
    #elif __FreeBSD__
        return "FreeBSD";
    #elif __unix || __unix__
        return "Unix";
    #else
        return "Other";
    #endif
}
#endif""")
        h_file.close()
