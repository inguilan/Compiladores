antlr4 Expr.g4
antlr4 -Dlanguage=Python3 Expr.g4
javac -cp ".:$ANTLR_JAR" Expr*.java
echo "3+5" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig Expr root -tokens
echo "5+10" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig Expr root -tree
antlr4 -Dlanguage=Python3 -no-listener -visitor Expr.g4 (visitor)