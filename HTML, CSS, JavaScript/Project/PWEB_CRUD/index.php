<?php
    session_start();
    require 'dbcon.php';
?>

<?php include('includes/header.php');?>
  
    <div class="container mt-4">

        <?php include('message.php'); ?>

        <div class="row">
            <div class="col-md-12">
                <div class="card">
                    <div class="card-header">
                        <h4>Student Details
                            <a href="student_create.php" class="btn btn-primary float-end">Add Student</a>
                        </h4>
                    </div>
                    <div class="card-body">

                        <table class="table table-bordered table-striped">
                            <thead>
                                <tr>
                                    <th>NPM</th>
                                    <th>Nama Mahasiswa</th>
                                    <th>Email</th>
                                    <th>Nomor Telepon</th>
                                    <th>Jurusan</th>
                                    <th>Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php 
                                    $query = "SELECT * FROM mahasiswa";
                                    $query_run = mysqli_query($con, $query);
                                    if(mysqli_num_rows($query_run) > 0)
                                    {
                                        foreach($query_run as $mhs)
                                        {
                                            ?>
                                            <tr>
                                                <td><?= $mhs['npm']; ?></td>
                                                <td><?= $mhs['nama']; ?></td>
                                                <td><?= $mhs['email']; ?></td>
                                                <td><?= $mhs['notelp']; ?></td>
                                                <td><?= $mhs['jurusan']; ?></td>
                                                <td>
                                                    <a href="student_view.php?npm=<?=$mhs['npm']; ?>" class="btn btn-info btn-sm">View</a> <!-- method get -->
                                                    <a href="student_edit.php?npm=<?=$mhs['npm']; ?>" class="btn btn-success btn-sm">Edit</a> <!-- method get -->
                                                    <form action="code.php" method="POST" class="d-inline">
                                                        <button type="submit" name="delete_student" value="<?=$mhs['npm'];?>" class="btn btn-danger btn-sm">Delete</button>
                                                    </form>
                                                </td>
                                            </tr>
                                            <?php
                                        }
                                    }
                                    else
                                    {
                                        echo "<h5> No Record Found </h5>";
                                    }
                                ?>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
<?php include('includes/footer.php');?>