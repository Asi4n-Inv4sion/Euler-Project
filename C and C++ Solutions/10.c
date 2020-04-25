/*
Find the sum of all the primes below two million.
*/
#include <stdio.h>
#include <math.h>

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
    long long int sum = 2;
    for (long long int i = 3; i < 2000000; i += 2)
    {
        if (isPrime(i))
        {
            sum += i;
        }
    }
    printf("%lld\n", sum);
}
