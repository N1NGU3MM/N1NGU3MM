
//  Desafio
//  O programador Jr. recém contratado para o seu time já está s
//  uper empolgado e envolvido em um projeto. O que ele precisa fazer é verificar se o jogador 
//  que caiu em uma armadilha levou um dano. Porém, ele não sabe muito bem como fazer 
//  isso e pediu a sua ajuda. Você como um bom líder, foi ao socorro para ensina-lo.


using System;


public class Program
{
    public static void Main()
    {

        int dano = int.Parse(Console.ReadLine());
        
        if (dano >= 1){
          Console.WriteLine("Game over");
          

        } 
        else 
        {
          Console.WriteLine("Jogador continua a jogar");
          
 
        }
    }
}