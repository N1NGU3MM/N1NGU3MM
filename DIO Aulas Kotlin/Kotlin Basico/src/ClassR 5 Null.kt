fun main() {

    var neverNull: String = "This can't be null"            // 1 Declares a non-null String variable.
    
    neverNull = null                                        // 2 When trying to assign null to non-nullable variable, a compilation error is produced.
    
    var nullable: String? = "You can keep a null here"      // 3 Declares a nullable String variable.
    
    nullable = null                                         // 4 Sets the null value to the nullable variable. This is OK.
    
    var inferredNonNull = "The compiler assumes non-null"   // 5 When inferring types, the compiler assumes non-null for variables that are initialized with a value.
    
    inferredNonNull = null                                  // 6 When trying to assign null to a variable with inferred type, a compilation error is produced.
    
    fun strLength(notNull: String): Int {                   // 7 Declares a function with a non-null string parameter.
        return notNull.length
    }
    
    strLength(neverNull)                                    // 8 Calls the function with a String (non-nullable) argument. This is OK.
    strLength(nullable)                                     // 9 When calling the function with a String? (nullable) argument, a compilation error is produced.

}