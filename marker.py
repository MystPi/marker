import lark

def conv_to_HTML(p) -> str:
    if type(p) == lark.Tree:
        if p.data == 'start':
            ret = ''
            for child in p.children:
                ret += conv_to_HTML(child)
            return ret
        elif p.data == 'tag':
            t = p.children[0]
            children = p.children[1:]
            if len(children) > 0 and type(children[0]) == lark.Tree and children[0].data == 'attr':
                ret = f'<{t}{conv_to_HTML(children[0])}>'
                children = children[1:]
            else:
                ret = f'<{t}>'
            if len(children) > 0:
                for child in children:
                    ret += str(conv_to_HTML(child))
                ret += f'</{t}>'
            return ret
        elif p.data == 'eval':
            return eval(p.children[0])
        elif p.data == 'attr':
            ret = ''
            for child in p.children:
                ret += ' '
                ret += child.children[0]
                ret += '='
                ret += child.children[1]
            return ret
    elif type(p) == lark.Token:
        if p.type == 'STRING':
            return p.value[1:-1]

def make_website(code, create_file=True):
    grammar = r'''
        ?start : tag*

        tag : NAME attr? ("{" value* "}")?
        eval : "%" "{" /.+?(?=})/? "}"
        attr : "(" key_value ("," key_value)* ")"
        key_value : NAME ":" STRING
        
        ?value : tag
               | eval
               | STRING
          
        _STRING_INNER: /[\S\s]*?/
        _STRING_ESC_INNER: _STRING_INNER /(?<!\\)(\\\\)*?/

        STRING : "\"" _STRING_ESC_INNER "\""
        
        %import common.CNAME -> NAME
        %import common.WS
        %ignore WS
        %ignore /\#.*/
    '''

    parser = lark.Lark(grammar)
    parsed = parser.parse(code)

    if create_file:
        name = input('Name of HTML file (no .html extension) (enter nothing to quit): ')
        if not name:
            return
        name += '.html'
        with open(name, 'w') as file:
            if input(f'Are you sure you want to overwrite \'{name}\'? (y/n) ').lower() == 'n':
                return
            file.write(conv_to_HTML(parsed))
            print(f'Success! Open \'{name}\' in a web browser to see the website!')
    else:
        return conv_to_HTML(parsed)
