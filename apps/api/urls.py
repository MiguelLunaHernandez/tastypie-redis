from tastypie.api import Api 
from apps.api.resource import *

v1_api = Api(api_name='v1')

v1_api.register(CategoriaProductoResource())
v1_api.register(ProductoResource())
v1_api.register(KardexResource())
v1_api.register(SucursalSinInventarioResource())
