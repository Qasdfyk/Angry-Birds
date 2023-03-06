class fraction
{
    int num = 0;
    unsigned int denom = 1;

public:
    fraction() = default;
    fraction(int numertor, unsigned int denominator);

    int numerator() const; // jesli wiemy ze sie nie zmodyfikuje dodajemy const
    unsigned int denominator() const;

    bool thesame(fraction other) const;

    fraction add(fraction other) const;

    void print() const;
};

