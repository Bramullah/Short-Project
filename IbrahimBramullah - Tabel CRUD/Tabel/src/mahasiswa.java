import net.proteanit.sql.DbUtils;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.*;

public class mahasiswa {
    private JPanel Main;
    private JTextField txtid;
    private JTextField txtNama;
    private JTextField txtNPM;
    private JTextField txtTgl_lahir;
    private JTextField txtKelas;
    private JTextField txtNilai;
    private JButton createButton;
    private JTable table1;
    private JButton updateButton;
    private JButton readButton;
    private JButton deleteButton;
    private JTextField txtfield;

    public static void main(String[] args) {
        JFrame frame = new JFrame("mahasiswa");
        frame.setContentPane(new mahasiswa().Main);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }

    Connection con;
    PreparedStatement pst;

    public void connect(){

        try{
            Class.forName("com.mysql.jdbc.Driver");
            con = DriverManager.getConnection("jdbc:mysql://localhost/mahasiswa","root","");
            System.out.println("Succesful");

        }catch (ClassNotFoundException | SQLException ex){

        }


    }

    void main_table(){

        try{
            pst = con.prepareStatement("select * from mhs");
            ResultSet rs = pst.executeQuery();
            table1.setModel(DbUtils.resultSetToTableModel(rs));


        }catch (SQLException e){

            e.printStackTrace();
        }

    }


    public mahasiswa() {
        connect();
        main_table();
        createButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {


                String id, Nama, NPM, Tgl_lahir, Kelas, Nilai;

                id = txtid.getText();
                Nama = txtNama.getText();
                NPM = txtNPM.getText();
                Tgl_lahir = txtTgl_lahir.getText();
                Kelas = txtKelas.getText();
                Nilai = txtNilai.getText();


                try{
                    pst = con.prepareStatement("insert into mhs(id,Nama,NPM,Tgl_lahir,Kelas,Nilai)values(?,?,?,?,?,?)");
                    pst.setString(1,id);
                    pst.setString(2,Nama);
                    pst.setString(3,NPM);
                    pst.setString(4,Tgl_lahir);
                    pst.setString(5,Kelas);
                    pst.setString(6,Nilai);
                    pst.executeUpdate();

                    JOptionPane.showMessageDialog(null,"Data Created!");
                    main_table();
                    txtid.setText("");
                    txtNama.setText("");
                    txtNPM.setText("");
                    txtTgl_lahir.setText("");
                    txtKelas.setText("");
                    txtNilai.setText("");
                    txtNama.requestFocus();

                }catch (SQLException e1){

                    e1.printStackTrace();
                }

            }
        });
        readButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                try{
                    String an_id = txtfield.getText();

                    pst = con.prepareStatement("select id,Nama,NPM,Tgl_lahir,Kelas,Nilai from mhs where id = ?");
                    pst.setString(1,an_id);
                    ResultSet rs = pst.executeQuery();

                    if (rs.next()==true){
                        String idid = rs.getString(1);
                        String a_Nama = rs.getString(2);
                        String an_NPM = rs.getString(3);
                        String a_Tgl_lahir = rs.getString(4);
                        String a_Kelas = rs.getString(5);
                        String a_Nilai = rs.getString(6);

                        txtid.setText(idid);
                        txtNama.setText(a_Nama);
                        txtNPM.setText(an_NPM);
                        txtTgl_lahir.setText(a_Tgl_lahir);
                        txtKelas.setText(a_Kelas);
                        txtNilai.setText(a_Nilai);


                    }else{

                        txtid.setText("");
                        txtNama.setText("");
                        txtNPM.setText("");
                        txtTgl_lahir.setText("");
                        txtKelas.setText("");
                        txtNilai.setText("");
                        JOptionPane.showMessageDialog(null,"Invalid id!");
                    }

                }catch (SQLException ex){

                }



            }
        });
        updateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                String id, Nama, NPM, Tgl_lahir, Kelas, Nilai;

                id = txtid.getText();
                Nama = txtNama.getText();
                NPM = txtNPM.getText();
                Tgl_lahir = txtTgl_lahir.getText();
                Kelas = txtKelas.getText();
                Nilai = txtNilai.getText();

                try{
                    pst = con.prepareStatement("update mhs set id = ?,Nama = ?,NPM = ?,Tgl_lahir = ?,Kelas = ?,Nilai = ?");
                    pst.setString(1,id);
                    pst.setString(2,Nama);
                    pst.setString(3,NPM);
                    pst.setString(4,Tgl_lahir);
                    pst.setString(5,Kelas);
                    pst.setString(6,Nilai);

                    pst.executeUpdate();
                    JOptionPane.showMessageDialog(null,"Data Updated!");
                    main_table();
                    txtid.setText("");
                    txtNama.setText("");
                    txtNPM.setText("");
                    txtTgl_lahir.setText("");
                    txtKelas.setText("");
                    txtNilai.setText("");
                    txtNama.requestFocus();

                }catch (SQLException e1){

                    e1.printStackTrace();
                }

            }
        });
        deleteButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                String id;

                id = txtfield.getText();

                try{
                    pst = con.prepareStatement("delete from mhs where id = ?");

                    pst.setString(1,id);

                    pst.executeUpdate();
                    JOptionPane.showMessageDialog(null,"Data Deleted!");
                    main_table();
                    txtid.setText("");
                    txtNama.setText("");
                    txtNPM.setText("");
                    txtTgl_lahir.setText("");
                    txtKelas.setText("");
                    txtNilai.setText("");
                    txtNama.requestFocus();

                }catch (SQLException e1){

                    e1.printStackTrace();
                }



            }
        });
    }
}
