/*NewtonAndSecant.cpp
Uses a function defined in f and the interval defined as constants
to calculate the root of a function across the interval using both 
Newton's Method and the Secant Method.

Adam Anthony
CS340 SP15
2/17/15
*/
#include <iostream>
#include <cmath>
#include <iomanip>

//bounds of the interval
#define A 1
#define B 4
//The tolerance allowed
#define TOL 1E-5
//Maximum number of iterations of either method before failure
#define MAXIT 100
//Guesses for order of convergence
#define SECANT_ALPHA 1
#define NEWTON_ALPHA 1
using namespace std;

double f(double);
double derivF(double);
double lambda(double[MAXIT], int, int, int);

int main()
{
	double a = A, b = B;
	double newton[MAXIT];
	int iteration = 1;
	newton[0] = 0;
	newton[1] = a + (b - a) / 2;
	
	bool foundRoot = false;

	//Newton's Method
	cout << "Newton's Method (alpha: " << NEWTON_ALPHA << ")"  << endl << endl;

	while(!foundRoot && iteration <= MAXIT)
	{
		newton[++iteration] = newton[iteration-1] - 
			f(newton[iteration - 1]) / derivF(newton[iteration-1]);

		foundRoot = (abs(newton[iteration - 1] - newton[iteration]) <= TOL);
	}

	if (!foundRoot)
	{
		cout << "Failed to find a root using Newton's Method after " <<
			MAXIT << " iterations." << endl <<endl;
	}
	else
	{
		for (int i = 0; i < iteration; i++)
		{
			cout << "Iteration: " << setw(3) << left << i + 1;
			cout << " prevP: " << setw(7) << left << newton[i];
			cout << " p: " << setw(7) << left << newton[i + 1];
			cout << " lambda: " << setw(7) << left << lambda(newton, NEWTON_ALPHA, i, iteration) << endl;
		}
	}

	//reset variables for Secant
	foundRoot = false;
	a=A; b=B;
	double secant[MAXIT];
	iteration=2;
	secant[2] = a + (b - a) / 3;
	secant[1] = b - (b - a) / 3;
	secant[0] = 0;

	//Secant Method
	cout << endl << "Secant Method (alpha: " <<  SECANT_ALPHA << ")" << endl << endl;

	while (!foundRoot && iteration <= MAXIT)
	{
		secant[++iteration] = secant[iteration-1] - 
			(f(secant[iteration - 1])*(secant[iteration - 1] - secant[iteration-2])) / 
			(f(secant[iteration - 1]) - f(secant[iteration - 2]));

		foundRoot = (abs(secant[iteration - 1] - secant[iteration]) <= TOL);
	}
	
	if (!foundRoot)
	{
		cout << "Failed to find a root using the Secant Method after " <<
			MAXIT << " iterations." << endl << endl;
	}
	else
	{
		for (int i = 2; i <= iteration; i++)
		{
			cout << "Iteration: " << setw(3) << left << i-1;
			cout << " prevP2: " << setw(7) << left << secant[i-2];
			cout << " prevP: " << setw(7) << left << secant[i-1];
			cout << " p: " << setw(7) << left << secant[i];
			cout << " lambda: " << setw(7) << left << lambda(secant, SECANT_ALPHA, i, iteration) << endl;
		}
	}

	system("pause");

	return 0;
}

double f(double x)
{
	return x*x*x - 2*x*x - 5;
	//return sin(x) - exp(-x);
	//return x*x*x*x-4*x*x+4 - log(x);
	//return x*x*x - 6 * x*x + 9 * x - 4;
}
double derivF(double x)
{
	return 3*x*x - 4*x;
	//return cos(x) + exp(-x);
	//return 4 * x*x*x -8*x - 1 / x;
	//return 3 * x*x - 12 * x + 9;
}

double lambda(double sequence[MAXIT], int alpha, int index, int maxIteration)
{
	
	double denom = 1;

	//mostly so I don't have to use pow
	while (alpha-- > 0)
	{
		denom *= abs(sequence[index] - sequence[maxIteration]);
	}
	return abs(sequence[index+1]-sequence[maxIteration])/ denom;
}