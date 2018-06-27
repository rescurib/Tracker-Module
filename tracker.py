#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 13:22:52 2018
@author: Rodolfo E. Escobar U.
contact: r.escurib@gmail.com
"""
from datetime import datetime,timedelta
from time import mktime
from astropy.time import Time
import astropy.units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz, Angle, get_sun
import numpy as np
 

class ElAzMount:
    def __init__(self):
        self.Lat = None
        self.Lon = None
        self.Height = None
        
    def setLocation(self,Lat,Lon,Height = 0.0):
        """This method set the observer location. 
           The angles must be strings in format: "<>d<>m<>s".
           Height must be float.
           The default height is set to sea level.
        """
        self.location = EarthLocation(lat=Angle(Lat), 
                                      lon=Angle(Lon), 
                                      height=Height*u.m)
        self.Lat = self.location.lat
        self.Lon = self.location.lon
        self.Height = self.location.height
        
    def eq2hor(self,RA,DEC):
        """This method returns an array [El Az]
           computed from RA and DEC given the location
           of the observer.
           
           RA  string format : "<>h<>m<>s"
           DEC string format : "<>d<>m<>s"
        """
        #Update time
        utc_time = Time(datetime.utcnow(), scale='utc')
        time = utc_time 

        #Set eq
        O = SkyCoord(dec=Angle(DEC),ra=Angle(RA),frame='icrs')
        
        #Compute hor
        O = O.transform_to(AltAz(obstime=time,location=self.location))
            
        return ([O.alt.degree,O.az.degree])
    
    def SolarTracking(self):
        """
        Returns current horizontal coordinates of the Sun
        """
        #Update time
        utc_time = Time(datetime.utcnow(), scale='utc')
        time = utc_time 

        locframe = AltAz(obstime=time, location=self.location)
        s = get_sun(time).transform_to(locframe)
        return ([s.alt.degree,s.az.degree])

    def Sun_Pos_by_date(self,date):
        """
        Returns horizontal coordinates given specific date
        """
        ts = mktime(date.timetuple())
        utc_time = Time(datetime.utcfromtimestamp(ts), scale='utc')
        time = Time(utc_time, scale='utc')
        locframe = AltAz(obstime=time, location=self.location)
        s = get_sun(time).transform_to(locframe)
        return ([s.alt.degree,s.az.degree])
    
    def sweep_matrix(self,sweep_center,n,m,az_stride=1.0,el_stride=1.0):
        """
        This method returns two arrays that contain a set of
        points of a spatial matrix nxm centered in the Sun (at given time) 
        for radio astronomy imaging.
        
        Az and El strides are expresed in degrees.
        """
        [a,az] = self.Sun_Pos_by_date(sweep_center)
        [ad,azd] = self.Sun_Pos_by_date(sweep_center-timedelta(hours=0.1*az_stride))

        #Diferecnial de rotación
        thd = np.arctan2(azd-az,ad-a)

        #Matriz de rotación
        R = [[np.cos(thd), -np.sin(thd)], [np.sin(thd),np.cos(thd)]]

        vp = []
        for i in range(int(-(n-1)/2),int((n-1)/2+1)):
            for j in range(int(-(m-1)/2),int((m-1)/2+1)):
                vp.append(np.dot((i,j),R))
                x,y = zip(*vp)
        return np.array(x)*az_stride,np.array(y)*el_stride
    
    def __repr__(self):
        return "Mount location:\n Lat: {},\n Lon: {},\n Height: {}".format(self.Lat,self.Lon,self.Height)
        