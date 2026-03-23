#!/bin/bash

cd /Users/biswajit/AI/Astrology/Report

# Create folders
mkdir -p Navamsa_D9 Marriage_Spouse Nadi_Astrology \
         Jaimini_Astrology House_Lords Divisional_Charts \
         Transit_Foreign General_Reference Specific_Topics Misc

# Charts folder — move D1 chart in, move D9 out to Navamsa_D9
mv "Chart.pdf" Charts/
mv "D9-Chart.pdf" Navamsa_D9/

# Navamsa_D9 — D9 + all Navamsa files
# NOTE: Navamsha.pdf duplicate removed (was listed twice in original)
# NOTE: Cyrillic filename д9.pdf handled directly
mv "д9.pdf" Navamsa_D9/ 2>/dev/null || echo "Warning: д9.pdf not found — check filename manually"
mv "Nava-Masa.pdf" \
   "navamsa-2.pdf" \
   "navamsa-pdf.pdf" \
   "navamsa.pdf" \
   "Navamsha.pdf" \
   "Navamsa-and-Astrological-Predictions.pdf" \
   "Navamsa-and-Marriage.pdf" \
   "Navamsa-and-Married-Life.pdf" \
   "Navamsa-Chart-in-Predictions.pdf" \
   "Navamsa-Chart-is-a-Very-Important-Chart-in-Vedic-Astrology.pdf" \
   "Navamsa-Chart.pdf" \
   "Navamsa-D-9-Chart-Prediction-Analysis-In-Vedic-Astrology-pdf.pdf" \
   "Navamsa-D-9-Chart.pdf" \
   "Navamsa-Interpretation.pdf" \
   "Navamsa-Notes.pdf" \
   "Navamsa-Sanjay-Rath.pdf" \
   "Navamsa-Visti-Larsen.pdf" \
   "Plutonicdesire-Net-d9-Chart.pdf" \
   "Pushkara-Navamsha.pdf" \
   "Secrets-of-D9.pdf" \
   "Secrets-of-the-D9-chart.pdf" \
   "Tips-to-read-navamsa-chart-by-aashay-shroff.pdf" \
   "Use-of-Navamsa-Chart-in-astrology.pdf" \
   "Interpretation-of-Navamsa-Chart.pdf" \
   "ilide.info-navamsa-chart-pr_a937ef5425a87c8fe094f7ceb48bb4f6.pdf" \
   Navamsa_D9/

# Marriage_Spouse
mv "406861145-Spouse-from-Navamsa-Chart-docx-docx.pdf" \
   "All-About-Spouse-via-Astrology-Thevedichoroscope.pdf" \
   "ASTROLOGICAL-INDICATIONS-OF-APPEARANCE-OF-SPOUSE.pdf" \
   "BLOG-6-INDICATION-OF-BAD-MARRIAGE-BY-ASTROLOGY.pdf" \
   "Extra-Marital-Relationship-And-Vedic-Astrology.pdf" \
   "Future-Spouse-Prospective-Life-Partner-Appearance-How-to-Find-Fut.pdf" \
   "future-spouse-prospective-life-partner-appearance-how-to-find-outpdf.pdf" \
   "how-to-find-spouse-first-alphabet.pdf" \
   "ilide.info-decoding-the-mysteries-of-upapada-lagna-pr_df3317c692681f1877480a5e875d33ff.pdf" \
   "intercaste-marraige.pdf" \
   "Marriage-Matching-Through-Upa-Pada.pdf" \
   "Marriage-Related-Astrological-Rules-Under-Bhrigu-n.pdf" \
   "Marriage-timing-in-astrology-Easy-Method-to-predict-Exact-age-and-date.pdf" \
   "Nakshatra-Yoni-and-your.pdf" \
   "Predicting Marriage.pdf" \
   "Spouse-from-Navamsa-Chart-docx-2.pdf" \
   "Spouse-from-Navamsa-Chart-docx.pdf" \
   "Spouse-From-Navamsha.pdf" \
   "Spouse-Prediction-Astrology-Beautiful-Wife-and-Handsome-Husband-by-Date-of-Birth-and-Time.pdf" \
   Marriage_Spouse/

# Nadi_Astrology
mv "244-Nadi-Job.pdf" \
   "Basic-Rules-of-Bhrigu-Nandi-Nadi-Astrology.pdf" \
   "BNN-Bootcamp-3-Combinations-Part-1-1.pdf" \
   "BNN-Diploma-17-Progression-of-Jupiter.pdf" \
   "BNN-Diploma-Class-13.pdf" \
   "BNR-RVA-Software.pdf" \
   "ilide.info-bhrighu-saral-paddathi-pr_ee49385e48216e1df40c13b73516d507.pdf" \
   "Nadi-Intrduction.pdf" \
   "Satyamma-Bharadwaj-Practical-Nadi-Astrology.pdf" \
   "Teqniques-of-Predection-by-Nidhi-Soni.pdf" \
   "Time-of-1st-and-2nd-Marriage-in-BNN.pdf" \
   Nadi_Astrology/

# Jaimini_Astrology
mv "Atmakaraka-PART-2.pdf" \
   "Darakaraka-2.pdf" \
   "Darakaraka-Planets-Life-Partner-Spouse-Details-With-Jaimini-Astrology.pdf" \
   "Darakaraka.pdf" \
   "K-N-Rao-Jaiminis-Chara-Dasha.pdf" \
   Jaimini_Astrology/

# House_Lords
mv "2HL-in-Different-Hs.pdf" \
   "7-Th-Lord-in-8th-Jupiter.pdf" \
   "7th-House-Planets.pdf" \
   "7th-lord.pdf" \
   "HOUSE-LORDS-IN-DIFFERENT-HOUSES-doc.pdf" \
   "Lord-of-7th-House.pdf" \
   "Lord-of-Ascendant.pdf" \
   House_Lords/

# Divisional_Charts — D7 and D10 only (NOT D9)
mv "DashamshaChart-1551973430078.pdf" \
   "SAPTAMSA-D7.pdf" \
   Divisional_Charts/

# Transit_Foreign
mv "BNN-Diploma-20-Transit-of-Rahu-ketu-and-daily-and-monthly-transits.pdf" \
   "Foreign-Travel-and-Settlement-in-Astrology.pdf" \
   Transit_Foreign/

# General_Reference
mv "Astro-Direction.pdf" \
   "Graha-pdf.pdf" \
   "ICAS-Jyotish-Praveen-II-Study-Material.pdf" \
   "K-N-Rao-and-Meenakshi-Raut-Applied-Astrology.pdf" \
   "KN-RAO-S-Astrology-Lessons.pdf" \
   "Lesson-3.pdf" \
   "New-techniques-of-predictions-1.pdf" \
   "Objective-Question-Paper.pdf" \
   "paper.pdf" \
   "paperpdf-1591437649.pdf" \
   "prediction-is-an-art.pdf" \
   General_Reference/

# Specific_Topics — specific subject files
mv "baby-boy.pdf" \
   "Mars-and-Bodyfriend.pdf" \
   "Shy.pdf" \
   Specific_Topics/

# Misc — non-astrology
mv "Specific-Relief-Act-MCQ.pdf" Misc/

echo "✅ Done. Verifying folder contents..."
echo ""
echo "=== Charts ==="
ls Charts/
echo ""
echo "=== Navamsa_D9 ==="
ls Navamsa_D9/
echo ""
echo "=== Marriage_Spouse ==="
ls Marriage_Spouse/
echo ""
echo "=== Nadi_Astrology ==="
ls Nadi_Astrology/
echo ""
echo "=== Jaimini_Astrology ==="
ls Jaimini_Astrology/
echo ""
echo "=== House_Lords ==="
ls House_Lords/
echo ""
echo "=== Divisional_Charts ==="
ls Divisional_Charts/
echo ""
echo "=== Transit_Foreign ==="
ls Transit_Foreign/
echo ""
echo "=== General_Reference ==="
ls General_Reference/
echo ""
echo "=== Specific_Topics ==="
ls Specific_Topics/
echo ""
echo "=== Misc ==="
ls Misc/
echo ""
echo "=== Remaining in Report root (should be empty except Charts subfolder) ==="
ls -la | grep -v "^d" | grep -v "^total"