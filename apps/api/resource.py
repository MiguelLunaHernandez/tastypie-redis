
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from apps.core.models import *

from apps.redis.redis_ import *
import json
from django.core import serializers

class CategoriaProductoResource(ModelResource):
    
    class Meta:
        
        queryset = CategoriaProducto.objects.all()
        resource_name = 'categoriaproducto'
        authorization = Authorization()
        always_return_data = True

    def get_object_list(self, request):
        
        return super(CategoriaProductoResource, self).get_object_list(request)

    def obj_get_list(self, bundle, **kwargs):

        """
        Este metodo es el primero en ser llamda cuando se realiza
        una peticion GET
        """
        #preguntamos si existe en cache 

        resultcache = ExitCache('CategoriaProducto')

        if resultcache: 
            print "desde cache"
            #si es 1 existe la cache 
            result = GetCache('CategoriaProducto')
            print result
            return result
        else:
            print "desde ORM"
            result =  self.get_object_list(self)
            SaveCache('CategoriaProducto', result)

            print result
            return result


    
class ProductoResource(ModelResource):
    
    categoria_producto = fields.ForeignKey(CategoriaProductoResource, 'categoria_producto', full=True, null=True)
    
    class Meta:
        
        queryset = Producto.objects.all()
        resource_name = 'producto'
        always_return_data = True
        authorization = Authorization()
        filtering = {
                "categoria": ["exact"],
                "codigo": ["icontains", "iexact"],
                }
        
        
class KardexResource(ModelResource):

    """ Kardex : este se puede usar en la seccion de inventario general ."""
    
    sucursal = fields.ForeignKey("apps.api.resource.SucursalSinInventarioResource", 'sucursal', full=True)
    producto = fields.ForeignKey(ProductoResource, 'producto', full=True)

    class Meta:
        
        allowed_methods = ["get"]
        queryset = Kardex.objects.all()
        always_return_data = True
        resource_name = 'kardex'
        filtering = {
                
                "sucursal": ["exact"],
                "producto": ["exact"],
                "fecha": ["lte", "gte", "lt", "gt"],
                }
        authorization = Authorization()

    def get_object_list(self, request):

        """
        Este metodo es el primero en ser llamda cuando se realiza
        una peticion GET
        """
#        preguntamos si existe en cache

        resultcache = ExitCache('kardex')

        print 'resultado de resultcache = %s' %(resultcache)

        if resultcache:
            #si es 1 existe la cache 
            print 'desde chache'
            result = GetCache('kardex')
            #print len(result)
            #results = json.dumps(result)
            #print results
            return result
        else:
            print 'desde ORM'
            result = super(KardexResource, self).get_object_list(request) #self.get_object_list(self)
            print 'termino la consuilta'
            print 'tamano %s' % (len(result))

            SaveCache('kardex', result)

            return result

class SucursalSinInventarioResource(ModelResource):
    
    class Meta:
        resource_name = 'sucursales'
        queryset = Sucursal.objects.all()
        filtering = {
	    "nombre": ["icontains"]
	    }
    
    def get_object_list(self, request):
        return super(KardexResource, self).get_object_list(request)

    def obj_get_list(self, bundle, **kwargs):

        """
        Este metodo es el primero en ser llamda cuando se realiza
        una peticion GET
        """
        #preguntamos si existe en cache 

        resultcache = ExitCache('sucursalsininventario')

        if resultcache:
            #si es 1 existe la cache 
            result = GetCache('sucursalsininventario')
            return result
        else:
            result =  self.get_object_list(self)
            SaveCache('sucursalsin inventario', result)
            return result

