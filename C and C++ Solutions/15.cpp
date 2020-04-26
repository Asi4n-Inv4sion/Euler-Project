/*
Starting in the top left corner of a 2×2 grid, and only being able to move
to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
*/
# include <iostream>
using namespace std;

// This takes way too long
long long int num_of_routes(int length, int width)
{
    if (length == 0 && width == 0)
    {
        return 1;
    }
    else if (length == 0)
    {
        return num_of_routes(length, width - 1);
    }
    else if (width == 0)
    {
        return num_of_routes(length - 1, width);
    }
    else
    {
        return num_of_routes(length, width - 1) + num_of_routes(length - 1, width);
    }
}

long long int factorial(int n)
{
    long long int fact = 1;
    for (int i = 1; i <= n; i++)
    {
        fact *= i;
    }
    return fact;
}

// THIS DOESNT WORK, even the long long int is not largest enough to hold 40!
long long int faster(int length, int width)
{
    // using the formula for find a path in a grid (length + width)C(length or width)
    return factorial(length + width) / (factorial(length) * factorial(width));
}

int main()
{
    cout << num_of_routes(20, 20);
}
