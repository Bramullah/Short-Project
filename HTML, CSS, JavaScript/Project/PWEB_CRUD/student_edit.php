<?php
session_start();
require 'dbcon.php';
?>

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">

    <title>Student Edit</title>
</head>
<body>
  
    <div class="container mt-5">

        <?php include('message.php'); ?>

        <div class="row">
            <div class="col-md-12">
                <div class="card">
                    <div class="card-header">
                        <h4>Student Edit 
                            <a href="index.php" class="btn btn-danger float-end">BACK</a>
                        </h4>
                    </div>
                    <div class="card-body">

                        <?php
                        if(isset($_GET['npm']))
                        {
                            $mhs_npm = mysqli_real_escape_string($con, $_GET['npm']);
                            $query = "SELECT * FROM mahasiswa WHERE npm='$mhs_npm' ";
                            $query_run = mysqli_query($con, $query);

                            if(mysqli_num_rows($query_run) > 0)
                            {
                                $mhs = mysqli_fetch_array($query_run);
                                ?>
                                <form action="code.php" method="POST">
                                <input type="hidden" name="mhs_npm" value="<?= $mhs['npm']; ?>">
                                    <div class="mb-3">
                                        <label>NPM</label>
                                        <input type="number" name="npm" value="<?=$mhs['npm'];?>" class="form-control">
                                    </div>
                                    <div class="mb-3">
                                        <label>Nama Mahasiswa</label>
                                        <input type="text" name="nama" value="<?=$mhs['nama'];?>" class="form-control">
                                    </div>
                                    <div class="mb-3">
                                        <label>Email</label>
                                        <input type="email" name="email" value="<?=$mhs['email'];?>" class="form-control">
                                    </div>
                                    <div class="mb-3">
                                        <label>Nomor Telepon</label>
                                        <input type="text" name="notelp" value="<?=$mhs['notelp'];?>" class="form-control">
                                    </div>
                                    <div class="mb-3">
                                        <label>Jurusan</label>
                                        <input type="text" name="jurusan" value="<?=$mhs['jurusan'];?>" class="form-control">
                                    </div>
                                    <div class="mb-3">
                                        <button type="submit" name="update_student" class="btn btn-primary">
                                            Update Student
                                        </button>
                                    </div>

                                </form>
                                <?php
                            }
                            else
                            {
                                echo "<h4>No Such NPM Found</h4>";
                            }
                        }
                        ?>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>