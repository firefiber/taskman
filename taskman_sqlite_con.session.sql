-- CREATE TABLES --

-- Users table
-- @block:
CREATE TABLE Users(
    id BLOB PRIMARY KEY DEFAULT(lower(hex(randomblob(16)))),
    username TEXT,
    email TEXT UNIQUE,
    password TEXT,
    join_date TEXT DEFAULT CURRENT_TIMESTAMP,
    is_activated BOOLEAN DEFAULT 0
);

-- Tasks table
-- @block:
CREATE TABLE Tasks(
    id BLOB PRIMARY KEY DEFAULT(lower(hex(randomblob(16)))),
    name TEXT,
    description TEXT,
    done BOOLEAN DEFAULT 0,
    owner_id TEXT,
    entry_date TEXT DEFAULT CURRENT_TIMESTAMP,
    start_date TEXT,
    end_date TEXT,
    total_duration REAL,
    FOREIGN KEY(owner_id) REFERENCES Users(id)
);

-- Sessions table
-- @block:
CREATE TABLE Sessions(
    id BLOB PRIMARY KEY DEFAULT(lower(hex(randomblob(16)))),
    task_id TEXT,
    start_time TEXT DEFAULT CURRENT_TIMESTAMP,
    end_time TEXT, 
    duration REAL,
    was_manually_stopped BOOLEAN DEFAULT 0,
    FOREIGN KEY(task_id) REFERENCES Tasks(id)
);

-- Blocks table
-- @block:
CREATE TABLE Blocks(
    id BLOB PRIMARY KEY DEFAULT(lower(hex(randomblob(16)))),
    task_id TEXT,
    size TEXT,
    basis TEXT,
    FOREIGN KEY(task_id) REFERENCES Tasks(id)
);

-- Dependencies table
-- @block:
CREATE TABLE Dependencies(
    task_id TEXT,
    depends_on_id TEXT,
    PRIMARY KEY(task_id, depends_on_id),
    FOREIGN KEY(task_id) REFERENCES Tasks(id),
    FOREIGN KEY(depends_on_id) REFERENCES Tasks(id)
);

-- Assignments table
-- @block:
CREATE TABLE Assignments(
    task_id TEXT,
    assigned_to_id TEXT,
    assigned_by_id TEXT,
    assigned_on_date TEXT DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(task_id, assigned_to_id),
    FOREIGN KEY(task_id) REFERENCES Tasks(id),
    FOREIGN KEY(assigned_to_id) REFERENCES Users(id),
    FOREIGN KEY(assigned_by_id) REFERENCES Users(id)
);


-- DROP TABLES --
-- @block:
DROP TABLE Users;

-- @block:
DROP TABLE Tasks;

-- @block:
DROP TABLE Sessions;

-- @block:
DROP TABLE Blocks;

-- @block:
DROP TABLE Dependencies;

-- @block:
DROP TABLE Assignments;

-- INSERT DATA --

-- @block:
INSERT INTO Users(username) VALUES('test_user');

-- @block:
SELECT * FROM Users;