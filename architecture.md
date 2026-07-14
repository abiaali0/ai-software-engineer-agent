# Architecture Notes

Use this document to describe the real architecture after recovering the project.

## Components

1. Issue ingestion
2. Repository context retrieval
3. Agent or prompt workflow
4. Code-change generation
5. Isolated Docker test execution
6. Error analysis and repair
7. Pull-request summary generation
8. API layer
9. User interface

## Design Decisions

Document:

- Why each framework was selected
- How repository context was retrieved
- How prompts were structured
- How generated code was validated
- How Docker isolation worked
- How failures were handled
- What the system could not reliably do
