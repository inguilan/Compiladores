// Generated from MiGramatica.g4 by ANTLR 4.9.3
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MiGramaticaParser}.
 */
public interface MiGramaticaListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MiGramaticaParser#query}.
	 * @param ctx the parse tree
	 */
	void enterQuery(MiGramaticaParser.QueryContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiGramaticaParser#query}.
	 * @param ctx the parse tree
	 */
	void exitQuery(MiGramaticaParser.QueryContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiGramaticaParser#column_list}.
	 * @param ctx the parse tree
	 */
	void enterColumn_list(MiGramaticaParser.Column_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiGramaticaParser#column_list}.
	 * @param ctx the parse tree
	 */
	void exitColumn_list(MiGramaticaParser.Column_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiGramaticaParser#column}.
	 * @param ctx the parse tree
	 */
	void enterColumn(MiGramaticaParser.ColumnContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiGramaticaParser#column}.
	 * @param ctx the parse tree
	 */
	void exitColumn(MiGramaticaParser.ColumnContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiGramaticaParser#table}.
	 * @param ctx the parse tree
	 */
	void enterTable(MiGramaticaParser.TableContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiGramaticaParser#table}.
	 * @param ctx the parse tree
	 */
	void exitTable(MiGramaticaParser.TableContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiGramaticaParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(MiGramaticaParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiGramaticaParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(MiGramaticaParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiGramaticaParser#operator}.
	 * @param ctx the parse tree
	 */
	void enterOperator(MiGramaticaParser.OperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiGramaticaParser#operator}.
	 * @param ctx the parse tree
	 */
	void exitOperator(MiGramaticaParser.OperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiGramaticaParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(MiGramaticaParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiGramaticaParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(MiGramaticaParser.ValueContext ctx);
}