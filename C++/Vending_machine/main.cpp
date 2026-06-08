#include <iostream>
#include <vector>
#include <string>

struct Item{ // Use of a struct to store variables
    std::string name;
    double price;
};

bool money_check(double balance, const std::vector<Item>& stock, int choice){ // Demonstration of passing my struct to funtion
    if (balance - stock[choice - 1].price < 0) {
        std::cout << "Leave me alone your in poverty" << std::endl;
        return true;
    }
    return false;
}

int main(){

    double balance = 10;
    int choice; 

    std::vector<Item> stock = { // A vector that holds objects
        {"Cola",   1.50}, // Each entry to the struct
        {"Crisps", 0.80},
        {"Water",  1.00},
        {"Chocolate",   1.20}
    };

    while (true){

        std::cout << "Options: Cola, Crisps, Water, Chocolate" << std::endl;

        std::cout << "Balance: " << balance << std::endl;

        std::cout << "Enter your choice (0 to exit): ";
        std::cin >> choice;

        if (choice >= 1 && choice <= 4 && money_check(balance, stock, choice)) continue;

        switch (choice){ // Switch statement to give user multiple choices
            case 0: // Case 0 is the entry of an int, use if statement for strings
                std::cout << "Goodbye!" << std::endl;
                return 0; // Exit program
            case 1:
                std::cout << "You picked Cola" << std::endl;
                balance = balance - stock[0].price;
                break; // Break out of case statement after choice is ran
            case 2:
                std::cout << "You picked Crisps" << std::endl;
                balance = balance - stock[1].price;
                break;
            case 3:
                std::cout << "You picked Water" << std::endl;
                balance = balance - stock[2].price;
                break;
            case 4:
                std::cout  << "You picked Chocolate" << std::endl;
                balance = balance - stock[3].price;
                break;
            default:
                std::cout << "Invalid Choice " << std::endl;
                break;
        }

    }


};