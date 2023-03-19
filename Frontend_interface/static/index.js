function previewImage(event) {
    var reader = new FileReader();
    reader.onload = function(){
      var img = document.getElementById("preview");
      img.src = reader.result;
    }
    reader.readAsDataURL(event.target.files[0]);

    const fileInput = document.getElementById('image-upload');
    const file = fileInput.files[0];
    const fileUrl = URL.createObjectURL(file);
    console.log(fileUrl);
}

function openExcel() {
    const url = "form.xlsx";
    const options = "width=800,height=600,left=200,top=100";
    window.open(url, "", options);
}
  
function handleFileUpload() {
  const fileInput = document.getElementById('myFileInput');
  const filePath = fileInput.value; // This may not return the full path due to security restrictions
  const fileName = fileInput.files[0].name; // This will return the file name with extension
  console.log('File path:', filePath);
  console.log('File name:', fileName);
}

function toggleTable() {
  var table = document.getElementsByClassName("display-results");
  if (table.style.display === "none") {
    table.style.display = "block";
  } else {
    table.style.display = "block";
  }
}