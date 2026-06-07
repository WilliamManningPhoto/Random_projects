#include <iostream>

void old(int age); // Forward declarations
void enter_name(int age);

void enter_name(int age){
    std::cout << "You are " << age << " years old." << std::endl;
    old(age); // Call of a function before this function
}

void old(int age){

    if (age > 18){ // If stateents are easy and structured
        std::cout << "You are an adult.";
    } else {
        std::cout << "Well done you haven't hit level 18 yet.";
    }

}

int main(){ // Main start
    int age;
    std::cout << "Enter your age: ";
    std::cin >> age;

    enter_name(age);

    return 0; // Completed program
}

/*
- Order of functions dont matter if you use forward declarations.
-  Remember to pass arguments to functions.
- Made it to this level of programming in C++ in 1 hour Yippe.
*/

