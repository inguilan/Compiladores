echo "SELECT * FROM personas WHERE id>=1;" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig MiGramatica query -tokens
echo "SELECT * FROM personas WHERE id>=1;" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig MiGramatica query -tree
javac -cp ".:$ANTLR_JAR" MiGramatica*.java