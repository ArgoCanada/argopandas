CDF       
      	DATE_TIME         	STRING256         STRING64   @   STRING32       STRING8       STRING4       STRING2       N_PROF        N_PARAM       N_LEVELS   ?   N_CALIB          	   title         Argo float vertical profile    institution       CSIO   source        
Argo float     history       f2020-10-31T00:40:36Z creation (software version 1.10 (version 30.06.2020 for ARGO_simplified_profile))     
references        (http://www.argodatamgt.org/Documentation   user_manual_version       1.0    Conventions       Argo-3.1 CF-1.6    featureType       trajectoryProfile      software_version      51.10 (version 30.06.2020 for ARGO_simplified_profile)         :   	DATA_TYPE                  	long_name         	Data type      conventions       Argo reference table 1     
_FillValue                     3?   FORMAT_VERSION                 	long_name         File format version    
_FillValue                    4   HANDBOOK_VERSION               	long_name         Data handbook version      
_FillValue                    4   REFERENCE_DATE_TIME                 	long_name         !Date of reference for Julian days      conventions       YYYYMMDDHHMISS     
_FillValue                    4    DATE_CREATION                   	long_name         Date of file creation      conventions       YYYYMMDDHHMISS     
_FillValue                    40   DATE_UPDATE                 	long_name         Date of update of this file    conventions       YYYYMMDDHHMISS     
_FillValue                    4@   PLATFORM_NUMBER                   	long_name         Float unique identifier    conventions       WMO float identifier : A9IIIII     
_FillValue                    4P   PROJECT_NAME                  	long_name         Name of the project    
_FillValue                  @  4X   PI_NAME                   	long_name         "Name of the principal investigator     
_FillValue                  @  4?   STATION_PARAMETERS                       	long_name         ,List of available parameters for the station   conventions       Argo reference table 3     
_FillValue                    4?   CYCLE_NUMBER               	long_name         Float cycle number     conventions       =0...N, 0 : launch cycle (if exists), 1 : first complete cycle      
_FillValue         ??        5?   	DIRECTION                  	long_name         !Direction of the station profiles      conventions       -A: ascending profiles, D: descending profiles      
_FillValue                    5?   DATA_CENTRE                   	long_name         .Data centre in charge of float data processing     conventions       Argo reference table 4     
_FillValue                    5?   PARAMETER_DATA_MODE                   	long_name         Delayed mode or real time data     conventions       >R : real time; D : delayed mode; A : real time with adjustment     
_FillValue                    5?   PLATFORM_TYPE                     	long_name         Type of float      conventions       Argo reference table 23    
_FillValue                     5?   FLOAT_SERIAL_NO                   	long_name         Serial number of the float     
_FillValue                     6   FIRMWARE_VERSION                  	long_name         Instrument firmware version    
_FillValue                     6(   WMO_INST_TYPE                     	long_name         Coded instrument type      conventions       Argo reference table 8     
_FillValue                    6H   JULD               	long_name         ?Julian day (UTC) of the station relative to REFERENCE_DATE_TIME    standard_name         time   units         "days since 1950-01-01 00:00:00 UTC     conventions       8Relative julian days with decimal part (as parts of day)   
_FillValue        A.?~       axis      T      
resolution        >?E?r?_K        6L   JULD_QC                	long_name         Quality on date and time   conventions       Argo reference table 2     
_FillValue                    6T   JULD_LOCATION                  	long_name         @Julian day (UTC) of the location relative to REFERENCE_DATE_TIME   units         "days since 1950-01-01 00:00:00 UTC     conventions       8Relative julian days with decimal part (as parts of day)   
_FillValue        A.?~       
resolution        >?E?r?_K        6X   LATITUDE               	long_name         &Latitude of the station, best estimate     standard_name         latitude   units         degree_north   
_FillValue        @?i?       	valid_min         ?V?        	valid_max         @V?        axis      Y           6`   	LONGITUDE                  	long_name         'Longitude of the station, best estimate    standard_name         	longitude      units         degree_east    
_FillValue        @?i?       	valid_min         ?f?        	valid_max         @f?        axis      X           6h   POSITION_QC                	long_name         ,Quality on position (latitude and longitude)   conventions       Argo reference table 2     
_FillValue                    6p   POSITIONING_SYSTEM                    	long_name         Positioning system     
_FillValue                    6t   CONFIG_MISSION_NUMBER                  	long_name         :Unique number denoting the missions performed by the float     conventions       !1...N, 1 : first complete mission      
_FillValue         ??        6|   	PARAMETER            
               	long_name         /List of parameters with calibration information    conventions       Argo reference table 3     
_FillValue                    6?   SCIENTIFIC_CALIB_EQUATION            
               	long_name         'Calibration equation for this parameter    
_FillValue                    7?   SCIENTIFIC_CALIB_COEFFICIENT         
               	long_name         *Calibration coefficients for this equation     
_FillValue                    ;?   SCIENTIFIC_CALIB_COMMENT         
               	long_name         .Comment applying to this parameter calibration     
_FillValue                    ??   SCIENTIFIC_CALIB_DATE            
                	long_name         Date of calibration    conventions       YYYYMMDDHHMISS     
_FillValue                  8  C?   PROFILE_PRES_QC                	long_name         #Global quality flag of PRES profile    conventions       Argo reference table 2a    
_FillValue                    C?   PROFILE_TEMP_QC                	long_name         #Global quality flag of TEMP profile    conventions       Argo reference table 2a    
_FillValue                    C?   PROFILE_PSAL_QC                	long_name         #Global quality flag of PSAL profile    conventions       Argo reference table 2a    
_FillValue                    C?   PROFILE_DOXY_QC                	long_name         #Global quality flag of DOXY profile    conventions       Argo reference table 2a    
_FillValue                    C?   PRES         	      
   	long_name         )Sea water pressure, equals 0 at sea-level      standard_name         sea_water_pressure     
_FillValue        G?O?   units         decibar    	valid_min                	valid_max         F;?    C_format      %7.1f      FORTRAN_format        F7.1   
resolution        =???   axis      Z        0  C?   PRES_QC          	         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  ?  F?   PRES_ADJUSTED            	      
   	long_name         )Sea water pressure, equals 0 at sea-level      standard_name         sea_water_pressure     
_FillValue        G?O?   units         decibar    	valid_min                	valid_max         F;?    C_format      %7.1f      FORTRAN_format        F7.1   
resolution        =???   axis      Z        0  G?   PRES_ADJUSTED_QC         	         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  ?  J?   PRES_ADJUSTED_ERROR          	         	long_name         VContains the error on the adjusted values as determined by the delayed mode QC process     
_FillValue        G?O?   units         decibar    C_format      %7.1f      FORTRAN_format        F7.1   
resolution        =???     0  K?   TEMP         	      	   	long_name         $Sea temperature in-situ ITS-90 scale   standard_name         sea_water_temperature      
_FillValue        G?O?   units         degree_Celsius     	valid_min         ?      	valid_max         B      C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     0  N?   TEMP_QC          	         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  ?  R    
TEMP_dPRES           	         	long_name         6TEMP pressure displacement from original sampled value     
_FillValue        G?O?   units         decibar      0  R?   TEMP_ADJUSTED            	      	   	long_name         $Sea temperature in-situ ITS-90 scale   standard_name         sea_water_temperature      
_FillValue        G?O?   units         degree_Celsius     	valid_min         ?      	valid_max         B      C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     0  V   TEMP_ADJUSTED_QC         	         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  ?  YL   TEMP_ADJUSTED_ERROR          	         	long_name         VContains the error on the adjusted values as determined by the delayed mode QC process     
_FillValue        G?O?   units         degree_Celsius     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     0  Z   PSAL         	      	   	long_name         Practical salinity     standard_name         sea_water_salinity     
_FillValue        G?O?   units         psu    	valid_min         @      	valid_max         B$     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     0  ]H   PSAL_QC          	         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  ?  `x   
PSAL_dPRES           	         	long_name         6PSAL pressure displacement from original sampled value     
_FillValue        G?O?   units         decibar      0  aD   PSAL_ADJUSTED            	      	   	long_name         Practical salinity     standard_name         sea_water_salinity     
_FillValue        G?O?   units         psu    	valid_min         @      	valid_max         B$     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     0  dt   PSAL_ADJUSTED_QC         	         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  ?  g?   PSAL_ADJUSTED_ERROR          	         	long_name         VContains the error on the adjusted values as determined by the delayed mode QC process     
_FillValue        G?O?   units         psu    C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     0  hp   DOXY         	      	   	long_name         Dissolved oxygen   standard_name         *moles_of_oxygen_per_unit_mass_in_sea_water     
_FillValue        G?O?   units         micromole/kg   	valid_min         ??     	valid_max         D     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     0  k?   DOXY_QC          	         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  ?  n?   
DOXY_dPRES           	         	long_name         6DOXY pressure displacement from original sampled value     
_FillValue        G?O?   units         decibar      0  o?   DOXY_ADJUSTED            	      	   	long_name         Dissolved oxygen   standard_name         *moles_of_oxygen_per_unit_mass_in_sea_water     
_FillValue        G?O?   units         micromole/kg   	valid_min         ??     	valid_max         D     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     0  r?   DOXY_ADJUSTED_QC         	         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  ?  u?   DOXY_ADJUSTED_ERROR          	         	long_name         VContains the error on the adjusted values as determined by the delayed mode QC process     
_FillValue        G?O?   units         micromole/kg   C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     0  v?Argo synthetic profile          1.0 1.2 19500101000000  20201031004036  20201031004036  2902746 CHINA ARGO PROJECT                                              FEI CHAI                                                        PRES                                                            TEMP                                                            PSAL                                                            DOXY                                                               A   HZ  AAAAPROVOR                          P32826-17CH001                  5900A04                         841 @?o#Eg?1   @?o#Eg?@5$Z?1@b ?t?j1   GPS        PRES                                                            TEMP                                                            PSAL                                                            DOXY                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            DOXY_ADJ = GAIN*DOXY                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            GAIN = 1.0472                                                                                                                                                                                                                                                   none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            GAIN determined from WOA2013 O2sat along the five initial float cycles                                                                                                                                                                                                                                    20200817125145A   A   A   A   ????=???>????L??????@ff@   @@  @Y??@y??@???@???@?33@?33@???@???@???A??A??A??A33A#33Ap  Ax  A?33A?33BffBffB2ffB4ffB\??B^??B???B???B?33B?33B?33B?33B???B???B?ffB?ffB?  B?  B?ffB?ffC?3C33C??C?C??C?C$?3C%33C/  C/? C8?fC9ffCB??CC?CS??CTL?Cm??CnL?C???C?ٚC?ٚC??C??C?L?C??C?Y?C?@ C?? C???C?ٚC?@ C΀ C?ٚC??C??C?Y?C?Y?C???D fD &fD` D? D?3D?3D&fDFfD?D,?D` D? D%?fD%?fD+?3D+?3D29?D2Y?D8L?D8l?D>? D>? DD??DD??DKfDK&fDQL?DQl?DW? DW? D]?fD^fDd,?DdL?Dj` Dj? Dp? Dp? DvٚDv??D}33D}S3D???D???D???D???D??fD??fD?3D?3D?&fD?6fD?C3D?S3D?l?D?|?D???D???D???D???D??fD??fD???D???D?fD?&fD?6fD?FfD?L?D?\?D?l?D?|?D???D???D??3D??3D?? D?? D?3D?3D?  D? D?#3D?33D?FfD?VfD?l?D?|?DɌ?Dɜ?D̬?D̼?D??fD??fD?? D?  D?	?D??D?)?D?9?D?i?D?y?D?vfD߆fD???D???D???D???D???D???D??3D?3D??D?,?D?6fD?FfD?VfD?ffD?i?D?y?111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111????=???>????L??????@ff@   @@  @Y??@y??@???@???@?33@?33@???@???@???A??A??A??A33A#33Ap  Ax  A?33A?33BffBffB2ffB4ffB\??B^??B???B???B?33B?33B?33B?33B???B???B?ffB?ffB?  B?  B?ffB?ffC?3C33C??C?C??C?C$?3C%33C/  C/? C8?fC9ffCB??CC?CS??CTL?Cm??CnL?C???C?ٚC?ٚC??C??C?L?C??C?Y?C?@ C?? C???C?ٚC?@ C΀ C?ٚC??C??C?Y?C?Y?C???D fD &fD` D? D?3D?3D&fDFfD?D,?D` D? D%?fD%?fD+?3D+?3D29?D2Y?D8L?D8l?D>? D>? DD??DD??DKfDK&fDQL?DQl?DW? DW? D]?fD^fDd,?DdL?Dj` Dj? Dp? Dp? DvٚDv??D}33D}S3D???D???D???D???D??fD??fD?3D?3D?&fD?6fD?C3D?S3D?l?D?|?D???D???D???D???D??fD??fD???D???D?fD?&fD?6fD?FfD?L?D?\?D?l?D?|?D???D???D??3D??3D?? D?? D?3D?3D?  D? D?#3D?33D?FfD?VfD?l?D?|?DɌ?Dɜ?D̬?D̼?D??fD??fD?? D?  D?	?D??D?)?D?9?D?i?D?y?D?vfD߆fD???D???D???D???D???D???D??3D?3D??D?,?D?6fD?FfD?VfD?ffD?i?D?y?111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?A?|?A?|?A??qA??7A?x?A?n?A?u?A?~?A?zmA?t?A?v?A?x?A?q?A?ffA?a\A?^5A?_?A?`BA?M?A?;dA?9?A?7LA???A???A?\$A?S?A???A◍AڿoA?O?A?/QA???A?g A??AǛ?A?O?A?§A?~?A???A?p?A???A?t?A???A??#A??sA??^A??<A?l?A?;A??A?/?A?ȴA?JAA?VA???A??!A???A??A?m-A?M?A?=?A??A??A??wA?IA?n?A~?(A~?Ap?PAp=qAckAc+A\5?A\bAQ??AQ?hAF??AFz?A78?A6?yA+laA+/AQ?AoA0?A??AG_A$?A??A?j@???@??@?a?@?@ӗj@?33@ɊS@?X@???@?j@???@???@?\?@?E?@??P@??P@?!?@?
=@?@???@?SW@?E?@?@?@?&?@??@???@??@?^5@??@???@3?@?@t?@s?
@il?@i7L@d#F@d1@_?@^??@[?,@[ƨ@Va?@VE?@PpF@PQ?@Km?@KS?@E޻@E@B??@B?!@?<?@?+@<@<1@84?@8 ?@4??@4?/@0(?@0b@,?t@,z?@(&?@(b@$ݔ@$??@!?@!x?@%?@{@??@??@?<@Ĝ@Ӿ@??@??@??@4@??@\}@S?@?}@?@?@|?@?@{@?L@?@?0@?F@
??@
~?@??@??@r@ff@??@??@? @?j@+?@(?@H@C?@??@~?@?M@?^@ ??@ ?9818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181?       ?L??    ?       ????    ????    ????    ????    ?       ?       ?       ????    ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       A?|?A?|?A??qA??7A?x?A?n?A?u?A?~?A?zmA?t?A?v?A?x?A?q?A?ffA?a\A?^5A?_?A?`BA?M?A?;dA?9?A?7LA???A???A?\$A?S?A???A◍AڿoA?O?A?/QA???A?g A??AǛ?A?O?A?§A?~?A???A?p?A???A?t?A???A??#A??sA??^A??<A?l?A?;A??A?/?A?ȴA?JAA?VA???A??!A???A??A?m-A?M?A?=?A??A??A??wA?IA?n?A~?(A~?Ap?PAp=qAckAc+A\5?A\bAQ??AQ?hAF??AFz?A78?A6?yA+laA+/AQ?AoA0?A??AG_A$?A??A?j@???@??@?a?@?@ӗj@?33@ɊS@?X@???@?j@???@???@?\?@?E?@??P@??P@?!?@?
=@?@???@?SW@?E?@?@?@?&?@??@???@??@?^5@??@???@3?@?@t?@s?
@il?@i7L@d#F@d1@_?@^??@[?,@[ƨ@Va?@VE?@PpF@PQ?@Km?@KS?@E޻@E@B??@B?!@?<?@?+@<@<1@84?@8 ?@4??@4?/@0(?@0b@,?t@,z?@(&?@(b@$ݔ@$??@!?@!x?@%?@{@??@??@?<@Ĝ@Ӿ@??@??@??@4@??@\}@S?@?}@?@?@|?@?@{@?L@?@?0@?F@
??@
~?@??@??@r@ff@??@??@? @?j@+?@(?@H@C?@??@~?@?M@?^@ ??@ ?9818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?BDBDBoB\B@BoBB\B?BoBoBoB?B?B?BhBhBhBnBuBuBuBB?Bb?BffB?B?BP@BR?B\?B]/BZFBZBY$BYB\?B]/BWcBW
BW
BW
BS%BR?BMBL?B=<B<jB'?B&?B?[B??B? B?jB??B?7BcLBaHBI?BH?B?B?B ?B  B
??B
?B
??B
?VB
3B
1'B	??B	?mB	?NB	?qB	?BB	?B	O?B	N?B	?B	DB?$B?NB?/B?dB?BB??B??B?B|B{?B??B?%B} B|?Bv?Bv?B??B?=B?PB??B?B??B	?B	B	B	B	B	%B	">B	"?B	>?B	?}B	K?B	K?B	Z?B	[#B	c*B	cTB	n^B	n?B	q?B	q?B	??B	?B	?!B	??B	??B	??B	??B	?B	?B	?3B	?:B	?dB	?nB	ŢB	ΪB	??B	??B	?B	?$B	?HB	?LB	?fB	?jB	??B	??B	??B	??B	??B
?B
B

B

=B
EB
oB
uB
?B
?B
?B
"?B
"?B
)?B
)?B
0 B
0!B
1"B
1'B
3)B
33B
44B
49B
7<B
7LB
=RB
=qB
AtB
A?B
F?B
F?B
I?B
I?B
J?B
J?B
N?B
N?B
T?B
T?B
[B
[#B
^%B
^5B
`8B
`BB
bDB
bNB
dPB
dZB
e[B
e`B
faB
ffB
hhB
hs818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181?       ?L??    ?       ????    ????    ????    ????    ?       ?       ?       ????    ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       BDBDBoB\B@BoBB\B?BoBoBoB?B?B?BhBhBhBnBuBuBuBB?Bb?BffB?B?BP@BR?B\?B]/BZFBZBY$BYB\?B]/BWcBW
BW
BW
BS%BR?BMBL?B=<B<jB'?B&?B?[B??B? B?jB??B?7BcLBaHBI?BH?B?B?B ?B  B
??B
?B
??B
?VB
3B
1'B	??B	?mB	?NB	?qB	?BB	?B	O?B	N?B	?B	DB?$B?NB?/B?dB?BB??B??B?B|B{?B??B?%B} B|?Bv?Bv?B??B?=B?PB??B?B??B	?B	B	B	B	B	%B	">B	"?B	>?B	?}B	K?B	K?B	Z?B	[#B	c*B	cTB	n^B	n?B	q?B	q?B	??B	?B	?!B	??B	??B	??B	??B	?B	?B	?3B	?:B	?dB	?nB	ŢB	ΪB	??B	??B	?B	?$B	?HB	?LB	?fB	?jB	??B	??B	??B	??B	??B
?B
B

B

=B
EB
oB
uB
?B
?B
?B
"?B
"?B
)?B
)?B
0 B
0!B
1"B
1'B
3)B
33B
44B
49B
7<B
7LB
=RB
=qB
AtB
A?B
F?B
F?B
I?B
I?B
J?B
J?B
N?B
N?B
T?B
T?B
[B
[#B
^%B
^5B
`8B
`BB
bDB
bNB
dPB
dZB
e[B
e`B
faB
ffB
hhB
hs818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?C9??G?O?C:??G?O?C:[?G?O?C:
?G?O?C:NG?O?C:?G?O?C:wG?O?C:IyG?O?C:(?G?O?C:H1G?O?C:=?G?O?C:pbG?O?C;??G?O?CCPbG?O?CH?yG?O?CK?)G?O?CL ?G?O?CI??G?O?CE??G?O?CAq?G?O?CA?G?O?CA?G?O?CA\G?O?C</?G?O?C7"?G?O?C9J?G?O?C;Q'G?O?C>?G?O?C?? G?O?C???G?O?CB??G?O?CD?;G?O?CBG?G?O?C??G?O?C<ҰG?O?C;xRG?O?C8??G?O?C6??G?O?C2R?G?O?C+w
G?O?CY?G?O?C?hG?O?C??G?O?C?G?O?B??FG?O?B?,?G?O?B??G?O?B?ؓG?O?B??G?O?B???G?O?B?1'G?O?BvhG?O?Bs??G?O?Bo??G?O?Bh?}G?O?BfS?G?O?Bb??G?O?BZ?5G?O?BVG?O?BOS?G?O?BG?FG?O?BAbG?O?BEm?G?O?BI?G?O?BN?G?O?BP%?G?O?BTJ?G?O?BZbG?O?B`M?G?O?Bg??G?O?BlĜG?O?Bq?G?O?Bx?hG?O?B~x?G?O?B??G?O?B?gmG?O?B?I7G?O?B?;?G?O?B?:^G?O?B???G?O?B??1G?O?B?PbG?O?B??uG?O?B??DG?O?B?-G?O?B?XG?O?B???G?O?B??G?O?B?\?G?O?B??3G?O?B?{?G?O?B??G?O?B?G?O?B??G?O?B?yXG?O?B?Q?G?O?B?ffG?O?B?ɺG?O?B?o?G?O?B??oG?O?B??VG?O?Bѐ?G?O?3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3     G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?    G?O?CB??G?O?CC
?G?O?CC(4G?O?CB?:G?O?CB?aG?O?CB??G?O?CB??G?O?CC?G?O?CB??G?O?CC?G?O?CC?G?O?CC=?G?O?CDi`G?O?CL??G?O?CRe?G?O?CU{?G?O?CU?G?O?CS)?G?O?CN??G?O?CJ??G?O?CJ??G?O?CJ?sG?O?CJ,?G?O?CEDG?O?C???G?O?CB
)G?O?CD)	G?O?CF?"G?O?CH?pG?O?CI?G?O?CK?5G?O?CM??G?O?CKs?G?O?CH	|G?O?CE??G?O?CDRG?O?CA??G?O?C?SG?O?C:?#G?O?C3?VG?O?C$?NG?O?C?%G?O?C??G?O?C?AG?O?B?7?G?O?B??G?O?B?*NG?O?B?JG?O?B?nMG?O?B??G?O?B?J?G?O?B?׬G?O?Br?G?O?Bz?&G?O?Bs?qG?O?Bq3?G?O?Bm?G?O?Be3hG?O?B`pG?O?BY?G?O?BQ#?G?O?BJ-?G?O?BN??G?O?BS`?G?O?BWՐG?O?BY??G?O?B^PzG?O?Bd[?G?O?Bj??G?O?Br??G?O?Bw?&G?O?B|??G?O?B?&?G?O?B?>+G?O?B?W6G?O?B??'G?O?B?G?O?B?G?G?O?B?vAG?O?B??EG?O?B?/G?O?B??G?O?B???G?O?B?hG?O?B?nG?O?B?2xG?O?B??3G?O?B?@G?O?B??=G?O?B?G2G?O?B?%uG?O?B?9G?O?B?kG?O?B??G?O?B??'G?O?B??
G?O?B? ?G?O?B?t?G?O?B?.?G?O?B٢"G?O?Bک?G?O?B?u?G?O?1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 @?K"G?O?@?C?G?O?@?CIG?O?@?;{G?O?@?8?G?O?@?3?G?O?@?3?G?O?@?0>G?O?@?(?G?O?@?,?G?O?@?)|G?O?@??G?O?@?G?O?@??G?O?@???G?O?@?t?G?O?@??G?O?@?b?G?O?@??EG?O?@???G?O?@?L?G?O?@?F?G?O?@??G?O?@???G?O?@???G?O?@???G?O?@?]G?O?@??G?O?@?2nG?O?@??CG?O?@?*?G?O?@???G?O?@???G?O?@?EsG?O?@???G?O?@?FG?O?@?:G?O?@?ЗG?O?@??kG?O?@??G?O?@?)gG?O?@Ř?G?O?@Ǎ?G?O?@ȯ?G?O?@ʆXG?O?@??G?O?@?ݭG?O?@??~G?O?@Т?G?O?@??G?O?@?iG?O?@?D?G?O?@Ҋ-G?O?@?~rG?O?@ңyG?O?@?E?G?O?@?JG?O?@???G?O?@??G?O?@???G?O?@ҙpG?O?@ҵ?G?O?@??%G?O?@?k3G?O?@??G?O?@єgG?O?@?D?G?O?@??lG?O?@С?G?O?@?OwG?O?@???G?O?@?TlG?O?@??EG?O?@?q?G?O?@??VG?O?@͘?G?O?@?'?G?O?@?ĜG?O?@?LoG?O?@?׮G?O?@?cMG?O?@???G?O?@?\?G?O?@ɺ?G?O?@?0BG?O?@Ȉ?G?O?@???G?O?@?wTG?O?@??pG?O?@?@YG?O?@ūvG?O?@?	G?O?@?m?G?O?@??G?O?@?_?G?O?@¿?G?O?@?#G?O?@??G?O?@???G?O?@?E?G?O?@??EG?O?@??G?O?