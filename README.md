# Módulo de conversión de coordenadas para monturas altazimutales

Este es un módulo basado en [Astropy](http://www.astropy.org/) que permite crear un objeto para una montura 
localizada en un punto sobre la Tierra el cual contiene métodos (funciones adaptadas a las caracteristicas del objeto) 
que retornan un array de coordenadas horizontales a partir de coorenadas ecuatoriales.También incluye métodos de seguimiento solar.

El módulo no contiene rutinas de control de motores. Las funciones de conversión permiten crear referencias de control que 
pueden ser enviadas a un controlador (Ejem. controladores de la familia [Pololu Jrk](https://www.pololu.com/category/95/pololu-jrk-motor-controllers-with-feedback)).

Los métodos que contiene el módulo son los siguientes:

* tracker.ElAzMount() &emsp; &emsp; &emsp; &emsp; &emsp; &ensp;&emsp;&emsp;&emsp;&ensp; Crea objeto de montura
  * .setLocation(Lat,Lon,Height) &emsp;&emsp;&emsp;&emsp;&ensp; Establece ubicación del observador.
  * .eq2hor(DEC,RA)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&emsp;&emsp;&emsp;&ensp; Convierte coordenadas ecuatoriales a horizontales.
  * .SolarTracking()&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; Retorna la altura y azimut solares en tiempo real.
  * .Sun_Pos_By_Date(date)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;Retorna la altura y azimut solares para una fecha dada.
  * .Sweep_Matrix(date,n,m,xstep,ystep)&emsp; Retorna matriz de barrido para el Sol.
