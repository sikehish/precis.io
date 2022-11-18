const logout = document.getElementsByClassName("logout")[0];

if (logout)
  logout.addEventListener("click", (e) => {
    setTimeout(function () {
      // location.replace("http://127.0.0.1:8000/accounts/logout");
      location.reload();
    }, 100);
  });
// console.log(logout);
