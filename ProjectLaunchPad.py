from pathlib import Path
import subprocess

base = Path.home() / "Desktop"
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
projects_number=[1,2,3]
def Menu():
    
    MENU = """
    ========================
    Developer LaunchPad
    ========================

    1. New Django Project
    2. New React Project
    3. Full Stack Project
    4. Python Bot
    5. Quit
    """

    print(MENU)

def create_project():
    project_select=int(input("Give Your Choice - "))

    if project_select in projects_number:
        
        project_name=input("Give Project Name - ")
        try:
            project_path=Path(f'{base}/{project_name}')
            project_path.mkdir(parents=True,exist_ok=True)
            command=['git','init']
            try:
                result=subprocess.run(
                    command,
                    cwd=project_path,
                    text=True,
                    check= True
                )
            
            except Exception as e:
                print(e)


        
        except Exception as e:
            print(e)
        if project_select==1:
            print('Coming Soon. . .')
        elif project_select==2:
            print('Coming Soon. . .')
        else:
            for folder in folders:
                (project_path/folder).mkdir(parents=True,exist_ok=True)
            for file in files:
                (project_path/file).touch()


    if project_select==4:
        bot_name=input('Give Bot Name - ')
        try:
            bot_path=Path(f'{base}/{bot_name}')
            bot_path.mkdir(parents=True,exist_ok=True)
        except Exception as e:
            print(e)
    if project_select==5:
        print("Ok Good Bye ...")
        return





Menu()
create_project()
