"""<!DOCTYPE html>
<html>
  <head>
    <title>Load Text File Example</title>
  </head>
  <body>
    <input type="file" id="input-file" onchange="loadFile()">
    <div id="output"></div>

    <script>
      function loadFile() {
        var input = document.getElementById("input-file");
        var file = input.files[0];

        var reader = new FileReader();
        reader.onload = function() {
          var text = reader.result;
          var output = document.getElementById("output");
          output.innerText = text;
        };
        reader.readAsText(file);
      }
    </script>
  </body>
</html>
"""