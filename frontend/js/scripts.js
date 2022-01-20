$(function () {
  function list_users() {
    $.ajax({
      url: "http://localhost:5000/users",
      method: "GET",
      dataType: "json",
      success: list,
      error: () => alert("error when reading data, verify server"),
    });
    function list(users) {
      $("#roleTableBody").empty();
      $("#userTableBody").empty();

      showOnlyContent("users-table");
      for (const user of users) {
        line =
          "<tr>" +
          "<td>" + user.id + "</td>" +
          "<td>" + user.name + "</td>" +
          "<td>" + user.email + "</td>" +
          "<td>" + user.role?.authority + "</td>" +
          "</tr>";
        $("#userTableBody").append(line);
      }
    }
  }

  function list_roles() {
    $.ajax({
      url: "http://localhost:5000/roles",
      method: "GET",
      dataType: "json",
      success: list,
      error: () => alert("error when reading data, verify server"),
    });
    function list(roles) {
      $("#userTableBody").empty();
      $("#roleTableBody").empty();

      showOnlyContent("roles-table");
      for (const role of roles) {
        line =
          "<tr>" +
          "<td>" + role.id + "</td>" +
          "<td>" + role.authority + "</td>" +
          "</tr>";
        $("#roleTableBody").append(line);
      }
    }
  }

  function showOnlyContent(showOnlyThisOne) {
    $("#roles-table").addClass("invisible");
    $("#users-table").addClass("invisible");
    $("#initial-content").addClass("invisible");

    $(`#${showOnlyThisOne}`).removeClass("invisible");
  }

  $(document).on("click", "#link-list-roles", function () {
    list_roles();
  });

  $(document).on("click", "#link-list-users", function () {
    list_users();
  });

  $(document).on("click", "#link-home", function () {
    showOnlyContent("initial-content");
  });

  $(document).on("click", "#btn-add-user", function () {
    name = $("#user-name").val();
    email = $("#email").val();
    password = $("#password").val();
    roleId = $("#user-role").val();

    var data = JSON.stringify({
      name,
      email,
      password,
      roleId
    });

    $.ajax({
      url: "http://localhost:5000/users",
      type: "POST",
      dataType: "json",
      contentType: "application/json",
      data,
      success: addedUser,
      error: errorWhenAdding,
    });
    function addedUser(response) {
      alert("User added with success!");
      $("#user-name").val("");
      $("#email").val("");
      $("#password").val("");
      $("#user-role").val("");
    }
    function errorWhenAdding(response) {
      alert(`ERRO: ${response.result}: ${response.details}`);
    }
  });

  $("#modalAddUser").on("hide.bs.modal", function (event) {
    if (!$("#users-table").hasClass("invisible")) {
      list_users();
    }
  });

  showOnlyContent("initial-content");
});
