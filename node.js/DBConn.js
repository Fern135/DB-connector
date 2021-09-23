
class MySql {
    constructor(host, username, password, database) {
        this.host = host;
        this.username = username;
        this.password = password;
        this.database = database;
        this.mysql = require('mysql');
    }

    // init the connection
    init() {
        try {
            this.con = this.mysql.createConnection({
                host: this.host,
                user: this.username,
                password: this.password,
                database: this.database
            });
        } catch (error) {
            console.log(`${error}`);
        }
    }

    // connect to the db
    connect() {
        this.con.connect(function (err) {
            if (err) throw err;
            return ("Connected!");
        });
    }

    // run the sql query
    query(query) {
        this.con.query(query, function (err, result) {
            if (err) throw err;
            return result;
        });
    }

    // inserting many at once
    insert_many(table_name, rows = [], values = []) {
        var sql = `INSERT INTO ${table_name} (${rows}) VALUES ?`;
        // var values = [];

        this.con.query(sql, [values], function (err, result) {
            if (err) throw err;
            return (`Number of records inserted: ${result.affectedRows}`);
        });
    }

    // select all
    select_all(table_name) {
        this.con.query(`SELECT * FROM ${table_name}`, function (err, result, fields) {
            if (err) throw err;
            return result;
        });
    }

    // select from specific row and table
    specific_select(table_name, rows = []) {
        this.con.query(`SELECT (${rows}) FROM ${table_name}`, function (err, result, fields) {
            if (err) throw err;
            return result;
        });
    }

}

