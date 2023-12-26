# Oblache
This is public tracker for my Oblache project.  
Here would be REST API description, tests and so on.

## DB States
Current (0.24v) state machine (PlantUML) of the databases:  
```
"/db_create"->creating : Order accepted
creating->created : Success
creating->creation_error : Fail
created->deleting: "/db_delete" order accepted
deleting->deletion_error: Fail
deleting->deleted: Success
deletion_error->deleted : Manual deletion
creation_error->deleted : Manual deletion
```

To visualize https://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000