<?php

class MySQL
{
    private $conn;
    private $server_name;
    private $user_name;
    private $pass_word;
    private $database;

    public function __construct($server_name, $user_name, $pass_word, $database)
    {
        $this->servername = $server_name;
        $this->username   = $user_name;
        $this->password   = $pass_word;
        $this->database   = $database;

        // Create connection
        $this->conn = mysqli_connect($this->servername, $this->username, $this->password, $this->database);

        try {
            // Check connection
            if (!$this->conn) {
                die("Connection failed: " . mysqli_connect_error());
            }
            echo "Connected successfully";
        } catch (Exception $e) {
            return json_encode(
                array(
                    "Server" => $e
                )
            );
        }
    }

    function __destruct(){ // when the object is done being used
        mysqli_close($this->conn);
    }

    public function query($sql)
    {
        /*
            use this for the prepared statements
            i - integer
            d - double
            s - string
            b - BLOB
        */
        try {
            $data = mysqli_real_escape_string($this->conn, $sql);

            mysqli_query($this->conn, $data);
        } catch (Exception $e) {
            echo ($e);
        }
    }
}
