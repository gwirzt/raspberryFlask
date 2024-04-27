from db import Base, engine, session    
from models import Producto

Base.metadata.create_all(engine)

session.add(Producto('Coca Cola', 1.5, 'Refresco de cola'))
session.add(Producto('Pepsi', 1.5, 'Refresco de cola'))
session.add(Producto('Manzana', 1.0, 'Fruta'))

session.commit()

productos = session.query(Producto).all()
for producto in productos:
    print(producto)
    
session.close()


