$(function() {
    
  function list_courses() {
      $.ajax({
          url: 'http://localhost:5000/courses',
          method: 'GET',
          dataType: 'json',
          success: list,
          error: () => alert("error when reading data, verify server"),
      });
      function list(courses) {
          $('#courseTableBody').empty();

          showOnlyContent("courses-table");       
          for (const course of courses) {
              line = '<tr>' + 
              '<td>' + course.name + '</td>' + 
              '<td>' + course.imgUri + '</td>' + 
              '<td>' + course.imgGrayUri + '</td>' + 
              '</tr>';
              $('#courseTableBody').append(line);
          }
      }
  }

  function showOnlyContent(showOnlyThisOne) {
      $("#courses-table").addClass('invisible');
      $("#initial-content").addClass('invisible');

      $(`#${showOnlyThisOne}`).removeClass('invisible');      
  }

  $(document).on("click", "#link-list-courses", function() {
    list_courses();
  });
  
  $(document).on("click", "#link-home", function() {
    showOnlyContent("initial-content");
  });

  $(document).on("click", "#btn-add-course", function() {
      name = $("#course-name").val();
      imgUri = $("#course-img-uri").val();
      imgGrayUri = $("#course-img-uri-gray").val();

      var data = JSON.stringify({ name: name, imgUri: imgUri, imgGrayUri: imgGrayUri });
      
      $.ajax({
          url: 'http://localhost:5000/courses',
          type: 'POST',
          dataType: 'json',
          contentType: 'application/json', 
          data,
          success: addedCourse,
          error: errorWhenAdding,
      });
      function addedCourse(response) {
          if (response.result == "ok") {
              alert("Course added with success!");
              
              $("#course-name").val("");
              $("#course-img-uri").val("");
              $("#course-img-uri-gray").val("");
          } else {
              alert(`${response.result}: ${response.details}`);
          }            
      }
      function errorWhenAdding(response) {
          alert(`ERRO: ${response.result}: ${response.details}`);
      }
  });

  $('#modalAddCourse').on('hide.bs.modal', function(event) {
      if (! $("#courses-table").hasClass('invisible')) {
          list_courses();
      }
  });

  showOnlyContent("initial-content");
});
