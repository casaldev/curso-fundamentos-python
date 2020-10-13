
# import os
 
# filename = 'zen_python.txt'
# path = os.path.abspath(filename)
 
# print('path: \t\t', path)
# print('basename: \t', os.path.basename(path))
# print('dirname: \t', os.path.dirname(path))
# print('splitext: \t', os.path.splitext(path))
# print('split: \t\t', os.path.split(path))
 
# readme_path = os.path.join(
#     os.path.dirname(path), '..', '..', 'README.rst')
# print('readme path: \t', readme_path)
# print('normalized: \t', os.path.normpath(readme_path))


# import os
# from tempfile import NamedTemporaryFile, TemporaryDirectory
 
# with TemporaryDirectory(dir='.') as td:
#     print('Temp directory:', td)
#     with NamedTemporaryFile(dir=td) as t:
#         name = t.name
#         print(os.path.abspath(name))


# import os
 
# with os.scandir('.') as it:
#     for entry in it:
#         print(
#             entry.name, entry.path,
#             'File' if entry.is_file() else 'Folder'
#         )

# import os
 
# for root, dirs, files in os.walk('.'):
#     print(os.path.abspath(root))
#     if dirs:
#         print('Pastas:')
#         for dir_ in dirs:
#             print(dir_)
#         print()
#     if files:
#         print('Arquivos:')
#         for filename in files:
#             print(filename)
#         print()

import tarfile

with tarfile.open('zen_python.tar.gz', 'w:gz') as tar:
    tar.add('zen_python.txt')
    tar.add('content2.txt')
    tar.add('subfolder/content3.txt')
    tar.add('subfolder/content4.txt')

with tarfile.open('example.tar.gz', 'r:gz') as tar:
    tar.extractall('extract_tar')


from zipfile import ZipFile

with ZipFile('zen_python.zip', 'w') as zp:
    zp.write('zen_python.txt')
    zp.write('content2.txt')
    zp.write('subfolder/content3.txt')
    zp.write('subfolder/content4.txt')


with ZipFile('example.zip') as zp:
    zp.extract('content1.txt', 'extract_zip')
    zp.extract('subfolder/content3.txt', 'extract_zip')