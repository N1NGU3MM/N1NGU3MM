
// Desafio
// Durante o desenvolvimento de um jogo, você precisa verificar se a conversa com um dos personagens vai caber no balão desenvolvido pelo artista.
// Para isso,você resolveu desenvolver um programa vai ler cada caractere das frases,
// incluindo pontuação e espaços, e verificar se elas possuem 45 ou menos caracteres.



using System;
                    
public class Programas
{
    public static void Main()
    {
      Console.WriteLine("");
      string fraseDeEntrada = Console.ReadLine();
        
      if ( fraseDeEntrada.Length <= 45)
      {
        Console.WriteLine("Suficiente");
      }
        
      else
      {
        Console.WriteLine("Nao suficiente");
      }
        //TODO: crie a condição necessaria, utilizando if - else, para resolver o problema;
    }
}