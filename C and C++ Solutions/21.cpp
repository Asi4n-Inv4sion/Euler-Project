/*
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n)

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
*/

# include <iostream>
# include <cmath>
using namespace std;

int sum_of_factors(int n)
{
    int factors = 1;
    for (int i = 2; i <= (int)pow(n, 0.5) + 1; i++)
    {
        if (n % i == 0)
        {
            factors += i + n/i;
        }
    }

    if ((int)pow(n, 0.5) * (int)pow(n, 0.5) == n)
    {
        factors -= (int)pow(n, 0.5);
    }

    return factors;
}

int main()
{
    int sum = 0;
    for (int i = 2; i < 10000; i++)
    {
        int j = sum_of_factors(i);
        if (j < 10000 && j > i)
        {
            // cout << i << ':' << sum_of_factors(j);
            if (sum_of_factors(j) == i)
            {
                sum += i + j;
            }
        }
    }
    cout << sum;
}
