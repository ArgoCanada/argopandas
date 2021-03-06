CDF      
      	DATE_TIME         STRING2       STRING4       STRING8       STRING16      STRING32       STRING64   @   	STRING256         N_PROF        N_PARAM       N_LEVELS   e   N_CALIB       	N_HISTORY             	   title         Argo float vertical profile    institution       CSIO   source        
Argo float     history       2018-05-24T06:28:07Z creation      
references        (http://www.argodatamgt.org/Documentation   comment       	free text      user_manual_version       3.1    Conventions       Argo-3.1 CF-1.6    featureType       trajectoryProfile         @   	DATA_TYPE                  	long_name         	Data type      conventions       Argo reference table 1     
_FillValue                    6?   FORMAT_VERSION                 	long_name         File format version    
_FillValue                    6?   HANDBOOK_VERSION               	long_name         Data handbook version      
_FillValue                    6?   REFERENCE_DATE_TIME                 	long_name         !Date of reference for Julian days      conventions       YYYYMMDDHHMISS     
_FillValue                    6?   DATE_CREATION                   	long_name         Date of file creation      conventions       YYYYMMDDHHMISS     
_FillValue                    6?   DATE_UPDATE                 	long_name         Date of update of this file    conventions       YYYYMMDDHHMISS     
_FillValue                    6?   PLATFORM_NUMBER                   	long_name         Float unique identifier    conventions       WMO float identifier : A9IIIII     
_FillValue                    6?   PLATFORM_TYPE                     	long_name         Type of float      conventions       Argo reference table 23    
_FillValue                     6?   PROJECT_NAME                  	long_name         Name of the project    
_FillValue                  @  7   PI_NAME                   	long_name         "Name of the principal investigator     
_FillValue                  @  7X   STATION_PARAMETERS           	            	long_name         ,List of available parameters for the station   conventions       Argo reference table 3     
_FillValue                  0  7?   CYCLE_NUMBER               	long_name         Float cycle number     conventions       =0...N, 0 : launch cycle (if exists), 1 : first complete cycle      
_FillValue         ??        7?   	DIRECTION                  	long_name         !Direction of the station profiles      conventions       -A: ascending profiles, D: descending profiles      
_FillValue                    7?   DATA_CENTRE                   	long_name         .Data centre in charge of float data processing     conventions       Argo reference table 4     
_FillValue                    7?   DC_REFERENCE                  	long_name         (Station unique identifier in data centre   conventions       Data centre convention     
_FillValue                     7?   DATA_STATE_INDICATOR                  	long_name         1Degree of processing the data have passed through      conventions       Argo reference table 6     
_FillValue                    7?   	DATA_MODE                  	long_name         Delayed mode or real time data     conventions       >R : real time; D : delayed mode; A : real time with adjustment     
_FillValue                    7?   FLOAT_SERIAL_NO                   	long_name         Serial number of the float     
_FillValue                     7?   FIRMWARE_VERSION                  	long_name         Instrument firmware version    
_FillValue                     8   WMO_INST_TYPE                     	long_name         Coded instrument type      conventions       Argo reference table 8     
_FillValue                    8<   JULD               	long_name         ?Julian day (UTC) of the station relative to REFERENCE_DATE_TIME    standard_name         time   units         "days since 1950-01-01 00:00:00 UTC     conventions       8Relative julian days with decimal part (as parts of day)   
resolution        >?E?r?_K   
_FillValue        A.?~       axis      T           8@   JULD_QC                	long_name         Quality on date and time   conventions       Argo reference table 2     
_FillValue                    8H   JULD_LOCATION                  	long_name         @Julian day (UTC) of the location relative to REFERENCE_DATE_TIME   units         "days since 1950-01-01 00:00:00 UTC     conventions       8Relative julian days with decimal part (as parts of day)   
resolution        >?E?r?_K   
_FillValue        A.?~            8L   LATITUDE               	long_name         &Latitude of the station, best estimate     standard_name         latitude   units         degree_north   
_FillValue        @?i?       	valid_min         ?V?        	valid_max         @V?        axis      Y           8T   	LONGITUDE                  	long_name         'Longitude of the station, best estimate    standard_name         	longitude      units         degree_east    
_FillValue        @?i?       	valid_min         ?f?        	valid_max         @f?        axis      X           8\   POSITION_QC                	long_name         ,Quality on position (latitude and longitude)   conventions       Argo reference table 2     
_FillValue                    8d   POSITIONING_SYSTEM                    	long_name         Positioning system     
_FillValue                    8h   PROFILE_PRES_QC                	long_name         #Global quality flag of PRES profile    conventions       Argo reference table 2a    
_FillValue                    8p   PROFILE_TEMP_QC                	long_name         #Global quality flag of TEMP profile    conventions       Argo reference table 2a    
_FillValue                    8t   PROFILE_PSAL_QC                	long_name         #Global quality flag of PSAL profile    conventions       Argo reference table 2a    
_FillValue                    8x   VERTICAL_SAMPLING_SCHEME                  	long_name         Vertical sampling scheme   conventions       Argo reference table 16    
_FillValue                    8|   CONFIG_MISSION_NUMBER                  	long_name         :Unique number denoting the missions performed by the float     conventions       !1...N, 1 : first complete mission      
_FillValue         ??        9|   PRES         
      
   	long_name         )Sea water pressure, equals 0 at sea-level      standard_name         sea_water_pressure     
_FillValue        G?O?   units         decibar    	valid_min                	valid_max         F;?    C_format      %7.1f      FORTRAN_format        F7.1   
resolution        =???   axis      Z        ?  9?   PRES_QC          
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  h  ;   PRES_ADJUSTED            
      	   	long_name         )Sea water pressure, equals 0 at sea-level      standard_name         sea_water_pressure     
_FillValue        G?O?   units         decibar    	valid_min                	valid_max         F;?    C_format      %7.1f      FORTRAN_format        F7.1   
resolution        =???     ?  ;|   PRES_ADJUSTED_QC         
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  h  =   PRES_ADJUSTED_ERROR          
         	long_name         VContains the error on the adjusted values as determined by the delayed mode QC process     
_FillValue        G?O?   units         decibar    C_format      %7.1f      FORTRAN_format        F7.1   
resolution        =???     ?  =x   TEMP         
      	   	long_name         $Sea temperature in-situ ITS-90 scale   standard_name         sea_water_temperature      
_FillValue        G?O?   units         degree_Celsius     	valid_min         ?      	valid_max         B      C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     ?  ?   TEMP_QC          
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  h  @?   TEMP_ADJUSTED            
      
   	long_name         $Sea temperature in-situ ITS-90 scale   standard_name         sea_water_temperature      
_FillValue        G?O?   units         degree_Celsius     	valid_min         ?      	valid_max         B      comment       In situ measurement    C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     ?  A   TEMP_ADJUSTED_QC         
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  h  B?   TEMP_ADJUSTED_ERROR          
         	long_name         VContains the error on the adjusted values as determined by the delayed mode QC process     
_FillValue        G?O?   units         degree_Celsius     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     ?  C   PSAL         
      	   	long_name         Practical salinity     standard_name         sea_water_salinity     
_FillValue        G?O?   units         psu    	valid_min         @      	valid_max         B$     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     ?  D?   PSAL_QC          
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  h  F,   PSAL_ADJUSTED            
      	   	long_name         Practical salinity     standard_name         sea_water_salinity     
_FillValue        G?O?   units         psu    	valid_min         @      	valid_max         B$     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     ?  F?   PSAL_ADJUSTED_QC         
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  h  H(   PSAL_ADJUSTED_ERROR          
         	long_name         VContains the error on the adjusted values as determined by the delayed mode QC process     
_FillValue        G?O?   units         psu    C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     ?  H?   	PARAMETER               	            	long_name         /List of parameters with calibration information    conventions       Argo reference table 3     
_FillValue                  0  J$   SCIENTIFIC_CALIB_EQUATION               	            	long_name         'Calibration equation for this parameter    
_FillValue                    JT   SCIENTIFIC_CALIB_COEFFICIENT            	            	long_name         *Calibration coefficients for this equation     
_FillValue                    MT   SCIENTIFIC_CALIB_COMMENT            	            	long_name         .Comment applying to this parameter calibration     
_FillValue                    PT   SCIENTIFIC_CALIB_DATE               	             	long_name         Date of calibration    conventions       YYYYMMDDHHMISS     
_FillValue                  ,  ST   HISTORY_INSTITUTION                      	long_name         "Institution which performed action     conventions       Argo reference table 4     
_FillValue                    S?   HISTORY_STEP                     	long_name         Step in data processing    conventions       Argo reference table 12    
_FillValue                    S?   HISTORY_SOFTWARE                     	long_name         'Name of software which performed action    conventions       Institution dependent      
_FillValue                    S?   HISTORY_SOFTWARE_RELEASE                     	long_name         2Version/release of software which performed action     conventions       Institution dependent      
_FillValue                    S?   HISTORY_REFERENCE                        	long_name         Reference of database      conventions       Institution dependent      
_FillValue                  @  S?   HISTORY_DATE                      	long_name         #Date the history record was created    conventions       YYYYMMDDHHMISS     
_FillValue                    S?   HISTORY_ACTION                       	long_name         Action performed on data   conventions       Argo reference table 7     
_FillValue                    S?   HISTORY_PARAMETER                        	long_name         (Station parameter action is performed on   conventions       Argo reference table 3     
_FillValue                    S?   HISTORY_START_PRES                    	long_name          Start pressure action applied on   
_FillValue        G?O?   units         decibar         S?   HISTORY_STOP_PRES                     	long_name         Stop pressure action applied on    
_FillValue        G?O?   units         decibar         S?   HISTORY_PREVIOUS_VALUE                    	long_name         +Parameter/Flag previous value before action    
_FillValue        G?O?        S?   HISTORY_QCTEST                       	long_name         <Documentation of tests performed, tests failed (in hex form)   conventions       EWrite tests performed when ACTION=QCP$; tests failed when ACTION=QCF$      
_FillValue                    T Argo profile    3.1 1.2 19500101000000  20180524062807  20180524062807  2902746 PROVOR                          CHINA ARGO PROJECT                                              FEI CHAI                                                        PRES            TEMP            PSAL               A   HZ  0421_32826001_001               2B  A   P32826-17CH001                  5900A04                         841 @?eR?1   @?eR?@4??1'@bB$?/?1   GPS     A   A   A   Primary sampling: averaged []                                                                                                                                                                                                                                      >L???fff??33@9??@?  @?  @?  @?33A33A??Aq??A͙?B33B6ffB^ffB???B?33B?33B?33Bҙ?B?  B?ffCL?CL?CL?C&?C/  C9ffCCL?CT?fCm?3C?Y?C??C?? C?  C?s3C?ٚCΙ?C??C?L?C?ٚD ?3Dy?D??D?D  Dl?D%??D,fD2y?D8l?D>??DE?DKFfDQy?DW??D]?fDd  Djl?Dp??Dw  D}3D?? D?ٚD??3D?  D?FfD?Y?D?s3D???D???D??3D?  D?  D?6fD?\?D??3D??fD?ٚD?? D?? D??D?9?D?VfD?vfD?? D̶fD??fD?  D??D?@ D?` D?|?D??fD???D???D?  D?fD?I?D?l?D??f11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111   >L???fff??33@9??@?  @?  @?  @?33A33A??Aq??A͙?B33B6ffB^ffB???B?33B?33B?33Bҙ?B?  B?ffCL?CL?CL?C&?C/  C9ffCCL?CT?fCm?3C?Y?C??C?? C?  C?s3C?ٚCΙ?C??C?L?C?ٚD ?3Dy?D??D?D  Dl?D%??D,fD2y?D8l?D>??DE?DKFfDQy?DW??D]?fDd  Djl?Dp??Dw  D}3D?? D?ٚD??3D?  D?FfD?Y?D?s3D???D???D??3D?  D?  D?6fD?\?D??3D??fD?ٚD?? D?? D??D?9?D?VfD?vfD?? D̶fD??fD?  D??D?@ D?` D?|?D??fD???D???D?  D?fD?I?D?l?D??f11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111   G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?A???A???A?1'A???A??
A??A?S?A?\)A??A???A???A??!AߑhAۗ?A?bA?bNA?bNA?|?A?ffA?VA?M?A???A??A?M?A??RA?ffA??`A?JA???A???A?x?A?M?A?r?A??}A??PAp??Act?AU+AGXA:?A*??A??A;dA??@???@??@??w@?(?@???@?C?@???@???@?Z@???@??+@???@?;d@?{@?I?@???@}p?@w;d@o?@i7L@e?@_??@W?;@PbN@Jn?@E?}@A?#@?
=@;o@4?@/??@+t?@(A?@%/@!??@ bN@??@33@??@V@/@??@??@??@ ?@??@O?@?F@	??@\)@??@1@~?@?7@ ?u???????11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111   A???A???A?1'A???A??
A??A?S?A?\)A??A???A???A??!AߑhAۗ?A?bA?bNA?bNA?|?A?ffA?VA?M?A???A??A?M?A??RA?ffA??`A?JA???A???A?x?A?M?A?r?A??}A??PAp??Act?AU+AGXA:?A*??A??A;dA??@???@??@??w@?(?@???@?C?@???@???@?Z@???@??+@???@?;d@?{@?I?@???@}p?@w;d@o?@i7L@e?@_??@W?;@PbN@Jn?@E?}@A?#@?
=@;o@4?@/??@+t?@(A?@%/@!??@ bN@??@33@??@V@/@??@??@??@ ?@??@O?@?F@	??@\)@??@1@~?@?7@ ?u???????11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111   G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?B	?1B
<jB
??B
??B
??B
?uB
?\B
?%B
?%B
?=B
?%B
?B
?fB?BR?BS?BW
B??BƨBPB6FB:^BO?BZB33B??B?sB?/BƨB?jBx?B(?B	7B
?NB
??B
2-B	?`B	??B	XB	#?B??BɺB??B??B?uB??B??B??B?{B??B??B?-BƨB?
B?sB	oB	/B	7LB	<jB	dZB	o?B	}?B	?hB	??B	??B	??B	??B	?}B	ɺB	??B	?#B	?TB	?B	??B	??B
B
DB
oB
?B
?B
#?B
(?B
/B
2-B
5?B
9XB
<jB
=qB
B?B
F?B
I?B
N?B
R?B
W
B
ZB
\)B
^5B
`BB
cTB
ffB
ff11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111   B	?1B
<jB
??B
??B
??B
?uB
?\B
?%B
?%B
?=B
?%B
?B
?fB?BR?BS?BW
B??BƨBPB6FB:^BO?BZB33B??B?sB?/BƨB?jBx?B(?B	7B
?NB
??B
2-B	?`B	??B	XB	#?B??BɺB??B??B?uB??B??B??B?{B??B??B?-BƨB?
B?sB	oB	/B	7LB	<jB	dZB	o?B	}?B	?hB	??B	??B	??B	??B	?}B	ɺB	??B	?#B	?TB	?B	??B	??B
B
DB
oB
?B
?B
#?B
(?B
/B
2-B
5?B
9XB
<jB
=qB
B?B
F?B
I?B
N?B
R?B
W
B
ZB
\)B
^5B
`BB
cTB
ffB
ff11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111   G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?PRES            TEMP            PSAL            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                                                                        HZ  ARGQ                                                                        20180524062807  QCP$                G?O?G?O?G?O?D7BFE                                                                                                                               G?O?G?O?G?O?0               