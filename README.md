# marker
Marker is a language that transpiles directly to HTML.

## Example
```py
from marker import generate

print(generate('p (style: "color: red") {"Hello, world!"}'))

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
>        br
>        p {
>            "1 + 2 = "
>            % {1 + 2} # The '%' tag evaluates python code using the 'eval' function and can't contain any newlines.
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
>        <br>
>        <p>1 + 2 = 3</p>
>    </body>
></html>
>```
> (Note that the resulting HTML isn't really formatted.)
## Usage
### In a Python script
```py
from marker import generate

html = generate(marker_code)
```
### From the command line
```bash
python3 marker.py [marker code file] [optional output file]
```
If `[optional output file]` is omitted, the result will be printed to the terminal.