<?php
if($_POST){
    $name = $_POST['commentForm'];
    $email = $_POST['form_email'];
    $message = $_POST['form_msg'];

//send email
    mail("j.andrew.sears@gmail.com", "51 Deep comment from" .$email, $message);
}
?>
