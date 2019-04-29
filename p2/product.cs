using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp2.classes
{
    class product
    {
        public void addProduct(string name, double price, string category, string bn)
        {
            SqlConnection con = new SqlConnection(ConsoleApp2.Properties.Settings.Default.A3ConnectionString);
            DataClasses1DataContext db = new DataClasses1DataContext(con);

            Product p= new Product();
            p.name = name;
            p.price = price;
            p.category = category;
            var bi = from B in db.Brands where B.name==bn select (B.Id);
            p.Brand_ID = bi.First();
            db.Products.InsertOnSubmit(p);
            db.SubmitChanges();

        }

        public IEnumerable<object> showall ()
        {
            SqlConnection con = new SqlConnection(ConsoleApp2.Properties.Settings.Default.A3ConnectionString);
            DataClasses1DataContext db = new DataClasses1DataContext(con);

            var x = (from P in db.Products
                     join b in db.Brands on P.Brand_ID equals b.Id
                     where P.Brand_ID == b.Id
                     select new { Name = P.name, Price = P.price, Category = P.category, Brand = b.name }).ToList<object>();

            return x.ToList();

        }

        public IEnumerable<object> Sprice(double price)
        {
            SqlConnection con = new SqlConnection(ConsoleApp2.Properties.Settings.Default.A3ConnectionString);
            DataClasses1DataContext db = new DataClasses1DataContext(con);

            var x = (from P in db.Products
                     join b in db.Brands on P.Brand_ID equals b.Id
                     where( P.Brand_ID == b.Id && P.price<=price)
                     select new { Name = P.name, Price = P.price, Category = P.category, Brand = b.name }).ToList<object>();

            return x.ToList();

        }

        public IEnumerable<object> SortByPrice( int a)
        {
            SqlConnection con = new SqlConnection(ConsoleApp2.Properties.Settings.Default.A3ConnectionString);
            DataClasses1DataContext db = new DataClasses1DataContext(con);

            if (a==1)
            {
                var x = from p in db.Products orderby p.price ascending select p.name;
                return x.ToList();

            }

            else
            {
                var b = from p in db.Products orderby p.price descending select p.name;
                return b.ToList();

            }



        }

        public IEnumerable<object> SortByName(int a)
        {
            SqlConnection con = new SqlConnection(ConsoleApp2.Properties.Settings.Default.A3ConnectionString);
            DataClasses1DataContext db = new DataClasses1DataContext(con);

            if (a == 1)
            {
                var x = from p in db.Products orderby p.name ascending select  new { Name = p.name, Price = p.price, Category = p.category };
                return x.ToList();

            }
            else
            {
                var b = from p in db.Products orderby p.name descending select  new { Name = p.name, Price = p.price, Category = p.category };
                return b.ToList();

            }




        }
    }
}
