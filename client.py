"""Conditional Branch Router & State Evaluator.
100% Python Standard Library.
"""

class ConditionalBranchRouter:
    """Evaluates branching predicates over agent workflow state."""
    @staticmethod
    def evaluate_predicate(predicate_expr: str, state: dict) -> bool:
        allowed_names = {k: v for k, v in state.items()}
        try:
            return bool(eval(predicate_expr, {"__builtins__": None}, allowed_names))
        except Exception:
            return False

    @staticmethod
    def route_next_node(current_node: str, routes: list, state: dict) -> str:
        for r in routes:
            pred = r.get("predicate", "default")
            if pred == "default" or ConditionalBranchRouter.evaluate_predicate(pred, state):
                return r["target"]
        return "END"
