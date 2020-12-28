function handleNavBar() {
    var x = document.getElementById("navbar_top");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
} 