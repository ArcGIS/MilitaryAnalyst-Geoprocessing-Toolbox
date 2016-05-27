# coding: utf-8
# -----------------------------------------------------------------------------
# Copyright 2016 Esri
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------

# ==================================================
# TableToPointTestCase.py
# --------------------------------------------------
# requirements:
# * ArcGIS Desktop 10.X+ or ArcGIS Pro 1.X+
# * Python 2.7 or Python 3.4
#
# author: ArcGIS Solutions
# company: Esri
#
# ==================================================
# history:
# 5/18/2016 - DJH - initial creation
# 5/26/2016 - MF - change unittest fail pattern to catch tool errors
# ==================================================

import unittest
import arcpy
import os
import UnitTestUtilities
import Configuration

class RadialLineOfSightTestCase(unittest.TestCase):
    ''' Test all tools and methods related to the Radial Line Of Sight tool
    in the Military Tools toolbox'''

    inputTable = None
    outputPoints = None

    def setUp(self):
        ''' RadialLineOfSightTestCase.setUp '''
        if Configuration.DEBUG == True: print(".....RadialLineOfSightTestCase.setUp")

        UnitTestUtilities.checkArcPy()
        if(Configuration.militaryScratchGDB == None) or (not arcpy.Exists(Configuration.militaryScratchGDB)):
            Configuration.militaryScratchGDB = UnitTestUtilities.createScratch(Configuration.militaryDataPath)
            arcpy.env.scratchWorkspace = Configuration.militaryScratchGDB

        self.observers = os.path.join(Configuration.militaryInputDataGDB, "Observers")
        self.inputSurface = os.path.join(Configuration.militaryInputDataGDB, "ElevationUTM_Zone10")
        self.outputRLOS = os.path.join(Configuration.militaryScratchGDB, "outputRadialLineOfSight")

        if arcpy.CheckExtension("Spatial") == "Available":
            arcpy.CheckOutExtension("Spatial")
            arcpy.AddMessage("Spatial checked out")

    def tearDown(self):
        ''' RadialLineOfSightTestCase.tearDown '''
        if Configuration.DEBUG == True: print(".....RadialLineOfSightTestCase.tearDown")
        arcpy.CheckInExtension("Spatial");
        UnitTestUtilities.deleteScratch(Configuration.militaryScratchGDB)

    def test_radial_line_of_sight_desktop(self):
        ''' Testing the Radial Line Of Sight tool for ArcGIS for Desktop '''
        try:
            runToolMessage = ".....RadialLineOfSightTestCase.test_radial_line_of_sight_desktop"
            arcpy.ImportToolbox(Configuration.military_DesktopToolboxPath, "mt")
            print(runToolMessage)
            Configuration.Logger.info(runToolMessage)

            arcpy.RadialLineOfSight_mt(self.observers, self.inputSurface, self.outputRLOS)
            featureCount = int(arcpy.GetCount_management(self.outputRLOS).getOutput(0))
        
            self.assertTrue(arcpy.Exists(self.outputRLOS))
            self.assertEqual(featureCount, int(3501))
    
        except arcpy.ExecuteError:
            self.fail(arcpy.GetMessages())
            UnitTestUtilities.handleArcPyError()
        except:
            self.fail("FAIL: " + runToolMessage)
            UnitTestUtilities.handleGeneralError()
        
    def test_radial_line_of_sight_pro(self):
        ''' Testing the Radial Line Of Sight tool for ArcGIS Pro '''
        try:
            runToolMessage = ".....RadialLineOfSightTestCase.test_radial_line_of_sight_pro"
            arcpy.ImportToolbox(Configuration.military_ProToolboxPath, "mt")
            print(runToolMessage)
            Configuration.Logger.info(runToolMessage)

            arcpy.RadialLineOfSight_mt(self.observers, self.inputSurface, self.outputRLOS)
            featureCount = int(arcpy.GetCount_management(self.outputRLOS).getOutput(0))
        
            self.assertTrue(arcpy.Exists(self.outputRLOS))
            self.assertEqual(featureCount, int(3501))
    
        except arcpy.ExecuteError:
            self.fail(arcpy.GetMessages())
            UnitTestUtilities.handleArcPyError()
        except:
            self.fail("FAIL: " + runToolMessage)
            UnitTestUtilities.handleGeneralError()

    # def test_radial_line_of_sight_desktop(self):
    #     arcpy.AddMessage(".....Testing Radial Line Of Sight (Desktop).")
    #     self.test_radial_line_of_sight(Configuration.military_DesktopToolboxPath)
            
    # def test_radial_line_of_sight_pro(self):
    #     arcpy.AddMessage(".....Testing Radial Line Of Sight (Pro).")
    #     self.test_radial_line_of_sight(Configuration.military_ProToolboxPath)

    # def test_radial_line_of_sight(self, toolboxPath):
    #     try:
    #         arcpy.ImportToolbox(toolboxPath, "mt")
    #         runToolMessage = ".....RadialLineOfSightTestCase.test_Radial_line_of_sight"
    #         print(runToolMessage)
    #         Configuration.Logger.info(runToolMessage)
    # 
    #         arcpy.RadialLineOfSight_mt(self.observers, self.inputSurface, self.outputRLOS)
    #         featureCount = int(arcpy.GetCount_management(self.outputRLOS).getOutput(0))
    #     
    #         self.assertTrue(arcpy.Exists(self.outputRLOS))
    #         self.assertEqual(featureCount, int(3501))
    # 
    #     except arcpy.ExecuteError:
    #         print(".....test_radial_line_of_sight.arcpy.ExecuteError.....")
    #         print("self: " + str(self))
    #         # these guys crash the except:
    #         #self.fail()
    #         self.fail("test_radial_line_of_sight failed")
    #         #self.fail("test_radial_line_of_sight failed".encode(encoding='ascii'))
    #         #self.fail("test_radial_line_of_sight failed".encode(encoding='utf-8'))
    #         #self.fail(arcpy.GetMessages())
    #         #UnitTestUtilities.handleArcPyError()
    #     except:
    #         UnitTestUtilities.handleGeneralError()
