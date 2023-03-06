#include <iostream>
#include "fraction.h"
#include <algorithm>


fraction::fraction(int numerator, unsigned int denominator)
{   
    unsigned int nosignnum = std::abs(numerator);
    unsigned int gcd = std::__gcd(nosignnum, denominator);

    num = numerator / (int)gcd;
    denom = denominator / gcd;
}

int fraction::numerator() const
{
    return num;
}

unsigned int fraction::denominator() const
{
    return denom;
}

bool fraction::thesame(fraction other) const
{   
    return numerator() == other.numerator() &&
            denominator() == other.denominator();

}

fraction fraction::add(fraction other) const
{
    int nnum = numerator()*other.denominator() +
                denominator()*other.numerator();
    int ndenom = denominator()*other.denominator();
    return fraction(nnum, ndenom);
}

void fraction::print() const
{
    std::cout<<numerator();
    if (denominator() != 0)
        std::cout<<'/' << denominator() ;
    std::cout<< '\n';
}

