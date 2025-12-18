function changeText() {
  document.getElementById("message").innerText = "This Text changed";
}

function changeColor() {
  document.getElementById("message").style.color = "Red";
}

function showText() {
  let name = document.getElementById("name").value;
  document.getElementById("title").innerText = "Hello, " + name;
}
