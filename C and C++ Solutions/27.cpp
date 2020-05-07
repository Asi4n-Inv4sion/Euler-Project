/*
Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer
values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and
certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for
the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with n=0.
*/

#include <iostream>
#include <cmath>
using namespace std;

int isPrime(long long int n)
{
    if (n == 2)
    {
        return 1;
    }

    for (long long int i = 2; i < (long long int)pow(n, 0.5) + 2; i++)
    {
        if (n % i == 0)
        {
            return 0;
        }
    }

    return 1;
}

int main()
{
    int longest[] = {0, 0, 0}; // keep track of {a, b, num of consecutive primes}
    for (int a = -999; a <= 1000; a++)
    {
        for (int b = -999; b <= 1000; b++)
        {
            // cout << "checking" << a << ':' << b << '\n';
            int i = 0;
            while (isPrime(abs(i*i + a*i + b)))
            {
                i++;
            }
            if (i > longest[2])
            {
                longest[0] = a;
                longest[1] = b;
                longest[2] = i;
            }
        }
    }
    cout << longest[0]*longest[1];
}
