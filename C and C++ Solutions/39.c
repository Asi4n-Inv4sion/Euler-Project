/*
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?
*/

#include <stdio.h>
#include <math.h>

int main()
{
    int sol_arr[1001];
    for (int i = 0; i <= 1000; i++)
    {
        sol_arr[i] = 0;
    }

    for (int a = 1; a <= 1000; a++)
    {
        for (int b = 1; b <= a; b++)
        {
            double c = sqrt(pow(a, 2) + pow(b, 2));
            if (floor(c) == ceil(c))
            {
                int c_int = (int)c;

                if (b > 0 && a + b + c_int <= 1000)
                {
                    // printf("found sol to %d: %d, %d, %d\n", a+b+c_int, a, b, c_int);
                    sol_arr[a+b+c_int] += 1;
                }
            }
        }
    }
    int largest = 1;
    for (int i = 1; i < 1000; i++)
    {
        // printf("%d:%d\n", i, sol_arr[i]);
        if (sol_arr[i] > sol_arr[0])
        {
            sol_arr[0] = sol_arr[i];
            largest = i;
        }
    }
    printf("%d\n", largest);
}
