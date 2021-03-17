<?php
    
    $mysqli= new $mysqli("localhost", "root", "", "shoe_recycling");

    //check connection

    if ($mysqli->connect_errno){
        echo "Connection MYSQLi error" . $mysqli->connect_error;
        exit();
    }
    
?>