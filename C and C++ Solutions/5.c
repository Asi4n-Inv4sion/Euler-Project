/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/
#include <stdio.h>

int main()
{
    int n = 20;
    int found = 0;
    while (found == 0)
    {
        int div = 1;
        for (int i = 3; i <= 20; i++)
        {
            if (n % i != 0)
            {
                div = 0;
            }
        }

        if (div == 1)
        {
            found = 1;
        }
        else
        {
            n += 20;
        }
    }

    printf("%d\n", n);
}
