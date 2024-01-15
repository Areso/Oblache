# Oblache
This is public tracker for my Oblache project.  
Here would be REST API description, tests and so on.

## DB States
Current version (0.24) state machine (PlantUML) of the databases:  
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

Visualize:
![image](https://www.plantuml.com/plantuml/png/ZSun3i8m38NXdLDOsIls3XtP40C7g4pyX2952NBR-nDCBDHER8d-JxR3MHvpLF2AC4psIEL98zrKeCGnuhL2JbwwWJHotrfTbcDBjSnGhTh8XLF-TiWm2J8-S2HRQry4gljLhjpxk3xja26_G_Q-0plrocNZJ0xifB_a6m00)

## PROJECT TESTS

For Project tests documentation please [Readme for Tests](./README_TESTS.md)
