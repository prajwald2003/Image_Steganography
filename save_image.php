<!-- save_image.php -->

<?php
$folderPath = $_POST['folderPath'];
$fileName = $_POST['fileName'];
$data = $_POST['data'];

// Create the folder if it doesn't exist
if (!file_exists($folderPath)) {
  mkdir($folderPath, 0777, true);
}

// Save the image file
file_put_contents($folderPath . $fileName, base64_decode($data));
?>
