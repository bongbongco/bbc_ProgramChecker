import wmi
from _winreg import (HKEY_LOCAL_MACHINE, KEY_ALL_ACCESS, OpenKey, EnumValue, QueryValueEx)


class ExtractManager:
    def __init__(self):
        self.registry = wmi.Registry()
        self.installed_program_key = r'Software\Microsoft\Windows\CurrentVersion\Uninstall'
        self.names = None

    def extract_data(self):
        for subkey in self.names:
            try:
                path = "{}\\{}".format(
                        self.installed_program_key, 
                        subkey
                        )

                key = OpenKey(HKEY_LOCAL_MACHINE, path, 0, KEY_ALL_ACCESS)

                try:
                    print(QueryValueEx(key, 'DisplayName')[0])
                except:
                    pass # regkey

            except:
                pass # OpenKey Error

    def work(self):
        result, self.names = self.registry.EnumKey(
                hDefKey=HKEY_LOCAL_MACHINE,
                sSubKeyName=self.installed_program_key
                )
        
        self.extract_data()


class ReportManager:
    def __init__(self):
        pass


def main():
    extractManager = ExtractManager()
    extractManager.work()

if __name__=="__main__":
    main()
