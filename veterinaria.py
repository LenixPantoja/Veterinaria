
class Mascota:
  def __init__(self, pCodigoMascota,pNombreMascota, pColor, pRaza, pDiagnosticos):
    
    self.__nombreMascota=pNombreMascota
    self.__color=pColor
    self.__raza=pRaza
    self.__codigoMascota=pCodigoMascota
    self.__diagnostico=pDiagnosticos

  def setNombre(self, pNombreMascota):
    self.__nombreMascota=pNombreMascota

  def setColor(self, pColor):
    self.__color=pColor

  def setRaza(self, pRaza):
    self.__raza=pRaza

  def setCodigo(self, pCodigoMascota):
    self.__codigoMascota=pCodigoMascota
  
  def setDiagnosticos(self, pDiagnosticos):
    self.__diagnosticos=pDiagnosticos
    


class Persona():
  #***Constructor de persona
  
  def __init__(self, pCodigoPersona, pNombre, pApellidos, pIdentificacion, pTelefono, pDireccion):

    self.__codigoPersona=pCodigoPersona
    self.__nombre=pNombre
    self.__apellidos=pApellidos
    self.__identificacion=pIdentificacion
    self.__telefono=pTelefono
    self.__direccion=pDireccion

  def setCodigoPersona(self, pCodigoPersona):
    self.__codigoPersona=pCodigoPersona

  def setNombre(self, pNombre):
    self.__nombre=pNombre

  def setApellidos(self, pApellidos):
    self.__apellidos=pApellidos

  def setIdentificacion(self,pIdentificacion):
    self.__identificacion=pIdentificacion

  def setTelefono(self, pTelefono):
    self.__telefono=pTelefono

  def setDireccion(self,pDireccion):
    self.__direccion=pDireccion


  def getCodigoPersona(self):
    return self.__codigoPersona
  def getNombre(self):
    return self.__nombre
  
  def getApellidos(self):
    return self.__apellidos
  
  def getIdentificacion(self):
    return self.__identificacion

  def getTelefono(self):
    return self.__telefono
    
  def getDireccion(self):
    return self.__direccion


class Medico(Persona):
  
  def __init__(self, pCodigoPersona, pNombre, pApellido,pIdentificacion,pTelefono,pDireccion, pEspecialización):
    super().__init__(pCodigoPersona, pNombre, pApellido, pIdentificacion, pTelefono,pDireccion)              
    self.__especializacion=pEspecializacion
    
  def setEspecializacion(self, pEspecialidad):
    self.__especializacion=pEspecializacion

  def getEspecializacion(self):
    return self.__especializacion

class Cliente(Persona,Mascota):
  def __init__(self, pCodigoPersona, pNombre, pApellido,pIdentificacion, pTelefono, pDireccion,pCodigoMascota,pNombreMascota, pColor, pRaza, pDiagnosticos,pCodigoMascota,pNombreMascota, pColor, pRaza, pDiagnosticos)

  Persona.__init__(self, pCodigoPersona, pNombre, pApellidos, pIdentificacion, pTelefono, pDireccion)
  Mascota.__init__(self, pCodigoMascota,pNombreMascota, pColor, pRaza, pDiagnosticos)




