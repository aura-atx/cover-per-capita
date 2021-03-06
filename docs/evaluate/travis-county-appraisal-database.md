# Data set name

**Source**:

## Evaluation

The table and column descriptions can be found here: [Appraisal-Export-Layout](https://www.traviscad.org/wp-content/uploads/2017/04/Appraisal-Export-Layout_20140427.xlsx).

### Relevant data

| Property | Description |
|---|---|
|entry count|432173|
|GEO_ID|Geographic ID (use to drop duplicate entries)|
|SITUS_NUM|Property number|
|SITUS_STREET|Street name|
|SITUS_STREET_SUFFIX|Street suffix|
|SITUS_ZIP|Zipcode|
|LAND_ACRES|Sum of the acres based on land segments (must be divided by 10000)|

The table which contains the information we are interested in is `PUBLIC.PROP`.
The table structure is BIG. There are 400+ columns. Each entry is roughly 35KB.

Here is the query to retrieve the relevant values from the data set:
```sql
SELECT
	LOWER(RTRIM(GEO_ID)) AS GEO_ID,
	MIN(LOWER(RTRIM(SITUS_NUM))) AS SITUS_NUM,
	LOWER(RTRIM(SITUS_STREET)) AS SITUS_STREET,
	LOWER(RTRIM(SITUS_STREET_SUFFIX)) AS SITUS_STREET_SUFFIX,
	LOWER(RTRIM(SITUS_ZIP)) AS SITUS_ZIP,
	MIN(LAND_ACRES / 10000.000) AS LAND_ACRES
FROM
	PUBLIC.PROP
WHERE
	PROP_TYPE_CD LIKE 'R%'
	AND GEO_ID IS NOT NULL
	AND GEO_ID != ''
GROUP BY LOWER(RTRIM(GEO_ID)), LOWER(RTRIM(SITUS_STREET)), LOWER(RTRIM(SITUS_STREET_SUFFIX)), LOWER(RTRIM(SITUS_ZIP))
```

### Other findings

The `SITUS_STREET_SUFFIX` need to be normalized. See the [List of used suffixes] and their meaning.

We found 303 entries with duplicated `GEO_ID`, but completely different addresses (use `LOWER(RTRIM(SITUS_NUM)) AS SITUS_NUM,` to replicate).

#### Feature example

```json
{
  "SELECT * FROM PUBLIC.PROP WHERE SITUS_ZIP='78705' AND SITUS_STREET LIKE '%HARMON%'": [
    {
      "PROP_ID": 771775,
      "PROP_TYPE_CD": "R    ",
      "PROP_VAL_YR": 2017,
      "SUP_NUM": 0,
      "SUP_ACTION": "  ",
      "SUP_CD": "          ",
      "SUP_DESC": "                     ",
      "GEO_ID": "0215080167                                        ",
      "PY_OWNER_ID": 1679361,
      "PY_OWNER_NAME": "SABINA-HARTFORD LLC ETAL                                              ",
      "PARTIAL_OWNER": "F",
      "UDI_GROUP": 0,
      "FILLER47": "  ",
      "PY_ADDR_LINE1": "                                                            ",
      "PY_ADDR_LINE2": "7020 FAIN PARK DR STE 5                                     ",
      "PY_ADDR_LINE3": "                                                            ",
      "PY_ADDR_CITY": "MONTGOMERY                                        ",
      "PY_ADDR_STATE": "AL                                                ",
      "PY_ADDR_COUNTRY": "     ",
      "PY_ADDR_ZIP": "36117",
      "PY_ADDR_ZIP_CASS": "7813",
      "PY_ADDR_ZIP_RT": "  ",
      "PY_CONFIDENTIAL_FLAG": "F",
      "PY_ADDRESS_SUPPRESS_FLAG": "F",
      "FILLER59": "                    ",
      "PY_ADDR_ML_DELIVERABLE": "Y",
      "FILLER61": "                           ",
      "SITUS_STREET_PREFX": "          ",
      "SITUS_STREET": "HARMON                                            ",
      "SITUS_STREET_SUFFIX": "AVE       ",
      "SITUS_CITY": "                              ",
      "SITUS_ZIP": "78705     ",
      "LEGAL_DESC": "LOT 7 BLK A EAST AVENUE SUBD                 ",
      "LEGAL_DESC2": "                                             ",
      "LEGAL_ACREAGE": 25650,
      "ABS_SUBDV_CD": "S17332    ",
      "HOOD_CD": "08WC2     ",
      "BLOCK": "A                                                 ",
      "TRACT_OR_LOT": "7                                                 ",
      "LAND_HSTD_VAL": 0,
      "LAND_NON_HSTD_VAL": 3351942,
      "IMPRV_HSTD_VAL": 0,
      "IMPRV_NON_HSTD_VAL": 62753775,
      "AG_USE_VAL": 0,
      "AG_MARKET": 0,
      "TIMBER_USE": 0,
      "TIMBER_MARKET": 0,
      "APPRAISED_VAL": 66105717,
      "TEN_PERCENT_CAP": 0,
      "ASSESSED_VAL": 66105717,
      "FILLER85": "                    ",
      "ARB_PROTEST_FLAG": "T",
      "FILLER87": null,
      "DEED_BOOK_ID": "                    ",
      "DEED_BOOK_PAGE": "                    ",
      "DEED_DT": "03292016                 ",
      "MORTGAGE_CO_ID": 0,
      "MORTAGE_CO_NAME": "                                                                      ",
      "MORTGAGE_ACCT_ID": "                                                  ",
      "JAN1_OWNER_ID": 0,
      "JAN1_OWNER_NAME": "                                                                      ",
      "JAN1_ADDR_LINE1": "                                                            ",
      "JAN1_ADDR_LINE2": "                                                            ",
      "JAN1_ADDR_LINE3": "                                                            ",
      "JAN1_ADDR_CITY": "                                                  ",
      "JAN1_ADDR_STATE": "                                                  ",
      "JAN1_ADDR_COUNTRY": "     ",
      "JAN1_ADDR_ZIP": "     ",
      "JAN1_ADDR_ZIP_CASS": "    ",
      "JAN1_ADDR_ZIP_RT": "  ",
      "JAN1_CONFIDENTIAL_FLAG": " ",
      "JAN1_ADDRESS_SUPPRESS_FLAG": "F",
      "FILLER107": "                                     ",
      "JAN1_ML_DELIVERABLE": " ",
      "HS_EXEMPT": "F",
      "OV65_EXEMPT": "F",
      "OV65_PRORATE_BEGIN": "                         ",
      "OV65_PRORATE_END": "                         ",
      "OV65S_EXEMPT": "F",
      "DP_EXEMPT": "F",
      "DV1_EXEMPT": "F",
      "DV1S_EXEMPT": "F",
      "DV2_EXEMPT": "F",
      "DV2S_EXEMPT": "F",
      "DV3_EXEMPT": "F",
      "DV3S_EXEMPT": "F",
      "DV4_EXEMPT": "F",
      "DV4S_EXEMPT": "F",
      "EX_EXEMPT": "F",
      "EX_PRORATE_BEGIN": "                         ",
      "EX_PRORATE_END": "                         ",
      "LVE_EXEMPT": "F",
      "AB_EXEMPT": "F",
      "EN_EXEMPT": "F",
      "FR_EXEMPT": "F",
      "HT_EXEMPT": "F",
      "PRO_EXEMPT": "F",
      "PC_EXEMPT": "F",
      "SO_EXEMPT": "F",
      "EX366_EXEMPT": "F",
      "CH_EXEMPT": "F",
      "IMPRV_STATE_CD": "B1        ",
      "LAND_STATE_CD": "B1        ",
      "PERSONAL_STATE_CD": "          ",
      "MINERAL_STATE_CD": "          ",
      "LAND_ACRES": 25650,
      "ENTITY_AGENT_ID": 2006,
      "ENTITY_AGENT_NAME": "MORRISON & HEAD LP                                                    ",
      "ENTITY_AGENT_ADDR_LINE1": "4210 SPICEWOOD SPRINGS RD STE 211                           ",
      "ENTITY_AGENT_ADDR_LINE2": "                                                            ",
      "ENTITY_AGENT_ADDR_LINE3": "                                                            ",
      "ENTITY_AGENT_CITY": "AUSTIN                                            ",
      "ENTITY_AGENT_STATE": "TX                                                ",
      "ENTITY_AGENT_COUNTRY": "     ",
      "ENTITY_AGENT_ZIP": "78759",
      "ENTITY_AGENT_CASS": "    ",
      "ENTITY_AGENT_RT": "  ",
      "FILLER152": "                                  ",
      "CA_AGENT_ID": 2006,
      "CA_AGENT_NAME": "MORRISON & HEAD LP                                                    ",
      "CA_AGENT_ADDR_LINE1": "4210 SPICEWOOD SPRINGS RD STE 211                           ",
      "CA_AGENT_ADDR_LINE2": "                                                            ",
      "CA_AGENT_ADDR_LINE3": "                                                            ",
      "CA_AGENT_CITY": "AUSTIN                                            ",
      "CA_AGENT_STATE": "TX                                                ",
      "CA_AGENT_COUNTRY": "     ",
      "CA_AGENT_ZIP": "78759",
      "CA_AGENT_ZIP_CASS": "    ",
      "CA_AGENT_ZIP_RT": "  ",
      "FILLER164": "                                  ",
      "ARB_AGENT_ID": 2006,
      "ARB_AGENT_NAME": "MORRISON & HEAD LP                                                    ",
      "ARB_AGENT_ADDR_LINE1": "4210 SPICEWOOD SPRINGS RD STE 211                           ",
      "ARB_AGENT_ADDR_LINE2": "                                                            ",
      "ARB_AGENT_ADDR_LINE3": "                                                            ",
      "ARB_AGENT_CITY": "AUSTIN                                            ",
      "ARB_AGENT_STATE": "TX                                                ",
      "ARB_AGENT_COUNTRY": "     ",
      "ARB_AGENT_ZIP": "78759",
      "ARB_AGENT_ZIP_CASS": "    ",
      "ARB_AGENT_ZIP_RT": "  ",
      "FILLER176": "                                  ",
      "MINERAL_TYPE_OF_INT": "     ",
      "MINERAL_INT_PCT": "000000000000000",
      "PRODUCTIVITY_USE_CODE": "   ",
      "FILLER180": "                                        ",
      "TIMBER_78_MARKET": 0,
      "AG_LATE_LOSS": 0,
      "LATE_FREEPORT_PENALTY": 0,
      "FILLER184": "  ",
      "FILLER185": "     ",
      "FILLER186": "  ",
      "DBA": "SABINA PH I                             ",
      "FILLER188": "                                      ",
      "MARKET_VALUE": 66105717,
      "FILLER190": "                    ",
      "FILLER191": "                    ",
      "FILLER192": "                    ",
      "FILLER193": " ",
      "FILLER194": " ",
      "FILLER195": "                                                                      ",
      "OV65_DEFERRAL_DATE": "                         ",
      "DP_DEFERRAL_DATE": "                         ",
      "REF_ID1": "                         ",
      "REF_ID2": "02150801670000           ",
      "SITUS_NUM": "3400           ",
      "SITUS_UNIT": "     ",
      "APPR_OWNER_ID": 1679361,
      "APPR_OWNER_NAME": "SABINA-HARTFORD LLC ETAL                                              ",
      "APPR_ADDR_LINE1": "                                                            ",
      "APPR_ADDR_LINE2": "7020 FAIN PARK DR STE 5                                     ",
      "APPR_ADDR_LINE3": "                                                            ",
      "APPR_ADDR_CITY": "MONTGOMERY                                        ",
      "APPR_ADDR_STATE": "AL                                                ",
      "APPR_ADDR_COUNTRY": "     ",
      "APPR_ADDR_ZIP": "36117",
      "APPR_ADDR_ZIP_CASS": "7813",
      "APPR_ADDR_ZIP_CASS_ROUTE": "  ",
      "APPR_ML_DELIVERABLE": "Y",
      "APPR_CONFIDENTIAL_FLAG": "F",
      "APPR_ADDRESS_SUPPRESS_FLAG": "F",
      "APPR_CONFIDENTIAL_NAME": "                                                                      ",
      "PY_CONFIDENTIAL_NAME": "                                                                      ",
      "JAN1_CONFIDENTIAL_NAME": "                                                                      ",
      "FILLER219": "     ",
      "RENDITION_FILED": "F",
      "RENDITION_DATE": "                         ",
      "RENDITION_PENALTY": 0,
      "RENDITION_PENALTY_DATE_PAID": "                         ",
      "RENDITION_FRAUD_PENALTY": 0,
      "RENDITION_FRAUD_PENALTY_DATE_PAID": "                         ",
      "FILLER226": "                    ",
      "ENTITIES": "0A, 01, 02, 03, 2J, 68             ",
      "ECO_EXEMPT": "F",
      "DATASET_ID": 6056,
      "DEED_NUM": "2016046823                                        ",
      "CHODO_EXEMPT": "F",
      "LOCAL_OPTION_PCT_ONLY_FLAG_HS": "F",
      "LOCAL_OPTION_PCT_ONLY_FLAG_OV65": "F",
      "LOCAL_OPTION_PCT_ONLY_FLAG_OV65S": "F",
      "LOCAL_OPTION_PCT_ONLY_FLAG_DP": "F",
      "FREEZE_ONLY_FLAG_OV65": "F",
      "FREEZE_ONLY_FLAG_OV65S": "F",
      "FREEZE_ONLY_FLAG_DP": "F",
      "APPLY_PERCENT_EXEMPTION_FLAG": "F",
      "EXEMPTION_PERCENTAGE": 1000000000000,
      "VIT_FLAG": "F",
      "LIH_EXEMPT": "F",
      "GIT_EXEMPT": "F",
      "DPS_EXEMPT": "F",
      "DPS_DEFERRAL_DATE": "                         ",
      "LOCAL_OPTION_PCT_ONLY_FLAG_DPS": "F",
      "FREEZE_ONLY_FLAG_DPS": "F",
      "DVHS_EXEMPT": "F",
      "HS_QUALIFY_YR": 0,
      "OV65_QUALIFY_YR": 0,
      "OV65S_QUALIFY_YR": 0,
      "DP_QUALIFY_YR": 0,
      "DPS_QUALIFY_YR": 0,
      "DV1_QUALIFY_YR": 0,
      "DV1S_QUALIFY_YR": 0,
      "DV2_QUALIFY_YR": 0,
      "DV2S_QUALIFY_YR": 0,
      "DV3_QUALIFY_YR": 0,
      "DV3S_QUALIFY_YR": 0,
      "DV4_QUALIFY_YR": 0,
      "DV4S_QUALIFY_YR": 0,
      "DVHS_QUALIFY_YR": 0,
      "EX_QUALIFY_YR": 0,
      "AB_QUALIFY_YR": 0,
      "EN_QUALIFY_YR": 0,
      "FR_QUALIFY_YR": 0,
      "HT_QUALIFY_YR": 0,
      "PRO_QUALIFY_YR": 0,
      "PC_QUALIFY_YR": 0,
      "SO_QUALIFY_YR": 0,
      "EX366_QUALIFY_YR": 0,
      "CH_QUALIFY_YR": 0,
      "ECO_QUALIFY_YR": 0,
      "CHODO_QUALIFY_YR": 0,
      "LIH_QUALIFY_YR": 0,
      "GIT_QUALIFY_YR": 0,
      "MORTGAGE_ADDR_LINE1": "                                                            ",
      "MORTGAGE_ADDR_LINE2": "                                                            ",
      "MORTGAGE_ADDR_LINE3": "                                                            ",
      "MORTGAGE_ADDR_CITY": "                                                  ",
      "MORTGAGE_ADDR_STATE": "                                                  ",
      "MORTGAGE_ADDR_COUNTRY": "     ",
      "MORTGAGE_ADDR_ZIP": "     ",
      "MORTGAGE_ADDR_ZIP_CASS": "    ",
      "MORTGAGE_ADDR_ZIP_RT": "  ",
      "MORTGAGE_ADDR_ML_DELIVERABLE": " ",
      "SIC_CODE": "          ",
      "OMITTED_PROPERTY_FLAG": "N",
      "HS_PRORATE_BEGIN": "                         ",
      "HS_PRORATE_END": "                         ",
      "OV65S_PRORATE_BEGIN": "                         ",
      "OV65S_PRORATE_END": "                         ",
      "DP_PRORATE_BEGIN": "                         ",
      "DP_PRORATE_END": "                         ",
      "DV1_PRORATE_BEGIN": "                         ",
      "DV1_PRORATE_END": "                         ",
      "DV1S_PRORATE_BEGIN": "                         ",
      "DV1S_PRORATE_END": "                         ",
      "DV2_PRORATE_BEGIN": "                         ",
      "DV2_PRORATE_END": "                         ",
      "DV2S_PRORATE_BEGIN": "                         ",
      "DV2S_PRORATE_END": "                         ",
      "DV3_PRORATE_BEGIN": "                         ",
      "DV3_PRORATE_END": "                         ",
      "DV3S_PRORATE_BEGIN": "                         ",
      "DV3S_PRORATE_END": "                         ",
      "DV4_PRORATE_BEGIN": "                         ",
      "DV4_PRORATE_END": "                         ",
      "DV4S_PRORATE_BEGIN": "                         ",
      "DV4S_PRORATE_END": "                         ",
      "LVE_PRORATE_BEGIN": "                         ",
      "LVE_PRORATE_END": "                         ",
      "AB_PRORATE_BEGIN": "                         ",
      "AB_PRORATE_END": "                         ",
      "EN_PRORATE_BEGIN": "                         ",
      "EN_PRORATE_END": "                         ",
      "FR_PRORATE_BEGIN": "                         ",
      "FR_PRORATE_END": "                         ",
      "HT_PRORATE_BEGIN": "                         ",
      "HT_PRORATE_END": "                         ",
      "PRO_PRORATE_BEGIN": "                         ",
      "PRO_PRORATE_END": "                         ",
      "PC_PRORATE_BEGIN": "                         ",
      "PC_PRORATE_END": "                         ",
      "SO_PRORATE_BEGIN": "                         ",
      "SO_PRORATE_END": "                         ",
      "EX366_PRORATE_BEGIN": "                         ",
      "EX366_PRORATE_END": "                         ",
      "CH_PRORATE_BEGIN": "                         ",
      "CH_PRORATE_END": "                         ",
      "DPS_PRORATE_BEGIN": "                         ",
      "DPS_PRORATE_END": "                         ",
      "ECO_PRORATE_BEGIN": "                         ",
      "ECO_PRORATE_END": "                         ",
      "CHODO_PRORATE_BEGIN": "                         ",
      "CHODO_PRORATE_END": "                         ",
      "LIH_PRORATE_BEGIN": "                         ",
      "LIH_PRORATE_END": "                         ",
      "GIT_PRORATE_BEGIN": "                         ",
      "GIT_PRORATE_END": "                         ",
      "CLT_EXEMPT": "F",
      "CLT_PRORATE_BEGIN": "                         ",
      "CLT_PRORATE_END": "                         ",
      "CLT_QUALIFY_YR": 0,
      "DVHSS_EXEMPT": "F",
      "DVHSS_PRORATE_BEGIN": "                         ",
      "DVHSS_PRORATE_END": "                         ",
      "DVHSS_QUALIFY_YR": 0,
      "OMITTED_IMPRV_HSTD_VAL": 0,
      "OMITTED_IMPRV_NON_HSTD_VAL": 0,
      "DVHS_PRORATE_BEGIN": "                         ",
      "DVHS_PRORATE_END": "                         ",
      "EX_XD_EXEMPT": " ",
      "EX_XD_QUALIFY_YR": null,
      "EX_XD_PRORATE_BEGIN": "                         ",
      "EX_XD_PRORATE_END": "                         ",
      "EX_XF_EXEMPT": " ",
      "EX_XF_QUALIFY_YR": null,
      "EX_XF_PRORATE_BEGIN": "                         ",
      "EX_XF_PRORATE_END": "                         ",
      "EX_XG_EXEMPT": " ",
      "EX_XG_QUALIFY_YR": null,
      "EX_XG_PRORATE_BEGIN": "                         ",
      "EX_XG_PRORATE_END": "                         ",
      "EX_XH_EXEMPT": " ",
      "EX_XH_QUALIFY_YR": null,
      "EX_XH_PRORATE_BEGIN": "                         ",
      "EX_XH_PRORATE_END": "                         ",
      "EX_XI_EXEMPT": " ",
      "EX_XI_QUALIFY_YR": null,
      "EX_XI_PRORATE_BEGIN": "                         ",
      "EX_XI_PRORATE_END": "                         ",
      "EX_XJ_EXEMPT": " ",
      "EX_XJ_QUALIFY_YR": null,
      "EX_XJ_PRORATE_BEGIN": "                         ",
      "EX_XJ_PRORATE_END": "                         ",
      "EX_XL_EXEMPT": " ",
      "EX_XL_QUALIFY_YR": null,
      "EX_XL_PRORATE_BEGIN": "                         ",
      "EX_XL_PRORATE_END": "                         ",
      "EX_XM_EXEMPT": " ",
      "EX_XM_QUALIFY_YR": null,
      "EX_XM_PRORATE_BEGIN": "                         ",
      "EX_XM_PRORATE_END": "                         ",
      "EX_XN_EXEMPT": " ",
      "EX_XN_QUALIFY_YR": null,
      "EX_XN_PRORATE_BEGIN": "                         ",
      "EX_XN_PRORATE_END": "                         ",
      "EX_XO_EXEMPT": " ",
      "EX_XO_QUALIFY_YR": null,
      "EX_XO_PRORATE_BEGIN": "                         ",
      "EX_XO_PRORATE_END": "                         ",
      "EX_XP_EXEMPT": " ",
      "EX_XP_QUALIFY_YR": null,
      "EX_XP_PRORATE_BEGIN": "                         ",
      "EX_XP_PRORATE_END": "                         ",
      "EX_XQ_EXEMPT": " ",
      "EX_XQ_QUALIFY_YR": null,
      "EX_XQ_PRORATE_BEGIN": "                         ",
      "EX_XQ_PRORATE_END": "                         ",
      "EX_XR_EXEMPT": " ",
      "EX_XR_QUALIFY_YR": null,
      "EX_XR_PRORATE_BEGIN": "                         ",
      "EX_XR_PRORATE_END": "                         ",
      "EX_XS_EXEMPT": " ",
      "EX_XS_QUALIFY_YR": null,
      "EX_XS_PRORATE_BEGIN": "                         ",
      "EX_XS_PRORATE_END": "                         ",
      "EX_XT_EXEMPT": " ",
      "EX_XT_QUALIFY_YR": null,
      "EX_XT_PRORATE_BEGIN": "                         ",
      "EX_XT_PRORATE_END": "                         ",
      "EX_XU_EXEMPT": " ",
      "EX_XU_QUALIFY_YR": null,
      "EX_XU_PRORATE_BEGIN": "                         ",
      "EX_XU_PRORATE_END": "                         ",
      "EX_XV_EXEMPT": " ",
      "EX_XV_QUALIFY_YR": null,
      "EX_XV_PRORATE_BEGIN": "                         ",
      "EX_XV_PRORATE_END": "                         ",
      "EX_XA_EXEMPT": " ",
      "EX_XA_QUALIFY_YR": null,
      "EX_XA_PRORATE_BEGIN": "                         ",
      "EX_XA_PRORATE_END": "                         ",
      "LVE_QUALIFY_YR": null,
      "PPV_EXEMPT": "F",
      "PPV_QUALIFY_YR": null,
      "PPV_PRORATE_BEGIN": "                         ",
      "PPV_PRORATE_END": "                         ",
      "DVCH_EXEMPT": "F",
      "DVCH_QUALIFY_YR": null,
      "DVCH_PRORATE_BEGIN": "                         ",
      "DVCH_PRORATE_END": "                         ",
      "DVCHS_EXEMPT": "F",
      "DVCHS_QUALIFY_YR": null,
      "DVCHS_PRORATE_BEGIN": "                         ",
      "DVCHS_PRORATE_END": "                         ",
      "MASSS_EXEMPT": "F",
      "MASSS_QUALIFY_YR": null,
      "MASSS_PRORATE_BEGIN": "                         ",
      "MASSS_PRORATE_END": "                         ",
      "PP_LATE_INTERSTATE_ALLOCATION_VAL": 0
    }
  ]
}
```

## Extras

### List of used suffixes

|SITUS_STREET_SUFFIX|Meaning|
|-------------------|---|
|(pvt)|
|ave|avenue|
|bend|
|blf|
|blvd|
|bnd|
|ci|
|cir|
|clf|
|cove|
|crk|
|crt|
|ct|
|cv|
|cyn|
|dr|
|drive|
|dv|
|flds|
|hl|
|holw|
|hwy|
|hy|
|ln|
|lndg|
|loop|
|lp|
|mdws|
|n|
|park|
|parkway|
|pass|
|path|
|pkwy|
|pl|
|place|
|plc|
|ps|
|pt|
|pvt|
|rd|road|
|rdg|
|rg|
|row|
|run|
|skwy|
|sq|
|st|
|ter|
|terr|
|tr|
|trc|
|trce|
|trl|
|view|
|vista|
|vly|
|vw|
|walk|
|way|way|
|wy|
|xing|crossing|

