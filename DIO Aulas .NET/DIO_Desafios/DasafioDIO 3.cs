// Desafio
// Você e sua equipe estão finalizando um jogo. Porém, ele está muito pesado e você sabem que é devido a grande parte dos Assets
// (recursos que compõem o jogo) não utilizados mas que ainda estão na pasta.
// O artista disse que nomeou tudo que estava sendo usado como “_usado”,
// portanto, você pensou em criar um programa que encontrasse e deletasse todos os arquivos que não tivessem esse sufixo.





using System;
                    
public class Programs
{
    public static void Main()
    {
      
      string fraseAVerifica = "_usado";

      Console.WriteLine("");
      string fraseDeEntrada = Console.ReadLine();

      if (fraseDeEntrada.Contains(fraseAVerifica, StringComparison.OrdinalIgnoreCase))
      {
        Console.WriteLine("Contem, mantido");
      }
      else 
      {
        Console.WriteLine("Nao contem, deletado");
      }
        //TODO: crie a condição necessaria, utilizando if - else, para resolver o problema;
    }
}