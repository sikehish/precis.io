const togglePassword = document.querySelectorAll(".togglePassword");
// const password = document.querySelectorAll(".id_password");

togglePassword.forEach((el) => {
  el.addEventListener("click", function (e) {
    const ele = el.previousElementSibling;
    const type = ele.getAttribute("type") === "password" ? "text" : "password";
    ele.setAttribute("type", type);

    // toggle the eye slash icon
    this.classList.toggle("fa-eye-slash");
  });
});

document.querySelectorAll("input").forEach((el) => {
  el.setAttribute("autocomplete", "off");
});
