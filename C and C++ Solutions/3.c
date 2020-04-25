/*
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
*/
# include <stdio.h>
# include <math.h>

int isPrime(long long int n)
{
    for (long long int i = 2; i < (long long int)pow(n, 0.5) + 2; i++)
    {
        if (n % i == 0)
        {
            return 0;
        }
    }
    return 1;
}

long long int largest_prime_factor(long long int n)
{
    for (long long int i = 1; i < (long long int)(n / 2); i++)
    {
        if (n % i == 0)
        {
            long long int factor = n / i;
            if (isPrime(factor))
            {
                return factor;
            }
        }
    }
}

int main()
{
    long long int num = 600851475143;

    long long int prime_factor = largest_prime_factor(num);
    printf("%lld\n", prime_factor);
}
