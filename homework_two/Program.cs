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
            int minx = -100;
            int maxx = 100;
            int miny = -200;
            int maxy = 200;

            // dimensions used to construct array to hold grid
            int dimx = minx - maxx + 1;
            int dimy = miny - maxy + 1;

            // three dimensional array grid will hold grid points and function values
            double[,,] grid = new double[dimx, dimy, 5]; 

            
            for (int i = minx; i <= maxx; i++)
            {
                for (int j = miny; j <= maxy; j++)
                {
                    grid[i, j, 0] = minx + i;  // r coordinate
                    grid[i, j, 1] = miny + i;  // theta coodrinate

                    // Funct will calculate the effective gravity for a point
                    grid[i, j, 2] = FunctR(grid[i, j, 0], grid[i, j, 1]);  // f_r(r,theta)
                    grid[i, j, 3] = FunctTheta(grid[i, j, 0], grid[i, j, 1]);  // f_theta(r,theta)

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



            int k = FindMax(1, 2);
            Console.WriteLine(k);

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
        }

        private static double Potential(double r, double theta)
        {
            return (-1 * Globals.G * Globals.M1 * Globals.M2 ) / r;

            //throw new NotImplementedException();
        }

        private static double FunctR(double r, double theta)
        {
            throw new NotImplementedException();
        }

        private static double FunctTheta(double r, double theta)
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

    }
}


