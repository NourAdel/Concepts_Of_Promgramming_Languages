using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;
using ConsoleApp2.classes;

namespace ConsoleApp2
{
    class Program


    {


        static void Main(string[] args)
        {
           
          

             while(true)

             {
                 Console.Write("1) Show Products");
                 Console.Write("\n");
                 Console.Write("2) Add Products");
                 Console.Write("\n");
                 Console.Write("3) Show Products with price less than...");
                 Console.Write("\n");
                 Console.Write("4) Show Brands");
                 Console.Write("\n");
                 Console.Write("5) Show Products in specific order");
                 Console.Write("\n");
                 Console.Write("6) Exit");
                 Console.Write("\n");

                 int programOption = Convert.ToInt32(Console.ReadLine());
                 if (programOption == 1)
                 {
                     product x = new product();
                     var xx = x.showall();
                     foreach (var y in xx)
                     {
                         Console.Write(y);
                         Console.Write("\n");


                     }
                 }

                 else if (programOption == 2)
                 {
                     Console.Write("how many Products do you want to add?");
                     int pn = Convert.ToInt32(Console.ReadLine());
                     for (int i = 0; i < pn; i++)
                     {
                         Console.Write("Enter the Product name: ");
                         string name = Console.ReadLine();
                         Console.Write("Enter the Product Price: ");
                         double Price = Convert.ToDouble(Console.ReadLine());
                         Console.Write("Enter the Product category: ");
                         string cat = Console.ReadLine();
                         Console.Write("Enter the product's Brand name: ");
                         string bn = Console.ReadLine();
                         brand b = new brand();
                         var allbrands = b.showallb();
                         foreach (var l in allbrands)
                         {
                             Console.Write(l);
                             Console.Write("\n");
                         }
                         int g=0 ;
                         foreach (var f in allbrands)
                         {
                             if (f.ToString() == bn)
                             { g = 1; }
                         }

                         if (g == 0)
                         {
                             Console.Write("This brand does not exist, type '1' to add it or '2' to discard the product.");
                             int o = Convert.ToInt32(Console.ReadLine());
                             if (o == 1)
                             {
                                 b.addBrand(bn);
                                 product k = new product();
                                 k.addProduct(name, Price, cat, bn);
                                 continue;
                             }

                             else if (o == 2)
                             { continue; }
                         }

                         product p = new product();
                         p.addProduct(name, Price, cat, bn);


                     }
                 }

                 else if (programOption == 3)
                 {
                     Console.Write("Enter the price boundry: ");
                     double pp = Convert.ToDouble(Console.ReadLine());
                     product p = new product();
                     var sp = p.Sprice(pp);
                     foreach (var e in sp)
                     {
                         Console.Write(e);
                         Console.Write("\n");
                     }
                 }

                 else if (programOption==4)
                {

                    brand b = new brand();
                    b.brandsSorted();
                }

                 else if (programOption == 5)
                 {
                     Console.Write(" '1' : By Name      '2' :By Price");
                     Console.Write("\n");
                     int n = Convert.ToInt32(Console.ReadLine());
                     Console.Write(" '1' : asending order      '2' : descnding order");
                     Console.Write("\n");
                     int a = Convert.ToInt32(Console.ReadLine());
                     product p = new product();
                     if (n == 1)
                     {
                        var h= p.SortByName(a);
                        foreach (var t in h)
                         {
                             Console.Write(t);
                             Console.Write("\n");
                         }
                     }
                     else if (n == 2)
                     {
                         var q=p.SortByPrice(a);
                         foreach (var t in q)
                         {
                             Console.Write(t);
                             Console.Write("\n");
                         }
                     }

                 }

                 else if (programOption==6)
                 {
                     break;
                 }





             }
         }
        }


    }
