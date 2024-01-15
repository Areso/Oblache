# Oblache
This is public tracker for my Oblache project.  
Here would be REST API description, tests and so on.

## DB States
Current version (0.24) state machine (PlantUML) of the databases:  
```
"/db_create"->creating : Order accepted
creating->"/db_create" : db_uuid
creating->created : Success
creating->creation_error : Fail
created->deleting: "/db_delete" order accepted
deleting->deletion_error: Fail
deleting->deleted: Success
deletion_error->deleted : Manual deletion
creation_error->deleted : Manual deletion
```

Visualize:
![image](https://www.plantuml.com/plantuml/png/ZOun3i8m34NtdiBg7h5toCY663X0PM8BHOeIv3RtnoGOsavijjxxzXzFT9-3CAuyEj-6c1ymmLM81J04VgvCWn7djmdrTAarReNEIDcjQdnPZYoMFBD84LNE6DFmIJXFdFWjJj2-j5M_b7qNiyotS_tQ4JFzYkpzhw0zBfWh9Z2XL_h7V040)

## PROJECT TESTS

For Project tests documentation please [Readme for Tests](./README_TESTS.md)
