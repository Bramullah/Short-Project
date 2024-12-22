<?php
session_start();
require 'dbcon.php';

if(isset($_POST['delete_student']))
{
    $mhs_npm = mysqli_real_escape_string($con, $_POST['delete_student']);

    $query = "DELETE FROM mahasiswa WHERE npm='$mhs_npm' ";
    $query_run = mysqli_query($con, $query);

    if($query_run)
    {
        $_SESSION['message'] = "Student Deleted Successfully";
        header("Location: index.php");
        exit(0);
    }
    else
    {
        $_SESSION['message'] = "Student Not Deleted";
        header("Location: index.php");
        exit(0);
    }
}

if(isset($_POST['update_student']))
{
    $mhs_npm = mysqli_real_escape_string($con, $_POST['mhs_npm']);

    $npm = mysqli_real_escape_string($con, $_POST['npm']);
    $nama = mysqli_real_escape_string($con, $_POST['nama']);
    $email = mysqli_real_escape_string($con, $_POST['email']);
    $notelp = mysqli_real_escape_string($con, $_POST['notelp']);
    $jurusan = mysqli_real_escape_string($con, $_POST['jurusan']);

    $query = "UPDATE mahasiswa SET npm =$npm, nama='$nama', email='$email', notelp='$notelp', jurusan='$jurusan' WHERE npm='$mhs_npm'";
    $query_run = mysqli_query($con, $query);

    if($query_run)
    {
        $_SESSION['message'] = "Student Updated Successfully";
        header("Location: index.php");
        exit(0);
    }
    else
    {
        $_SESSION['message'] = "Student Not Updated";
        header("Location: index.php");
        exit(0);
    }

}


if(isset($_POST['save_student']))
{
    $npm = mysqli_real_escape_string($con, $_POST['npm']);
    $nama = mysqli_real_escape_string($con, $_POST['nama']);
    $email = mysqli_real_escape_string($con, $_POST['email']);
    $notelp = mysqli_real_escape_string($con, $_POST['notelp']);
    $jurusan = mysqli_real_escape_string($con, $_POST['jurusan']);

    $query = "INSERT INTO mahasiswa VALUES ($npm,'$nama','$email','$notelp','$jurusan')";

    $query_run = mysqli_query($con, $query);
    if($query_run)
    {
        $_SESSION['message'] = "Student Created Successfully";
        header("Location: student_create.php");
        exit(0);
    }
    else
    {
        $_SESSION['message'] = "Student Not Created";
        header("Location: student_create.php");
        exit(0);
    }
}

?>