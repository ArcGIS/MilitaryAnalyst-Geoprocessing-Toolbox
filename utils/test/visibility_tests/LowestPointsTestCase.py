# coding: utf-8
'''
-----------------------------------------------------------------------------
Copyright 2016 Esri
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-----------------------------------------------------------------------------

==================================================
LowestPointsTestCase.py
--------------------------------------------------
requirements:
* ArcGIS Desktop 10.X+ or ArcGIS Pro 1.X+
* Python 2.7 or Python 3.4

author: ArcGIS Solutions
company: Esri

==================================================
history:
5/11/2016 - JH - initial creation
5/31/2016 - MF - change error handling
==================================================
'''

import os
import unittest

import arcpy

# Add parent folder to python path if running test case standalone
import sys
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), '..')))

import UnitTestUtilities
import Configuration

class LowestPointsTestCase(unittest.TestCase):
    ''' Test all tools and methods related to the Lowest Points tool
    in the Military Tools toolbox'''

    inputArea = None
    inputSurface = None
    outputPoints = None

    def setUp(self):
        ''' Initialization needed if running Test Case standalone '''
        Configuration.GetLogger()
        Configuration.GetPlatform()
        ''' End standalone initialization '''
            
        Configuration.Logger.debug(".....LowestPointsTestCase.setUp")

        UnitTestUtilities.checkArcPy()
        if not arcpy.Exists(Configuration.militaryScratchGDB):
            Configuration.militaryScratchGDB = UnitTestUtilities.createScratch(Configuration.currentPath)

        self.inputArea = os.path.join(Configuration.militaryInputDataGDB, "AreaofInterest")
        self.inputSurface = os.path.join(Configuration.militaryInputDataGDB, "ElevationUTM_Zone10")

        UnitTestUtilities.checkGeoObjects([Configuration.toolboxUnderTest, \
            self.inputArea, self.inputSurface])

        self.outputPoints = os.path.join(Configuration.militaryScratchGDB, "outputLowestPoints")

        if arcpy.CheckExtension("Spatial") == "Available":
            arcpy.CheckOutExtension("Spatial")
            arcpy.AddMessage("Spatial checked out")

        arcpy.ImportToolbox(Configuration.toolboxUnderTest)  

    def tearDown(self):
        Configuration.Logger.debug(".....LowestPointsTestCase.tearDown")
        arcpy.CheckInExtension("Spatial");
        # UnitTestUtilities.deleteScratch(Configuration.militaryScratchGDB)

    def test_lowest_points(self):
        ''' Test Lowest Points tool in ArcGIS Desktop '''
        Configuration.Logger.info("...LowestPointsTestCase.test_lowest_points")

        arcpy.env.overwriteOutput = True

        arcpy.LowestPoints_mt(self.inputArea, self.inputSurface, self.outputPoints)
        self.assertTrue(arcpy.Exists(self.outputPoints), "Output dataset does not exist or was not created")
        pointCount = int(arcpy.GetCount_management(self.outputPoints).getOutput(0))
        expectedFeatures = int(6)
        self.assertEqual(pointCount, expectedFeatures, "Expected %s features, but got %s" % (str(expectedFeatures), str(pointCount)))
        return
        
if __name__ == "__main__":
    unittest.main()