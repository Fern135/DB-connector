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
                    "server" => $e
                )
            );
        }
    }

    public function query($sql)
    {
        try {
            mysqli_query($this->conn, $sql);
            mysqli_close($this->conn);
        } catch (Exception $e) {
            echo ($e);
        }
    }
}
