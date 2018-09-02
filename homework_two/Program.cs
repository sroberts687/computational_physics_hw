using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace homework_two
{
    class Program
    {

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

        static void Main(string[] args)
        {

            Console.WriteLine("Homework two, Sarah Roberts.");

            int minx = -100;
            int maxx = 100;
            int dimx = minx - maxx + 1;
            int miny = -200;
            int maxy = 200;
            int dimy = miny - maxy + 1;

            // three dimensional array grid will hold grid points and function values
            double[,,] grid = new double[dimx, dimy, 4]; 

            
            for (int i = minx; i <= maxx; i++)
            {
                for (int j = miny; j <= maxy; j++)
                {
                    grid[i, j, 0] = minx + i;  // x coordinate
                    grid[i, j, 1] = miny + i;  // y coodrinate

                    grid[i, j, 2] = functx(grid[i, j, 0], grid[i, j, 1]);  // f_x(x,y)
                    grid[i, j, 3] = functy(grid[i, j, 0], grid[i, j, 1]);  // f_y(x,y)

                }
            }

             


            int k = FindMax(1, 2);
            Console.WriteLine(k);

            // keep window open
            Console.WriteLine("\n Press any key to exit.");
            Console.ReadKey();

        }

        private static double functy(double x, double y)
        {
            throw new NotImplementedException();
        }

        private static double functx(double x, double y)
        {
            throw new NotImplementedException();
        }

        private static double funct(double v1, double v2)
        {
            throw new NotImplementedException();
        }
    }
}


