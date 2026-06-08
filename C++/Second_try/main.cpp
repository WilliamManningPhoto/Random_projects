#include <iostream>

void old(){ // First function in the list cant call others
    std::string text = "Mate your so old";

    std::cout << text << std::endl;
}

void enter_name(int age){
    std::cout << "You are " << age << " years old." << std::endl;
    old(); // Call of a function before this function
}

int main(){ // Main start
    int age;
    std::cout << "Enter your age: ";
    std::cin >> age;

    enter_name(age);

    return 0; // Completed program
}