# schema for Phase 2
# CS 480, Fall 2025

# group name: popeyes
# Logan Lucas - lluca5
# Jonathan Kang - jkang87
# Henry Chen - hchen250

CREATE TABLE "User" (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    role VARCHAR(7) NOT NULL CHECK(role IN ('EndUser', 'Admin', 'Curator')),
    username VARCHAR(20) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    last_activity_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "Document" (
    document_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    type VARCHAR(50),
    source VARCHAR(50),
    added_by INT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    has_been_processed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (added_by) REFERENCES "User"(id)
);

CREATE TABLE "QueryLog" (
    query_id SERIAL PRIMARY KEY,
    id INT NOT NULL,
    text VARCHAR(255) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id) REFERENCES "User"(id)
);

CREATE TABLE "QueryLogDocument" (
    query_id INT,
    document_id INT,
    PRIMARY KEY (query_id, document_id),
    FOREIGN KEY (query_id) REFERENCES "QueryLog"(query_id),
    FOREIGN KEY (document_id) REFERENCES "Document"(document_id)
);