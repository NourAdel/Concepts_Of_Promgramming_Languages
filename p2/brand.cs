using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;
using System.Collections;


namespace ConsoleApp2.classes
{
    class brand
    {
        public void addBrand(string name)
        {
            SqlConnection con = new SqlConnection(ConsoleApp2.Properties.Settings.Default.A3ConnectionString);
            DataClasses1DataContext db = new DataClasses1DataContext(con);

            Brand b = new Brand();
            b.name = name;
            db.Brands.InsertOnSubmit(b);
            db.SubmitChanges();

        }

        public IEnumerable<object> showallb()
        {
            SqlConnection con = new SqlConnection(ConsoleApp2.Properties.Settings.Default.A3ConnectionString);
            DataClasses1DataContext db = new DataClasses1DataContext(con);

            var x = from p in db.Brands select p.name;
            return x.ToList();

        }

        public void brandsSorted()
        {
            SqlConnection con = new SqlConnection(ConsoleApp2.Properties.Settings.Default.A3ConnectionString);
            DataClasses1DataContext db = new DataClasses1DataContext(con);
            ArrayList a = new ArrayList();
            var x = from p in db.Products group p by p.Brand_ID into grouping select new { grouping.Key, m = from p2 in grouping select p2.name };
            int[] keys = new int[x.Count()];
            int[] counts = new int[x.Count()];
            int l = 0;
            foreach (var G in x)
            {
                keys[l] = G.Key;
                counts[l] = G.m.Count();
                l++;
          
            }
            

            
            for (int i = 0; i < x.Count(); i++)
            {
                for (int j = i + 1; j < x.Count(); j++)
                {
                    if (counts[j] < counts[i])
                    {
                        var tmp = counts[i];
                        counts[i] = counts[j];
                        counts[j] = tmp;

                        var tmp1 = keys[i];
                        keys[i] = keys[j];
                        keys[j] = tmp1;
                    }
                }
            }
            int t = 0;
            foreach (int j in keys)
            {
                var tn = from b in db.Brands where b.Id == j select b.name;
                Console.Write(tn.First());
                Console.Write("  :  ");
                Console.Write(counts[t]);
                Console.Write(" product/s");
                Console.Write("\n");
                t++;



            }
        }
    }
}
