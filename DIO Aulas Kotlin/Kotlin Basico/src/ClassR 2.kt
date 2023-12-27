fun printMessager(message: String): Unit {  // 1. It's an function using for call println
    println(message)  // 2. Remember [fun] is usingo for determined a function 
}

<<<<<<< HEAD
fun printMessagerWithPrefix(message: String, prefix: String = "info"){ // 3. If not seted an prefix, the prefix is [info] 
=======
fun printMessagerWinthPrefix(message: String, prefix: String = "info"){ // 3. If not seted an prefix, the prefix is [info] 
>>>>>>> 8731789f5577687a5e68cc0d44efac0a1eb753ee
    println("[$prefix] $message")
}

fun sum(x: Int, y: Int): Int { // 4. Is a function of math [sum]
    return x + y
}


fun multiply(x: Int, y: Int) = x * y // 5. It's a forme of using a function a an unique line


fun main(){                                            // 6. 
    printMessager("Hello")                            // 7.
    printMessagerWithPrefix("Hello", "Log")           // 8.
<<<<<<< HEAD
    printMessagerWithPrefix(message = ("Hello"))       // 9.
    printMessagerWithPrefix(prefix = "Log", message = "Hello" )  // 10. 
    println(sum(1, 2)) 
    println(multiply(2, 4))  
}
=======
    printlnMessageWithPrefix(prefix = ("Hello"))       // 9.
    printlnMessageWithPrefix(prefix = "Log", message = "Hello")  // 10. 
    println(sum(1, 2)) 
    println(multiply(2, 4))    
}  
>>>>>>> 8731789f5577687a5e68cc0d44efac0a1eb753ee
