from pathlib import Path

base = Path.cwd()

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
    project_name=input("Give Name - ")
    if project_select==1:
        try:
            project_path=Path(f'{base}/{project_name}')
            project_path.mkdir(parents=True,exist_ok=True)
        
        except Exception as e:
            print(e)




Menu()
create_project()
