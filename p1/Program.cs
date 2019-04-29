using System;
public class Exercise11
{
    public static void Main()
    {
        


        
       int n = Convert.ToInt32(Console.ReadLine());
        int[] arr1 = new int[n];
        int  i, j, tmp;
        
        for (i = 0; i < n; i++)
        {
            arr1[i] = Convert.ToInt32(Console.ReadLine());
        }
        
        int k = Convert.ToInt32(Console.ReadLine());
       if (k>n)
            { Console.Write("invalid index!");
            Console.Write("\n\n");
        }
       else
        {
            for (i = 0; i < n; i++)
            {
                for (j = i + 1; j < n; j++)
                {
                    if (arr1[j] < arr1[i])
                    {
                        tmp = arr1[i];
                        arr1[i] = arr1[j];
                        arr1[j] = tmp;
                    }
                }
            }

            Console.Write(arr1[n - k]);
            Console.Write("\n\n");
        }
        
    }

}