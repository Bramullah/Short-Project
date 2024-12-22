<?php
//koneksi ke database mysql 
$con = mysqli_connect("localhost","root","","test_akademik"); 

if(!$con){
    die('Connection Failed'. mysqli_connect_error());
}
?>