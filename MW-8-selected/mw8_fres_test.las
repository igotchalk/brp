~Version
#MNEM .UNIT                VALUE  : DESCRIPTION                    
 VERS .                      2.0  : CWLS LOG ASCII STANDARD - VERSION 2.0 
 WRAP .                       NO  : ONE LINE PER DEPTH STEP        
~Well
#MNEM .UNIT           VALUE  : DESCRIPTION                    
 STRT  .F               20.0  : Start Depth                    
 STOP  .F               40.0  : Stop Depth                     
 STEP  .F               0.25  : Step                           
 NULL  .             -999.25  : Null Value                     
 COMP  .                      : Company                        
 WELL  .                      : Well                           
 FLD   .                      : Field                          
 SEC   .                      : Section                        
 TOWN  .                      : Township (e.g. 42S)            
 RANG  .                      : Range  (e.g. 25E)              
 LOC   .                      : Location (Sec Town Range)      
 LOC1  .                      : Location 1 (quarter calls)     
 LOC2  .                      : Location 2 (footages)          
 PROV  .                      : Province                       
 CTRY  .                      : Country                        
 STAT  .                      : State                          
 CNTY  .                      : County                         
 API   .                      : API-Number                     
 UWI   .                      : Unique Well ID                 
 SRVC  .                      : Service Company                
 LIC   .                      : Licence Number                 
 DATE  .                      : Date preferred format is MM/DD/YYYY 
 LATI  .DEG                   : Latitude                       
 LONG  .DEG                   : Longitude                      
 GDAT  .               NAD27  : Geodetic Datum                 
 X     .                      : X or East-West coordinate      
 Y     .                      : Y or North South coordinate    
 HZCS  .                 UTM  : Horizontal Co-ordinate System  
 UTM   .                      : UTM Location                   
 STUS  .                      : Well Status                    
~Parameter
#MNEM .UNIT           VALUE  : DESCRIPTION                    
 EGL   .F                     : Ground Level Elevation         
 EKB   .F                     : Kelly Bushing Elevation        
 EDF   .F                     : Derrick Floor Elevation        
 ERT   .F                     : Rotary Table Elevation         
 TDL   .F                     : Total Depth Logger             
 TDD   .F                     : Total Depth Driller            
 CSGL  .F                     : Casing Bottom Logger           
 CSGD  .F                     : Casing Bottom Driller          
 CSGS  .IN                    : Casing Size                    
 CSGW  .LB                    : Casing Weight                  
 BS    .IN                    : Bit Size                       
 DFT   .                      : Mud type                       
 MSS   .                      : Mud Sample Source              
 DFD   .gm/cc                 : Mud Density                    
 DFV   .s/qt                  : Mud Viscosity (Funnel)         
 DFL   .cc                    : Fluid Loss                     
 PH    .                      : PH                             
 RM    .OHM-M                 : Resistivity of Mud             
 MST   .DEG-F                 : Temperature of Mud             
 RMF   .OHM-M                 : Resistivity of Mud Filtrate    
 MFT   .DEG-F                 : Temperature of Mud Filtrate    
 RMC   .OHM-M                 : Resistivity of Mud Cake        
 MCST  .DEG-F                 : Temperature of Mud Cake        
 BHT   .DEG-F                 : Maximum Recorded Temperature   
 RMB   .OHM-M                 : Resitivity @ BHT               
 TIMC  .DATE                  : Date/Time Circulation Stopped  
 TIML  .DATE                  : Date/Time Logger Tagged Bottom 
 UNIT  .                      : Logging Unit Number            
 BASE  .                      : Home Base of Logging Unit      
 ENG   .                      : Recording Engineer             
 WIT   .                      : Witnessed By                   
~Curve
#MNEM .UNIT           VALUE  : DESCRIPTION                    
 DEPT  .F                     : Depth                          
 FRES  .OHM-M                 : Fluid Resistivity              
~ASCII  DEPT FRES
 20.0 23.887
 20.25 23.845
 20.5 23.803
 20.75 23.761
 21.0 23.718
 21.25 23.676
 21.5 23.634
 21.75 23.592
 22.0 23.558
 22.25 23.561
 22.5 23.564
 22.75 23.566
 23.0 23.569
 23.25 23.571
 23.5 23.574
 23.75 23.577
 24.0 23.579
 24.25 23.582
 24.5 23.585
 24.75 23.587
 25.0 23.59
 25.25 23.592
 25.5 23.595
 25.75 23.598
 26.0 23.6
 26.25 23.603
 26.5 23.605
 26.75 23.608
 27.0 23.611
 27.25 23.613
 27.5 23.616
 27.75 23.618
 28.0 23.621
 28.25 23.624
 28.5 23.626
 28.75 23.629
 29.0 23.631
 29.25 23.634
 29.5 23.621
 29.75 23.597
 30.0 23.573
 30.25 23.549
 30.5 23.525
 30.75 23.501
 31.0 23.478
 31.25 23.454
 31.5 23.43
 31.75 23.406
 32.0 23.382
 32.25 23.358
 32.5 23.334
 32.75 23.31
 33.0 23.238
 33.25 23.165
 33.5 23.091
 33.75 23.018
 34.0 22.945
 34.25 22.871
 34.5 22.798
 34.75 22.725
 35.0 22.652
 35.25 22.578
 35.5 22.505
 35.75 22.432
 36.0 22.358
 36.25 22.285
 36.5 22.212
 36.75 22.139
 37.0 22.024
 37.25 21.854
 37.5 21.685
 37.75 21.515
 38.0 21.346
 38.25 21.176
 38.5 21.007
 38.75 20.837
 39.0 20.667
 39.25 20.529
 39.5 20.41
 39.75 -999.25
 40.0 -999.25
