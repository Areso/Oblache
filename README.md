# Oblache
This is public tracker for my Oblache project.  
Here would be REST API description, tests and so on.

## DB States
All the states:  
```
    # 0 db_creating          - EXCEPTION                        - OK
    # 1 db_created           -   NORMAL FLOW                    - OK
    # 2 error                -     COVERED with manual deletion - OK
    # 3 deleting             - EXCEPTION                        - OK
    # 4 deleted              -FILTERED OUT O on previous step   - OK
    # 5 read_only_threshold  -   NORMAL FLOW                    - OK
    # 6 error_creating       -     COVERED with manual deletion - OK
    # 7 error_deleting       - EXCEPTION                        - OK
    # 8 error_ro_threshold   - EXCEPTION?--???
    # 9 manual_deleting      - EXCEPTION?---??/
```

Current version (0.25) state machine (PlantUML) of the databases:  
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
