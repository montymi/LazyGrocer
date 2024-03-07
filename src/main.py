from controller.dataController import DataController

def main(db):
    print(type(db))

if __name__ == "__main__":
    db = DataController()
    main(db)