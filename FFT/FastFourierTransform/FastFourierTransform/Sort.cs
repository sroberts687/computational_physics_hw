using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FastFourierTransform
{
    class Sort
    {
         static void Main(string[] args)
        {
            Console.Out.WriteLine("Hello World!");

            int[] b = { 5, 6, 34, 2, 0 };
             Console.Out.WriteLine(string.Join(",", b), "\n");
            selectSort(b);
             Console.Out.WriteLine(string.Join(",", b), "\n");

             Console.In.ReadLine();
        }

        static void selectSort(int[] a)
         {  
            for(int bottom = a.Length -1; bottom >= 1; bottom--)
            {
                int largestInd = 0;
                //search for largest
                for(int i = 0; i <= bottom; i++)
                {
                    if(a[i] > a[largestInd])
                    {
                        largestInd = i;
                    }
                }

                //swap values
                int temp = a[bottom];
                a[bottom] = a[largestInd];
                a[largestInd] = temp;
            }
            
         }
    }
}
