# genpark-conditional-branch-router-state-evaluator-skill

Dynamic condition routing engine evaluating boolean expressions against active agent state records.

## Architecture

```mermaid
flowchart TD
    State[Agent State Dict] --> Evaluator[Predicate Evaluator]
    Routes[Branching Candidate Routes] --> Evaluator
    Evaluator --> Decision{Matching Predicate}
    Decision -->|True| NextNode[Next Workflow Step]
    Decision -->|Fallback| DefaultNode[Default Path]
```

## Features
- **Sandbox Evaluation**: Zero access to built-in system functions.
- **Fallback Handling**: Graceful fallback to default routes.
