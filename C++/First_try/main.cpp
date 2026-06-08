#include <iostream> // Pull header file from the standard library

int main() { // Creation of a function, int means returning 0 is sucess of function
    std::string name = "Will"; // String of my name Will,(std:: being a prefix)
    int age = 20; // Declaration of integer variable

    std::cout << "Hello, " << name << std::endl;
    std::cout << "Age: " << age << std::endl;
    /* 
    std::cout - standard character output to
    << strea operator, like the comma in python (no brackets)
    "Hello" is my string from earlier
    << name - chains on the name variable ("Will")
    << std::endl - insertion of a newline and flushing buffer -
    causing output to be immediate
    */


    return 0; // Exit main and return 0 for program completion
}