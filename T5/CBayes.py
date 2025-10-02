# -*- coding: utf-8 -*-
# Programador: Martínez Alfaro Felipe de Jesús.
import pandas as pd
import numpy as np

class CBayes:
  def __init__(self, df,columna:int = 0,continuo:bool = False,div:int = 10):
    self.c = columna
    self.df = df
    self.atrib = df.columns.values
    self.C = df[self.atrib[self.c]].unique()
    self.continuo = continuo
    if continuo:
      self.div = div
      # Obtengo los rangos minimos y maximos de cada atributo, sin contar la columna especie...
      self.df_min = df.drop('especie', axis=1).min()
      self.df_max = df.drop('especie', axis=1).max()
      # Creo los rangos con d ...
      self.tam_rangos = (self.df_max-self.df_min)/div
    pass;
  
  # Supongamos que quiero obtener el subrango de un valor que pertenece a un tipo de atributo
  def s(self,valor, atributo):
    subrango = (valor-self.df_min[atributo])/self.tam_rangos[atributo]
    #print('div: (',valor,'-',df_min[atributo],')/',tam_rangos[atributo],' = ',subrango)
    subrango = min(self.div-1,int( subrango ))
    return subrango;
  
  # Cuento las posibilidades de que un atributo continuo tenga un valor x_i y que sea de la clase c...
  def siYc(self,valor,atributo,clase):
    s_i = self.s(valor,atributo)                                                # Obtengo el subrango de mi valor.
    s_n = df[atributo].apply(lambda x: self.s(x,atributo))                      # Obtengo el subrango de cada elemento de la columna del atributo.
    si_y_c = df[ (s_n == s_i) & (df['especie'] == clase)][atributo]             # Obtengo todas las filas del atributo que están en el mismo rango y pertenecen a la clase c
    #print(si_y_c)
    return si_y_c.count()                                                       # Finalmente obtengo la probabilidad condicionada de P(si y c).
  
  # Cuento las posibilidades de que un atributo discreto tenga un valor x_i y que sea de la clase c...
  def xiYc(self,valor,atributo,clase):
    return df[ (df[self.atrib[self.c]] == valor) & (df['especie'] == clase)][atributo].count()

  # Probabilidad condicionada P(x|c) * P(c)
  def xYc(self,elemento,clase):
    ans = 1                                                                     # Siempre va a haber 1 aunque no haya.
    atribs = np.delete(self.atrib.copy(),self.c)                                # Solo reviso los atributos, por ello le quito la columna de la clase.
    #print(type(elemento) == type([]))
    #print(type(elemento) == type(df))
    #print(type(elemento) == type(np.zeros(1)) )
    #if(type(elemento) == type([]) or type(np.zeros(1)) ):
    for i in range(len(elemento)):                                              # Para cada valor del atributo del elemnto...
      if self.continuo:
        tam = self.siYc(elemento[i],atribs[i],clase)                            # Cuento los elmentos que están en el rango y son de la clase dada.
      else:
        tam = self.xiYc(elemento[i],atribs[i],clase)                            # Cuento los elmentos con el mismo atributo y son de la clase dada.
      ans *= 1 if tam == 0 else tam                                             # Para que no se vaya a 0 lo que hago es multiplicar por 1.
      #print(ans)
      pass;
    return ans;                                                                 # Devuelvo la multiplicatoria de los conteos.

  # Le pido a mi clasificador que trate de clasificar un elmento que le doy.
  def clasificar(self,elemento):
    return max(self.C, key=lambda c: self.xYc(elemento,c))
  pass;
