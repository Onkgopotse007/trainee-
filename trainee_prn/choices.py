from edc_constants.constants import OTHER


CAUSE_OF_DEATH_CAT = (
    ('suicide', 'Suicide'),
    ('trauma', 'Trauma/Accident'),
    ('no_info', 'No information available'),
    (OTHER, 'Other, specify'),)



DEATH_INFO_SOURCE = (
    ('death_certificate_review', 'Death Certificate Review'),
    ('clinician', 'Clinician'),
    ('next_of_kin1', 'Next of kin 1'),
    ('inpatient_medical_file', 'Inpatient medical file'),
    ('fam_member', 'family member (specify relationship)'),
    (OTHER, 'Other (specify)'),
)



DEATH_PLACE = (
    ('home_or_community', 'Home or in the community'),
    ('facility', 'At facility'),
    ('unknown', 'Place of death unknown')
)

DISPOSITION = (
    ('exit', 'Exit'),
)


DISTRICT = (
    ('chobe', 'Chobe - Chobe'),
    ('bobonong', 'Central - Bobonong'),
    ('boteti', 'Central - Boteti'),
    ('mahalapye', 'Central - Mahalapye'),
    ('orapa', 'Central - Orapa'),
    ('serowe_palapye', 'Central - Serowe/Palapye'),
    ('tutume', 'Central - Tutume'),
    ('CKGR', 'ghanzi - CKGR'),
    ('ghanzi', 'ghanzi - Ghanzi'),
    ('kgalagdi_north', 'Kgalagadi North'),
    ('kgalagadi_south', 'Kgalagadi South'),
    ('kgatleng', 'Kgatleng'),
    ('kweneng_east', 'Kweneng - East'),
    ('kweneng_west', 'Kweneng - West'),
    ('delta', 'north West - Delta'),
    ('ngamiland_north', 'North West - Ngamiland Nort'),
    ('ngamiland_south', 'North East - Ngamiland South'),
    ('north_east', 'North East'),
    ('barolong', 'Southern - Barolong'),
    ('ngwaketse', 'Southern - Ngwaketse'),
    ('ngwaketse_west', 'Southern - Ngwaketse West'),
)

FACILITY = (
    ('athlone_hospital', 'Athlone Hospital'),
    ('bamalete_lutheran_hospital', 'Bamalete Lutheran Hospital'),
    ('bokaa_clinic', 'Bokaa clinic'),
    ('deborah_reteif_memorial_hospital', 'Deborah. Reteif. Memorial Hospital'),
    ('goodhope_hospital', 'Goodhope Hospital'),
    ('gweta_hospital', 'Gweta Hospital'),
    ('kanye_sda_hospital', 'Kanye SDA Hospital'),
    ('lentsweletau_clinic', 'Lentsweletau clinic'),
    ('lerala_clinic', 'Lerala clinic'),
    ('letlhakeng_clinic', 'Letlhakeng clinic'),
    ('mahalapye_hospital', 'Mahalapye Hospital'),
    ('mandunyane_clinic', 'Mandunyane clinic'),
    ('manga_clinic', 'Manga clinic'),
    ('masunga_primary_hospital', 'Masunga Primary Hospital'),
    ('masunga_clinic', 'Masunga clinic'),
    ('mathangwane_clinic', 'Mathangwane clinic'),
    ('maunatlala_clinic', 'Maunatlala clinic'),
    ('metsimotlhabe_clinic', 'Metsimotlhabe clinic'),
    ('mmadianare_primary_hospital', 'Mmadinare Primary Hospital'),
    ('mmankgodi_clinic', 'Mmankgodi clinic'),
    ('mmathethe_clinic', 'Mmathethe clinic'),
    ('molapowabojang_clinic', 'Molapowabojang clinic'),
    ('nata_clinic', 'Nata clinic'),
    ('nyangagwe_hospital', 'Nyangagwe Hospital'),
    ('oodi_clinic', 'Oodi clinic'),
    ('otse_clinic', 'Otse clinic'),
    ('palapye_hospital', 'Palapye Hospital'),
    ('princess_marina_hospital', 'Princess Marina Hospital'),
    ('ramokgonami_clinic', 'Ramokgonami clinic'),
    ('scottish_livingstone_hospital', 'Scottish Livingstone Hospital'),
    ('sefophe_clinic', 'Sefophe clinic'),
    ('selibe_phikwe_hospital', 'Selibe Phikwe Hospital'),
    ('sheleketla_clinic', 'Sheleketla clinic'),
    ('shoshong_clinic', 'Shoshong clinic'),
    ('tati_siding_clinic', 'Tati Siding clinic'),
    ('thamaga_hospital', 'Thamaga Hospital'),
    (OTHER, 'Other (specify)')
)

FACILITY_TYPE = (
    ('health_post', 'health post'),
    ('primary_clinic', 'primary clinic'),
    ('primary_hospital', 'primary hospital'),
    ('secondary_hospital', 'secondary hospital'),
    ('referral_hospital', 'referral hospital')
)


REASON_FOR_EXIT = (
    ('death', 'Patient death'),
    ('eval_complete', 'Evaluation complete'),
    ('declines_further_eval',
     'Patient or clinician declines further evaluation'),
    ('patient_requests_removal', 'Patient requests removal from Trainee'),
    (OTHER, 'Other (specify)'),
)