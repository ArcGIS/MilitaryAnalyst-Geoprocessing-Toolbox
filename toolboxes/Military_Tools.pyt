# coding: utf-8
'''
------------------------------------------------------------------------------
 Copyright 2017-2018 Esri
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
   http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
------------------------------------------------------------------------------
 ==================================================
 Military_Tools.pyt
 --------------------------------------------------
 requirements: ArcGIS 10.3.1+, ArcGIS Pro 2.1+
 author: ArcGIS Solutions
 contact: support@esri.com
 company: Esri
 ==================================================
 description: 
 Python toolbox container for Military Tools.
 ==================================================
'''

from scripts.ConversionTools import *
from scripts.GRGTools import *
from scripts.VisTools import *

class Toolbox(object):
    '''
    Military Tools Toolbox class container.
    '''

    def __init__(self):
        ''' constructor '''
        self.label = "Military Tools for ArcGIS"
        self.alias = "mt"
        self.description = "A Geoprocessing Toolbox for ArcGIS for Desktop that contains collections of tools to import geometry from tables, determine ranges, and provide basic visibility analysis capabilities."

        self.tools = [CreateGRGFromArea,
					CreateGRGFromPoint,
					CreateReferenceSystemGRGFromArea,
					AddLinearLineOfSightFields,
					AddRadialLineOfSightObserverFields,
					RadialLineOfSightAndRange,
					TableToPolygon]

