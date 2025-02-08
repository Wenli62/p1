const mysql = require('mysql2/promise');
const mongoose = require('mongoose')

// Establish connection to mysql database
const sqlConnection = mysql.createPool({
    host: 'localhost',
    user: 'root',
    password: 'zxcvbnm',
    database: 'db_vote',
    port: 3311,
    waitForConnections: true,
    connectionLimit: 10,
    maxIdle: 10,
    idleTimeout: 60000,
    queueLimit: 0
});

// Establish connection to mongodb database

mongoose.set("strictQuery", false);

const username = "db_user"
const password = "zxcvbnm"
const host = "localhost"
const port = 12345
const database = "db_vote"

export const mongoConnection = async () => {
    await mongoose.connect(`mongodb://${username}:${password}@${host}:${port}}/${database}`)
};

exports.connection = sqlConnection;