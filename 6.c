/*
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/
# include <stdio.h>

int sumOfSquare(int n)
{
    return n * (n+1) * (2*n + 1) / 6;
}

int squareOfSum(int n)
{
    int sum = n * (n+1) / 2;
    return sum * sum;
}

int main()
{
    int dif = squareOfSum(100) - sumOfSquare(100);
    printf("%d\n", dif);
}
