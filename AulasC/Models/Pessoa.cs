using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace AulasC.Models
{
    public class Pessoa
    {
        public string Name { get; set; }
        public int Age { get; set; }


        public void Present()
        {
            Console.WriteLine($"Hello, my name is {Name}, I have {Age} ages.");
        }
    }
}