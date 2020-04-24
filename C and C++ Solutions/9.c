/*
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
*/

// Thanks to blackpenredpen for the algorithm: https://www.youtube.com/watch?v=n6vL2KiWrD4
#include <stdio.h>

int main()
{
    for (int m = 1; m <= 50; m++)
    {
        for (int n = 1; n <= 50; n++)
        {
            // blackpenredpen's algorithm for Pythagorean triplets
            long int a = 2*m*n;
            long int b = m*m - n*n;
            long int c = m*m + n*n;
            if (b > 0 && a + b + c == 1000)
            {
                printf("a: %ld b: %ld c: %ld abc: %ld\n", a, b, c, a*b*c);
                return 1;
            }
        }
    }
}
