CDF      
      	DATE_TIME         STRING2       STRING4       STRING8       STRING16      STRING32       STRING64   @   	STRING256         N_PROF        N_PARAM       N_LEVELS   g   N_CALIB       	N_HISTORY             	   title         Argo float vertical profile    institution       CSIO   source        
Argo float     history       2018-06-13T10:00:19Z creation      
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
_FillValue                  h  ;   PRES_ADJUSTED            
      	   	long_name         )Sea water pressure, equals 0 at sea-level      standard_name         sea_water_pressure     
_FillValue        G?O?   units         decibar    	valid_min                	valid_max         F;?    C_format      %7.1f      FORTRAN_format        F7.1   
resolution        =???     ?  ;?   PRES_ADJUSTED_QC         
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  h  =    PRES_ADJUSTED_ERROR          
         	long_name         VContains the error on the adjusted values as determined by the delayed mode QC process     
_FillValue        G?O?   units         decibar    C_format      %7.1f      FORTRAN_format        F7.1   
resolution        =???     ?  =?   TEMP         
      	   	long_name         $Sea temperature in-situ ITS-90 scale   standard_name         sea_water_temperature      
_FillValue        G?O?   units         degree_Celsius     	valid_min         ?      	valid_max         B      C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     ?  ?$   TEMP_QC          
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  h  @?   TEMP_ADJUSTED            
      
   	long_name         $Sea temperature in-situ ITS-90 scale   standard_name         sea_water_temperature      
_FillValue        G?O?   units         degree_Celsius     	valid_min         ?      	valid_max         B      comment       In situ measurement    C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     ?  A(   TEMP_ADJUSTED_QC         
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  h  B?   TEMP_ADJUSTED_ERROR          
         	long_name         VContains the error on the adjusted values as determined by the delayed mode QC process     
_FillValue        G?O?   units         degree_Celsius     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     ?  C,   PSAL         
      	   	long_name         Practical salinity     standard_name         sea_water_salinity     
_FillValue        G?O?   units         psu    	valid_min         @      	valid_max         B$     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     ?  D?   PSAL_QC          
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  h  Fd   PSAL_ADJUSTED            
      	   	long_name         Practical salinity     standard_name         sea_water_salinity     
_FillValue        G?O?   units         psu    	valid_min         @      	valid_max         B$     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     ?  F?   PSAL_ADJUSTED_QC         
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  h  Hh   PSAL_ADJUSTED_ERROR          
         	long_name         VContains the error on the adjusted values as determined by the delayed mode QC process     
_FillValue        G?O?   units         psu    C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o     ?  H?   	PARAMETER               	            	long_name         /List of parameters with calibration information    conventions       Argo reference table 3     
_FillValue                  0  Jl   SCIENTIFIC_CALIB_EQUATION               	            	long_name         'Calibration equation for this parameter    
_FillValue                    J?   SCIENTIFIC_CALIB_COEFFICIENT            	            	long_name         *Calibration coefficients for this equation     
_FillValue                    M?   SCIENTIFIC_CALIB_COMMENT            	            	long_name         .Comment applying to this parameter calibration     
_FillValue                    P?   SCIENTIFIC_CALIB_DATE               	             	long_name         Date of calibration    conventions       YYYYMMDDHHMISS     
_FillValue                  ,  S?   HISTORY_INSTITUTION                      	long_name         "Institution which performed action     conventions       Argo reference table 4     
_FillValue                    S?   HISTORY_STEP                     	long_name         Step in data processing    conventions       Argo reference table 12    
_FillValue                    S?   HISTORY_SOFTWARE                     	long_name         'Name of software which performed action    conventions       Institution dependent      
_FillValue                    S?   HISTORY_SOFTWARE_RELEASE                     	long_name         2Version/release of software which performed action     conventions       Institution dependent      
_FillValue                    S?   HISTORY_REFERENCE                        	long_name         Reference of database      conventions       Institution dependent      
_FillValue                  @  S?   HISTORY_DATE                      	long_name         #Date the history record was created    conventions       YYYYMMDDHHMISS     
_FillValue                    T   HISTORY_ACTION                       	long_name         Action performed on data   conventions       Argo reference table 7     
_FillValue                    T(   HISTORY_PARAMETER                        	long_name         (Station parameter action is performed on   conventions       Argo reference table 3     
_FillValue                    T,   HISTORY_START_PRES                    	long_name          Start pressure action applied on   
_FillValue        G?O?   units         decibar         T<   HISTORY_STOP_PRES                     	long_name         Stop pressure action applied on    
_FillValue        G?O?   units         decibar         T@   HISTORY_PREVIOUS_VALUE                    	long_name         +Parameter/Flag previous value before action    
_FillValue        G?O?        TD   HISTORY_QCTEST                       	long_name         <Documentation of tests performed, tests failed (in hex form)   conventions       EWrite tests performed when ACTION=QCP$; tests failed when ACTION=QCF$      
_FillValue                    THArgo profile    3.1 1.2 19500101000000  20180613100019  20180613100019  2902746 PROVOR                          CHINA ARGO PROJECT                                              FEI CHAI                                                        PRES            TEMP            PSAL               A   HZ  0421_32826001_003               2B  A   P32826-17CH001                  5900A04                         841 @?jB^Р1   @?jB^Р@5??-V@b5?7Kƨ1   GPS     A   A   A   Primary sampling: averaged []                                                                                                                                                                                                                                          ?333?ٙ?@333@?  @?ff@?ff@陚A??A??A$??AvffA?33BffB333B\??B???B???B?  B?  B?  B?33B???C?3C??C?3C&?C/L?C9??CC? CTL?Cm??C?s3C?&fC?ffC?s3C?33C??3C?L?C??fC???C??3D ,?D` D??DS3D3DffD%?3D+?3D2,?D8?fD?fDD??DK&fDQs3DW?fD^  DdY?Dj? Dp??DwfD}L?D???D??fD??3D??D?33D?S3D?? D???D??fD?ٚD?	?D?  D?<?D?P D?p D???D?? D?ٚD???D?I?D?<?D?S3D?p Dɓ3D̼?D?ٚD?? D??D?VfD?VfD?s3D???D??fD?ٚD?? D??D?C3D?` D?? D?Y?1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111     ?333?ٙ?@333@?  @?ff@?ff@陚A??A??A$??AvffA?33BffB333B\??B???B???B?  B?  B?  B?33B???C?3C??C?3C&?C/L?C9??CC? CTL?Cm??C?s3C?&fC?ffC?s3C?33C??3C?L?C??fC???C??3D ,?D` D??DS3D3DffD%?3D+?3D2,?D8?fD?fDD??DK&fDQs3DW?fD^  DdY?Dj? Dp??DwfD}L?D???D??fD??3D??D?33D?S3D?? D???D??fD?ٚD?	?D?  D?<?D?P D?p D???D?? D?ٚD???D?I?D?<?D?S3D?p Dɓ3D̼?D?ٚD?? D??D?VfD?VfD?s3D???D??fD?ٚD?? D??D?C3D?` D?? D?Y?1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?A?M?A?A?A?7LA?A?A?C?A?M?A?Q?A?K?A?I?A?{A?oA??/A??A?~?A???A?K?A?9XA???AΡ?A?%A?
=A?K?A??DA?%A?`BA?\)A?hsA?n?A???A?`BA?hsA??A?A?"?A???Aw??Am"?A^??AR  AAO?A3??A&??A??AM?A?H@??!@ۅ@???@?J@?/@?
=@???@??!@?dZ@??@?b@? ?@?1'@???@???@?S?@~V@s?
@k?
@f?R@_??@Y?#@R~?@M?-@IG?@C??@>ȴ@9?7@5`B@2?\@/?;@+dZ@(Ĝ@&5?@"?H@
=@??@?!@r?@E?@~?@bN@V@??@o@	?7@v?@??@?@??@ ??@ A???{????r????y??z????
1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 A?M?A?A?A?7LA?A?A?C?A?M?A?Q?A?K?A?I?A?{A?oA??/A??A?~?A???A?K?A?9XA???AΡ?A?%A?
=A?K?A??DA?%A?`BA?\)A?hsA?n?A???A?`BA?hsA??A?A?"?A???Aw??Am"?A^??AR  AAO?A3??A&??A??AM?A?H@??!@ۅ@???@?J@?/@?
=@???@??!@?dZ@??@?b@? ?@?1'@???@???@?S?@~V@s?
@k?
@f?R@_??@Y?#@R~?@M?-@IG?@C??@>ȴ@9?7@5`B@2?\@/?;@+dZ@(Ĝ@&5?@"?H@
=@??@?!@r?@E?@~?@bN@V@??@o@	?7@v?@??@?@??@ ??@ A???{????r????y??z????
1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?B
??B
?B
?B
?B
?B
??B
??B
??B
??B
??B
?FB
?wB
??B
?/BR?BffB?PB?B{BL?B7LBYB_;B\)BR?BH?B8RB,BbB?mB?3BffB,B
??B
??B
YB
?B	ǮB	?B	33B??BĜB??B?VBz?BffBffBu?B?1B??BƨB?yB??B??B??B	B	hB	"?B	7LB	F?B	aHB	jB	~?B	?hB	??B	?B	?FB	??B	??B	??B	?)B	?`B	??B	??B	??B
B
JB
oB
?B
?B
?B
"?B
&?B
.B
33B
7LB
:^B
=qB
A?B
D?B
G?B
M?B
Q?B
VB
YB
]/B
_;B
aHB
dZB
gmB
hsB
k?B
l?1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 B
??B
?B
?B
?B
?B
??B
??B
??B
??B
??B
?FB
?wB
??B
?/BR?BffB?PB?B{BL?B7LBYB_;B\)BR?BH?B8RB,BbB?mB?3BffB,B
??B
??B
YB
?B	ǮB	?B	33B??BĜB??B?VBz?BffBffBu?B?1B??BƨB?yB??B??B??B	B	hB	"?B	7LB	F?B	aHB	jB	~?B	?hB	??B	?B	?FB	??B	??B	??B	?)B	?`B	??B	??B	??B
B
JB
oB
?B
?B
?B
"?B
&?B
.B
33B
7LB
:^B
=qB
A?B
D?B
G?B
M?B
Q?B
VB
YB
]/B
_;B
aHB
dZB
gmB
hsB
k?B
l?1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?G?O?PRES            TEMP            PSAL            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                                                                        HZ  ARGQ                                                                        20180613100019  QCP$                G?O?G?O?G?O?D7BFE                                                                                                                               G?O?G?O?G?O?0               