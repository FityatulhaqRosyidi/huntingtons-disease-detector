

# Threshold for detecting DNA patterns
# >= 40 : Terdeteksi Huntington
# >= 36 : Terdeteksi Gejala Ringan Huntington
# >= 27 : Tidak ada penyakit Huntington, namun berpotensi mewariskan gen penyakit Huntington
# < 27 : normal

INTERMEDIATE_THRESHOLD = 27
SYMPTOM_THRESHOLD = 36

INTERMEDIATE_PATTERN = "CAG" * INTERMEDIATE_THRESHOLD
SYMPTOM_PATTERN = "CAG" * SYMPTOM_THRESHOLD

