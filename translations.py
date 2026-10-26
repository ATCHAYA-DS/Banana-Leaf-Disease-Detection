"""
Comprehensive translations for Robust Banana Leaf Disease Detection application.
Languages supported:
- en: English
- ta: Tamil (தமிழ்)
- hi: Hindi (हिन्दी)
- te: Telugu (తెలుగు)
- ml: Malayalam (മലയാളം)
- kn: Kannada (ಕನ್ನಡ)
"""

TRANSLATIONS = {
    "en": {
        "app_title": "Robust Banana Leaf Disease Detection",
        "app_tagline": "AI-Powered Diagnostic Tool for Healthy & Resilient Banana Plantations",
        "nav_home": "Home",
        "nav_detect": "Detect Disease",
        "nav_dashboard": "Dashboard",
        "nav_about": "About Project",
        "demo_mode_badge": "DEMO MODE (Baseline Computer Vision)",
        "demo_mode_desc": "No trained CNN model weights found in /model directory. Predictions are generated using OpenCV computer vision heuristics for educational and demonstration purposes.",
        "model_trained_badge": "CNN MODEL ACTIVE",
        "upload_title": "Upload Banana Image",
        "upload_desc": "Upload a clear photo of a banana leaf or an entire banana plant for automated diagnostic analysis.",
        "mode_single": "Single Leaf Image",
        "mode_whole": "Whole Banana Plant Image",
        "drag_drop_text": "Drag and drop leaf or plant photo here, or click to browse",
        "supported_formats": "Supports: JPG, JPEG, PNG (Max 16 MB)",
        "btn_analyze": "Analyze Disease Now",
        "btn_analyzing": "Analyzing Image...",
        "btn_another": "Analyze Another Image",
        "btn_speak": "Listen to Diagnosis",
        "btn_stop_speak": "Stop Voice",
        "btn_view_dashboard": "View Farm Dashboard",
        "features_title": "Key Capabilities",
        "feature_1_title": "Single & Whole-Plant Analysis",
        "feature_1_desc": "Analyze individual leaves or upload full-plant images where leaves are automatically isolated and inspected.",
        "feature_2_title": "OpenCV Preprocessing",
        "feature_2_desc": "Noise reduction, bilateral filtering, and CLAHE shadow/sunlight illumination compensation.",
        "feature_3_title": "Explainable AI (XAI)",
        "feature_3_desc": "Grad-CAM visual heatmaps highlight affected leaf tissue, explaining why the diagnosis was made.",
        "feature_4_title": "Farmer Guidance & Voice",
        "feature_4_desc": "Actionable agronomic advice with multi-language voice narration in 6 regional languages.",
        "how_it_works_title": "How It Works",
        "step_1": "1. Upload Leaf or Plant Photo",
        "step_1_desc": "Capture a clear image under natural daylight without heavy blur.",
        "step_2": "2. Preprocessing & Segmentation",
        "step_2_desc": "OpenCV removes lighting glare, shadows, and isolates individual leaf regions.",
        "step_3": "3. AI Diagnostic & Grad-CAM",
        "step_3_desc": "Neural network detects symptoms and generates an XAI attention map overlay.",
        "step_4": "4. Results & Farmer Advice",
        "step_4_desc": "Receive instant status, disease name, recommendations, and audio readout.",
        "result_heading": "Disease Diagnosis Results",
        "status_healthy": "HEALTHY PLANT",
        "status_diseased": "DISEASE DETECTED",
        "label_disease": "Identified Condition",
        "label_confidence": "Diagnostic Confidence",
        "label_status": "Health Status",
        "label_explanation": "Visual Diagnosis Explanation",
        "label_recommendations": "Practical Management Recommendations",
        "label_prevention": "Prevention & Field Hygiene Tips",
        "safety_disclaimer": "Safety Disclaimer: These suggestions are for agricultural guidance only. Do not apply chemical pesticides without consultation. Always verify with your local agricultural extension officer or Krishi Vigyan Kendra (KVK).",
        "tab_original": "Original Image",
        "tab_preprocessed": "Preprocessed (Shadow/Noise Removed)",
        "tab_xai": "Explainable AI (Grad-CAM Heatmap)",
        "xai_explanation_note": "The heat map highlights in warm colors (red/orange) the exact symptomatic spots, necrotic lesions, or chlorotic streaks that triggered the diagnostic detection.",
        "whole_plant_summary": "Whole-Plant Segmentation Analysis",
        "whole_plant_desc": "Our vision system identified individual leaf regions from the whole-plant image. Below is the multi-leaf diagnostic breakdown:",
        "dashboard_title": "Farmer Disease Surveillance Dashboard",
        "stat_total": "Total Images Analyzed",
        "stat_healthy": "Healthy Leaves",
        "stat_diseased": "Diseased Leaves",
        "stat_ratio": "Health Ratio",
        "chart_distribution": "Disease Distribution Summary",
        "recent_table_title": "Recent Crop Scans",
        "col_thumbnail": "Scan",
        "col_date": "Timestamp",
        "col_mode": "Type",
        "col_disease": "Diagnosis",
        "col_confidence": "Confidence",
        "col_status": "Status",
        "col_action": "Action",
        "btn_view": "View Details",
        "btn_clear_history": "Clear History",
        "no_records": "No scans recorded yet. Upload your first banana leaf image!",
        "footer_text": "Robust Banana Leaf Disease Detection — Supporting Farmers with Practical AI",
        "disease_info": {
            "Healthy": {
                "name": "Healthy Banana Leaf",
                "status": "Healthy",
                "explanation": "Leaf shows rich, uniform green coloration with intact venation. No visible fungal spots, chlorosis, or necrotic streaks detected.",
                "recommendations": [
                    "Continue standard balanced fertilizer regimen (NPK + micro-nutrients) to maintain vigorous foliage.",
                    "Ensure adequate field drainage and maintain 2.0 to 2.5 meter plant spacing to allow sunlight penetration.",
                    "Routinely inspect undersides of older leaves during humid and rainy periods as early detection is vital."
                ],
                "prevention": [
                    "Sanitize cutting tools before trimming suckers or removing older dried leaves.",
                    "Use certified disease-free tissue-cultured banana plantlets for new plantations."
                ]
            },
            "Black Sigatoka": {
                "name": "Black Sigatoka (Pseudocercospora fijiensis)",
                "status": "Diseased",
                "explanation": "Characteristic dark reddish-brown to black narrow streaks visible parallel to leaf veins, coalescing into sunken necrotic patches with yellow halos.",
                "recommendations": [
                    "Perform sanitary de-leafing: prune and safely bury or burn heavily infected leaves to reduce airborne ascospore inoculum.",
                    "Improve plantation aeration and drainage to reduce moisture persistence on leaf surfaces.",
                    "Apply approved bio-control sprays like Neem oil extract or Pseudomonas fluorescens on emerging unfurled leaves.",
                    "Avoid overhead sprinkler irrigation; switch to drip irrigation to prevent spore dispersal."
                ],
                "prevention": [
                    "Widen plant spacing to facilitate rapid morning dew drying.",
                    "Apply potassium and silica supplements to strengthen leaf epidermal cell walls against fungal penetration."
                ]
            },
            "Yellow Sigatoka": {
                "name": "Yellow Sigatoka (Pseudocercospora musae)",
                "status": "Diseased",
                "explanation": "Pale yellow or yellowish-green elongated streaks developing into oval lesions with grayish-white centers surrounded by a distinct yellow chlorotic margin.",
                "recommendations": [
                    "Prune out older spotted leaves before fungal fruiting structures mature and discharge conidia spores.",
                    "Maintain optimal soil drainage to avoid waterlogged conditions which promote fungal infection cycles.",
                    "Spray approved copper-based organic formulations or bio-fungicides in accordance with regional agricultural university advice.",
                    "Ensure balanced potash fertilization; avoid excess nitrogen which produces succulent, disease-prone leaf tissue."
                ],
                "prevention": [
                    "Keep orchard floor clean and weed-free to lower microclimate humidity beneath the canopy.",
                    "Inspect crops bi-weekly during monsoon seasons for prompt early stage intervention."
                ]
            },
            "Panama Disease": {
                "name": "Panama Disease (Fusarium Wilt - Fusarium oxysporum)",
                "status": "Diseased",
                "explanation": "Pronounced yellowing starting from oldest outer leaf margins progressing inward toward the midrib, followed by petiole buckling, leaf wilting, and skirt collapse.",
                "recommendations": [
                    "Strictly quarantine infected banana mats. Dig an isolating trench around affected clumps to prevent fungal spread via root-to-root contact or runoff.",
                    "Never transfer soil, farming implements, or suckers from this infected area to clean fields.",
                    "Sterilize machetes, spades, and footwear with 10% sodium hypochlorite or farm disinfectant.",
                    "Enrich root zone with organic compost blended with Trichoderma harzianum or Trichoderma viride to suppress soil pathogen populations."
                ],
                "prevention": [
                    "Plant resistant banana cultivars or tissue culture varieties recommended for your region.",
                    "Immediately report suspected Fusarium wilt outbreaks to your local agricultural department or Krishi Vigyan Kendra (KVK)."
                ]
            }
        }
    },
    "ta": {
        "app_title": "வாழை இலை நோய் கண்டறிதல் மற்றும் வழிகாட்டி",
        "app_tagline": "விவசாயிகளுக்கான எளிய மற்றும் துல்லியமான செயற்கை நுண்ணறிவு (AI) தொழில்நுட்பம்",
        "nav_home": "முகப்பு",
        "nav_detect": "நோய் கண்டறிதல்",
        "nav_dashboard": "விவசாயி டாஷ்போர்டு",
        "nav_about": "திட்டம் பற்றி",
        "demo_mode_badge": "மாதிரி முறை (டெமோ பயன்முறை)",
        "demo_mode_desc": "பயிற்சி பெற்ற CNN மாடல் கோப்பு இல்லை. OpenCV கணினி பார்வை மூலம் மாதிரி முடிவுகள் காட்டப்படுகின்றன.",
        "model_trained_badge": "AI மாடல் செயல்படுகிறது",
        "upload_title": "வாழை இலை படம் பதிவேற்றவும்",
        "upload_desc": "நோய் கண்டறிய ஒரு வாழை இலை அல்லது முழு வாழை மரத்தின் தெளிவான புகைப்படத்தை பதிவேற்றவும்.",
        "mode_single": "ஒற்றை இலை படம்",
        "mode_whole": "முழு வாழை மரம் படம்",
        "drag_drop_text": "படத்தை இங்கே இழுத்து விடவும் அல்லது தேர்வு செய்ய கிளிக் செய்யவும்",
        "supported_formats": "ஆதரிக்கப்படும் வடிவங்கள்: JPG, JPEG, PNG (அதிகபட்சம் 16 MB)",
        "btn_analyze": "நோயை கண்டறியவும்",
        "btn_analyzing": "படம் பகுப்பாய்வு செய்யப்படுகிறது...",
        "btn_another": "மற்றொரு படத்தை சோதிக்கவும்",
        "btn_speak": "முடிவை தமிழில் கேட்கவும்",
        "btn_stop_speak": "குரலை நிறுத்தவும்",
        "btn_view_dashboard": "டாஷ்போர்டை பார்க்கவும்",
        "features_title": "முக்கிய அம்சங்கள்",
        "feature_1_title": "இலை & முழு மர பகுப்பாய்வு",
        "feature_1_desc": "ஒற்றை இலை அல்லது முழு மரத்தில் உள்ள ஒவ்வொரு இலையையும் தானாக பிரித்து கண்டறியும் வசதி.",
        "feature_2_title": "OpenCV முன்கூட்டிய செயலாக்கம்",
        "feature_2_desc": "நிழல், அதிக சூரிய ஒளி மற்றும் இரைச்சலை நீக்கி தெளிவான படத்தை உருவாக்குகிறது.",
        "feature_3_title": "விளக்கக்கூடிய AI (Grad-CAM)",
        "feature_3_desc": "இலையில் பாதிக்கப்பட்ட பகுதிகளை வண்ண வெப்ப வரைபடம் மூலம் தெளிவாக காட்டுகிறது.",
        "feature_4_title": "விவசாயி ஆலோசனை & குரல் உதவி",
        "feature_4_desc": "எளிய தமிழில் சிகிச்சை முறைகள் மற்றும் குரல் வழி வாசிப்பு வசதி.",
        "how_it_works_title": "இது எவ்வாறு இயங்குகிறது",
        "step_1": "1. புகைப்படத்தை பதிவேற்றவும்",
        "step_1_desc": "வாழை இலை அல்லது மரத்தின் தெளிவான படத்தை எடுக்கவும்.",
        "step_2": "2. பட செயலாக்கம்",
        "step_2_desc": "OpenCV நிழல் மற்றும் வெளிச்சத்தை சரிசெய்து இலைகளை அடையாளம் காண்கிறது.",
        "step_3": "3. AI நோய் ஆய்வு",
        "step_3_desc": "செயற்கை நுண்ணறிவு நோயை கண்டறிந்து வெப்ப வரைபடத்தை உருவாக்குகிறது.",
        "step_4": "4. முடிவுகள் & விவசாயி ஆலோசனை",
        "step_4_desc": "நோய் பெயர், துல்லிய சதவீதம் மற்றும் எளிய மேலாண்மை வழிகாட்டலை பெறவும்.",
        "result_heading": "நோய் கண்டறிதல் முடிவுகள்",
        "status_healthy": "ஆரோக்கியமான பயிர்",
        "status_diseased": "நோய் கண்டறியப்பட்டுள்ளது",
        "label_disease": "கண்டறியப்பட்ட நோய்",
        "label_confidence": "துல்லிய சதவீதம்",
        "label_status": "பயிர் நிலை",
        "label_explanation": "நோயின் விளக்கம்",
        "label_recommendations": "பரிந்துரைக்கப்படும் மேலாண்மை முறைகள்",
        "label_prevention": "தடுப்பு மற்றும் சுகாதார குறிப்புகள்",
        "safety_disclaimer": "பாதுகாப்பு எச்சரிக்கை: இந்த பரிந்துரைகள் பொதுவான விவசாய வழிகாட்டுதலுக்காக மட்டுமே. மருந்துகளை பயன்படுத்தும் முன் எப்போதும் வேளாண்மை அலுவலர் அல்லது வேளாண் அறிவியல் மைய (KVK) வல்லுநர்களை அணுகவும்.",
        "tab_original": "அசல் படம்",
        "tab_preprocessed": "செயலாக்கப்பட்ட படம் (நிழல் நீக்கப்பட்டது)",
        "tab_xai": "AI வெப்ப வரைபடம் (Grad-CAM)",
        "xai_explanation_note": "சிவப்பு மற்றும் மஞ்சள் நிறப் பகுதிகள், AI மாதிரி நோயை உறுதி செய்ய கவனம் செலுத்திய பாதிக்கப்பட்ட திசுக்களைக் குறிக்கின்றன.",
        "whole_plant_summary": "முழு மர இலைகளின் பகுப்பாய்வு",
        "whole_plant_desc": "முழு மர புகைப்படத்தில் இருந்து தனித்தனி இலைகள் பிரிக்கப்பட்டு ஒவ்வொன்றாக ஆய்வு செய்யப்பட்டன:",
        "dashboard_title": "விவசாயி நோய் கண்காணிப்பு டாஷ்போர்டு",
        "stat_total": "மொத்த படங்கள்",
        "stat_healthy": "ஆரோக்கியமான இலைகள்",
        "stat_diseased": "பாதிக்கப்பட்ட இலைகள்",
        "stat_ratio": "ஆரோக்கிய விகிதம்",
        "chart_distribution": "நோய் பரவல் சுருக்கம்",
        "recent_table_title": "சமீபத்திய சோதனைகள்",
        "col_thumbnail": "படம்",
        "col_date": "தேதி & நேரம்",
        "col_mode": "வகை",
        "col_disease": "கண்டறியப்பட்ட நிலை",
        "col_confidence": "துல்லியம்",
        "col_status": "நிலை",
        "col_action": "செயல்",
        "btn_view": "விவரம் பார்க்க",
        "btn_clear_history": "வரலாற்றை அழிக்க",
        "no_records": "இதுவரை எந்த சோதனையும் செய்யப்படவில்லை. உங்கள் முதல் வாழை இலை படத்தை பதிவேற்றவும்!",
        "footer_text": "வாழை இலை நோய் கண்டறிதல் — விவசாயிகளுக்கு உதவும் எளிய தொழில்நுட்பம்",
        "disease_info": {
            "Healthy": {
                "name": "ஆரோக்கியமான வாழை இலை",
                "status": "ஆரோக்கியமானது",
                "explanation": "இலை சீரான அடர் பச்சை நிறத்துடன் ஆரோக்கியமாக உள்ளது. பூஞ்சை புள்ளிகளோ, மஞ்சள் கோடுகளோ அல்லது திசு அழிவுகளோ இல்லை.",
                "recommendations": [
                    "பயிரின் வீரியத்தை தக்கவைக்க சமச்சீர் உர மேலாண்மையை (NPK + நுண்சத்துக்கள்) தொடரவும்.",
                    "தோட்டத்தில் நல்ல வடிகால் வசதியை ஏற்படுத்தி, சூரிய ஒளி நன்கு பட செடிகளுக்கு இடையே 2.0 முதல் 2.5 மீட்டர் இடைவெளி விடவும்.",
                    "மழை மற்றும் ஈரப்பதமான காலங்களில் பழைய இலைகளின் அடிப்பகுதியை தவறாமல் கண்காணிக்கவும்."
                ],
                "prevention": [
                    "கன்றுகளை வெட்டும்போது அல்லது காய்ந்த இலைகளை அகற்றும் போது கருவிகளை தூய்மைப்படுத்தவும்.",
                    "புதிய நடவுக்கு சான்றளிக்கப்பட்ட திசு வளர்ப்பு வாழை கன்றுகளைப் பயன்படுத்தவும்."
                ]
            },
            "Black Sigatoka": {
                "name": "கருப்பு சிகடோகா இலைப்புள்ளி நோய் (Black Sigatoka)",
                "status": "பாதிக்கப்பட்டது",
                "explanation": "இலை நரம்புகளுக்கு இணையாக அடர் பழுப்பு அல்லது கருப்பு நிற குறுகிய கோடுகள் தோன்றி, பின்னர் காய்ந்த திட்டுகளாக மாறுகின்றன.",
                "recommendations": [
                    "தீவிரமாக பாதிக்கப்பட்ட இலைகளை வெட்டி அப்புறப்படுத்தி, தீயிட்டு அல்லது குழி தோண்டி பாதுகாப்பாக புதைக்கவும்.",
                    "காற்றோட்டத்தை அதிகரிக்கவும், இலைகளில் ஈரப்பதம் தேங்காமல் இருக்க வடிகால் வசதியை சீரமைக்கவும்.",
                    "வேப்பெண்ணெய் கரைசல் அல்லது அங்கீகரிக்கப்பட்ட சூடோமோனாஸ் (Pseudomonas fluorescens) கரைசலை தெளிக்கவும்.",
                    "மேலிருந்து தெளிக்கும் தெளிப்பான்களை தவிர்த்து சொட்டு நீர் பாசன முறையை பயன்படுத்தவும்."
                ],
                "prevention": [
                    "மரங்களுக்கு இடையே போதிய இடைவெளி விட்டு காலை நேர பனி விரைவாக காய வழிவகுக்கவும்.",
                    "இலையின் நோய் எதிர்ப்பு திறனை அதிகரிக்க சாம்பல் சத்து (பொட்டாஷ்) உரங்களை முறையாக இடவும்."
                ]
            },
            "Yellow Sigatoka": {
                "name": "மஞ்சள் சிகடோகா இலைப்புள்ளி நோய் (Yellow Sigatoka)",
                "status": "பாதிக்கப்பட்டது",
                "explanation": "இலைகளில் வெளிர் மஞ்சள் அல்லது நீள்வட்ட புள்ளிகள் தோன்றி, அவற்றின் நடுப்பகுதி சாம்பல் நிறமாகவும் சுற்றிலும் மஞ்சள் வளையமாகவும் காட்சியளிக்கும்.",
                "recommendations": [
                    "நோய் தாக்கிய முதிர்ந்த இலைகளை வெட்டி தோட்டத்தில் இருந்து அப்புறப்படுத்தவும்.",
                    "தோட்டத்தில் தண்ணீர் தேங்காமல் பார்த்துக் கொள்ளவும், நீர் தேங்குவது பூஞ்சை பரவுவதை தூண்டும்.",
                    "வேளாண் பல்கலைக்கழக வழிகாட்டுதலின்படி தாமிர கரைசல் (Copper hydroxide) அல்லது இயற்கை பூஞ்சாண கொல்லிகளை தெளிக்கவும்.",
                    "அதிகப்படியான தழைச்சத்து உரங்களை தவிர்த்து சமச்சீர் பொட்டாஷ் உரங்களை வழங்கவும்."
                ],
                "prevention": [
                    "தோட்டத்தை களைகள் இல்லாமல் சுத்தமாக வைத்து ஈரப்பதத்தை குறைக்கவும்.",
                    "மழைக்காலங்களில் வாரம் இருமுறை பயிர்களை பரிசோதித்து ஆரம்பத்திலேயே கட்டுப்படுத்தவும்."
                ]
            },
            "Panama Disease": {
                "name": "பனாமா வாடல் நோய் (Panama Wilt - Fusarium)",
                "status": "பாதிக்கப்பட்டது",
                "explanation": "வெளிப்புற கீழ் இலைகளின் ஓரங்கள் மஞ்சள் நிறமாக மாறி நரம்புகளை நோக்கி பரவி, இலைக்காம்புகள் உடைந்து மடிந்து தொங்கும்.",
                "recommendations": [
                    "பாதிக்கப்பட்ட வாழை மரத்தை உடனடியாக தனிமைப்படுத்தவும். வேர்கள் வழியே பரவாமல் தடுக்க சுற்றிலும் ஆழமான அகழி வெட்டவும்.",
                    "பாதிக்கப்பட்ட இடத்திலிருந்து மண், உபகரணங்கள் அல்லது கன்றுகளை நல்ல நிலத்திற்கு கொண்டு செல்ல வேண்டாம்.",
                    "வெட்டுக் கத்திகள் மற்றும் கருவிகளை பிளீச்சிங் பவுடர் கரைசலில் நன்கு நனைத்து கிருமி நீக்கம் செய்யவும்.",
                    "வேர் மண்டலத்தில் டிரைக்கோடெர்மா விரிடி (Trichoderma viride) கலந்த மக்கிய தொழுவுரத்தை இட்டு நோய் வளர்ச்சியை கட்டுப்படுத்தவும்."
                ],
                "prevention": [
                    "உங்கள் பகுதிக்கு பரிந்துரைக்கப்பட்ட நோய் எதிர்ப்பு திறன் கொண்ட ரகங்களை நடவு செய்யவும்.",
                    "நோய் கண்டறியப்பட்டால் உடனடியாக வட்டார வேளாண்மை அலுவலர் அல்லது வேளாண் அறிவியல் மையத்திற்கு தகவல் தெரிவிக்கவும்."
                ]
            }
        }
    },
    "hi": {
        "app_title": "केले के पत्ते के रोग की पहचान",
        "app_tagline": "किसानों के लिए सरल, भरोसेमंद एवं सटीक AI आधारित कृषि साधन",
        "nav_home": "मुख्य पृष्ठ",
        "nav_detect": "रोग पहचानें",
        "nav_dashboard": "डैशबोर्ड",
        "nav_about": "परियोजना विवरण",
        "demo_mode_badge": "डेमो मोड (कंप्यूटर विज़न)",
        "demo_mode_desc": "कोई प्रशिक्षित CNN मॉडल नहीं मिला। OpenCV कंप्यूटर विज़न द्वारा प्रदर्शन परिणाम दिखाए जा रहे हैं।",
        "model_trained_badge": "प्रशिक्षित CNN मॉडल सक्रिय",
        "upload_title": "केले के पत्ते की फोटो अपलोड करें",
        "upload_desc": "रोग की जांच के लिए केले के एक पत्ते अथवा पूरे केले के पौधे की स्पष्ट तस्वीर अपलोड करें।",
        "mode_single": "एकल पत्ती फोटो",
        "mode_whole": "पूरा केला पौधा फोटो",
        "drag_drop_text": "यहाँ फोटो खींचकर लाएँ या चुनने के लिए क्लिक करें",
        "supported_formats": "स्वीकृत प्रारूप: JPG, JPEG, PNG (अधिकतम 16 MB)",
        "btn_analyze": "रोग का विश्लेषण करें",
        "btn_analyzing": "विश्लेषण जारी है...",
        "btn_another": "अन्य फोटो जांचें",
        "btn_speak": "आवाज़ में सुनें",
        "btn_stop_speak": "आवाज़ रोकें",
        "btn_view_dashboard": "डैशबोर्ड देखें",
        "features_title": "मुख्य विशेषताएँ",
        "feature_1_title": "एकल पत्ती एवं सम्पूर्ण पौधा विश्लेषण",
        "feature_1_desc": "एक पत्ती या पूरे पौधे की तस्वीर अपलोड करें, पत्तों को स्वतः अलग कर जांचा जाएगा।",
        "feature_2_title": "OpenCV प्री-प्रोसेसिंग",
        "feature_2_desc": "धूप, छाया और शोर को दूर कर विश्लेषण हेतु स्पष्ट छवि तैयार करता है।",
        "feature_3_title": "स्पष्ट AI (Grad-CAM हीटमैप)",
        "feature_3_desc": "पत्ते के प्रभावित हिस्सों को रंगीन हीटमैप द्वारा चिन्हित करता है।",
        "feature_4_title": "किसान सलाह एवं बोलकर सुनाना",
        "feature_4_desc": "व्यावहारिक सुझाव तथा 6 क्षेत्रीय भाषाओं में बोलकर परिणाम सुनाने की सुविधा।",
        "how_it_works_title": "यह कैसे कार्य करता है",
        "step_1": "1. फोटो अपलोड करें",
        "step_1_desc": "प्राकृतिक रोशनी में केले के पत्ते या पौधे की साफ़ फोटो खींचें।",
        "step_2": "2. प्री-प्रोसेसिंग और पत्ता विभाजन",
        "step_2_desc": "OpenCV छाया और चमक को हटाकर विश्लेषण के लिए तैयार करता है।",
        "step_3": "3. AI रोग पहचान",
        "step_3_desc": "कृत्रिम बुद्धिमत्ता रोग के लक्षण पहचानकर हीटमैप बनाती है।",
        "step_4": "4. परिणाम एवं किसान सलाह",
        "step_4_desc": "रोग का नाम, विश्वसनीयता प्रतिशत और उपचार सुझाव प्राप्त करें।",
        "result_heading": "रोग निदान परिणाम",
        "status_healthy": "पौधा स्वस्थ है",
        "status_diseased": "रोग के लक्षण पाए गए",
        "label_disease": "पहचाना गया रोग",
        "label_confidence": "सटीकता प्रतिशत",
        "label_status": "स्वास्थ्य स्थिति",
        "label_explanation": "निदान का स्पष्ट विवरण",
        "label_recommendations": "व्यावहारिक प्रबंधन सुझाव",
        "label_prevention": "रोकथाम एवं खेत की स्वच्छता",
        "safety_disclaimer": "सुरक्षा अस्वीकरण: ये सुझाव केवल कृषि मार्गदर्शन के लिए हैं। किसी भी रासायनिक कीटनाशक का उपयोग करने से पहले स्थानीय कृषि प्रसार अधिकारी या कृषि विज्ञान केंद्र (KVK) से परामर्श अवश्य लें।",
        "tab_original": "मूल फोटो",
        "tab_preprocessed": "प्रोसेस की गई फोटो",
        "tab_xai": "AI हीटमैप (Grad-CAM)",
        "xai_explanation_note": "लाल और पीले गर्म रंग उन प्रभावित क्षेत्रों को दर्शाते हैं जिन पर AI ने रोग का निर्णय लेते समय ध्यान केंद्रित किया।",
        "whole_plant_summary": "सम्पूर्ण पौधे के पत्तों का विश्लेषण",
        "whole_plant_desc": "कंप्यूटर विज़न द्वारा पौधे के अलग-अलग पत्तों को पहचान कर जांचा गया:",
        "dashboard_title": "किसान फसल निगरानी डैशबोर्ड",
        "stat_total": "कुल जांची गई तस्वीरें",
        "stat_healthy": "स्वस्थ पत्तियां",
        "stat_diseased": "रोगग्रस्त पत्तियां",
        "stat_ratio": "स्वास्थ्य अनुपात",
        "chart_distribution": "रोग वितरण सारांश",
        "recent_table_title": "हाल की जांचें",
        "col_thumbnail": "फोटो",
        "col_date": "दिनांक व समय",
        "col_mode": "प्रकार",
        "col_disease": "रोग स्थिति",
        "col_confidence": "सटीकता",
        "col_status": "स्थिति",
        "col_action": "क्रिया",
        "btn_view": "विवरण देखें",
        "btn_clear_history": "इतिहास साफ़ करें",
        "no_records": "अभी कोई जांच दर्ज नहीं है। अपनी पहली तस्वीर अपलोड करें!",
        "footer_text": "केले के पत्ते के रोग की पहचान — किसानों के हित में सरल तकनीक",
        "disease_info": {
            "Healthy": {
                "name": "स्वस्थ केला पत्ता",
                "status": "स्वस्थ",
                "explanation": "पत्ता एकसमान हरे रंग और स्वस्थ नसों से युक्त है। इस पर फफूंद, पीले धब्बे या मृत ऊतक नहीं पाए गए।",
                "recommendations": [
                    "संतुलित खाद (NPK एवं सूक्ष्म पोषक तत्व) देते रहें ताकि पौधे मजबूत रहें।",
                    "खेत में जल निकासी सुनिश्चित करें तथा पौधों के बीच 2 से 2.5 मीटर की दूरी बनाए रखें।",
                    "बरसात और नमी के मौसम में पुराने पत्तों के निचले हिस्से का नियमित निरीक्षण करें।"
                ],
                "prevention": [
                    "पौधों की छंटाई के औजारों को हमेशा विसंक्रमित (साफ) रखें।",
                    "नई रोपाई हेतु प्रमाणित रोगमुक्त टिश्यू कल्चर के पौधे ही लगाएं।"
                ]
            },
            "Black Sigatoka": {
                "name": "ब्लैक सिगाटोका रोग (Black Sigatoka)",
                "status": "रोगग्रस्त",
                "explanation": "पत्ते की नसों के समानांतर गहरे भूरे या काले रंग की संकीर्ण धारियां दिखती हैं जो बाद में सूखकर मृत धब्बे बना लेती हैं।",
                "recommendations": [
                    "अधिक संक्रमित पत्तों को काटकर खेत से दूर गड्ढे में दबाएं या नष्ट करें ताकि बीजाणु न फैलें।",
                    "खेत में वायु प्रवाह बढ़ाएं और जलभराव रोकें ताकि पत्तों पर नमी अधिक समय न टिके।",
                    "नीम तेल का घोल या स्वीकृत स्यूडोमोनास बायो-कंट्रोल का छिड़काव नए पत्तों पर करें।",
                    "ऊपर से फव्वारा सिंचाई न करें, केवल ड्रिप (टपक) सिंचाई का उपयोग करें।"
                ],
                "prevention": [
                    "पौधों में पर्याप्त दूरी रखें ताकि ओस सुबह जल्दी सूख सके।",
                    "पोटेशियम की उचित मात्रा दें जिससे पत्तों की बाहरी परत रोग प्रतिरोधक बन सके।"
                ]
            },
            "Yellow Sigatoka": {
                "name": "येलो सिगाटोका रोग (Yellow Sigatoka)",
                "status": "रोगग्रस्त",
                "explanation": "हल्के पीले धब्बे अंडाकार घावों में बदलते हैं जिनके केंद्र धूसर और किनारे स्पष्ट पीले छल्लेदार होते हैं।",
                "recommendations": [
                    "पुराने धब्बेदार पत्तों को समय पर काटकर अलग करें ताकि नए पत्तों में संक्रमण न फैले।",
                    "खेत में पानी न भरने दें; अत्यधिक नमी फफूंद को तेज़ी से बढ़ाती है।",
                    "कृषि विश्वविद्यालय की सलाह अनुसार कॉपर हाइड्रोक्साइड या जैविक फफूंदनाशक का छिड़काव करें।",
                    "अत्यधिक यूरिया (नाइट्रोजन) से बचें, पोटाश खाद का संतुलित प्रयोग करें।"
                ],
                "prevention": [
                    "खेत को खरपतवार मुक्त रखें ताकि पौधों के नीचे नमी का स्तर कम रहे।",
                    "मानसून के दौरान पाक्षिक निरीक्षण कर शुरूआती अवस्था में ही नियंत्रण करें।"
                ]
            },
            "Panama Disease": {
                "name": "पनामा रोग (फ्यूजेरियम विल्ट)",
                "status": "रोगग्रस्त",
                "explanation": "निचले पुराने पत्तों के किनारों से पीलापन शुरू होकर मध्य शिरा की ओर बढ़ता है, डंठल मुड़ जाते हैं और पत्ते सूखकर लटक जाते हैं।",
                "recommendations": [
                    "संक्रमित पौधे को तुरंत अलग करें। जड़ों के रास्ते फैलाव रोकने के लिए चारों ओर गहरी नाली खोदें।",
                    "संक्रमित स्थान की मिट्टी, औजार या पौधे के हिस्से स्वस्थ खेत में कभी न ले जाएं।",
                    "कुदाल व हंसिया जैसे औजारों को ब्लीच या कीटाणुनाशक घोल से अवश्य धोएं।",
                    "जड़ों के आसपास ट्राइकोडर्मा विरिडी या ट्राइकोडर्मा हार्ज़िएनम से उपचारित गोबर की खाद डालें।"
                ],
                "prevention": [
                    "क्षेत्र के लिए अनुशंसित रोग-प्रतिरोधी किस्मों की ही रोपाई करें।",
                    "पनामा रोग का संदेह होने पर तुरंत स्थानीय कृषि अधिकारी या KVK को सूचित करें।"
                ]
            }
        }
    },
    "te": {
        "app_title": "అరటి ఆకు తెగుళ్ల గుర్తింపు వ్యవస్థ",
        "app_tagline": "రైతుల కోసం సులభమైన మరియు ఖచ్చితమైన ఆర్టిఫిషియల్ ఇంటెలిజెన్స్ (AI)",
        "nav_home": "హోమ్",
        "nav_detect": "తెగులు గుర్తింపు",
        "nav_dashboard": "రైతు డాష్‌బోర్డ్",
        "nav_about": "ప్రాజెక్ట్ వివరాలు",
        "demo_mode_badge": "డెమో మోడ్ (కంప్యూటర్ విజన్)",
        "demo_mode_desc": "శిక్షణ పొందిన మోడల్ అందుబాటులో లేదు. ప్రదర్శన ఫలితాలు చూపించబడుతున్నాయి.",
        "model_trained_badge": "AI మోడల్ సిద్ధంగా ఉంది",
        "upload_title": "అరటి ఆకు ఫోటో అప్‌లోడ్ చేయండి",
        "upload_desc": "తెగులును గుర్తించడానికి అరటి ఆకు లేదా మొత్తం అరటి చెట్టు ఫోటోను అప్‌లోడ్ చేయండి.",
        "mode_single": "ఒకే ఆకు ఫోటో",
        "mode_whole": "మొత్తం అరటి చెట్టు ఫోటో",
        "drag_drop_text": "ఫోటోను ఇక్కడ లాగండి లేదా ఎంచుకోవడానికి క్లిక్ చేయండి",
        "supported_formats": "సహాయక ఫార్మాట్లు: JPG, JPEG, PNG (గరిష్టంగా 16 MB)",
        "btn_analyze": "తెగులును విశ్లేషించండి",
        "btn_analyzing": "విశ్లేషిస్తోంది...",
        "btn_another": "మరో ఫోటోను పరీక్షించండి",
        "btn_speak": "వాయిస్‌లో వినండి",
        "btn_stop_speak": "వాయిస్ ఆపండి",
        "btn_view_dashboard": "డాష్‌బోర్డ్ చూడండి",
        "features_title": "ప్రధాన లక్షణాలు",
        "feature_1_title": "ఒకే ఆకు & మొత్తం చెట్టు విశ్లేషణ",
        "feature_1_desc": "ఒకే ఆకు లేదా చెట్టులోని ప్రతి ఆకును వేరువేరుగా స్వయంచాలకంగా విశ్లేషించవచ్చు.",
        "feature_2_title": "OpenCV ప్రాసెసింగ్",
        "feature_2_desc": "నీడలు, అధిక సూర్యరశ్మిని తగ్గించి స్పష్టమైన చిత్రాన్ని రూపొందిస్తుంది.",
        "feature_3_title": "వివరణాత్మక AI (Grad-CAM)",
        "feature_3_desc": "తెగులు సోకిన భాగాలను రంగుల హీట్‌మ్యాప్ ద్వారా స్పష్టంగా చూపిస్తుంది.",
        "feature_4_title": "రైతు సలహాలు & వాయిస్ అసిస్టెంట్",
        "feature_4_desc": "తెలుగులో స్పష్టమైన చిట్కాలు మరియు వాయిస్ ద్వారా ఫలితాలను వినే సదుపాయం.",
        "how_it_works_title": "ఇది ఎలా పనిచేస్తుంది",
        "step_1": "1. ఫోటోను అప్‌లోడ్ చేయండి",
        "step_1_desc": "స్పష్టమైన కాంతిలో ఆకు లేదా చెట్టు ఫోటో తీయండి.",
        "step_2": "2. చిత్ర ప్రాసెసింగ్",
        "step_2_desc": "నీడలను తొలగించి విశ్లేషణకు సిద్ధం చేస్తుంది.",
        "step_3": "3. AI విశ్లేషణ",
        "step_3_desc": "తెగులును గుర్తించి హీట్‌మ్యాప్‌ను సృష్టిస్తుంది.",
        "step_4": "4. ఫలితాలు & సలహాలు",
        "step_4_desc": "తెగులు పేరు, నివారణ పద్ధతులు మరియు వాయిస్ గైడెన్స్ పొందండి.",
        "result_heading": "తెగులు నిర్ధారణ ఫలితాలు",
        "status_healthy": "ఆరోగ్యకరమైన పంట",
        "status_diseased": "తెగులు గుర్తించబడింది",
        "label_disease": "గుర్తించిన తెగులు",
        "label_confidence": "ఖచ్చితత్వ శాతం",
        "label_status": "ఆరోగ్య స్థితి",
        "label_explanation": "వివరణ",
        "label_recommendations": "యాజమాన్య పద్ధతులు",
        "label_prevention": "నివారణ మరియు పరిశుభ్రత",
        "safety_disclaimer": "గమనిక: ఈ సూచనలు వ్యవసాయ మార్గదర్శకత్వం కోసం మాత్రమే. రసాయనాలను ఉపయోగించే ముందు వ్యవసాయ అధికారిని లేదా కృషి విజ్ఞాన కేంద్రాన్ని (KVK) సంప్రదించండి.",
        "tab_original": "అసలు ఫోటో",
        "tab_preprocessed": "ప్రాసెస్ చేసిన ఫోటో",
        "tab_xai": "AI హీట్‌మ్యాప్ (Grad-CAM)",
        "xai_explanation_note": "ఎరుపు మరియు పసుపు రంగు ప్రాంతాలు తెగులు తీవ్రత ఉన్న భాగాలను సూచిస్తాయి.",
        "whole_plant_summary": "మొత్తం చెట్టు ఆకుల విశ్లేషణ",
        "whole_plant_desc": "చెట్టులోని ప్రతి ఆకును ప్రత్యేకంగా గుర్తించి విశ్లేషించబడింది:",
        "dashboard_title": "రైతు పంట పర్యవేక్షణ డాష్‌బోర్డ్",
        "stat_total": "మొత్తం స్కాన్లు",
        "stat_healthy": "ఆరోగ్యకరమైన ఆకులు",
        "stat_diseased": "తెగులు సోకిన ఆకులు",
        "stat_ratio": "ఆరోగ్య నిష్పత్తి",
        "chart_distribution": "తెగుళ్ల విస్తరణ సారాంశం",
        "recent_table_title": "ఇటీవలి పరీక్షలు",
        "col_thumbnail": "ఫోటో",
        "col_date": "తేదీ & సమయం",
        "col_mode": "రకం",
        "col_disease": "నిర్ధారణ",
        "col_confidence": "ఖచ్చితత్వం",
        "col_status": "స్థితి",
        "col_action": "చర్య",
        "btn_view": "వివరాలు",
        "btn_clear_history": "చరిత్రను తుడవండి",
        "no_records": "ఇంకా ఎలాంటి రికార్డులు లేవు. మొదటి ఫోటోను అప్‌లోడ్ చేయండి!",
        "footer_text": "అరటి ఆకు తెగుళ్ల గుర్తింపు వ్యవస్థ — రైతులకు సాంకేతిక సాయం",
        "disease_info": {
            "Healthy": {
                "name": "ఆరోగ్యకరమైన అరటి ఆకు",
                "status": "ఆరోగ్యకరమైనది",
                "explanation": "ఆకు ఏకరీతి ఆకుపచ్చ రంగుతో ఆరోగ్యంగా ఉంది. ఎలాంటి ఫంగస్ మచ్చలు లేదా తెగులు లక్షణాలు లేవు.",
                "recommendations": [
                    "పంట బలంగా ఉండటానికి సమతుల్య ఎరువులను (NPK) కొనసాగించండి.",
                    "తోటలో నీరు నిలవకుండా చూసుకోండి మరియు తగినంత ఎండ సోకేలా 2 నుండి 2.5 మీటర్ల దూరం పాటించండి.",
                    "వర్షాకాలంలో ఆకుల అడుగు భాగాన్ని క్రమం తప్పకుండా పరిశీలించండి."
                ],
                "prevention": [
                    "ఆకులను కత్తిరించే పనిముట్లను ఎప్పటికప్పుడు శుభ్రపరచండి.",
                    "కొత్త తోటల కోసం ధృవీకరించబడిన టిష్యూ కల్చర్ మొక్కలను మాత్రమే వాడండి."
                ]
            },
            "Black Sigatoka": {
                "name": "బ్లాక్ సిగటోకా తెగులు (Black Sigatoka)",
                "status": "తెగులు సోకింది",
                "explanation": "ఆకు ఈనెలకు సమాంతరంగా ముదురు గోధుమ లేదా నలుపు రంగు చారలు ఏర్పడి ఆకులు ఎండిపోతాయి.",
                "recommendations": [
                    "తీవ్రంగా దెబ్బతిన్న ఆకులను కోసి తోట బయట గుంత తీసి పూడ్చివేయండి.",
                    "తోటలో గాలి ప్రసరణ పెంచండి మరియు తేమ త్వరగా ఆరిపోయేలా చూడండి.",
                    "వేప నూనె లేదా ఆమోదించబడిన సూడోమోనాస్ ద్రావణాన్ని పిచికారీ చేయండి.",
                    "స్ప్రింక్లర్లకు బదులుగా డ్రిప్ ఇరిగేషన్ వాడండి."
                ],
                "prevention": [
                    "మొక్కల మధ్య సరైన దూరం పాటించండి.",
                    "పొటాష్ ఎరువులను తగినంతగా అందించి ఆకుల రోగనిరోధక శక్తిని పెంచండి."
                ]
            },
            "Yellow Sigatoka": {
                "name": "ఎల్లో సిగటోకా తెగులు (Yellow Sigatoka)",
                "status": "తెగులు సోకింది",
                "explanation": "ఆకులపై పసుపు రంగు మచ్చలు ఏర్పడి వాటి మధ్య భాగం బూడిద రంగులోకి మారి ఎండిపోతాయి.",
                "recommendations": [
                    "తెగులు సోకిన ఆకులను కత్తిరించి నాశనం చేయండి.",
                    "తోటలో నీటి నిల్వ లేకుండా చేసి తేమను తగ్గించండి.",
                    "వ్యవసాయ నిపుణుల సలహా మేరకు కాపర్ హైడ్రాక్సైడ్ లేదా జీవ శిలీంధ్ర నాశిని పిచికారీ చేయండి.",
                    "నత్రజని అధికంగా వాడకండి, పొటాష్ ఎరువులకు ప్రాధాన్యత ఇవ్వండి."
                ],
                "prevention": [
                    "తోటలో కలుపు లేకుండా శుభ్రంగా ఉంచండి.",
                    "వర్షాకాలంలో క్రమం తప్పకుండా పంటను పరిశీలించండి."
                ]
            },
            "Panama Disease": {
                "name": "పనామా తెగులు (Panama Wilt - Fusarium)",
                "status": "తెగులు సోకింది",
                "explanation": "క్రింది ముదురు ఆకుల అంచుల నుండి పసుపు రంగు మొదలై కాడలు విరిగి ఆకులు కిందకు వేలాడతాయి.",
                "recommendations": [
                    "తెగులు సోకిన చెట్లను వెంటనే వేరు చేయండి. ఇతర చెట్లకు పాకకుండా చుట్టూ లోతైన కందకం తీయండి.",
                    "ఆ ప్రాంతపు మట్టిని లేదా పనిముట్లను మంచి పొలాల్లోకి తీసుకెళ్లకండి.",
                    "కత్తులు, గడ్డపారలను బ్లీచింగ్ ద్రావణంతో శుద్ధి చేయండి.",
                    "ట్రైకోడెర్మా విరిడే కలిపిన పశువుల ఎరువును మొదళ్ల వద్ద వేయండి."
                ],
                "prevention": [
                    "తెగులును తట్టుకునే రకాలను మాత్రమే సాగు చేయండి.",
                    "ఈ తెగులు కనిపిస్తే వెంటనే స్థానిక వ్యవసాయ అధికారికి తెలియజేయండి."
                ]
            }
        }
    },
    "ml": {
        "app_title": "വാഴയില രോഗനിർണ്ണയ സഹായി",
        "app_tagline": "കർഷകർക്കായി ലളിതവും കാര്യക്ഷമവുമായ കൃത്രിമബുദ്ധി (AI) സാങ്കേതികവിദ്യ",
        "nav_home": "ഹോം",
        "nav_detect": "രോഗം കണ്ടെത്തുക",
        "nav_dashboard": "ഡാഷ്‌ബോർഡ്",
        "nav_about": "പദ്ധതിയെക്കുറിച്ച്",
        "demo_mode_badge": "ഡെമോ മോഡ് (കമ്പ്യൂട്ടർ വിഷൻ)",
        "demo_mode_desc": "പരിശീലനം ലഭിച്ച മോഡൽ ലഭ്യമല്ല. ഡെമോ ഫലങ്ങൾ കാണിക്കുന്നു.",
        "model_trained_badge": "AI മോഡൽ സജീവം",
        "upload_title": "വാഴയില ചിത്രം അപ്‌ലോഡ് ചെയ്യുക",
        "upload_desc": "രോഗം കണ്ടെത്തുന്നതിനായി വാഴയിലയുടെയോ മുഴുവൻ വാഴയുടെയോ വ്യക്തമായ ചിത്രം നൽകുക.",
        "mode_single": "ഒറ്റ ഇല ചിത്രം",
        "mode_whole": "മുഴുവൻ വാഴ ചിത്രം",
        "drag_drop_text": "ചിത്രം ഇവിടെ ഡ്രോപ്പ് ചെയ്യുക അല്ലെങ്കിൽ തിരഞ്ഞെടുക്കുക",
        "supported_formats": "JPG, JPEG, PNG (പരമാവധി 16 MB)",
        "btn_analyze": "രോഗം പരിശോധിക്കുക",
        "btn_analyzing": "പരിശോധിക്കുന്നു...",
        "btn_another": "മറ്റൊരു ചിത്രം പരിശോധിക്കുക",
        "btn_speak": "ശബ്ദത്തിൽ കേൾക്കുക",
        "btn_stop_speak": "ശബ്ദം നിർത്തുക",
        "btn_view_dashboard": "ഡാഷ്‌ബോർഡ് കാണുക",
        "features_title": "പ്രധാന സവിശേഷതകൾ",
        "feature_1_title": "ഇല & വാഴ പരിശോധന",
        "feature_1_desc": "ഒറ്റ ഇലയോ മുഴുവൻ വാഴയിലയോ സ്വയം തിരിച്ച് പരിശോധിക്കുന്നു.",
        "feature_2_title": "OpenCV പ്രീ-പ്രോസസ്സിംഗ്",
        "feature_2_desc": "നിഴലും വെളിച്ചവ്യത്യാസങ്ങളും ഒഴിവാക്കി ചിത്രം വ്യക്തമാക്കുന്നു.",
        "feature_3_title": "വിശദീകരണ AI (Grad-CAM)",
        "feature_3_desc": "രോഗബാധിത പ്രദേശങ്ങൾ കളർ ഹീറ്റ്മാപ്പ് വഴി കാണിക്കുന്നു.",
        "feature_4_title": "കർഷക നിർദ്ദേശങ്ങളും ശബ്ദസഹായവും",
        "feature_4_desc": "മലയാളത്തിലുള്ള പ്രതിവിധികൾ കേൾക്കാനുള്ള ശബ്ദസഹായം.",
        "how_it_works_title": "പ്രവർത്തന രീതി",
        "step_1": "1. ഫോട്ടോ എടുക്കുക",
        "step_1_desc": "നല്ല വെളിച്ചത്തിൽ വാഴയിലയുടെ ചിത്രം എടുക്കുക.",
        "step_2": "2. പ്രോസസ്സിംഗ്",
        "step_2_desc": "നിഴലുകൾ മാറ്റി ഇലകളെ തിരിച്ചറിയുന്നു.",
        "step_3": "3. AI വിശകലനം",
        "step_3_desc": "രോഗലക്ഷണങ്ങൾ കണ്ടെത്തി അടയാളപ്പെടുത്തുന്നു.",
        "step_4": "4. ഫലങ്ങളും പ്രതിവിധിയും",
        "step_4_desc": "രോഗവിവരങ്ങളും നിർദ്ദേശങ്ങളും ശബ്ദത്തിലൂടെ അറിയുക.",
        "result_heading": "രോഗനിർണ്ണയ ഫലം",
        "status_healthy": "ആരോഗ്യമുള്ള വാഴ",
        "status_diseased": "രോഗലക്ഷണം കണ്ടെത്തി",
        "label_disease": "കണ്ടെത്തിയ രോഗം",
        "label_confidence": "കൃത്യത ശതമാനം",
        "label_status": "ആരോഗ്യനില",
        "label_explanation": "രോഗവിവരണം",
        "label_recommendations": "പരിപാലന നിർദ്ദേശങ്ങൾ",
        "label_prevention": "പ്രതിരോധ മാർഗ്ഗങ്ങൾ",
        "safety_disclaimer": "ശ്രദ്ധിക്കുക: ഈ നിർദ്ദേശങ്ങൾ കാർഷിക മാർഗ്ഗനിർദ്ദേശത്തിന് മാത്രമുള്ളതാണ്. കീടനാശിനികൾ ഉപയോഗിക്കുന്നതിന് മുമ്പ് കൃഷി ഓഫീസറുമായി ബന്ധപ്പെടുക.",
        "tab_original": "യഥാർത്ഥ ചിത്രം",
        "tab_preprocessed": "പ്രോസസ്സ് ചെയ്ത ചിത്രം",
        "tab_xai": "AI ഹീറ്റ്മാപ്പ് (Grad-CAM)",
        "xai_explanation_note": "ചുവപ്പ്, മഞ്ഞ നിറങ്ങൾ രോഗം ബാധിച്ച ഭാഗങ്ങളെ വ്യക്തമാക്കുന്നു.",
        "whole_plant_summary": "മുഴുവൻ ഇലകളുടെയും പരിശോധന",
        "whole_plant_desc": "ചിത്രത്തിലെ ഓരോ ഇലയും പ്രത്യേകം വേർതിരിച്ചു പരിശോധിച്ചു:",
        "dashboard_title": "കർഷക ഡാഷ്‌ബോർഡ്",
        "stat_total": "ആകെ പരിശോധനകൾ",
        "stat_healthy": "ആരോഗ്യമുള്ളവ",
        "stat_diseased": "രോഗം ബാധിച്ചവ",
        "stat_ratio": "ആരോഗ്യ അനുപാതം",
        "chart_distribution": "രോഗങ്ങളുടെ കണക്ക്",
        "recent_table_title": "സമീപകാല പരിശോധനകൾ",
        "col_thumbnail": "ചിത്രം",
        "col_date": "തീയതി",
        "col_mode": "തരം",
        "col_disease": "രോഗം",
        "col_confidence": "കൃത്യത",
        "col_status": "നില",
        "col_action": "വിവരം",
        "btn_view": "കാണുക",
        "btn_clear_history": "ചരിത്രം ഒഴിവാക്കുക",
        "no_records": "പരിശോധനകളൊന്നും ലഭ്യമല്ല. ആദ്യ ചിത്രം അപ്‌ലോഡ് ചെയ്യുക!",
        "footer_text": "വാഴയില രോഗനിർണ്ണയ സഹായി — കർഷകർക്കായി ആധുനിക സാങ്കേതികവിദ്യ",
        "disease_info": {
            "Healthy": {
                "name": "ആരോഗ്യമുള്ള വാഴയില",
                "status": "ആരോഗ്യമുള്ളത്",
                "explanation": "ഇലയിൽ രോഗലക്ഷണങ്ങളോ കുത്തുകളോ ഇല്ല. നല്ല പച്ചനിറവും ആരോഗ്യവുമുണ്ട്.",
                "recommendations": [
                    "സന്തുലിതമായ വളപ്രയോഗം (NPK) തുടരുക.",
                    "തോട്ടത്തിൽ വെള്ളം കെട്ടിക്കിടക്കാതെ നോക്കുക, വായുസഞ്ചാരം ഉറപ്പാക്കുക.",
                    "മഴക്കാലത്ത് ഇലകൾ കൃത്യമായി നിരീക്ഷിക്കുക."
                ],
                "prevention": [
                    "ഉപകരണങ്ങൾ എപ്പോഴും അണുവിമുക്തമാക്കി സൂക്ഷിക്കുക.",
                    "രോഗമില്ലാത്ത ടിഷ്യുകൾച്ചർ തൈകൾ മാത്രം നടുക."
                ]
            },
            "Black Sigatoka": {
                "name": "ബ്ലാക്ക് സിഗട്ടോക രോഗം (Black Sigatoka)",
                "status": "രോഗബാധിതം",
                "explanation": "ഇലകളിൽ കറുപ്പോ തവിട്ടോ നിറത്തിലുള്ള വരകൾ കാണപ്പെടുകയും ഇലകൾ കരിഞ്ഞുപോവുകയും ചെയ്യുന്നു.",
                "recommendations": [
                    "രോഗം ബാധിച്ച ഇലകൾ വെട്ടിമാറ്റി കുഴിച്ചുമൂടുകയോ കത്തിക്കുകയോ ചെയ്യുക.",
                    "തോട്ടത്തിൽ വായുസഞ്ചാരവും ഡ്രെയിനേജും ഉറപ്പുവരുത്തുക.",
                    "വേപ്പെണ്ണ മിശ്രിതമോ സ്യൂഡോമോണസോ തളിക്കുക.",
                    "ഡ്രിപ്പ് ഇറിഗേഷൻ രീതി പിന്തുടരുക."
                ],
                "prevention": [
                    "വാഴകൾ തമ്മിൽ കൃത്യമായ അകലം പാലിക്കുക.",
                    "പൊട്ടാഷ് വളങ്ങൾ നൽകി പ്രതിരോധശേഷി വർദ്ധിപ്പിക്കുക."
                ]
            },
            "Yellow Sigatoka": {
                "name": "മഞ്ഞ സിഗട്ടോക രോഗം (Yellow Sigatoka)",
                "status": "രോഗബാധിതം",
                "explanation": "ഇലകളിൽ മഞ്ഞപ്പുള്ളികൾ വരികയും അവയുടെ നടുഭാഗം ചാരനിറമായി മാറുകയും ചെയ്യുന്നു.",
                "recommendations": [
                    "പഴയ ബാധിത ഇലകൾ മുറിച്ചുമാറ്റുക.",
                    "വെള്ളക്കെട്ട് ഒഴിവാക്കുക.",
                    "കൃഷി വിദഗ്ദ്ധന്റെ നിർദ്ദേശപ്രകാരം കോപ്പർ മിശ്രിതം തളിക്കുക.",
                    "അമിത യൂറിയ ഒഴിവാക്കി പൊട്ടാഷ് നൽകുക."
                ],
                "prevention": [
                    "തോട്ടം കളകളില്ലാതെ വൃത്തിയായി സൂക്ഷിക്കുക.",
                    "മഴക്കാലത്ത് കൃത്യമായ ഇടവേളകളിൽ പരിശോധിക്കുക."
                ]
            },
            "Panama Disease": {
                "name": "പനാമ വാട്ടം രോഗം (Panama Wilt)",
                "status": "രോഗബാധിതം",
                "explanation": "താഴത്തെ ഇലകളുടെ അരികുകൾ മഞ്ഞനിറമായി തണ്ടുകൾ ഒടിഞ്ഞുതൂങ്ങുന്നു.",
                "recommendations": [
                    "രോഗം ബാധിച്ച വാഴ മാറ്റിനിർത്തുക, ചുറ്റും കിടങ്ങുണ്ടാക്കുക.",
                    "ഇവിടുത്തെ മണ്ണോ ഉപകരണങ്ങളോ മറ്റ് സ്ഥലങ്ങളിലേക്ക് മാറ്റരുത്.",
                    "കത്തികളും മറ്റ് ഉപകരണങ്ങളും ബ്ലീച്ചിംഗ് ലായനിയിൽ കഴുകുക.",
                    "ട്രൈക്കോഡെർമ ചേർത്ത ചാണകപ്പൊടി ചുവട്ടിൽ ചേർക്കുക."
                ],
                "prevention": [
                    "രോഗപ്രതിരോധ ശേഷിയുള്ള ഇനങ്ങൾ നടുക.",
                    "രോഗം കണ്ടാലുടൻ അടുത്തുള്ള കൃഷിഭവനുമായി ബന്ധപ്പെടുക."
                ]
            }
        }
    },
    "kn": {
        "app_title": "ಬಾಳೆ ಎಲೆ ರೋಗ ಪತ್ತೆ ಮತ್ತು ಮಾರ್ಗದರ್ಶಿ",
        "app_tagline": "ರೈತರಿಗಾಗಿ ಸರಳ ಮತ್ತು ನಿಖರವಾದ ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ (AI) ತಂತ್ರಜ್ಞಾನ",
        "nav_home": "ಮುಖಪುಟ",
        "nav_detect": "ರೋಗ ಪತ್ತೆ",
        "nav_dashboard": "ರೈತ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
        "nav_about": "ಯೋಜನೆಯ ಬಗ್ಗೆ",
        "demo_mode_badge": "ಡೆಮೊ ಮೋಡ್ (ಕಂಪ್ಯೂಟರ್ ವಿಷನ್)",
        "demo_mode_desc": "ತರಬೇತಿ ಪಡೆದ ಮಾದರಿ ಲಭ್ಯವಿಲ್ಲ. ಡೆಮೊ ಫಲಿತಾಂಶಗಳನ್ನು ತೋರಿಸಲಾಗುತ್ತಿದೆ.",
        "model_trained_badge": "AI ಮಾದರಿ ಸಕ್ರಿಯವಾಗಿದೆ",
        "upload_title": "ಬಾಳೆ ಎಲೆಯ ಚಿತ್ರ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ",
        "upload_desc": "ರೋಗ ಪರೀಕ್ಷೆಗಾಗಿ ಬಾಳೆ ಎಲೆ ಅಥವಾ ಸಂಪೂರ್ಣ ಗಿಡದ ಸ್ಪಷ್ಟ ಚಿತ್ರವನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.",
        "mode_single": "ಒಂದೇ ಎಲೆಯ ಚಿತ್ರ",
        "mode_whole": "ಸಂಪೂರ್ಣ ಬಾಳೆ ಗಿಡದ ಚಿತ್ರ",
        "drag_drop_text": "ಚಿತ್ರವನ್ನು ಇಲ್ಲಿ ಎಳೆಯಿರಿ ಅಥವಾ ಆಯ್ಕೆ ಮಾಡಲು ಕ್ಲಿಕ್ ಮಾಡಿ",
        "supported_formats": "ಬೆಂಬಲಿತ ಮಾದರಿಗಳು: JPG, JPEG, PNG (ಗರಿಷ್ಠ 16 MB)",
        "btn_analyze": "ರೋಗ ವಿಶ್ಲೇಷಿಸಿ",
        "btn_analyzing": "ವಿಶ್ಲೇಷಿಸಲಾಗುತ್ತಿದೆ...",
        "btn_another": "ಮತ್ತೊಂದು ಚಿತ್ರ ಪರೀಕ್ಷಿಸಿ",
        "btn_speak": "ಧ್ವನಿಯಲ್ಲಿ ಕೇಳಿ",
        "btn_stop_speak": "ಧ್ವನಿ ನಿಲ್ಲಿಸಿ",
        "btn_view_dashboard": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್ ವೀಕ್ಷಿಸಿ",
        "features_title": "ಪ್ರಮುಖ ವೈಶಿಷ್ಟ್ಯಗಳು",
        "feature_1_title": "ಎಲೆ ಮತ್ತು ಗಿಡದ ವಿಶ್ಲೇಷಣೆ",
        "feature_1_desc": "ಒಂದೇ ಎಲೆ ಅಥವಾ ಗಿಡದ ಪ್ರತಿಯೊಂದು ಎಲೆಯನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ವಿಶ್ಲೇಷಿಸುತ್ತದೆ.",
        "feature_2_title": "OpenCV ಪ್ರಿ-ಪ್ರೊಸೆಸಿಂಗ್",
        "feature_2_desc": "ನೆರಳು ಮತ್ತು ಅತಿಯಾದ ಬೆಳಕನ್ನು ನಿವಾರಿಸಿ ಸ್ಪಷ್ಟ ಚಿತ್ರವನ್ನು ನೀಡುತ್ತದೆ.",
        "feature_3_title": "ವಿವರಣಾತ್ಮಕ AI (Grad-CAM)",
        "feature_3_desc": "ರೋಗಪೀಡಿತ ಭಾಗಗಳನ್ನು ಬಣ್ಣದ ಹೀಟ್‌ಮ್ಯಾಪ್ ಮೂಲಕ ತೋರಿಸುತ್ತದೆ.",
        "feature_4_title": "ರೈತ ಸಲಹೆಗಳು ಮತ್ತು ಧ್ವನಿ ಸಹಾಯಕ",
        "feature_4_desc": "ಕನ್ನಡದಲ್ಲಿ ಪರಿಹಾರ ಕ್ರಮಗಳು ಮತ್ತು ಧ್ವನಿ ಮೂಲಕ ಕೇಳುವ ಸೌಲಭ್ಯ.",
        "how_it_works_title": "ಇದು ಹೇಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ",
        "step_1": "1. ಫೋಟೋ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ",
        "step_1_desc": "ನೈಸರ್ಗಿಕ ಬೆಳಕಿನಲ್ಲಿ ಸ್ಪಷ್ಟ ಫೋಟೋ ತೆಗೆದುಕೊಳ್ಳಿ.",
        "step_2": "2. ಚಿತ್ರ ಪ್ರೊಸೆಸಿಂಗ್",
        "step_2_desc": "ನೆರಳುಗಳನ್ನು ಸರಿಪಡಿಸಿ ವಿಶ್ಲೇಷಣೆಗೆ ಸಿದ್ಧಪಡಿಸುತ್ತದೆ.",
        "step_3": "3. AI ರೋಗ ಪತ್ತೆ",
        "step_3_desc": "ರೋಗದ ಲಕ್ಷಣಗಳನ್ನು ಗುರುತಿಸಿ ಹೀಟ್‌ಮ್ಯಾಪ್ ತಯಾರಿಸುತ್ತದೆ.",
        "step_4": "4. ಫಲಿತಾಂಶ ಮತ್ತು ಸಲಹೆಗಳು",
        "step_4_desc": "ರೋಗದ ಹೆಸರು, ನಿಖರತೆ ಮತ್ತು ಸರಳ ಸಲಹೆಗಳನ್ನು ಧ್ವನಿಯಲ್ಲಿ ಪಡೆಯಿರಿ.",
        "result_heading": "ರೋಗ ಪತ್ತೆ ಫಲಿತಾಂಶ",
        "status_healthy": "ಆರೋಗ್ಯಕರ ಬೆಳೆ",
        "status_diseased": "ರೋಗದ ಲಕ್ಷಣಗಳು ಕಂಡುಬಂದಿವೆ",
        "label_disease": "ಗುರುತಿಸಲಾದ ರೋಗ",
        "label_confidence": "ನಿಖರತೆಯ ಶೇಕಡಾವಾರು",
        "label_status": "ಆರೋಗ್ಯ ಸ್ಥಿತಿ",
        "label_explanation": "ವಿವರಣೆ",
        "label_recommendations": "ನಿರ್ವಹಣಾ ಸಲಹೆಗಳು",
        "label_prevention": "ಮುನ್ನೆಚ್ಚರಿಕೆ ಕ್ರಮಗಳು",
        "safety_disclaimer": "ಸುರಕ್ಷತಾ ಎಚ್ಚರಿಕೆ: ಈ ಸಲಹೆಗಳು ಕೃಷಿ ಮಾರ್ಗದರ್ಶನಕ್ಕಾಗಿ ಮಾತ್ರ. ರಾಸಾಯನಿಕಗಳನ್ನು ಬಳಸುವ ಮುನ್ನ ಕೃಷಿ ಅಧಿಕಾರಿಗಳನ್ನು ಸಂಪರ್ಕಿಸಿ.",
        "tab_original": "ಮೂಲ ಚಿತ್ರ",
        "tab_preprocessed": "ಪ್ರೊಸೆಸ್ ಮಾಡಿದ ಚಿತ್ರ",
        "tab_xai": "AI ಹೀಟ್‌ಮ್ಯಾಪ್ (Grad-CAM)",
        "xai_explanation_note": "ಕೆಂಪು ಮತ್ತು ಹಳದಿ ಬಣ್ಣದ ಭಾಗಗಳು ರೋಗದ ತೀವ್ರತೆಯಿರುವ ಪ್ರದೇಶಗಳನ್ನು ಸೂಚಿಸುತ್ತವೆ.",
        "whole_plant_summary": "ಸಂಪೂರ್ಣ ಗಿಡದ ಎಲೆಗಳ ವಿಶ್ಲೇಷಣೆ",
        "whole_plant_desc": "ಚಿತ್ರದಲ್ಲಿನ ಪ್ರತಿಯೊಂದು ಎಲೆಯನ್ನು ಪ್ರತ್ಯೇಕವಾಗಿ ಗುರುತಿಸಿ ಪರೀಕ್ಷಿಸಲಾಗಿದೆ:",
        "dashboard_title": "ರೈತ ಕೃಷಿ ಮೇಲ್ವಿಚಾರಣಾ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
        "stat_total": "ಒಟ್ಟು ಸ್ಕ್ಯಾನ್‌ಗಳು",
        "stat_healthy": "ಆರೋಗ್ಯಕರ ಎಲೆಗಳು",
        "stat_diseased": "ರೋಗಪೀಡಿತ ಎಲೆಗಳು",
        "stat_ratio": "ಆರೋಗ್ಯ ಅನುಪಾತ",
        "chart_distribution": "ರೋಗಗಳ ಹಂಚಿಕೆ",
        "recent_table_title": "ಇತ್ತೀಚಿನ ಪರೀಕ್ಷೆಗಳು",
        "col_thumbnail": "ಚಿತ್ರ",
        "col_date": "ದಿನಾಂಕ ಮತ್ತು ಸಮಯ",
        "col_mode": "ಮಾದರಿ",
        "col_disease": "ರೋಗ",
        "col_confidence": "ನಿಖರತೆ",
        "col_status": "ಸ್ಥಿತಿ",
        "col_action": "ಕ್ರಮ",
        "btn_view": "ವಿವರ ನೋಡಿ",
        "btn_clear_history": "ಇತಿಹಾಸ ಅಳಿಸಿ",
        "no_records": "ಇನ್ನೂ ಯಾವುದೇ ಪರೀಕ್ಷೆಗಳು ದಾಖಲಾಗಿಲ್ಲ. ನಿಮ್ಮ ಮೊದಲ ಚಿತ್ರವನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ!",
        "footer_text": "ಬಾಳೆ ಎಲೆ ರೋಗ ಪತ್ತೆ — ರೈತರಿಗಾಗಿ ಆಧುನಿಕ ಕೃಷಿ ತಂತ್ರಜ್ಞಾನ",
        "disease_info": {
            "Healthy": {
                "name": "ಆರೋಗ್ಯಕರ ಬಾಳೆ ಎಲೆ",
                "status": "ಆರೋಗ್ಯಕರ",
                "explanation": "ಎಲೆಯು ಏಕರೂಪದ ಹಸಿರು ಬಣ್ಣದಿಂದ ಕೂಡಿದ್ದು ಆರೋಗ್ಯಕರವಾಗಿದೆ. ಯಾವುದೇ ಕಲೆಗಳು ಅಥವಾ ರೋಗಲಕ್ಷಣಗಳಿಲ್ಲ.",
                "recommendations": [
                    "ಗಿಡದ ಬೆಳವಣಿಗೆಗೆ ಸಮತೋಲಿತ ಗೊಬ್ಬರವನ್ನು (NPK) ಮುಂದುವರಿಸಿ.",
                    "ತೋಟದಲ್ಲಿ ನೀರು ನಿಲ್ಲದಂತೆ ನೋಡಿಕೊಳ್ಳಿ ಮತ್ತು ಸೂರ್ಯನ ಬೆಳಕು ಬೀಳಲು 2 ರಿಂದ 2.5 ಮೀಟರ್ ಅಂತರ ಕಾಪಾಡಿ.",
                    "ಮಳೆಗಾಲದಲ್ಲಿ ಹಳೆಯ ಎಲೆಗಳ ಕೆಳಭಾಗವನ್ನು ನಿಯಮಿತವಾಗಿ ಗಮನಿಸಿ."
                ],
                "prevention": [
                    "ಕತ್ತರಿಸುವ ಉಪಕರಣಗಳನ್ನು ಯಾವಾಗಲೂ ಸ್ವಚ್ಛವಾಗಿಡಿ.",
                    "ಹೊಸ ನಾಟಿಗೆ ಪ್ರಮಾಣೀಕೃತ ಟಿಶ್ಯೂ ಕಲ್ಚರ್ ಸಸಿಗಳನ್ನು ಬಳಸಿ."
                ]
            },
            "Black Sigatoka": {
                "name": "ಕಪ್ಪು ಸಿಗಟೋಕಾ ರೋಗ (Black Sigatoka)",
                "status": "ರೋಗಪೀಡಿತ",
                "explanation": "ಎಲೆಯ ರಕ್ತನಾಳಗಳಿಗೆ ಸಮಾನಾಂತರವಾಗಿ ಕಪ್ಪು ಅಥವಾ ಕಂದು ಬಣ್ಣದ ಪಟ್ಟಿಗಳು ಕಾಣಿಸಿಕೊಂಡು ಎಲೆ ಒಣಗುತ್ತದೆ.",
                "recommendations": [
                    "ರೋಗಪೀಡಿತ ಎಲೆಗಳನ್ನು ಕತ್ತರಿಸಿ ತೋಟದಿಂದ ಹೊರಗೆ ಗುಂಡಿಯಲ್ಲಿ ಮುಚ್ಚಿ ಅಥವಾ ನಾಶಪಡಿಸಿ.",
                    "ಗಾಳಿಯಾಡುವಿಕೆಯನ್ನು ಹೆಚ್ಚಿಸಿ ಮತ್ತು ತೇವಾಂಶ ಬೇಗನೆ ಆರುವಂತೆ ಮಾಡಿ.",
                    "ಬೇವಿನ ಎಣ್ಣೆ ಅಥವಾ ಸೂಡೊಮೊನಾಸ್ ದ್ರಾವಣವನ್ನು ಸಿಂಪಡಿಸಿ.",
                    "ತುಂತುರು ನೀರಾವರಿ ಬದಲು ಹನಿ ನೀರಾವರಿ ಬಳಸಿ."
                ],
                "prevention": [
                    "ಗಿಡಗಳ ನಡುವೆ ಸರಿಯಾದ ಅಂತರವಿರಲಿ.",
                    "ಪೊಟ್ಯಾಶ್ ಗೊಬ್ಬರ ನೀಡಿ ಎಲೆಯ ರೋಗನಿರೋಧಕ ಶಕ್ತಿಯನ್ನು ಹೆಚ್ಚಿಸಿ."
                ]
            },
            "Yellow Sigatoka": {
                "name": "ಹಳದಿ ಸಿಗಟೋಕಾ ರೋಗ (Yellow Sigatoka)",
                "status": "ರೋಗಪೀಡಿತ",
                "explanation": "ಎಲೆಗಳ ಮೇಲೆ ಹಳದಿ ಕಲೆಗಳು ಕಾಣಿಸಿಕೊಂಡು ಅವುಗಳ ಮಧ್ಯಭಾಗ ಬೂದು ಬಣ್ಣಕ್ಕೆ ತಿರುಗುತ್ತವೆ.",
                "recommendations": [
                    "ಹಳೆಯ ಕಲೆಗಳಿರುವ ಎಲೆಗಳನ್ನು ಕತ್ತರಿಸಿ ತೆಗೆಯಿರಿ.",
                    "ತೋಟದಲ್ಲಿ ನೀರು ನಿಲ್ಲದಂತೆ ಎಚ್ಚರವಹಿಸಿ.",
                    "ಕೃಷಿ ತಜ್ಞರ ಸಲಹೆಯಂತೆ ಕಾಪರ್ ಹೈಡ್ರಾಕ್ಸೈಡ್ ಸಿಂಪಡಿಸಿ.",
                    "ಅತಿಯಾದ ಯೂರಿಯಾ ತಪ್ಪಿಸಿ, ಪೊಟ್ಯಾಶ್ ಗೊಬ್ಬರಕ್ಕೆ ಆದ್ಯತೆ ನೀಡಿ."
                ],
                "prevention": [
                    "ತೋಟವನ್ನು ಕಳೆ ಮುಕ್ತವಾಗಿರಿಸಿ.",
                    "ಮಳೆಗಾಲದಲ್ಲಿ ವಾರಕ್ಕೆ ಎರಡು ಬಾರಿ ಪರಿಶೀಲಿಸಿ."
                ]
            },
            "Panama Disease": {
                "name": "ಪನಾಮಾ ಸೊರಗು ರೋಗ (Panama Wilt)",
                "status": "ರೋಗಪೀಡಿತ",
                "explanation": "ಕೆಳಗಿನ ಹಳೆಯ ಎಲೆಗಳ ಅಂಚುಗಳಿಂದ ಹಳದಿ ಬಣ್ಣ ಪ್ರಾರಂಭವಾಗಿ ತೊಟ್ಟುಗಳು ಮುರಿದು ನೇತಾಡುತ್ತವೆ.",
                "recommendations": [
                    "ರೋಗಪೀಡಿತ ಗಿಡವನ್ನು ತಕ್ಷಣ ಪ್ರತ್ಯೇಕಿಸಿ ಸುತ್ತಲೂ ಆಳವಾದ ಕಂದಕ ತೋಡಿ.",
                    "ಸೋಂಕಿತ ಮಣ್ಣು ಅಥವಾ ಉಪಕರಣಗಳನ್ನು ಬೇರೆ ಗದ್ದೆಗಳಿಗೆ ಸಾಗಿಸಬೇಡಿ.",
                    "ಕತ್ತಿ ಮತ್ತು ಉಪಕರಣಗಳನ್ನು ಬ್ಲೀಚಿಂಗ್ ದ್ರಾವಣದಲ್ಲಿ ತೊಳೆಯಿರಿ.",
                    "ಟ್ರೈಕೋಡರ್ಮಾ ಬೆರೆಸಿದ ಕೊಟ್ಟಿಗೆ ಗೊಬ್ಬರವನ್ನು ಗಿಡದ ಬುಡಕ್ಕೆ ಹಾಕಿ."
                ],
                "prevention": [
                    "ರೋಗ ನಿರೋಧಕ ತಳಿಗಳನ್ನು ಮಾತ್ರ ನೆಡಿ.",
                    "ರೋಗ ಕಂಡುಬಂದರೆ ತಕ್ಷಣ ಸ್ಥಳೀಯ ಕೃಷಿ ಅಧಿಕಾರಿಗಳಿಗೆ ತಿಳಿಸಿ."
                ]
            }
        }
    }
}
