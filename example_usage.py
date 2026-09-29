from client import ConditionalBranchRouter

state = {"confidence": 0.88, "error_count": 0}
routes = [
    {"predicate": "confidence > 0.85 and error_count == 0", "target": "auto_approve"},
    {"predicate": "default", "target": "manual_review"}
]
target = ConditionalBranchRouter.route_next_node("check", routes, state)
print("Selected Route Target:", target)
