using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;



namespace homework_two
{
    class Program
    {
        /* define global variables in a public, static class because C# does not allow
         * for global variable definitions */
        public static class Globals
        {
            public const double G = 1; // Unmodifiable
            public const double PI = 3.1415926;  // Unmodifiable
            public static double M1 = -1;  // Modifiable
            public static double M2 = -1;  // Modifiable
            public static double sep = -1; // Modifiable

            // search range for iterative methods
            public static double min = -700;
            public static double max = 700;

            // position of m1 and m2, respectively
            // current code written st x1 = 0 and x2 = sep
            internal static int x1;
            internal static double x2;
        }

        /* Main program defines grid size and asks for user to input values for M1, M2,
         * and seperation distance */
        static void Main(string[] args)
        {

            Console.WriteLine("Homework two, Sarah Roberts.");

            Console.WriteLine("Part (1)");

            // get Globals.{M1, M2, sep} from the user & ensure values are valid
            getInput();

            // initalize grid
            int minx = -200;
            int maxx = 200;
            int miny = -200;
            int maxy = 200;

            // dimensions used to construct array to hold grid
            int dimx = Math.Abs(minx) + Math.Abs(maxx) + 1;
            int dimy = Math.Abs(miny) + Math.Abs(maxy) + 1;

            // three dimensional array grid will hold grid points and function values
            double[,,] grid = new double[dimx, dimy, 5];

            Console.WriteLine("instantiated grid");

            
            for (int i = 0; i <= dimx; i++)
            {
                for (int j = 0; j <= dimy; j++)
                {
                    grid[i, j, 0] = minx + i;  // x coordinate
                    grid[i, j, 1] = miny + j;  // y coodrinate

                    // Funct will calculate the effective gravity for a point
                    grid[i, j, 2] = FunctX(grid[i, j, 0], grid[i, j, 1]);  // f_x(x,y)
                    grid[i, j, 3] = FunctY(grid[i, j, 0], grid[i, j, 1]);  // f_y(x,y)

                    grid[i, j, 4] = Potential(grid[i, j, 0], grid[i, j, 1]); // potential(r,theta)

                }
            }

            // output the x,y component of the acceleration at each grid point
            Console.WriteLine("x,y component of the acceleration at each grid point:");
            for (int i = minx; i <= maxx; i++)
            {
                for (int j = miny; j <= maxy; j++)
                {
                    // print the effective gravity in the format (a_r, a_theta)
                    // TODO: convert to (a_x, a_y)
                    Console.Write("( {0} , {1} ) \t", grid[i, j, 2], grid[i, j, 3]);

                    if (j == maxy)
                    {
                        Console.WriteLine();
                    }
                    
                }
            }

            // output the potential for each grid point
            Console.WriteLine("potential for each grid point: ");
            for (int i = minx; i <= maxx; i++)
            {
                for (int j = miny; j <= maxy; j++)
                {
                    Console.Write("{0} \t", grid[i, j, 4]);
                    if (j == maxy)
                    {
                        Console.WriteLine();
                    }
                }
            }

            // part 2
            Console.WriteLine("Part (2)");

            // TODO: generate contour plots
            // TODO: generate vector plot


            // part 3
            Console.WriteLine("Part (3)");



            // keep window open
            Console.WriteLine("\n Press any key to exit.");
            Console.ReadKey();

        }

        private static void getInput()
        {
            while (Globals.M1 < 0)
            {
                Console.WriteLine("enter a value for mass 1");
                Globals.M1 = Convert.ToDouble(Console.ReadLine());
            }

            while (Globals.M2 < 0)
            {
                Console.WriteLine("enter a value for mass 2");
                Globals.M2 = Convert.ToDouble(Console.ReadLine());
            }

            while (Globals.M2 < 0)
            {
                Console.WriteLine("enter a value for seperation between M1 and M2");
                Globals.sep = Convert.ToDouble(Console.ReadLine());
            }

            if (Globals.M1 <= Globals.M2)
            {
                double temp = Globals.M1;
                Globals.M1 = Globals.M2;
                Globals.M2 = temp;
            }

            // M1 >= M2, assign locations
            Globals.x1 = 0;
            Globals.x2 = Globals.sep;

        }

        private static double Potential(double x, double y)
        {
            return (-1 * Globals.G * Globals.M1 * Globals.M2 ) / Globals.sep;

            //throw new NotImplementedException();
        }

        private static double FunctX(double x, double y)
        {
            return (Globals.G * Globals.M1) / (x * x + y * y);
        }

        private static double FunctY(double x, double y)
        {
            throw new NotImplementedException();
        }

        private static double Funct(double v1, double v2)
        {
            throw new NotImplementedException();
        }

        private static int FindMax(int a, int b)
        {
            if (b > a)
            {
                return b;
            }
            else
            {
                return a;
            }
        }

        private static double L(double x)
        {
            // TODO: assign this properly for part (3)
            return Math.Cos(x);
        }

        // derivative of L(x)
        private static double Lderiv(double v)
        {
            throw new NotImplementedException();
        }

        // returns slope, according to funtion F
        // TODO: CHECK THIS!!!
        private static double Secant(double pm1, double pm2)
        {

            return pm1 - (L(pm1) * (pm1 - pm2)) / (L(pm1) - L(pm2));
        }

        private static double DoSecant()
        {
            // pull global range into local instance
            double min = Globals.min;
            double max = Globals.max;
            

            int i = 2;  // initialize step counter to two b/c we do first two iterations outside the loop
            double p = min + (max - min) / 2;
            double f = L(p);
            double tol = 0.0001;
            int maxIt = 50;


            double[] pValuesS = new double[maxIt];
            double[] fpValuesS = new double[maxIt];

            // initial conditions
            fpValuesS[0] = 1.5;
            fpValuesS[1] = Secant(min + (max - min) / 2, fpValuesS[0]);

            // optional output
            //Console.WriteLine(0 + "\t" + fpValuesS[0]);
            //Console.WriteLine(1 + "\t" + fpValuesS[1]);

            do
            {

                fpValuesS[i] = Secant(fpValuesS[i - 1], fpValuesS[i - 2]);

                //optional output
                // Console.WriteLine(i + "\t" + fpValuesS[i]);

                i++;

            } while (Math.Abs(fpValuesS[i - 1] - fpValuesS[i - 2]) > tol
              && i < maxIt - 1);

            return fpValuesS[i];
        }

        private static double DoNewtons()
        {
            int i = 0;
            int maxIt = 50;
            double tol = 0.0001;
            double min = Globals.min;
            double max = Globals.max;
            
            // function outputs
            double[] fpValuesN = new double[maxIt];
            // function inputs
            double[] pValuesN = new double[maxIt];
            // derivatives of function outputs
            double[] fprimeValuesN = new double[maxIt];

            // initial conditions
            pValuesN[0] = min + (max - min) / 2;
            fpValuesN[0] = L(min + (max - min) / 2);
            fprimeValuesN[0] = Lderiv(min + (max - min) / 2);

            // optional output
            //Console.WriteLine("0" + "\t" + pValuesN[0]);

            i++;

            do
            {
                pValuesN[i] = pValuesN[i - 1]
                  - (fpValuesN[i - 1] / fprimeValuesN[i - 1]);
                fpValuesN[i] = L(pValuesN[i]);
                fprimeValuesN[i] = Lderiv(pValuesN[i]);

                // optional output
                //Console.WriteLine(i + "\t" + pValuesN[i]);

                i++;

            } while (Math.Abs(pValuesN[i - 1] - pValuesN[i - 2]) > tol
              && i < maxIt - 1);

            return 0;
        }

        }
}


