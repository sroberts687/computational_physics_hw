/*Bisection Method.cpp
Uses a function defined in f and the interval defined as constants
to calculate the root of a function across the interval.

Assumes f(A) and f(B) have different signs.

Adam Anthony
CS340 SP15
2/9/15
*/
#include <iostream>
#include <cmath>
//bounds of the interval
#define A 0
#define B 1
#define TOL 1E-2
using namespace std;

double f(double);

void main()
{
	//bounds of the interval
	double a = A, b = B;
	//tolerance and point to evaluate at
	double p = 0, fa = f(a);
	//max iterations, and current iteration
	int iteration = 1, maxIterations = 100;
	
	while (iteration < maxIterations)
	{
		p = a + (b - a) / 2;
		double fp = f(p);

		//check to see if we're done
		//p-a = (b-a)/2
		if (p - a < TOL || fp == 0)
		{
			//print out solutin and return
			cout << "The root of the function on the interval [" << A <<
				", " << B << "] is x = " << p << endl;
			cout << "f(" << p << ") = " << fp << " after " << iteration << " iterations." << endl;
			break;
		}
		//else
		iteration++;
		if (fa*fp > 0)
		{
			//shift the location of a
			a = p;
			fa = fp;
		}
		else
		{
			//shift location of b
			b = p;
		}
	}

	system("pause");
}

double f(double x)
{
	//x^3-7x^2+14x-6
	return pow(x, 3) - 7 * pow(x, 2) + 14 * x - 6;
}
