'''
Created on Oct 30, 2017

@author: rene
'''
from Singleton.Borg import Borg
from Singleton.BorgObj import BorgObj
from Singleton.LazySingleton import LazySingleton
from Singleton.MetaSingleton import Logger, Database
from Singleton.MyInt import int
from Singleton.Singleton import Singleton
from Singleton.HealthCheck import HealthCheck


if __name__ == '__main__':
    s = Singleton()
    
    print("Object created", s)
    
    sl = Singleton()
    print("Object created", sl)
    
    s2 = LazySingleton()
    print("Object Created", LazySingleton.getInstance())
    sl2 = LazySingleton()
    
    b = Borg()
    b1 = Borg()
    b.x = 4
    
    print("Borg Object 'b': ", b)
    print("Borg Object 'b1': ", b1)
    print("Object State 'b': ", b.__dict__)
    print("Object State 'b1': ", b1.__dict__)
    
    b = BorgObj()
    b1 = BorgObj()
    
    print("Borg Object 'b': ", b)
    print("Borg Object 'b1': ", b1)
    print("Object State 'b': ", b.__dict__)
    print("Object State 'b1': ", b1.__dict__)
    
    i =int(4,5)
    
    logger1 = Logger()
    logger2 = Logger()
    print(logger1, logger2)
    
    db1 = Database().connect()
    db2 = Database().connect()
    
    print("Database Objects DB1", db1)
    print("Database Objects DB2", db2)
    
    hc1 = HealthCheck()
    hc2 = HealthCheck()
    
    hc1.addServer()
    print("Schedule health check for servers (1)...")
    
    for i in range(4):
        print("Checking ", hc1._servers[i])
    
    print(hc1)
    print(hc2)
    
    hc2.changeServer()
    print("Schedule health check for servers (2)...")
     
    for i in range(4):
        print("Checking ", hc2._servers[i])