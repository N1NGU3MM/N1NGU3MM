class MutableStack<E>(vararg items: E) {              // 1 using <E> is tipper a parameter and creating a list  

    private val elements = items.toMutableList()
  
    fun push(element: E) = elements.add(element)        // 2
  
    fun peek(): E = elements.last()                     // 3 [peek] using for to take last of list 
  
    fun pop(): E = elements.removeAt(elements.size - 1)
  
    fun isEmpty() = elements.isEmpty()                 // 4 [isEmpety] using for verification it's empty
  
    fun size() = elements.size                        // 5 
  
    override fun toString() = "MutableStack(${elements.joinToString()})"
  }
  
  
  fun main() {
    val stack = MutableStack(0.62, 3.14, 2.7)
    stack.push(9.87)
    println(stack)
  
    println("peek(): ${stack.peek()}")
    println(stack)
  
    for (i in 1..stack.size()) {
      println("pop(): ${stack.pop()}")
      println(stack)
    }
  }




  // fun generic
  fun <E> mutableStackOf(vararg elements: E) = MutableStack(*elements)

fun main() {
  val stack = mutableStackOf(0.62, 3.14, 2.7)
  println(stack)
} //