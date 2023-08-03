var encryptedMessage = "";

function chooseImage(operation) {
  var fileInput = document.createElement('input');
  fileInput.type = 'file';

  // Trigger file selection dialog
  fileInput.click();

  fileInput.addEventListener('change', function(event) {
    var file = event.target.files[0];
    var reader = new FileReader();

    reader.onload = function(event) {
      var imageDataURL = event.target.result;

      // Call the corresponding function based on the operation
      if (operation === 'encrypt') {
        encryptImage(imageDataURL);
      } else if (operation === 'decrypt') {
        decryptImage(imageDataURL);
      }
    };

    reader.readAsDataURL(file);
  });
}
function encryptImage(imageDataURL) {
  var message = prompt('Enter the message to encrypt:');

  // Call the encrypt PHP script via AJAX, passing imageDataURL and message
  var formData = new FormData();
  formData.append('imageData', imageDataURL);
  formData.append('message', message);

  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'encrypt.php', true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);

        // Display the encryption result
        document.getElementById('encryptionResult').style.display = 'block';
        document.getElementById('encryptedText').innerText =   message
        document.getElementById('encryptedImagePath').innerText = 'Encrypted Image Path: ' + response.encryptedImagePath;
      } else {
        // Handle error
        console.error('Encryption failed:', xhr.responseText);
      }
    }
  };
  xhr.send(formData);
}


function decryptImage(imageDataURL) {
  var encryptedMessage = document.getElementById('encryptedText').innerText;
  
  document.getElementById('decryptionResult').style.display = 'block';
  document.getElementById('decryptedText').innerText =  encryptedMessage;
}
