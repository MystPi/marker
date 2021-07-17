# marker
Marker is a language that transpiles directly to HTML.

## Example
```py
from marker import make_website

print(make_website('p (style: "color: red") {"Hello, world!"}', False))

# Output:
# <p style="color: red">Hello, world!</p>
```

## Syntax
The syntax of Marker is very simple:
```
tag (attribute: "attribute value") { "tag contents" tag { "another tag" } } # Comment
```
Which can be expanded to entire HTML documents:
>```
>html {
>    head {
>        title { "Example page" }
>    }
>    body {
>        h1 (id: "header") {
>            "Example page!"
>        }
>        p {
>            "1 + 2 = "
>            % {1 + 2} # The '%' tag evaluates python code using the 'eval' function and must be a single line.
>        }
>    }
>}
>```
>Outputs:
>```html
><html>
>    <head>
>        <title>Example page</title>
>    </head>
>    <body>
>        <h1 id="header">Example page!</h1>
>        <p>1 + 2 = 3</p>
>    </body>
></html>
>```
## Usage
```py
from marker import make_website

make_website(marker_code[, create_file=True]) # Set create_file to False if you just want to return the HTML string.
```
