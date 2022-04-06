// simpl programming language

var line = ""
var programm : Seq[String] = Seq()
var write = true
var str = "string"
var int = 0
while (write) {
    line = readln("write programming")
    if (line == "// stop") {
        write = false
    }
    programm = programm :+ line
    println(line)
}

println("=====----- -----=====")

for (lp <- programm) {
    // print
    if (lp == "print (int)") println("printed : " + int)
    if (lp == "print (str)") println("printed : " + str)
    // input
    if (lp == "str = input()") str = readln("str input")
    if (lp == "int = input()") int = readInt("int input")
    // turtul control
    
}
