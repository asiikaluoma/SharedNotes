```
CREATE TABLE account (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        username VARCHAR(144) NOT NULL, 
        password VARCHAR(144) NOT NULL, 
        PRIMARY KEY (id)
)
```

```
CREATE TABLE notebook (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        title VARCHAR(255) NOT NULL, 
        description VARCHAR(1000), 
        owner_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(owner_id) REFERENCES account (id)
)
```

```
CREATE TABLE "UserNotebook" (
        account_id INTEGER NOT NULL, 
        notebook_id INTEGER NOT NULL, 
        PRIMARY KEY (account_id, notebook_id), 
        FOREIGN KEY(account_id) REFERENCES account (id), 
        FOREIGN KEY(notebook_id) REFERENCES notebook (id)
)
```

```
CREATE TABLE note (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        title VARCHAR(144) NOT NULL, 
        body VARCHAR(1000) NOT NULL, 
        notebook_id INTEGER NOT NULL, 
        creator_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(notebook_id) REFERENCES notebook (id), 
        FOREIGN KEY(creator_id) REFERENCES account (id)
)
```