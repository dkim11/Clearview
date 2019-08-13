  function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}

  //document.getElementById("LoginButton").onclick = doFunction;
  document.getElementById("LoginButton").onclick = function () { alert('hello!'); };


        function validateForm() {


        var un = document.loginform.username.value;
        var pw = document.loginform.password.value;


        if ((un.length > 0) && (pw.length > 0)) {

            /// Req
            var xhr = new XMLHttpRequest();
            var url = "http://127.0.0.1:1337/auth/local";
            xhr.open("POST", url, true);
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    var json = JSON.parse(xhr.responseText);
                    document.cookie = "AUTH" + "=" + json.jwt + ";path=/";
                    //alert(json.jwt);
                    //console.log(json.jwt);
                }
            };
            var data = JSON.stringify({"identifier": un, "password": pw});
            xhr.send(data);
            sleep(5000);
            location.reload();

        }
        else {
            alert ("Please check your username and password");
            return false;
        }
  }


  function signOut() {
        document.cookie =  'AUTH=;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
  }
