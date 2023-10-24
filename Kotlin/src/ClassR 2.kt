fun printMessager(message: String): Unit {  // 1. It's an function using for call println
    println(message)  // 2. Remember [fun] is usingo for determined a function 
}

fun printMessagerWithPrefix(message: String, prefix: String = "info"){ // 3. If not seted an prefiz, the prefix is [info] 
    println("[$prefix] $message")
}

fun sum(x: Int, y: Int): Int { // 4. Is a function of math [sum]
    return x + y
}

fun multiply(x: Int, y: Int) = x * y // 5. It's a forme of using a function a an unique line

fun main(){                                            // 6. 
    printMessager("Hello")                            // 7.
    printMessagerWithPrefix("Hello", "Log")           // 8.
    printMessagerWithPrefix(mesage = ("Hello")       // 9.
    printMessagerWithPrefix(prefix = "Log", message = "Hello" )  // 10. 
    println(sum(1, 2)) 
    println(multiply(2, 4))  
    