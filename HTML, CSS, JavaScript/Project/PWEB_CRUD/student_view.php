<?php
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

    <title>Student View</title>
</head>
<body>

    <div class="container mt-5">

        <div class="row">
            <div class="col-md-12">
                <div class="card">
                    <div class="card-header">
                        <h4>Student View Details 
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

                                    <div class="mb-3">
                                        <label>NPM</label>
                                        <p class="form-control">
                                            <?=$mhs['npm'];?>
                                        </p>
                                    <div class="mb-3">
                                        <label>Nama Mahasiswa</label>
                                        <p class="form-control">
                                            <?=$mhs['nama'];?>
                                        </p>
                                    </div>
                                    <div class="mb-3">
                                        <label>Email</label>
                                        <p class="form-control">
                                            <?=$mhs['email'];?>
                                        </p>
                                    </div>
                                    <div class="mb-3">
                                        <label>Nomor Telepon</label>
                                        <p class="form-control">
                                            <?=$mhs['notelp'];?>
                                        </p>
                                    </div>
                                    <div class="mb-3">
                                        <label>Jurusan</label>
                                        <p class="form-control">
                                            <?=$mhs['jurusan'];?>
                                        </p>
                                    </div>

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