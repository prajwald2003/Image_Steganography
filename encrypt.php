<?php
$imageData = $_POST['imageData'];
$message = $_POST['message'];

// Remove the data URI scheme prefix and decode the base64 image data
$imageData = str_replace('data:image/png;base64,', '', $imageData);
$imageData = str_replace(' ', '+', $imageData);
$imageDataDecoded = base64_decode($imageData);

// Generate a unique filename for the encrypted image
$encryptedImagePath = 'encrypted_images/encrytped_image.jpg';

// Save the image data to the encrypted_images folder
$fileSaved = file_put_contents($encryptedImagePath, $imageDataDecoded);

if ($fileSaved) {
  // Call the encrypt Python script with the generated image path and message
  $command = "python encrypt.py \"$encryptedImagePath\" \"$message\"";
  exec($command, $output);

  // Prepare the response
  $response = array(
    'encryptedImagePath' => $encryptedImagePath
  );
} else {
  // Error saving the image
  $response = array(
    'error' => 'Failed to save the image.'
  );
}

// Send the response as JSON
header('Content-Type: application/json');
echo json_encode($response);
?>
