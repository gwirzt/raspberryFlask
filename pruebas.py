from db import Base, engine, session
from controllers import articulos_show

Base.metadata.create_all(engine)

productos_json = articulos_show()
print(productos_json)

session.close()


