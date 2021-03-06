CDF      
      	DATE_TIME         STRING2       STRING4       STRING8       STRING16      STRING32       STRING64   @   	STRING256         N_PROF        N_PARAM       N_LEVELS   F   N_CALIB       	N_HISTORY             	   title         Argo float vertical profile    institution       CSIO   source        
Argo float     history       ?2005-09-26T10:36:27Z creation; 2018-11-23T01:57:22Z last update    
references        (http://www.argodatamgt.org/Documentation   comment       	free text      user_manual_version       3.1    Conventions       Argo-3.1 CF-1.6    featureType       trajectoryProfile         @   	DATA_TYPE                  	long_name         	Data type      conventions       Argo reference table 1     
_FillValue                    6?   FORMAT_VERSION                 	long_name         File format version    
_FillValue                    6?   HANDBOOK_VERSION               	long_name         Data handbook version      
_FillValue                    6?   REFERENCE_DATE_TIME                 	long_name         !Date of reference for Julian days      conventions       YYYYMMDDHHMISS     
_FillValue                    6?   DATE_CREATION                   	long_name         Date of file creation      conventions       YYYYMMDDHHMISS     
_FillValue                    6?   DATE_UPDATE                 	long_name         Date of update of this file    conventions       YYYYMMDDHHMISS     
_FillValue                    7    PLATFORM_NUMBER                   	long_name         Float unique identifier    conventions       WMO float identifier : A9IIIII     
_FillValue                    7   PLATFORM_TYPE                     	long_name         Type of float      conventions       Argo reference table 23    
_FillValue                     7   PROJECT_NAME                  	long_name         Name of the project    
_FillValue                  @  78   PI_NAME                   	long_name         "Name of the principal investigator     
_FillValue                  @  7x   STATION_PARAMETERS           	            	long_name         ,List of available parameters for the station   conventions       Argo reference table 3     
_FillValue                  0  7?   CYCLE_NUMBER               	long_name         Float cycle number     conventions       =0...N, 0 : launch cycle (if exists), 1 : first complete cycle      
_FillValue         ??        7?   	DIRECTION                  	long_name         !Direction of the station profiles      conventions       -A: ascending profiles, D: descending profiles      
_FillValue                    7?   DATA_CENTRE                   	long_name         .Data centre in charge of float data processing     conventions       Argo reference table 4     
_FillValue                    7?   DC_REFERENCE                  	long_name         (Station unique identifier in data centre   conventions       Data centre convention     
_FillValue                     7?   DATA_STATE_INDICATOR                  	long_name         1Degree of processing the data have passed through      conventions       Argo reference table 6     
_FillValue                    8   	DATA_MODE                  	long_name         Delayed mode or real time data     conventions       >R : real time; D : delayed mode; A : real time with adjustment     
_FillValue                    8   FLOAT_SERIAL_NO                   	long_name         Serial number of the float     
_FillValue                     8   FIRMWARE_VERSION                  	long_name         Instrument firmware version    
_FillValue                     8<   WMO_INST_TYPE                     	long_name         Coded instrument type      conventions       Argo reference table 8     
_FillValue                    8\   JULD               	long_name         ?Julian day (UTC) of the station relative to REFERENCE_DATE_TIME    standard_name         time   units         "days since 1950-01-01 00:00:00 UTC     conventions       8Relative julian days with decimal part (as parts of day)   
resolution        >?E?r?_K   
_FillValue        A.?~       axis      T           8`   JULD_QC                	long_name         Quality on date and time   conventions       Argo reference table 2     
_FillValue                    8h   JULD_LOCATION                  	long_name         @Julian day (UTC) of the location relative to REFERENCE_DATE_TIME   units         "days since 1950-01-01 00:00:00 UTC     conventions       8Relative julian days with decimal part (as parts of day)   
resolution        >?E?r?_K   
_FillValue        A.?~            8l   LATITUDE               	long_name         &Latitude of the station, best estimate     standard_name         latitude   units         degree_north   
_FillValue        @?i?       	valid_min         ?V?        	valid_max         @V?        axis      Y           8t   	LONGITUDE                  	long_name         'Longitude of the station, best estimate    standard_name         	longitude      units         degree_east    
_FillValue        @?i?       	valid_min         ?f?        	valid_max         @f?        axis      X           8|   POSITION_QC                	long_name         ,Quality on position (latitude and longitude)   conventions       Argo reference table 2     
_FillValue                    8?   POSITIONING_SYSTEM                    	long_name         Positioning system     
_FillValue                    8?   PROFILE_PRES_QC                	long_name         #Global quality flag of PRES profile    conventions       Argo reference table 2a    
_FillValue                    8?   PROFILE_TEMP_QC                	long_name         #Global quality flag of TEMP profile    conventions       Argo reference table 2a    
_FillValue                    8?   PROFILE_PSAL_QC                	long_name         #Global quality flag of PSAL profile    conventions       Argo reference table 2a    
_FillValue                    8?   VERTICAL_SAMPLING_SCHEME                  	long_name         Vertical sampling scheme   conventions       Argo reference table 16    
_FillValue                    8?   CONFIG_MISSION_NUMBER                  	long_name         :Unique number denoting the missions performed by the float     conventions       !1...N, 1 : first complete mission      
_FillValue         ??        9?   PRES         
      
   	long_name         )Sea water pressure, equals 0 at sea-level      standard_name         sea_water_pressure     
_FillValue        G?O?   units         decibar    	valid_min                	valid_max         F;?    C_format      %7.1f      FORTRAN_format        F7.1   
resolution        =???   axis      Z          9?   PRES_QC          
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  H  :?   PRES_ADJUSTED            
      	   	long_name         )Sea water pressure, equals 0 at sea-level      standard_name         sea_water_pressure     
_FillValue        G?O?   units         decibar    	valid_min                	valid_max         F;?    C_format      %7.1f      FORTRAN_format        F7.1   
resolution        =???       ;    PRES_ADJUSTED_QC         
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  H  <   PRES_ADJUSTED_ERROR          
         	long_name         VContains the error on the adjusted values as determined by the delayed mode QC process     
_FillValue        G?O?   units         decibar    C_format      %7.1f      FORTRAN_format        F7.1   
resolution        =???       <`   TEMP         
      	   	long_name         $Sea temperature in-situ ITS-90 scale   standard_name         sea_water_temperature      
_FillValue        G?O?   units         degree_Celsius     	valid_min         ?      	valid_max         B      C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o       =x   TEMP_QC          
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  H  >?   TEMP_ADJUSTED            
      
   	long_name         $Sea temperature in-situ ITS-90 scale   standard_name         sea_water_temperature      
_FillValue        G?O?   units         degree_Celsius     	valid_min         ?      	valid_max         B      comment       In situ measurement    C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o       >?   TEMP_ADJUSTED_QC         
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  H  ??   TEMP_ADJUSTED_ERROR          
         	long_name         VContains the error on the adjusted values as determined by the delayed mode QC process     
_FillValue        G?O?   units         degree_Celsius     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o       @8   PSAL         
      	   	long_name         Practical salinity     standard_name         sea_water_salinity     
_FillValue        G?O?   units         psu    	valid_min         @      	valid_max         B$     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o       AP   PSAL_QC          
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  H  Bh   PSAL_ADJUSTED            
      	   	long_name         Practical salinity     standard_name         sea_water_salinity     
_FillValue        G?O?   units         psu    	valid_min         @      	valid_max         B$     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o       B?   PSAL_ADJUSTED_QC         
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  H  C?   PSAL_ADJUSTED_ERROR          
         	long_name         VContains the error on the adjusted values as determined by the delayed mode QC process     
_FillValue        G?O?   units         psu    C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :?o       D   	PARAMETER               	            	long_name         /List of parameters with calibration information    conventions       Argo reference table 3     
_FillValue                  0  E(   SCIENTIFIC_CALIB_EQUATION               	            	long_name         'Calibration equation for this parameter    
_FillValue                    EX   SCIENTIFIC_CALIB_COEFFICIENT            	            	long_name         *Calibration coefficients for this equation     
_FillValue                    HX   SCIENTIFIC_CALIB_COMMENT            	            	long_name         .Comment applying to this parameter calibration     
_FillValue                    KX   SCIENTIFIC_CALIB_DATE               	             	long_name         Date of calibration    conventions       YYYYMMDDHHMISS     
_FillValue                  ,  NX   HISTORY_INSTITUTION                      	long_name         "Institution which performed action     conventions       Argo reference table 4     
_FillValue                    N?   HISTORY_STEP                     	long_name         Step in data processing    conventions       Argo reference table 12    
_FillValue                    N?   HISTORY_SOFTWARE                     	long_name         'Name of software which performed action    conventions       Institution dependent      
_FillValue                    N?   HISTORY_SOFTWARE_RELEASE                     	long_name         2Version/release of software which performed action     conventions       Institution dependent      
_FillValue                    N?   HISTORY_REFERENCE                        	long_name         Reference of database      conventions       Institution dependent      
_FillValue                  @  N?   HISTORY_DATE                      	long_name         #Date the history record was created    conventions       YYYYMMDDHHMISS     
_FillValue                    N?   HISTORY_ACTION                       	long_name         Action performed on data   conventions       Argo reference table 7     
_FillValue                    N?   HISTORY_PARAMETER                        	long_name         (Station parameter action is performed on   conventions       Argo reference table 3     
_FillValue                    N?   HISTORY_START_PRES                    	long_name          Start pressure action applied on   
_FillValue        G?O?   units         decibar         N?   HISTORY_STOP_PRES                     	long_name         Stop pressure action applied on    
_FillValue        G?O?   units         decibar         N?   HISTORY_PREVIOUS_VALUE                    	long_name         +Parameter/Flag previous value before action    
_FillValue        G?O?        O    HISTORY_QCTEST                       	long_name         <Documentation of tests performed, tests failed (in hex form)   conventions       EWrite tests performed when ACTION=QCP$; tests failed when ACTION=QCF$      
_FillValue                    OArgo profile    3.1 1.2 19500101000000  20050926103627  20181123015722  2900313 PROVOR                          CHINA ARGO PROJECT                                              JIANPING XU                                                     PRES            TEMP            PSAL               A   HZ  0019_23754_006                  2C  D   0327                                                            840 @?.?????1   @?.?2@y]@8 A?   @_?`@   1   ARGOS   A   A   A   Primary sampling: discrete []                                                                                                                                                                                                                                      A(  A???A???B   BH  Bn??B???B???B???B?33B???B?33C??C? C?fC L?C*??C3ffC>?CG??C\  Co??C??C??3C??3C?&fC??C??3C?  C??C???C?ffC?? C?ٚC?33D?fD?D?DٚD??D?D &fD%3D*?D/  D4  D93D=?fDB??DH?DNFfDT?3DZ? D`??DgS3Dm? Ds? Dz3D?FfD??3D???D?fD?I?D??3D??D?vfD?  DԀ D??3D퉚1111111111111111111111111111111111111111111111111111111111111111111111  A(  A???A???B   BH  Bn??B???B???B???B?33B???B?33C??C? C?fC L?C*??C3ffC>?CG??C\  Co??C??C??3C??3C?&fC??C??3C?  C??C???C?ffC?? C?ٚC?33D?fD?D?DٚD??D?D &fD%3D*?D/  D4  D93D=?fDB??DH?DNFfDT?3DZ? D`??DgS3Dm? Ds? Dz3D?FfD??3D???D?fD?I?D??3D??D?vfD?  DԀ D??3D퉚1111111111111111111111111111111111111111111111111111111111111111111111  @??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??@??A??;A?A???A???A?ĜAϕ?A?ĜA?Q?A?x?A???A?\)A??hA??TA?A???A???A?bA??RA???A??PA???A??A?ȴA???A?VA?A?A?hsA?-A?33A???A??DA|??Aq??Ad??AZz?AP?AJ=qA>??A3?A)??A%?
A/A33A	??A?!@???@???@?t?@ְ!@??y@???@???@?Z@??H@??/@??#@???@?K?@??!@?j@~?+@i?@W?@Kƨ@7?P@)&?@!??@??@J@S?1111111111111111111111111111111111111111111111111111111111111111111111  A??;A?A???A???A?ĜAϕ?A?ĜA?Q?A?x?A???A?\)A??hA??TA?A???A???A?bA??RA???A??PA???A??A?ȴA???A?VA?A?A?hsA?-A?33A???A??DA|??Aq??Ad??AZz?AP?AJ=qA>??A3?A)??A%?
A/A33A	??A?!@???@???@?t?@ְ!@??y@???@???@?Z@??H@??/@??#@???@?K?@??!@?j@~?+@i?@W?@Kƨ@7?P@)&?@!??@??@J@S?1111111111111111111111111111111111111111111111111111111111111111111111  ;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;o;oB
?B
??B
??B
??B
?#B+BL?B}?B??B?B?B?9B?!B?B??B??B??B??B??B??B?{B?JB{?Bl?BYBC?B49BoB
??B
?ZB
?qB
??B
o?B
8RB

=B	?/B	ÖB	?oB	_;B	:^B	+B	B?B??BƨB?FB?!B?B?B?!B??B?}B??B??B	C?B	ZB	`BB	o?B	?uB	?LB	?/B	??B	??B
PB
?B
/B
9XB
J?B
\)B
iy1111111111111111111111111111111111111111111111111111111111111111111111  B
??B
??B
?}B
ÖB
ɺB?B;dBl?B?B??B??B??B??B??B?{B?hB?VB?PB?DB?7B?Bz?BjB[#BG?B2-B"?BB
??B
??B
?B
?+B
^5B
&?B	??B	??B	?-B	?B	M?B	(?B	?B??B?BB??B??B??B??B??B??B??B?B?qB??B	2-B	H?B	N?B	^5B	?B	??B	??B	?/B	??B	??B
PB
?B
'?B
9XB
J?B
X1111111111111111111111111111111111111111111111111111111111111111111111  ;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
;??
PRES            TEMP            PSAL            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            PSAL_ADJUSTED = PSAL + dS, where dS is calculated from a potential conductivity (ref to 0 dbar) multiplicative adjustment term r.                                                                                                                               none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            WJO: r =0.9996(+/-0.0001), vertically averaged dS =-0.017(+/-0.004)                                                                                                                                                                                             The quoted error is manufacturer specified accuracy at time of laboratory calibration.                                                                                                                                                                          The quoted error is manufacturer specified accuracy with respect to ITS-90 at time of laboratory calibration.                                                                                                                                                   Significant salinity drift detected; WJO weighted least squares fit is adopted; PSAL_ADJ_ERR: max(WJO error, SBE sensor accuracy)                                                                                                                               200707260838082007072608380820070726083808  HZ  ARGQ                                                                                        QCP$                G?O?G?O?G?O?FFBFE           HZ  ARGQ                                                                                        QCF$                G?O?G?O?G?O?0               HZ  ARSQWJO 2.0 WOD2001                                                         20070726083808  IP                  G?O?G?O?G?O?                