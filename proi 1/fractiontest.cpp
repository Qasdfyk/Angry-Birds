#include <iostream>
#include "fraction.h"

int main()
{
    fraction f0;
    if (f0.numerator() != 0) std::cout<<"Error: incorrect numerator()\n";
    if (f0.denominator() != 1) std::cout<<"Error: incorrect numerator()\n";

    { // fikusny bloczek mozna go powtarzac bo za nawiasami f1 znika
        fraction f1(1, 2);
        if (f1.numerator() != 1) std::cout<<"Error: incorrect numerator()\n"; 
        if (f1.denominator() != 2) std::cout<<"Error: incorrect numerator()\n";
    }

    {
        fraction f1(2, 4);
        if (f1.numerator() != 1) std::cout<<"Error: incorrect numerator()\n"; 
        if (f1.denominator() != 2) std::cout<<"Error: incorrect numerator()\n";
        f1.print();
    }

    {
        fraction f1(-2, 4);
        fraction fcorrect(-1, 2);
        if (not f1.thesame(fcorrect)) std::cout<<"Error: incorrect fraction\n";
        if (f1.numerator() != -1) std::cout<<"Error: incorrect numerator()\n"; 
        if (f1.denominator() != 2) std::cout<<"Error: incorrect numerator()\n";
        f1.print();
    }    

    {
        fraction f1(1, 4);
        fraction f2(1, 2);
        fraction fres = f1.add(f2);
        fraction fcorrect(3, 4);
        if (not fres.thesame(fcorrect)) std::cout<<"Error: incorrect fraction after addition #1\n";
    }

    std::cout<<"End of tests.";
    return 0;
}