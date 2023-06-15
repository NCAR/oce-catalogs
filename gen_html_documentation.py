#!/usr/bin/env python

import os

import yaml

def write_html(title, table_dict, html_outfile):
    src_code = [f'<html>\n<head>\n<title>{title}</title>\n</head>',
                '<style>',
                'tr:nth-child(even) {',
                '  background-color: #DDDDDD',
                '}\ntable, th, td {',
                '  border: 0.5px solid black;',
                '  border-spacing: 0px;',
                '}\n</style>',
                '<body>',
                '<table>\n<tr>\n  <th>Catalog Key</th>\n  <th>Description</th>\n  <th>Path</th>\n</tr>',
                ]
    key_list = list(table_dict.keys())
    key_list.sort()
    for key in key_list:
        src_code.append(f'<tr>\n  <td>{table_dict[key]["name"]}</td>\n  <td>{table_dict[key]["description"]}</td>  <td>{table_dict[key]["path"]}</td>\n</tr>')
    src_code.append('</table>\n</body>\n</html>')
    with open(html_outfile, "w") as f:
        for n in range(len(src_code)):
            if n<len(src_code)-1:
                f.write(f'{src_code[n]}\n')
            else:
                f.write(src_code[n])

if __name__ == '__main__':
    table_dict = dict()
    with open('reference-datasets.yml') as f:
        catalog = yaml.safe_load(f)
        title = catalog['name']
        for key in catalog['sources']:
            table_dict[key] = {'name': key,
                            'path': catalog['sources'][key]['args']['urlpath'],
                            'description': catalog['sources'][key]['description']}

    html_out = 'index.html'
    write_html(title, table_dict, html_out)
