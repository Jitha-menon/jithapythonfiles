class vscode:
    def compile(self):
        print('compile')
    def execute(self):
        print('execute')

class pycharm:
    def compile(self):
        print('pycharm')
    def execute(self):
        print('pyyexecute')

class programer:
    def coding(self,ide):
        ide.compile()
        ide.execute()

dev=programer()
pyc=pycharm()
dev.coding(pyc)