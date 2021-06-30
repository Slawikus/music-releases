# Generated by Django 3.2 on 2021-06-26 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20210626_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='currency',
            field=models.CharField(blank=True, choices=[('AED', 'AEDUAE Dirham'), ('AFN', 'AFNAfghani'), ('ALL', 'ALLLek'), ('AMD', 'AMDArmenian Dram'), ('ANG', 'ANGNetherlands Antillean Guilder'), ('AOA', 'AOAKwanza'), ('ARS', 'ARSArgentine Peso'), ('AUD', 'AUDAustralian Dollar'), ('AWG', 'AWGAruban Florin'), ('AZN', 'AZNAzerbaijanian Manat'), ('BAM', 'BAMConvertible Mark'), ('BBD', 'BBDBarbados Dollar'), ('BDT', 'BDTTaka'), ('BGN', 'BGNBulgarian Lev'), ('BHD', 'BHDBahraini Dinar'), ('BIF', 'BIFBurundi Franc'), ('BMD', 'BMDBermudian Dollar'), ('BND', 'BNDBrunei Dollar'), ('BOB', 'BOBBoliviano'), ('BRL', 'BRLBrazilian Real'), ('BSD', 'BSDBahamian Dollar'), ('BTN', 'BTNNgultrum'), ('BWP', 'BWPPula'), ('BYN', 'BYNBelarusian Ruble'), ('BZD', 'BZDBelize Dollar'), ('CAD', 'CADCanadian Dollar'), ('CDF', 'CDFCongolese Franc'), ('CHF', 'CHFSwiss Franc'), ('CLP', 'CLPChilean Peso'), ('CNY', 'CNYYuan Renminbi'), ('COP', 'COPColombian Peso'), ('CRC', 'CRCCosta Rican Colon'), ('CUC', 'CUCPeso Convertible'), ('CUP', 'CUPCuban Peso'), ('CVE', 'CVECabo Verde Escudo'), ('CZK', 'CZKCzech Koruna'), ('DJF', 'DJFDjibouti Franc'), ('DKK', 'DKKDanish Krone'), ('DOP', 'DOPDominican Peso'), ('DZD', 'DZDAlgerian Dinar'), ('EGP', 'EGPEgyptian Pound'), ('ERN', 'ERNNakfa'), ('ETB', 'ETBEthiopian Birr'), ('EUR', 'EUREuro'), ('FJD', 'FJDFiji Dollar'), ('FKP', 'FKPFalkland Islands Pound'), ('GBP', 'GBPPound Sterling'), ('GEL', 'GELLari'), ('GHS', 'GHSGhana Cedi'), ('GIP', 'GIPGibraltar Pound'), ('GMD', 'GMDDalasi'), ('GNF', 'GNFGuinea Franc'), ('GTQ', 'GTQQuetzal'), ('GYD', 'GYDGuyana Dollar'), ('HKD', 'HKDHong Kong Dollar'), ('HNL', 'HNLLempira'), ('HRK', 'HRKKuna'), ('HTG', 'HTGGourde'), ('HUF', 'HUFForint'), ('IDR', 'IDRRupiah'), ('ILS', 'ILSNew Israeli Sheqel'), ('INR', 'INRIndian Rupee'), ('IQD', 'IQDIraqi Dinar'), ('IRR', 'IRRIranian Rial'), ('ISK', 'ISKIceland Krona'), ('JMD', 'JMDJamaican Dollar'), ('JOD', 'JODJordanian Dinar'), ('JPY', 'JPYYen'), ('KES', 'KESKenyan Shilling'), ('KGS', 'KGSSom'), ('KHR', 'KHRRiel'), ('KMF', 'KMFComoro Franc'), ('KPW', 'KPWNorth Korean Won'), ('KRW', 'KRWWon'), ('KWD', 'KWDKuwaiti Dinar'), ('KYD', 'KYDCayman Islands Dollar'), ('KZT', 'KZTTenge'), ('LAK', 'LAKKip'), ('LBP', 'LBPLebanese Pound'), ('LKR', 'LKRSri Lanka Rupee'), ('LRD', 'LRDLiberian Dollar'), ('LSL', 'LSLLoti'), ('LYD', 'LYDLibyan Dinar'), ('MAD', 'MADMoroccan Dirham'), ('MDL', 'MDLMoldovan Leu'), ('MGA', 'MGAMalagasy Ariary'), ('MKD', 'MKDDenar'), ('MMK', 'MMKKyat'), ('MNT', 'MNTTugrik'), ('MOP', 'MOPPataca'), ('MRO', 'MROOuguiya'), ('MUR', 'MURMauritius Rupee'), ('MVR', 'MVRRufiyaa'), ('MWK', 'MWKMalawi Kwacha'), ('MXN', 'MXNMexican Peso'), ('MYR', 'MYRMalaysian Ringgit'), ('MZN', 'MZNMozambique Metical'), ('NAD', 'NADNamibia Dollar'), ('NGN', 'NGNNaira'), ('NIO', 'NIOCordoba Oro'), ('NOK', 'NOKNorwegian Krone'), ('NPR', 'NPRNepalese Rupee'), ('NZD', 'NZDNew Zealand Dollar'), ('OMR', 'OMRRial Omani'), ('PAB', 'PABBalboa'), ('PEN', 'PENSol'), ('PGK', 'PGKKina'), ('PHP', 'PHPPhilippine Peso'), ('PKR', 'PKRPakistan Rupee'), ('PLN', 'PLNZloty'), ('PYG', 'PYGGuarani'), ('QAR', 'QARQatari Rial'), ('RON', 'RONRomanian Leu'), ('RSD', 'RSDSerbian Dinar'), ('RUB', 'RUBRussian Ruble'), ('RWF', 'RWFRwanda Franc'), ('SAR', 'SARSaudi Riyal'), ('SBD', 'SBDSolomon Islands Dollar'), ('SCR', 'SCRSeychelles Rupee'), ('SDG', 'SDGSudanese Pound'), ('SEK', 'SEKSwedish Krona'), ('SGD', 'SGDSingapore Dollar'), ('SHP', 'SHPSaint Helena Pound'), ('SLL', 'SLLLeone'), ('SOS', 'SOSSomali Shilling'), ('SRD', 'SRDSurinam Dollar'), ('SSP', 'SSPSouth Sudanese Pound'), ('STD', 'STDDobra'), ('SVC', 'SVCEl Salvador Colon'), ('SYP', 'SYPSyrian Pound'), ('SZL', 'SZLLilangeni'), ('THB', 'THBBaht'), ('TJS', 'TJSSomoni'), ('TMT', 'TMTTurkmenistan New Manat'), ('TND', 'TNDTunisian Dinar'), ('TOP', 'TOPPa’anga'), ('TRY', 'TRYTurkish Lira'), ('TTD', 'TTDTrinidad and Tobago Dollar'), ('TWD', 'TWDNew Taiwan Dollar'), ('TZS', 'TZSTanzanian Shilling'), ('UAH', 'UAHHryvnia'), ('UGX', 'UGXUganda Shilling'), ('USD', 'USDUS Dollar'), ('UYU', 'UYUPeso Uruguayo'), ('UZS', 'UZSUzbekistan Sum'), ('VEF', 'VEFBolívar'), ('VND', 'VNDDong'), ('VUV', 'VUVVatu'), ('WST', 'WSTTala'), ('XAF', 'XAFCFA Franc BEAC'), ('XAG', 'XAGSilver'), ('XAU', 'XAUGold'), ('XBA', 'XBABond Markets Unit European Composite Unit (EURCO)'), ('XBB', 'XBBBond Markets Unit European Monetary Unit (E.M.U.-6)'), ('XBC', 'XBCBond Markets Unit European Unit of Account 9 (E.U.A.-9)'), ('XBD', 'XBDBond Markets Unit European Unit of Account 17 (E.U.A.-17)'), ('XCD', 'XCDEast Caribbean Dollar'), ('XDR', 'XDRSDR (Special Drawing Right)'), ('XOF', 'XOFCFA Franc BCEAO'), ('XPD', 'XPDPalladium'), ('XPF', 'XPFCFP Franc'), ('XPT', 'XPTPlatinum'), ('XSU', 'XSUSucre'), ('XTS', 'XTSCodes specifically reserved for testing purposes'), ('XUA', 'XUAADB Unit of Account'), ('XXX', 'XXXThe codes assigned for transactions where no currency is involved'), ('YER', 'YERYemeni Rial'), ('ZAR', 'ZARRand'), ('ZMW', 'ZMWZambian Kwacha'), ('ZWL', 'ZWLZimbabwe Dollar')], max_length=3, null=True),
        ),
    ]
