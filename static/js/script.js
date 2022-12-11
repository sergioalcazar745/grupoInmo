$(document).ready(function () {
  //   $(this).scrollTop(0);

  $(".mr-auto .nav-item").bind("click", function (event) {
    event.preventDefault();
    var clickedItem = $(this);
    $(".mr-auto .nav-item").each(function () {
      $(this).removeClass("active");
    });
    clickedItem.addClass("active");
  });
});

/* --- Modal Image --- */

var modal = document.getElementById("myModal");
//var img = document.getElementById("myImg");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");

function clickImage(img) {
  modal.style.display = "block";
  modalImg.src = img.src;
  captionText.innerHTML = img.alt;
}

// img.onclick = function () {
//   modal.style.display = "block";
//   modalImg.src = this.src;
//   captionText.innerHTML = this.alt;
// };

var span = document.getElementsByClassName("close")[0];

if(span != undefined){
  span.onclick = function () {
    modal.style.display = "none";
  };
}

/* --- Scroll --- */

window.onscroll = function () {
  myFunction();
};

var header = document.getElementById("idMenu");
var sticky = header.offsetTop;

function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}

/* --- Maps --- */

function iniciarMap() {
  var coord = { lat:0 , lng:0  };
  var map = new google.maps.Map(document.getElementById("map"), {
    zoom: 10,
    center: coord,
  });
  var marker = new google.maps.Marker({
    position: coord,
    map: map,
  });
}

function downloadCV(nombre) {
  console.log(nombre)
  downloadInstance = document.createElement("a");
  downloadInstance.href = "/media/"+nombre;
  downloadInstance.target = "_blank";
  downloadInstance.download = nombre;
  document.body.appendChild(downloadInstance);
  downloadInstance.click();
  document.body.removeChild(downloadInstance);
}
