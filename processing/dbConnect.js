const mysql = require('mysql2/promise');
const { MongoClient } = require("mongodb");

// Establish connection to mysql database
const sqlConnection = mysql.createPool({
    host: 'mysql_db',
    user: 'root',
    password: 'zxcvbnm',
    database: 'db_grade',
    port: 3306,
    waitForConnections: true,
    connectionLimit: 10,
    maxIdle: 10,
    idleTimeout: 60000,
    queueLimit: 0
});

// Establish connection to mongodb database
const username = "root"
const password = "zxcvbnm"
const host = "mongo_db"
const port = 27017

const mongoURI = `mongodb://${username}:${password}@${host}:${port}`;

const mongoClient = new MongoClient(mongoURI);

exports.sqlConnection = sqlConnection;
exports.client = mongoClient;