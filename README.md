## Flask Application Design

**HTML Files**

- **index.html:** This is the main HTML file that will be rendered to the client. It should include a button that the user can click on to change the background color of the page.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Flask Color Change App</title>
</head>
<body>
  <h1>Flask Color Change App</h1>
  <p>Click the button to change the background color.</p>
  <button type="button" onclick="changeColor()">Change Color</button>

  <script>
    function changeColor() {
      // Get a random color
      var color = Math.floor(Math.random() * 16777215).toString(16);

      // Set the background color of the page
      document.body.style.backgroundColor = "#" + color;
    }
  </script>
</body>
</html>
```

**Routes**

- **/change_color:** This route will be called when the user clicks the button in the HTML file. It will generate a random color and return it as a JSON response.

```python
@app.route('/change_color', methods=['GET'])
def change_color():
  # Get a random color
  color = Math.floor(Math.random() * 16777215).toString(16)

  # Return the color as a JSON response
  return jsonify({'color': color})
```