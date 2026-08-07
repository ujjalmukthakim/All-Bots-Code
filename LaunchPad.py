import os
from pathlib import Path

print('========================\n' \
'Developer LaunchPad\n' \
'========================\n\n' \
'1. New Django Project\n' \
'2. New React Project\n' \
'3. Full Stack Project\n' \
'4. Python Bot\n' \
'5. Quit')


folders=[
    'backend',
    'frontend',
    'docs',
    'docker',
    'scripts'
]

files=[
    'README.md',
    '.gitignore',
    '.env.example'
]


try: 
   choice_input=int(input('- '))
   if choice_input==3:
       project_name=input("Project Name: ")

   folder_path=Path(f'/Users/apple/desktop/{project_name}')
   folder_path.mkdir(parents=True,exist_ok=True)
   for folder in folders:
       (folder_path / folder).mkdir(parents=True,exist_ok=True)
   for file in files:
       (folder_path / file).touch()
       
except:
    print('Error, This File Only Accept Number !')