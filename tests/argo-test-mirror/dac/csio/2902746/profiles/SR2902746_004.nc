CDF       
      	DATE_TIME         	STRING256         STRING64   @   STRING32       STRING8       STRING4       STRING2       N_PROF        N_PARAM       N_LEVELS   �   N_CALIB          	   title         Argo float vertical profile    institution       CSIO   source        
Argo float     history       f2020-10-31T00:40:29Z creation (software version 1.10 (version 30.06.2020 for ARGO_simplified_profile))     
references        (http://www.argodatamgt.org/Documentation   user_manual_version       1.0    Conventions       Argo-3.1 CF-1.6    featureType       trajectoryProfile      software_version      51.10 (version 30.06.2020 for ARGO_simplified_profile)         :   	DATA_TYPE                  	long_name         	Data type      conventions       Argo reference table 1     
_FillValue                     3�   FORMAT_VERSION                 	long_name         File format version    
_FillValue                    4   HANDBOOK_VERSION               	long_name         Data handbook version      
_FillValue                    4   REFERENCE_DATE_TIME                 	long_name         !Date of reference for Julian days      conventions       YYYYMMDDHHMISS     
_FillValue                    4    DATE_CREATION                   	long_name         Date of file creation      conventions       YYYYMMDDHHMISS     
_FillValue                    40   DATE_UPDATE                 	long_name         Date of update of this file    conventions       YYYYMMDDHHMISS     
_FillValue                    4@   PLATFORM_NUMBER                   	long_name         Float unique identifier    conventions       WMO float identifier : A9IIIII     
_FillValue                    4P   PROJECT_NAME                  	long_name         Name of the project    
_FillValue                  @  4X   PI_NAME                   	long_name         "Name of the principal investigator     
_FillValue                  @  4�   STATION_PARAMETERS                       	long_name         ,List of available parameters for the station   conventions       Argo reference table 3     
_FillValue                    4�   CYCLE_NUMBER               	long_name         Float cycle number     conventions       =0...N, 0 : launch cycle (if exists), 1 : first complete cycle      
_FillValue         ��        5�   	DIRECTION                  	long_name         !Direction of the station profiles      conventions       -A: ascending profiles, D: descending profiles      
_FillValue                    5�   DATA_CENTRE                   	long_name         .Data centre in charge of float data processing     conventions       Argo reference table 4     
_FillValue                    5�   PARAMETER_DATA_MODE                   	long_name         Delayed mode or real time data     conventions       >R : real time; D : delayed mode; A : real time with adjustment     
_FillValue                    5�   PLATFORM_TYPE                     	long_name         Type of float      conventions       Argo reference table 23    
_FillValue                     5�   FLOAT_SERIAL_NO                   	long_name         Serial number of the float     
_FillValue                     6   FIRMWARE_VERSION                  	long_name         Instrument firmware version    
_FillValue                     6(   WMO_INST_TYPE                     	long_name         Coded instrument type      conventions       Argo reference table 8     
_FillValue                    6H   JULD               	long_name         ?Julian day (UTC) of the station relative to REFERENCE_DATE_TIME    standard_name         time   units         "days since 1950-01-01 00:00:00 UTC     conventions       8Relative julian days with decimal part (as parts of day)   
_FillValue        A.�~       axis      T      
resolution        >�E�r�_K        6L   JULD_QC                	long_name         Quality on date and time   conventions       Argo reference table 2     
_FillValue                    6T   JULD_LOCATION                  	long_name         @Julian day (UTC) of the location relative to REFERENCE_DATE_TIME   units         "days since 1950-01-01 00:00:00 UTC     conventions       8Relative julian days with decimal part (as parts of day)   
_FillValue        A.�~       
resolution        >�E�r�_K        6X   LATITUDE               	long_name         &Latitude of the station, best estimate     standard_name         latitude   units         degree_north   
_FillValue        @�i�       	valid_min         �V�        	valid_max         @V�        axis      Y           6`   	LONGITUDE                  	long_name         'Longitude of the station, best estimate    standard_name         	longitude      units         degree_east    
_FillValue        @�i�       	valid_min         �f�        	valid_max         @f�        axis      X           6h   POSITION_QC                	long_name         ,Quality on position (latitude and longitude)   conventions       Argo reference table 2     
_FillValue                    6p   POSITIONING_SYSTEM                    	long_name         Positioning system     
_FillValue                    6t   CONFIG_MISSION_NUMBER                  	long_name         :Unique number denoting the missions performed by the float     conventions       !1...N, 1 : first complete mission      
_FillValue         ��        6|   	PARAMETER            
               	long_name         /List of parameters with calibration information    conventions       Argo reference table 3     
_FillValue                    6�   SCIENTIFIC_CALIB_EQUATION            
               	long_name         'Calibration equation for this parameter    
_FillValue                    7�   SCIENTIFIC_CALIB_COEFFICIENT         
               	long_name         *Calibration coefficients for this equation     
_FillValue                    ;�   SCIENTIFIC_CALIB_COMMENT         
               	long_name         .Comment applying to this parameter calibration     
_FillValue                    ?�   SCIENTIFIC_CALIB_DATE            
                	long_name         Date of calibration    conventions       YYYYMMDDHHMISS     
_FillValue                  8  C�   PROFILE_PRES_QC                	long_name         #Global quality flag of PRES profile    conventions       Argo reference table 2a    
_FillValue                    C�   PROFILE_TEMP_QC                	long_name         #Global quality flag of TEMP profile    conventions       Argo reference table 2a    
_FillValue                    C�   PROFILE_PSAL_QC                	long_name         #Global quality flag of PSAL profile    conventions       Argo reference table 2a    
_FillValue                    C�   PROFILE_DOXY_QC                	long_name         #Global quality flag of DOXY profile    conventions       Argo reference table 2a    
_FillValue                    C�   PRES         	      
   	long_name         )Sea water pressure, equals 0 at sea-level      standard_name         sea_water_pressure     
_FillValue        G�O�   units         decibar    	valid_min                	valid_max         F;�    C_format      %7.1f      FORTRAN_format        F7.1   
resolution        =���   axis      Z        (  C�   PRES_QC          	         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  �  F�   PRES_ADJUSTED            	      
   	long_name         )Sea water pressure, equals 0 at sea-level      standard_name         sea_water_pressure     
_FillValue        G�O�   units         decibar    	valid_min                	valid_max         F;�    C_format      %7.1f      FORTRAN_format        F7.1   
resolution        =���   axis      Z        (  G�   PRES_ADJUSTED_QC         	         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  �  J�   PRES_ADJUSTED_ERROR          	         	long_name         VContains the error on the adjusted values as determined by the delayed mode QC process     
_FillValue        G�O�   units         decibar    C_format      %7.1f      FORTRAN_format        F7.1   
resolution        =���     (  K�   TEMP         	      	   	long_name         $Sea temperature in-situ ITS-90 scale   standard_name         sea_water_temperature      
_FillValue        G�O�   units         degree_Celsius     	valid_min         �      	valid_max         B      C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :�o     (  N�   TEMP_QC          	         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  �  R    
TEMP_dPRES           	         	long_name         6TEMP pressure displacement from original sampled value     
_FillValue        G�O�   units         decibar      (  R�   TEMP_ADJUSTED            	      	   	long_name         $Sea temperature in-situ ITS-90 scale   standard_name         sea_water_temperature      
_FillValue        G�O�   units         degree_Celsius     	valid_min         �      	valid_max         B      C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :�o     (  U�   TEMP_ADJUSTED_QC         	         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  �  Y   TEMP_ADJUSTED_ERROR          	         	long_name         VContains the error on the adjusted values as determined by the delayed mode QC process     
_FillValue        G�O�   units         degree_Celsius     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :�o     (  Y�   PSAL         	      	   	long_name         Practical salinity     standard_name         sea_water_salinity     
_FillValue        G�O�   units         psu    	valid_min         @      	valid_max         B$     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :�o     (  ]   PSAL_QC          	         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  �  `8   
PSAL_dPRES           	         	long_name         6PSAL pressure displacement from original sampled value     
_FillValue        G�O�   units         decibar      (  a   PSAL_ADJUSTED            	      	   	long_name         Practical salinity     standard_name         sea_water_salinity     
_FillValue        G�O�   units         psu    	valid_min         @      	valid_max         B$     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :�o     (  d,   PSAL_ADJUSTED_QC         	         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  �  gT   PSAL_ADJUSTED_ERROR          	         	long_name         VContains the error on the adjusted values as determined by the delayed mode QC process     
_FillValue        G�O�   units         psu    C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :�o     (  h    DOXY         	      	   	long_name         Dissolved oxygen   standard_name         *moles_of_oxygen_per_unit_mass_in_sea_water     
_FillValue        G�O�   units         micromole/kg   	valid_min         ��     	valid_max         D     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :�o     (  kH   DOXY_QC          	         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  �  np   
DOXY_dPRES           	         	long_name         6DOXY pressure displacement from original sampled value     
_FillValue        G�O�   units         decibar      (  o<   DOXY_ADJUSTED            	      	   	long_name         Dissolved oxygen   standard_name         *moles_of_oxygen_per_unit_mass_in_sea_water     
_FillValue        G�O�   units         micromole/kg   	valid_min         ��     	valid_max         D     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :�o     (  rd   DOXY_ADJUSTED_QC         	         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                  �  u�   DOXY_ADJUSTED_ERROR          	         	long_name         VContains the error on the adjusted values as determined by the delayed mode QC process     
_FillValue        G�O�   units         micromole/kg   C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :�o     (  vXArgo synthetic profile          1.0 1.2 19500101000000  20201031004029  20201031004029  2902746 CHINA ARGO PROJECT                                              FEI CHAI                                                        PRES                                                            TEMP                                                            PSAL                                                            DOXY                                                               A   HZ  AAAAPROVOR                          P32826-17CH001                  5900A04                         841 @�l��tn�1   @�l��tn�@5��"��@b)XbM�1   GPS        PRES                                                            TEMP                                                            PSAL                                                            DOXY                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            DOXY_ADJ = GAIN*DOXY                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            GAIN = 1.0472                                                                                                                                                                                                                                                   none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            GAIN determined from WOA2013 O2sat along the five initial float cycles                                                                                                                                                                                                                                    20200817125145A   A   A   A   ����=���>���?fff?�ff?�ff@ff@&ff@Y��@y��@���@���@�ff@�ff@�33@�33@�  A   A	��A��A33A#33Ay��A���A�33A�33B	33B33B333B533B\��B^��B���B���B���B���B���B���B�  B�  Bҙ�Bә�B�33B�33B�  B�  C  C� C��CL�C�3C33C%  C%� C/  C/� C9  C9� CB�fCCffCT� CU  Cm� Cn  C�ffC��fC��fC�&fC�  C�@ C���C��C�&fC�ffC���C��C�@ C΀ C�ffCڦfC�33C�s3C�� C�  D l�D ��DY�Dy�D�fD�fD� D� D�D,�DFfDffD%��D%��D+��D,�D2�D29�D8@ D8` D>��D>ٚDD�3DD�3DK�DK9�DQY�DQy�DW�3DW�3D]��D^�Dd,�DdL�Djl�Dj��Dp��Dp��Dv� Dw  D}3D}33D��fD��fD���D���D��D���D�fD�&fD�,�D�<�D�I�D�Y�D�ffD�vfD�vfD��fD��fD��fD���D���D�� D�� D�3D�3D�&fD�6fD�S3D�c3D�p D�� D���D���D���D���D��3D��3D��3D�3D�&fD�6fD�,�D�<�D�P D�` D�s3Dƃ3DɆfDɖfD̩�D̹�D��fD��fD�� D�  D�3D�#3D�)�D�9�D�FfD�VfD�ffD�vfD� D� D婚D幚D���D���D��3D��3D��D��D�9�D�I�D�  D�0 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111  ����=���>���?fff?�ff?�ff@ff@&ff@Y��@y��@���@���@�ff@�ff@�33@�33@�  A   A	��A��A33A#33Ay��A���A�33A�33B	33B33B333B533B\��B^��B���B���B���B���B���B���B�  B�  Bҙ�Bә�B�33B�33B�  B�  C  C� C��CL�C�3C33C%  C%� C/  C/� C9  C9� CB�fCCffCT� CU  Cm� Cn  C�ffC��fC��fC�&fC�  C�@ C���C��C�&fC�ffC���C��C�@ C΀ C�ffCڦfC�33C�s3C�� C�  D l�D ��DY�Dy�D�fD�fD� D� D�D,�DFfDffD%��D%��D+��D,�D2�D29�D8@ D8` D>��D>ٚDD�3DD�3DK�DK9�DQY�DQy�DW�3DW�3D]��D^�Dd,�DdL�Djl�Dj��Dp��Dp��Dv� Dw  D}3D}33D��fD��fD���D���D��D���D�fD�&fD�,�D�<�D�I�D�Y�D�ffD�vfD�vfD��fD��fD��fD���D���D�� D�� D�3D�3D�&fD�6fD�S3D�c3D�p D�� D���D���D���D���D��3D��3D��3D�3D�&fD�6fD�,�D�<�D�P D�` D�s3Dƃ3DɆfDɖfD̩�D̹�D��fD��fD�� D�  D�3D�#3D�)�D�9�D�FfD�VfD�ffD�vfD� D� D婚D幚D���D���D��3D��3D��D��D�9�D�I�D�  D�0 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111  G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�A�\)A�\)A�Y�A�VA�R`A�M�A�7�A�oA��A��A�x�A�bNA�XKA�K�A�9�A�"�A�$�A�&�A��~A�p�A��A�-A���A�hAߤ
A�M�Aܮ�A܉7Aت`A�x�A�B A��A��xAύPA̖�A�n�A�=A���A���AƸRA�f�A�=qA�JA�A�%�A��A�_VA�/A���A��jA���A�=qA���A�A�A��A���A�$%A��`A��SA�p�A��A��yA��A�p�A���A�jA�`�A�K�AwL�Aw�Am�.Am�A^��A^5?AO�AN��AB�AAA2[
A21A%��A%\)AfA-A�A��A��A�@�$h@�@��@�^5@��@���@�y�@�9X@��x@ɺ^@���@�Z@���@���@��h@�Ĝ@��@�j@��@�~�@��@��@�&@�{@��@�ff@���@��@�\)@�?}@���@��@�ul@�^5@~��@~�+@v0@v@mj�@m?}@fK;@f$�@`U@`bN@\��@\�j@X�,@XĜ@Q΁@Q��@K��@K�F@F�@E�@@>@@ �@<=�@<(�@8e�@8Q�@3}|@3dZ@0�@0�`@-�@,�@)
)@(��@&#X@&{@#b@#S�@ Q$@ A�@�@�/@��@~�@}�@r�@ �@{@�@��@5�@&�@u[@l�@�@�T@1�@(�@
��@
�H@��@�9@�@��@��@@18@(�@��@�@�u@��@ X@ b?��?�{?��?��?�#�?��8181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181  ?       ����    ����    ����    ?       ?       ����    ����    ����    ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       A�\)A�\)A�Y�A�VA�R`A�M�A�7�A�oA��A��A�x�A�bNA�XKA�K�A�9�A�"�A�$�A�&�A��~A�p�A��A�-A���A�hAߤ
A�M�Aܮ�A܉7Aت`A�x�A�B A��A��xAύPA̖�A�n�A�=A���A���AƸRA�f�A�=qA�JA�A�%�A��A�_VA�/A���A��jA���A�=qA���A�A�A��A���A�$%A��`A��SA�p�A��A��yA��A�p�A���A�jA�`�A�K�AwL�Aw�Am�.Am�A^��A^5?AO�AN��AB�AAA2[
A21A%��A%\)AfA-A�A��A��A�@�$h@�@��@�^5@��@���@�y�@�9X@��x@ɺ^@���@�Z@���@���@��h@�Ĝ@��@�j@��@�~�@��@��@�&@�{@��@�ff@���@��@�\)@�?}@���@��@�ul@�^5@~��@~�+@v0@v@mj�@m?}@fK;@f$�@`U@`bN@\��@\�j@X�,@XĜ@Q΁@Q��@K��@K�F@F�@E�@@>@@ �@<=�@<(�@8e�@8Q�@3}|@3dZ@0�@0�`@-�@,�@)
)@(��@&#X@&{@#b@#S�@ Q$@ A�@�@�/@��@~�@}�@r�@ �@{@�@��@5�@&�@u[@l�@�@�T@1�@(�@
��@
�H@��@�9@�@��@��@@18@(�@��@�@�u@��@ X@ b?��?�{?��?��?�#�?��8181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181  G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�B
��B
��B
�HB
B
ǑB
��B
ΘB
��B
�yB
�ZB�B�B PB)�B8BI�BH�BG�B�bBŢB��B�B1�B8RB7ZB7LBD�BE�B7B6FB*�B)�B	�B1B1B1B	*B	7BVBBH�BK�B[HB\)BXBBXBOOBN�BI�BI�B4VB33BBoB�wB�B�HB��B��B��BiQBgmB	B+B
��B
��B
��B
��B
ZMB
YB
!�B
 �B	�B	��B	wqB	u�B	8�B	7LB�B��BƓBŢB�}B��B~�B}�Br�Br�Bi�BiyBkzBk�Bu�Bu�Bs�Bs�B�B� B�B�bB�B�3B�aB�B		�B	
=B	 OB	 �B	+�B	,B	6B	6FB	APB	A�B	?�B	?}B	@~B	@�B	H�B	H�B	Z�B	[#B	f-B	ffB	xvB	x�B	��B	�PB	�ZB	��B	��B	�B	�	B	�-B	�2B	�RB	�\B	ÖB	˝B	��B	��B	�B	�B	�HB	�MB	�mB	�rB	�B	�B	�B	��B	��B
 �B
B
	B
	7B
=B
bB
gB
�B
�B
�B
$�B
$�B
,�B
-B
2B
2-B
72B
7LB
<PB
<jB
@nB
@�B
D�B
D�B
H�B
H�B
K�B
K�B
O�B
O�B
P�B
P�B
R�B
R�B
T�B
T�B
U�B
VB
YB
YB
\B
\)B
_+B
_;B
c?B
cTB
hYB
hsB
ltB
l�8181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181  ?       ����    ����    ����    ?       ?       ����    ����    ����    ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       ?       B
��B
��B
�HB
B
ǑB
��B
ΘB
��B
�yB
�ZB�B�B PB)�B8BI�BH�BG�B�bBŢB��B�B1�B8RB7ZB7LBD�BE�B7B6FB*�B)�B	�B1B1B1B	*B	7BVBBH�BK�B[HB\)BXBBXBOOBN�BI�BI�B4VB33BBoB�wB�B�HB��B��B��BiQBgmB	B+B
��B
��B
��B
��B
ZMB
YB
!�B
 �B	�B	��B	wqB	u�B	8�B	7LB�B��BƓBŢB�}B��B~�B}�Br�Br�Bi�BiyBkzBk�Bu�Bu�Bs�Bs�B�B� B�B�bB�B�3B�aB�B		�B	
=B	 OB	 �B	+�B	,B	6B	6FB	APB	A�B	?�B	?}B	@~B	@�B	H�B	H�B	Z�B	[#B	f-B	ffB	xvB	x�B	��B	�PB	�ZB	��B	��B	�B	�	B	�-B	�2B	�RB	�\B	ÖB	˝B	��B	��B	�B	�B	�HB	�MB	�mB	�rB	�B	�B	�B	��B	��B
 �B
B
	B
	7B
=B
bB
gB
�B
�B
�B
$�B
$�B
,�B
-B
2B
2-B
72B
7LB
<PB
<jB
@nB
@�B
D�B
D�B
H�B
H�B
K�B
K�B
O�B
O�B
P�B
P�B
R�B
R�B
T�B
T�B
U�B
VB
YB
YB
\B
\)B
_+B
_;B
c?B
cTB
hYB
hsB
ltB
l�8181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181818181  G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�C:��G�O�C:�G�O�C:xRG�O�C:��G�O�C:�)G�O�C;�G�O�C;NG�O�C;�oG�O�C;��G�O�C<I�G�O�C<��G�O�CA�G�O�CF@ G�O�CG�sG�O�CI3G�O�CH�fG�O�CEkDG�O�CB^G�O�C?:�G�O�C=8�G�O�C6� G�O�C8��G�O�C:(�G�O�C<ڠG�O�C;��G�O�C<�=G�O�C;�G�O�C:lG�O�C9�G�O�C;+G�O�C;�ZG�O�CA
=G�O�CC-G�O�C?�/G�O�C<��G�O�C8��G�O�C/c�G�O�C*�bG�O�C-xG�O�C&�hG�O�C'�fG�O�C AG�O�C��G�O�C,�G�O�B�4�G�O�B�"NG�O�B���G�O�B�'mG�O�B�49G�O�B�4�G�O�B�y�G�O�Bv�\G�O�Bo"�G�O�BmW
G�O�Bl�^G�O�Bi7LG�O�Bc7LG�O�BX8RG�O�BF��G�O�B?�G�O�B<$�G�O�B;"�G�O�B;�\G�O�B@T�G�O�BG��G�O�BQ�G�O�BR�G�O�BT��G�O�BYG�O�B\�\G�O�Bb��G�O�Bg�3G�O�Bl�^G�O�Bp��G�O�Bt��G�O�B{1'G�O�B���G�O�B��1G�O�B���G�O�B��XG�O�B�G�O�B���G�O�B�bNG�O�B�!�G�O�B�0!G�O�B�e`G�O�B�;dG�O�B��/G�O�B���G�O�B�oG�O�B�*G�O�B���G�O�B�N�G�O�B�H�G�O�B�(sG�O�B�'mG�O�B�aHG�O�BȍPG�O�B̷�G�O�Bҟ�G�O�B�MPG�O�3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3       G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�    G�O�CCT,G�O�CCY G�O�CCE�G�O�CCj�G�O�CC�G�O�CC�G�O�CD%�G�O�CDmfG�O�CD��G�O�CE-�G�O�CE�!G�O�CJ5G�O�CO�G�O�CP��G�O�CR�[G�O�CR@�G�O�CN�=G�O�CKDCG�O�CHBG�O�CF'wG�O�C?�2G�O�CAmTG�O�CB��G�O�CE�G�O�CD�qG�O�CE�iG�O�CD��G�O�CC9G�O�CA�G�O�CDG�O�CD��G�O�CJ'IG�O�CLc�G�O�CH��G�O�CEn~G�O�CAqG�O�C7�OG�O�C2��G�O�C5��G�O�C.�G�O�C/oG�O�C'��G�O�C�G�O�C��G�O�C�AG�O�B�z�G�O�Bʨ�G�O�B���G�O�B�%G�O�B�|qG�O�B��HG�O�B��G�O�Bzl�G�O�Bx�}G�O�Bw�lG�O�Bt9�G�O�Bm�dG�O�Bbm�G�O�BP/wG�O�BH%�G�O�BE�G�O�BC��G�O�BDj-G�O�BIi|G�O�BQ�G�O�B[�GG�O�B\ߗG�O�B^��G�O�Bd
^G�O�Bf�G�O�Bm�1G�O�Br�|G�O�Bw�lG�O�B|2�G�O�B�F�G�O�B���G�O�B��nG�O�B�G�O�B�}iG�O�B��^G�O�B�08G�O�B�:G�O�B��G�O�B��G�O�B�Q*G�O�B��.G�O�B��yG�O�B�0$G�O�B�QmG�O�B��EG�O�B��G�O�BƨkG�O�B�J�G�O�B�P�G�O�B�.�G�O�B�Q�G�O�Bβ�G�O�B�&G�O�B�a�G�O�BܑOG�O�B�_>G�O�1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1   @�$�G�O�@�!�G�O�@��G�O�@�'KG�O�@�8�G�O�@�5OG�O�@�2yG�O�@�0�G�O�@�+�G�O�@�6�G�O�@�XlG�O�@�8@G�O�@���G�O�@�9�G�O�@�#CG�O�@���G�O�@�E�G�O�@��EG�O�@�x�G�O�@�=/G�O�@��{G�O�@�\9G�O�@�gBG�O�@�c�G�O�@��.G�O�@�:�G�O�@�}G�O�@��QG�O�@�PgG�O�@�a�G�O�@�x�G�O�@�?LG�O�@���G�O�@��mG�O�@�9�G�O�@���G�O�@���G�O�@�s$G�O�@��G�O�@�FG�O�@Ĥ�G�O�@�ބG�O�@�{G�O�@�5-G�O�@�!�G�O�@͒G�O�@οyG�O�@��G�O�@К3G�O�@�6�G�O�@ѹ�G�O�@��VG�O�@�� G�O�@���G�O�@�XtG�O�@��G�O�@у8G�O�@��CG�O�@�xG�O�@�F^G�O�@�5�G�O�@���G�O�@��gG�O�@ѹ4G�O�@э�G�O�@�=G�O�@���G�O�@�Z�G�O�@�),G�O�@��G�O�@ϙ�G�O�@�L�G�O�@��eG�O�@�sG�O�@�G�O�@͐�G�O�@�!qG�O�@̶4G�O�@�7cG�O�@˵G�O�@�6rG�O�@���G�O�@�4(G�O�@ɬG�O�@�$	G�O�@ȗyG�O�@��G�O�@ǉ�G�O�@���G�O�@�b]G�O�@��~G�O�@�C�G�O�@ĵ,G�O�@��G�O�@Í�G�O�@���G�O�@�^G�O�@��G�O�@�2�G�O�@��%G�O�@�dG�O�